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


class BudgetView(View):

    def get(self, request):
        pozycje=Budget.objects.all()
        form = BudgetForm()
        wykres_month()

        for_calculation = []
        kalkulacje = 0
        for element in pozycje:
            # for_calculation = np.array(element.money_min, dtype=np.float32)
            for_calculation.append(element.money_min)
            # for_calculation = [float(element.money_min) for element.money_min in pozycje]
        for elem in for_calculation:
            kalkulacje += elem
        return render(request, 'budget.html', {"pozycje":pozycje, "form":form, "kalkulacje":kalkulacje})

    def post(self, request):
        form = BudgetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            money_min = form.cleaned_data['money_min']
            money_max = form.cleaned_data['money_max']
            monthly = form.cleaned_data['monthly']
            opis = form.cleaned_data['opis']
            Budget.objects.create(name=name, money_min=money_min, money_max=money_max, monthly=monthly, opis=opis)
            return redirect('budget')


class MonthsBudgetView(View):

    def get(self, request):
        this_months_budget = MonthsBudget.objects.all()
        form = MonthsBudgetForm()
        wykresik = wykres_month()
        return render(request, 'budget-months.html', {"this_months_budget":this_months_budget, "form":form, "wykresik":wykresik})

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
            money_max = form.cleaned_data['money_max']
            monthly = form.cleaned_data['monthly']
            opis = form.cleaned_data['opis']
            pozycja.name=name
            pozycja.money_min=money_min
            pozycja.money_max=money_max
            pozycja.monthly=monthly
            pozycja.opis=opis
            pozycja.save()
            return redirect('budget')


class DeleteBudget(DeleteView):
    model = Budget
    success_url = '/budget'


class DeleteSkarbonki(DeleteView):
    model = Skarbonki
    success_url = '/skar-cele'


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
        return render(request, 'skar-cele.html', {"skarbonki":skarbonki, "form":form})

    def post(self, request):
        form = SkarbonkiForm(request.POST)
        if form.is_valid():
            money_for = form.cleaned_data['money_for']
            m_min = form.cleaned_data['m_min']
            m_max = form.cleaned_data['m_max']
            month = form.cleaned_data['month']
            opis = form.cleaned_data['opis']
            # zapasowa = form.cleaned_data['zapasowa']
            Skarbonki.objects.create(money_for=money_for, m_min=m_min, m_max=m_max, month=month, opis=opis)
            return redirect('skar-cele')


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
            m_max = form.cleaned_data['m_max']
            month = form.cleaned_data['month']
            opis = form.cleaned_data['opis']
            pozycja.money_for=money_for
            pozycja.m_min=m_min
            pozycja.m_max=m_max
            pozycja.month=month
            pozycja.opis=opis
            pozycja.save()
            return redirect('skar-cele')


class SkarbonkiNowy(View):
    def get(self, request):
        return render(request, 'skar-nowy.html')

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


class Akc(View):
    def get(self, request):
        spolka = "cdr"
        p = {"s": spolka}

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
        return render(request, 'akc.html', {"kurs":kurs, "zmiana_bezwzgledna":zmiana_wzgledna,
                                            "zmiana_wzgledna":zmiana_wzgledna,
                                            "transakcje":transakcje})







class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')



