from datetime import date
import requests
from bs4 import BeautifulSoup
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from matplotlib.pyplot import savefig
from .models import *
from .forms import *
from decimal import Decimal
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import matplotlib.dates as mdates




def kalkul():
    pozycje = Budget.objects.all()
    this_months_budget = MonthsBudget.objects.all()
    for_calculation = []
    kalkulacje = 0
    for element in pozycje:
        # for_calculation = np.array(element.money_min, dtype=np.float32)
        for_calculation.append(element.money_min)
        # for_calculation = [float(element.money_min) for element.money_min in pozycje]
    for elem in for_calculation:
        kalkulacje += elem
        return kalkulacje


def wykres_month():
    style.use('ggplot')

    plt.title('wykres z ostatnich 12 miesięcy')
    plt.xlabel('oś X')
    plt.ylabel('oś Y')
    plt.grid(True)

    queryset = MonthsBudget.objects.all().order_by('-month_date')
    x=[]
    y=[]
    for el in queryset:
        x.append(el.chosen_name_of_month)
        # x.append(el.month_date)
        y.append(el.month_cost)
    x1=x[0:12]
    y1=y[0:12]
    x1.reverse()
    y1.reverse()

    plt.bar(x1,y1)
    plt.tick_params(axis='x', rotation=290)
    # plt.show()
    savefig('static/wykres.png')




def wykres_month2():
    s0=Skarbonki.objects.all()
    # s=Skarbonki.objects.get(id=1)
    # s2=s.get_next_in_order
    # q=PaymentDay.objects.all()
    j=0
    for elem in s0:
        elll=PaymentDay.objects.all().filter(payment_skarbonki=elem.id)

        x = [0]
        y = [0]
        for el in elll:
            new_val=str(el.value_of)
            y += new_val
            new_dat=str(el.date_of)
            x += new_dat

            style.use('ggplot')
            plt.title('wykres')
            plt.xlabel('oś X')
            plt.ylabel('oś Y')
            plt.grid(True)
            plt.plot(x, y)
            plt.tick_params(axis='x', rotation=290)

            savefig('static/wykres-inny1.png')
            j+=1

        # nazwa{i}=PaymentDay.objects.all().filter(payment_skarbonki=elem.id)
        # i+=1

    # tworze=PaymentDay.objects.all().first()
    # q2=PaymentDay.objects.get(id=1)
    # a=AlreadyCollected.objects.all()
    # a2=AlreadyCollected.objects.get(target=q2.payment_skarbonki_id)

# # for element in q:
#     style.use('ggplot')
#     plt.title('wykres')
#     plt.xlabel('oś X')
#     plt.ylabel('oś Y')
#     plt.grid(True)
#     # y=element.date_of
#
#     x=[]
#     y=[]
#     j=0
#     for eleme in nazwa{j}:
#         x+=eleme.date_of
#         y+=eleme.value_of
#         plt.bar(x,y)
#         plt.tick_params(axis='x', rotation=290)
#         savefig(f'static/wykres-inny{j}.png')
#         j+=1

    # nazwa1 queryset --moze duzo

    # q2.date_of
    # q2.payment_skarbonki
    # q2.payment_skarbonki_id
    # q2.payment_collected
    # q2.payment_collected_id

    # q2.get_next_by_date_of()

    # for el in queryset:
    #     x.append(el.chosen_name_of_month)
    #     # x.append(el.month_date)
    #     y.append(el.month_cost)
    # x1=x[0:12]
    # y1=y[0:12]
    # x1.reverse()
    # y1.reverse()
    #
    # plt.bar(x1,y1)
    # plt.tick_params(axis='x', rotation=290)
    # savefig('static/wykres.png')




class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')



class BudgetView(View):#

    def get(self, request):
        pozycje=Budget.objects.all()
        form = BudgetForm()
        wykres_month()
        return render(request, 'budget.html', {"pozycje":pozycje, "form":form})

    def post(self, request):
        pozycje=Budget.objects.all()
        # for_calculation = []
        # kalkulacje = 0
        # for element in pozycje:
        #     for_calculation.append(element.money_min)
        # for elem in for_calculation:
        #     kalkulacje += elem

        doliczyc = []
        zapasowa = request.POST.getlist('zapasowa')
        for elements in pozycje:
            doliczyc.append(request.POST.get(f'{elements.id}'))

        my_sum = 0
        while zapasowa != []:
            elemencik = float(zapasowa.pop())
            my_sum += elemencik
        if doliczyc != []:
            for ell in doliczyc:
                if ell == '':
                    pass
                else:
                    do_sumy=float(ell)
                    my_sum += do_sumy

        def set_session(request):
            request.session["suma_przekazana"] = my_sum
        set_session(request)
        form = BudgetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            money_min = form.cleaned_data['money_min']
            monthly = form.cleaned_data['monthly']
            opis = form.cleaned_data['opis']
            Budget.objects.create(name=name, money_min=money_min, monthly=monthly, opis=opis)
            return render(request, 'budget.html', {"zapasowa":zapasowa,
                                                   "my_sum":my_sum,
                                                   "pozycje":pozycje,
                                                   "doliczyc": doliczyc,
                                                   "form":form})
        return render(request, 'budget.html', {"zapasowa": zapasowa,
                                               "my_sum": my_sum,
                                               "doliczyc":doliczyc,
                                               "pozycje": pozycje,
                                               "form": form})



class ModifyBudget(View):

    def get(self, request, id):
        pozycja=Budget.objects.get(id=id)
        form = BudgetForm(instance=pozycja)
        return render(request, 'modify-budget-pos.html', {"pozycja":pozycja, "form":form})

    def post(self, request, id):
        form = BudgetForm(request.POST)
        pozycja = Budget.objects.get(id=id)
        if form.is_valid():
            name = form.cleaned_data['name']
            money_min = form.cleaned_data['money_min']
            monthly = form.cleaned_data['monthly']
            opis = form.cleaned_data['opis']
            pozycja.name=name
            pozycja.money_min=money_min
            pozycja.monthly=monthly
            pozycja.opis=opis
            pozycja.save()
            return redirect('budget')


class DeleteBudget(DeleteView):
    model = Budget
    success_url = '/budget'




class MonthsBudgetView(View):#

    def get(self, request):
        this_months_budget = MonthsBudget.objects.all()
        form = MonthsBudgetForm()
        wykresik = wykres_month()
        return render(request, 'budget-months.html', {"this_months_budget":this_months_budget,
                                                      "form":form, "wykresik":wykresik})

    def post(self, request):
        form = MonthsBudgetForm(request.POST)
        if form.is_valid():
            chosen_name_of_month = form.cleaned_data['chosen_name_of_month']
            month_cost = form.cleaned_data['month_cost']
            description = form.cleaned_data['description']
            MonthsBudget.objects.create(chosen_name_of_month=chosen_name_of_month,
                                        month_cost=month_cost,
                                        description=description)
            return redirect('months-budget')



class MonthsBudgetPropositionView(View):#

    def get(self, request):
        form = MonthsBudgetForm(initial={'month_cost': request.session.get("suma_przekazana"),
                                         'month_date':date.today()})
        return render(request, 'budget-months-3.html', {"form":form})

    def post(self, request):
        form = MonthsBudgetForm(request.POST)
        if form.is_valid():
            chosen_name_of_month = form.cleaned_data['chosen_name_of_month']
            month_cost = form.cleaned_data['month_cost']
            description = form.cleaned_data['description']
            MonthsBudget.objects.create(chosen_name_of_month=chosen_name_of_month,
                                        month_cost=month_cost,
                                        description=description)
            return redirect('months-budget')


class ModifyMonths(View):

    def get(self, request, id):
        pozycja=MonthsBudget.objects.get(id=id)
        form = MonthsBudgetForm(instance=pozycja)
        return render(request, 'modify-months.html', {"pozycja":pozycja, "form":form})

    def post(self, request, id):
        form = MonthsBudgetForm(request.POST)
        pozycja = MonthsBudget.objects.get(id=id)
        if form.is_valid():
            chosen_name_of_month = form.cleaned_data['chosen_name_of_month']
            month_cost = form.cleaned_data['month_cost']
            description = form.cleaned_data['description']
            pozycja.chosen_name_of_month = chosen_name_of_month
            pozycja.month_cost = month_cost
            pozycja.description = description
            pozycja.save()
            return redirect('months-budget')


class DeleteMonths(DeleteView):
    model = MonthsBudget
    success_url = '/months-budget'





class SkarbonkiView(View):
    def get(self, request):
        return render(request, 'skarbonki.html')


class SkarbonkiCele(View):

    def get(self, request):
        skarbonki = Skarbonki.objects.all()
        form = SkarbonkiForm()
        s0 = Skarbonki.objects.all().first()
        eli=PaymentDay.objects.all().filter(payment_skarbonki=s0.id)
        return render(request, 'skar-cele.html', {"skarbonki":skarbonki, "form":form, "eli":eli})

    def post(self, request):
        skarbonki = Skarbonki.objects.all()
        form = SkarbonkiForm(request.POST)
        if form.is_valid():
            money_for = form.cleaned_data['money_for']
            m_min = form.cleaned_data['m_min']
            opis = form.cleaned_data['opis']
            Skarbonki.objects.create(money_for=money_for, m_min=m_min, opis=opis)

            s1 = Skarbonki.objects.get(money_for=money_for)
            a1 = AlreadyCollected.objects.create(collected=0)
            PaymentDay.objects.create(payment_skarbonki=s1,payment_collected=a1)

            zlap=PaymentDay.objects.get(payment_skarbonki_id=s1)
            return render(request, 'skar-cele.html', {"skarbonki":skarbonki, "form": form, "zlap":zlap})


class SkarbonkiNowy(View):

    def get(self, request):
        collected = AlreadyCollected.objects.all()
        skarbonki = Skarbonki.objects.all()
        return render(request, 'skar-nowy.html', {"collected":collected, "skarbonki":skarbonki})
    def post(self, request):
        collected = AlreadyCollected.objects.all()
        skarbonki = Skarbonki.objects.all()
        return render(request, 'skar-nowy.html', {"collected": collected,
                                            "skarbonki": skarbonki})


class ModifySkarbonki(View):

    def get(self, request, id):
        pozycja=Skarbonki.objects.get(id=id)
        form = SkarbonkiForm(instance=pozycja)
        return render(request, 'modify-skarb.html', {"pozycja":pozycja, "form":form})

    def post(self, request, id):
        form = SkarbonkiForm(request.POST)
        pozycja = Skarbonki.objects.get(id=id)
        if form.is_valid():
            money_for = form.cleaned_data['money_for']
            m_min = form.cleaned_data['m_min']
            opis = form.cleaned_data['opis']
            pozycja.money_for=money_for
            pozycja.m_min=m_min
            pozycja.opis=opis
            pozycja.save()
            return redirect('skar-cele')


class SkarbonkiMistake(View):
    def get(self, request):
        msg = "Dziś już wpłacono na owy cel! Czyżby nastąpiła pomyłka przy wpisywaniu kwoty?"
        skarbonki = Skarbonki.objects.all()
        return render(request, 'mistake.html', {"skarbonki":skarbonki, "msg":msg})
    def post(self, request):

        mistake_in = request.POST.get('mistake_in')
        mistake_id = int(mistake_in)
        mistake_value = request.POST.get('mistake_value')
        mistake_value_float = float(mistake_value)
        correct_value = request.POST.get('correct_value')
        correct_value_float = float(correct_value)

        # mistake_object=Skarbonki.objects.get(id=mistake_in.id)
        last_mistake=PaymentDay.objects.all().filter(payment_skarbonki_id=mistake_id).last()
        last_to_change=AlreadyCollected.objects.get(id=last_mistake.payment_collected_id)

        last_mistake.value_of -= mistake_value_float
        last_mistake.value_of =+ correct_value_float
        last_mistake.save()
        last_to_change.collected -= mistake_value_float
        last_to_change.collected -= correct_value_float
        last_to_change.save()

        return redirect('skarbonki')






lista_wynikow = []
lista_wynikow2 = []


class SkarbonkiCzas(View):

    def get(self, request):
        return render(request, 'skar-czas.html')

    def post(self, request):
        kwota1 = request.POST.get('kwota')
        kwota_mies2 = request.POST.get('kwota_mies')
        wynik0 = float(kwota1) / float(kwota_mies2)
        wynik1 = Decimal("%.2f" % wynik0)
        lista_wynikow.append(f"{kwota1} : {kwota_mies2} = {wynik1} \n")

        # napis = f"{kwota1}, ' : ',  {kwota_mies2}, ' = ', {wynik1}, '\n'"
        # f = open("porown1.txt", 'a', encoding="utf-8")
        # # f.write('napis próbny \n')
        # f.write(str(kwota1))
        # f.write(' : ')
        # f.write(str(kwota_mies2))
        # f.write( ' = ')
        # f.write(str(wynik1))
        # f.write('\n')
        # f.close()
        lista_wynikow.reverse()
        return render(request, 'skar-czas.html', {'wynik1':wynik1, "lista_wynikow":lista_wynikow})


class SkarbonkiKwota(View):

    def get(self, request):
        return render(request, 'skar-kwota.html')

    def post(self, request):
        kwota1 = request.POST.get('kwota')
        kwota_mies2 = request.POST.get('kwota_mies')
        wynik0 = float(kwota1) / float(kwota_mies2)
        wynik1 = Decimal("%.2f" % wynik0)
        lista_wynikow2.append(f"{kwota1} : {kwota_mies2} = {wynik1} \n")
        lista_wynikow2.reverse()
        return render(request, 'skar-kwota.html', {'wynik1':wynik1, "lista_wynikow2":lista_wynikow2})


class DeleteSkarbonki(DeleteView):#
    model = Skarbonki
    success_url = '/skar-cele'



class AlreadyCollectedView(View):

    def get(self, request):
        collected = AlreadyCollected.objects.all()
        skarbonki = Skarbonki.objects.all()
        return render(request, 'skar-pilnuj.html', {"collected":collected, "skarbonki":skarbonki})

    def post(self, request):
        collected = AlreadyCollected.objects.all()
        skarbonki = Skarbonki.objects.all()
        try:
            choose = request.POST.get('choose')
            chosen = int(choose)
            # if PaymentDay.objects.get(payment_skarbonki_id=chosen, date_of=date.today()):
            # try:
            #     zlap = PaymentDay.objects.get(payment_skarbonki_id=chosen, date_of=date.today())
            # except:

            def set_session2(request):
                # request.session["id_of_payment"] = zlap.id #platnosc z data
                request.session["chosen_id"] = chosen # id skarbonki

            set_session2(request)

            # zlapany = AlreadyCollected.objects.get(target=zlap.payment_skarbonki_id)
            # else:
            #     stworz = PaymentDay.objects.create(payment_skarbonki_id=chosen, date_of=date.today(), payment_collected_id=)
            return render(request, 'skar-pilnuj.html', {"chosen": chosen,
                                                        "collected": collected,
                                                        "skarbonki": skarbonki,
                                                            # "zlap": zlap,
                                                            # "zlapany": zlapany
                                                        })
        except:
            moj_x=request.session.get("chosen_id"),
            for e in moj_x:
                moj_x_nowy = e
            congrats = request.POST.get('congrats')
            congrats2 = float(congrats)
            moj_obiekt=PaymentDay.objects.filter(payment_skarbonki_id=moj_x_nowy).last()
            try:
                PaymentDay.objects.get(payment_skarbonki_id=moj_x_nowy, date_of=date.today())
                dzisiejszy_stary=PaymentDay.objects.get(payment_skarbonki_id=moj_x_nowy, date_of=date.today())

                return redirect('skar-mistake')

            except:
                dzisiejszy_nowy=PaymentDay.objects.create(payment_skarbonki_id=moj_x_nowy, date_of=date.today(), payment_collected_id=moj_obiekt.payment_collected_id, value_of=moj_obiekt.value_of)
                dzisiejszy_nowy.payment_skarbonki_id=moj_x_nowy
                dzisiejszy_nowy.payment_collected_id=moj_obiekt.payment_collected_id
                dzisiejszy_nowy.save()
                alr_powieksz = AlreadyCollected.objects.get(id=dzisiejszy_nowy.payment_collected_id)
                alr_powieksz.collected += congrats2
                alr_powieksz.save()
                dzisiejszy_nowy.value_of += congrats2
                dzisiejszy_nowy.save()
            return render(request, 'skar-pilnuj.html', {"collected": collected,
                                                        "skarbonki": skarbonki})


class Akc(View):
    def get(self, request):
        form = StockForm()
        spolka = "cdr"
        p = {"s": spolka}
        ctx = Stock.objects.all()
        odpowiedz = requests.get("http://stooq.pl/q/", params=p)
        soup = BeautifulSoup(odpowiedz.text, 'html.parser')

        # podejście 1: po id
        # znacznik_kurs = soup.find("span", id=f"aq_{spolka}_c1")
        # kurs = float(znacznik_kurs.text)
        # print(f"Podejście 1, kurs = {kurs}")

        #
        # # podejście 2a: po napisie, a potem find
        znacznik_kurs = soup.find(text="Kurs").parent.find("span")
        kurs = float(znacznik_kurs.text)
        if kurs:
            cdr_interests=Stock.objects.get(name='CDR')
            jednostki_cdr = cdr_interests.interests
            value_of_cdr = jednostki_cdr * kurs

        # print(f"Podejście 2a, kurs = {kurs}")
        #
        # # zmiana kursu
        znacznik_zmiana_bezwzgledna = soup.find("span", id=f"aq_{spolka}_m2")
        znacznik_zmiana_wzgledna = soup.find("span", id=f"aq_{spolka}_m3")

        zmiana_bezwzgledna = float(znacznik_zmiana_bezwzgledna.text)
        zmiana_wzgledna = float(znacznik_zmiana_wzgledna.text[1:-2]) / 100
        #
        # print(f"Podejście 1, zmiana_bezwzgledna = {zmiana_bezwzgledna}")
        # print(f"Podejście 1, zmiana_wzgledna = {zmiana_wzgledna}")
        #
        # # transakcje
        # # podejście 2b: po napisie, a potem next_element
        znacznik_transakcje = soup.find(text="Transakcje").next_element.next_element
        transakcje = int(znacznik_transakcje.text.replace(" ", ""))
        # print(f"Podejście 2b, transakcje = {transakcje}")

        return render(request, 'akc.html', {"kurs":kurs,
                                            "value_of_cdr":value_of_cdr,
                                            "zmiana_bezwzgledna":zmiana_wzgledna,
                                            "zmiana_wzgledna":zmiana_wzgledna,
                                            "transakcje":transakcje,
                                            "ctx":ctx,
                                            "form":form})
    def post(self, request):
        form = StockForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            enter_price = form.cleaned_data['enter_price']
            interests = form.cleaned_data['interests']
            value_of = form.cleaned_data['value_of']
            price = form.cleaned_data['price']
            dividend = form.cleaned_data['dividend']
            type_of_market = form.cleaned_data['type_of_market']
            www = form.cleaned_data['www']
            Stock.objects.create(name=name, enter_price=enter_price, interests=interests, value_of=value_of,
                                 price=price,dividend=dividend,type_of_market=type_of_market,www=www)
            return redirect('akc')



class ModifyStock(View):

    def get(self, request, id):
        pozycja=Stock.objects.get(id=id)
        form = StockForm(instance=pozycja)
        return render(request, 'modify-stock.html', {"pozycja":pozycja, "form":form})

    def post(self, request, id):
        form = StockForm(request.POST)
        pozycja = Stock.objects.get(id=id)
        form = StockForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            enter_price = form.cleaned_data['enter_price']
            interests = form.cleaned_data['interests']
            value_of = form.cleaned_data['value_of']
            price = form.cleaned_data['price']
            dividend = form.cleaned_data['dividend']
            type_of_market = form.cleaned_data['type_of_market']
            www = form.cleaned_data['www']
            pozycja.name=name
            pozycja.enter_price=enter_price
            pozycja.interests=interests
            pozycja.value_of=value_of
            pozycja.price=price
            pozycja.dividend=dividend
            pozycja.type_of_market=type_of_market
            pozycja.www=www
            pozycja.save()
            return redirect('akc')


class DeleteStock(DeleteView):
    model = Stock
    success_url = '/akc'



class CreditView(View):

    def get(self, request):
        wykres_month2()
        return render(request, 'credit.html')

    def post(self, request):
        return redirect('credit')

