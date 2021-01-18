import math
from datetime import date
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from decimal import Decimal
from matplotlib.pyplot import savefig
from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import numpy as np

from .models import Budget, PiggyBanks, MonthsBudget, Stock, AlreadyCollected, PaymentDay, Credits, Repayment, RepaymentDay, Income, AdditionalIncome
from .forms import BudgetForm, PiggyBanksForm, MonthsBudgetForm, StockForm, CreditsForm, IncomeForm, AdditionalIncomeForm


def wykres_month():
    plt.figure(1)
    plt.figure(figsize=(9, 7))
    plt.title('wydatki z ostatnich 12 miesięcy')
    plt.ylabel('zapisane miesięczne kwoty')
    queryset = MonthsBudget.objects.all().order_by('-month_date')
    xmonth = []
    ymonth = []
    for el in queryset:
        xmonth.append(el.chosen_name_of_month)
        ymonth.append(el.month_cost)
    xmonth1 = xmonth[0:12]
    ymonth1 = ymonth[0:12]
    xmonth1.reverse()
    ymonth1.reverse()
    plt.style.use('ggplot')
    plt.bar(xmonth1,ymonth1)
    plt.tick_params(axis='x', rotation=330)
    savefig('static/wykres.png')


def wykres8():
    x = []
    y = []
    s8 = PiggyBanks.objects.get(id=8)
    payments_for_obj = PaymentDay.objects.filter(payment_piggybanks=s8.id).order_by('date_of')
    max_y = s8.m_min
    obj_name = s8.money_for
    for el in payments_for_obj:
        new_value = el.value_of
        y.append(new_value)
        new_date = str(el.date_of)
        x.append(new_date)
    plt.figure(2)
    plt.figure(figsize=(11, 6))
    plt.style.use('ggplot')
    plt.title(f'wykres wpłat dla celu "{obj_name}"')
    plt.xlabel('DATY')
    plt.ylabel(f'Twój cel: {max_y}')
    plt.grid(True)
    plt.margins(0.1)
    plt.tick_params(axis='x', rotation=330)
    plt.plot(x, y, 'b*', markersize=18) # gwiazdka
    savefig('static/wykres-inny8.png')


def wykres9():
    x9 = []
    y9 = []
    s9 = PiggyBanks.objects.get(id=9)
    payments_for_obj9 = PaymentDay.objects.filter(payment_piggybanks=s9.id).order_by('date_of')
    max_y9 = s9.m_min
    obj9_name = s9.money_for
    for el in payments_for_obj9:
        new_value = el.value_of
        y9.append(new_value)
        new_date = str(el.date_of)
        x9.append(new_date)
    plt.figure(3)
    plt.figure(figsize=(11, 6))
    plt.title(f'wykres wpłat dla celu "{obj9_name}"')
    plt.xlabel('DATY')
    plt.ylabel(f'Twój cel: {max_y9}')
    plt.margins(0.1)
    plt.bar(x9, y9)
    savefig('static/wykres-inny9.png')


def wykres10():
    x10 = []
    y10 = []
    s10 = PiggyBanks.objects.get(id=10)
    payments_for_obj10 = PaymentDay.objects.filter(payment_piggybanks=s10.id).order_by('date_of')
    max_y10 = s10.m_min
    obj10_name = s10.money_for
    for el in payments_for_obj10:
        new_value = el.value_of
        y10.append(new_value)
        new_date = str(el.date_of)
        x10.append(new_date)
    plt.figure(4)
    plt.figure(figsize=(11, 6))
    plt.title(f'wykres wpłat dla celu "{obj10_name}"')
    plt.xlabel('DATY')
    plt.ylabel(f'Twój cel: {max_y10}')
    plt.grid(True)
    plt.margins(0.1)
    plt.plot(x10, y10, 'g--',  linewidth=2.5)
    savefig('static/wykres-inny10.png')


def wykres15():
    x15 = []
    y15 = []
    s15 = PiggyBanks.objects.get(id=15)
    payments_for_obj15 = PaymentDay.objects.filter(payment_piggybanks=s15.id).order_by('date_of')
    max_y15 = s15.m_min
    obj15_name = s15.money_for
    for el in payments_for_obj15:
        new_value = el.value_of
        y15.append(new_value)
        new_date = str(el.date_of)
        x15.append(new_date)
    plt.figure(5)
    plt.figure(figsize=(11, 6))
    plt.title(f'wykres wpłat dla celu "{obj15_name}"')
    plt.xlabel(f'Twój cel: {max_y15}')
    plt.ylabel('DATY')
    plt.grid(True)
    plt.margins(0.1)
    plt.barh(x15, y15)
    savefig('static/wykres-inny15.png')


def wykres16():
    x16 = []
    y16 = []
    s16 = PiggyBanks.objects.get(id=16)
    payments_for_obj16 = PaymentDay.objects.filter(payment_piggybanks=s16.id).order_by('date_of')
    max_y16 = s16.m_min
    obj16_name = s16.money_for
    for el in payments_for_obj16:
        new_value = el.value_of
        y16.append(new_value)
        new_date = str(el.date_of)
        x16.append(new_date)
    plt.figure(6)
    plt.figure(figsize=(11, 6))
    plt.title(f'wykres wpłat dla celu "{obj16_name}"')
    plt.xlabel('DATY')
    plt.ylabel(f'Twój cel: {max_y16}')
    plt.grid(True)
    plt.margins(0.1)
    plt.plot(x16, y16, 'y>', markersize=18)
    savefig('static/wykres-inny16.png')


def wykres24():
    x24 = []
    y24 = []
    s24 = PiggyBanks.objects.get(id=24)
    payments_for_obj24 = PaymentDay.objects.filter(payment_piggybanks=s24.id).order_by('date_of')
    max_y24 = s24.m_min
    obj24_name = s24.money_for
    for el in payments_for_obj24:
        new_value = el.value_of
        y24.append(new_value)
        new_date = str(el.date_of)
        x24.append(new_date)
    plt.figure(7)
    plt.figure(figsize=(11, 6))
    plt.title(f'wykres wpłat dla celu "{obj24_name}"')
    plt.xlabel('DATY')
    plt.ylabel(f'Twój cel: {max_y24}')
    plt.grid(True)
    plt.margins(0.1)
    plt.plot(x24, y24, linewidth=5.0)
    savefig('static/wykres-inny24.png')


def wykres_innego_typu():
    x = []
    y = []
    s8 = PiggyBanks.objects.get(id=8)
    payments_for_obj = PaymentDay.objects.filter(payment_piggybanks=s8.id).order_by('date_of')
    for el in payments_for_obj:
        new_value = el.value_of
        y.append(new_value)
        new_date = str(el.date_of)
        x.append(new_date)
    x9 = []
    y9 = []
    s9 = PiggyBanks.objects.get(id=9)
    payments_for_obj9 = PaymentDay.objects.filter(payment_piggybanks=s9.id).order_by('date_of')
    for el in payments_for_obj9:
        new_value = el.value_of
        y9.append(new_value)
        new_date = str(el.date_of)
        x9.append(new_date)
    x10 = []
    y10 = []
    s10 = PiggyBanks.objects.get(id=10)
    payments_for_obj10 = PaymentDay.objects.filter(payment_piggybanks=s10.id).order_by('date_of')
    for el in payments_for_obj10:
        new_value = el.value_of
        y10.append(new_value)
        new_date = str(el.date_of)
        x10.append(new_date)
    x15 = []
    y15 = []
    s15 = PiggyBanks.objects.get(id=15)
    payments_for_obj15 = PaymentDay.objects.filter(payment_piggybanks=s15.id).order_by('date_of')
    for el in payments_for_obj15:
        new_value = el.value_of
        y15.append(new_value)
        new_date = str(el.date_of)
        x15.append(new_date)
    x16 = []
    y16 = []
    s16 = PiggyBanks.objects.get(id=16)
    payments_for_obj16 = PaymentDay.objects.filter(payment_piggybanks=s16.id).order_by('date_of')
    for el in payments_for_obj16:
        new_value = el.value_of
        y16.append(new_value)
        new_date = str(el.date_of)
        x16.append(new_date)
    x24 = []
    y24 = []
    s24 = PiggyBanks.objects.get(id=24)
    payments_for_obj24 = PaymentDay.objects.filter(payment_piggybanks=s24.id).order_by('date_of')
    for el in payments_for_obj24:
        new_value = el.value_of
        y24.append(new_value)
        new_date = str(el.date_of)
        x24.append(new_date)

    plt.figure(8)
    plt.figure(figsize=(14, 7))
    plt.subplot()
    plt.plot(x, y, marker='o',  label="TV", linewidth=3, linestyle='-.')
    plt.plot(x9, y9, marker='o', label="strój", linewidth=3, linestyle='--')
    plt.plot(x10, y10, marker='o', label="kons.", linewidth=3)
    plt.plot(x15, y15, marker='o', label="rower", linewidth=3, linestyle='--')
    plt.plot(x16, y16, marker='o', label="zmyw.", linewidth=3)
    plt.plot(x24, y24, marker='o', label="cel", linewidth=3, linestyle='--')

    plt.legend(bbox_to_anchor=(0.95, 1), loc='upper left', borderaxespad=0.)#boczna legenda
    plt.title('wykres wpłat dla celu')
    plt.xlabel('DATY')
    plt.ylabel('KWOTY')
    plt.grid(True)
    plt.margins(0.1)
    savefig('static/wykres-innego-typu.png')


def wykres_credit1():
    x_cr1 = []
    y_cr1 = []
    credit1 = Credits.objects.get(id=7)
    payments_for_cr1 = RepaymentDay.objects.filter(repayment_credits_id=credit1.id).order_by('repayment_date')
    obj_cr1_name = credit1.name
    for el in payments_for_cr1:
        new_value = el.repayment_value
        y_cr1.append(new_value)
        new_date = str(el.repayment_date)
        x_cr1.append(new_date)
    plt.figure(9)
    plt.figure(figsize=(9, 6))
    plt.title(f'wykres wpłat dla celu "{obj_cr1_name}"')
    plt.xlabel('DATY')
    plt.ylabel('KWOTY')
    plt.grid(True)
    plt.margins(0.1)
    plt.plot(x_cr1, y_cr1, 'c*', markersize=18)  # gwiazdka
    savefig('static/wykres-kredyt-1.png')


def wykres_credit2():
    x_cr2 = []
    y_cr2 = []
    credit2 = Credits.objects.get(id=12)
    payments_for_cr2 = RepaymentDay.objects.filter(repayment_credits_id=credit2.id).order_by('repayment_date')
    obj_cr2_name = credit2.name
    for el in payments_for_cr2:
        new_value = el.repayment_value
        y_cr2.append(new_value)
        new_date = str(el.repayment_date)
        x_cr2.append(new_date)
    plt.figure(10)
    plt.figure(figsize=(9, 6))
    plt.title(f'wykres wpłat dla celu "{obj_cr2_name}"')
    plt.xlabel('DATY')
    plt.ylabel('KWOTY')
    plt.margins(0.1)
    plt.bar(x_cr2, y_cr2)
    savefig('static/wykres-kredyt-2.png')


def wykres_piggybanks_all():
    pozycje = PiggyBanks.objects.all()
    names_of = []
    already_c = []
    piggybanks_minus = []
    for element in pozycje:
        names_of.append(element.money_for)
        take = AlreadyCollected.objects.filter(paymentday__payment_piggybanks_id=element.id).order_by('paymentday__date_of').last()
        piggybanks_minus.append(element.m_min - take.collected)
        already_c.append(take.collected)

    plt.figure(11)
    plt.figure(figsize=(10, 7))
    plt.style.use('ggplot')
    plt.title('wykres wpłat - wszystkie cele')
    plt.grid(True)
    plt.margins(0.1)
    plt.bar(names_of, already_c, label='Dotychczas uzbierane')
    plt.bar(names_of, piggybanks_minus, label='Brakujące kwoty do całości', bottom=already_c)
    plt.legend()
    savefig('static/wykres-inny-pball.png')


def wykres_spending():
    pozycje = Budget.objects.all()
    spending_names = []
    spending_values = []
    explode = []
    for element in pozycje:
        spending_names.append(element.name)
        spending_values.append(element.money)
        explode.append(0.1)

    plt.figure(12)
    plt.figure(figsize=(6, 5.5))
    plt.title('wykres wydatków', fontdict={'fontname': 'monospace', 'fontsize': 21})
    plt.pie(spending_values, explode=explode, labels=spending_names, autopct='%.2f')
    savefig('static/wykres-spending-pie.png')


def wykres_income_for_spending():
    income_all = Income.objects.all()
    for_calculation = []
    calc = 0
    for element in income_all:
        for_calculation.append(element.value_of_income)
    for elem in for_calculation:
        calc += elem

    queryset = MonthsBudget.objects.all().order_by('-month_date')
    xmonth = []
    ymonth = []
    for el in queryset:
        xmonth.append(el.chosen_name_of_month)
        ymonth.append(el.month_cost)
    xmonth1 = xmonth[0:12]
    ymonth1 = ymonth[0:12]
    xmonth1.reverse()
    ymonth1.reverse()
    ymonth2income_vs_spending = []
    for e in ymonth1:
        ymonth2income_vs_spending.append(calc - e)

    plt.figure(13)
    plt.figure(figsize=(11, 6.5))
    plt.bar(xmonth1, ymonth2income_vs_spending, color='#00FF00', label='kwoty po odjęciu miesięcznych wydatków')
    plt.bar(xmonth1, ymonth1, label='zapisane miesięczne koszty', color='#008080', bottom=ymonth2income_vs_spending)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
               ncol=2, mode="expand", borderaxespad=0.)
    plt.tick_params(axis='x', rotation=340)
    savefig('static/wykres-income-for-spending.png')


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')


class IncomeView(View):

    def get(self, request):
        all_income = Income.objects.all()
        form = IncomeForm()
        for_calculation = []
        calc = 0
        for element in all_income:
            for_calculation.append(element.value_of_income)
        for elem in for_calculation:
            calc += elem
        try:
            wykres_income_for_spending()
            return render(request, 'income.html', {"all_income": all_income, "form": form, "calc": calc})
        except Exception:
            return render(request, 'income.html', {"all_income":all_income, "form":form, "calc":calc})

    def post(self, request):
        all_income = Income.objects.all()
        additional_income = float(request.POST.get('additional_income'))
        for_calculation = []
        calc = 0
        for element in all_income:
            for_calculation.append(element.value_of_income)
        for elem in for_calculation:
            calc += elem
        sum_of = calc + additional_income
        form = IncomeForm(request.POST)
        if form.is_valid():
            name_of_income = form.cleaned_data['name_of_income']
            value_of_income = form.cleaned_data['value_of_income']
            income_description = form.cleaned_data['income_description']
            Income.objects.create(name_of_income=name_of_income,
                                  value_of_income=value_of_income,
                                  income_description=income_description)
            return render(request, 'income.html', {"sum_of":sum_of,"all_income": all_income, "form": form, "calc": calc})
        return render(request, 'income.html', {"sum_of":sum_of,"all_income": all_income, "form": form, "calc": calc})


class ModifyIncome(View):

    def get(self, request, id):
        one_income = Income.objects.get(id=id)
        form = IncomeForm(instance=one_income)
        return render(request, 'income-modify.html', {"one_income":one_income, "form":form})

    def post(self, request, id):
        form = IncomeForm(request.POST)
        one_income = Income.objects.get(id=id)
        if form.is_valid():
            name_of_income = form.cleaned_data['name_of_income']
            value_of_income = form.cleaned_data['value_of_income']
            income_description = form.cleaned_data['income_description']
            one_income.name_of_income = name_of_income
            one_income.value_of_income = value_of_income
            one_income.income_description = income_description
            one_income.save()
            return redirect('income')


class DeleteIncome(DeleteView):
    model = Income
    success_url = '/income'


class AdditionalIncomeView(View):

    def get(self, request):
        additional_income = AdditionalIncome.objects.all()
        form = AdditionalIncomeForm()
        return render(request, 'additional-income.html', {"additional_income":additional_income, "form":form})

    def post(self, request):
        additional_income = AdditionalIncome.objects.all()
        form = AdditionalIncomeForm(request.POST)
        if form.is_valid():
            chosen_name = form.cleaned_data['chosen_name']
            amount_only = form.cleaned_data['amount_only']
            amount_with_monthly = form.cleaned_data['amount_with_monthly']
            income_description = form.cleaned_data['income_description']
            AdditionalIncome.objects.create(chosen_name=chosen_name,
                                            amount_only=amount_only,
                                            amount_with_monthly=amount_with_monthly,
                                            income_description=income_description)
            return render(request, 'additional-income.html', {"additional_income":additional_income, "form": form})


class ModifyAdditionalIncome(View):

    def get(self, request, id):
        pozycja = AdditionalIncome.objects.get(id=id)
        form = AdditionalIncomeForm(instance=pozycja)
        return render(request, 'additional-modify.html', {"pozycja":pozycja, "form":form})

    def post(self, request, id):
        form = AdditionalIncomeForm(request.POST)
        pozycja = AdditionalIncome.objects.get(id=id)
        if form.is_valid():
            chosen_name = form.cleaned_data['chosen_name']
            amount_only = form.cleaned_data['amount_only']
            amount_with_monthly = form.cleaned_data['amount_with_monthly']
            income_description = form.cleaned_data['income_description']
            pozycja.chosen_name = chosen_name
            pozycja.amount_only = amount_only
            pozycja.amount_with_monthly = amount_with_monthly
            pozycja.income_description = income_description
            pozycja.save()
            return redirect('additional-income')


class DeleteAdditionalIncome(DeleteView):
    model = AdditionalIncome
    success_url = '/additional-income'


class BudgetView(View):

    def get(self, request):
        pozycje = Budget.objects.all()
        form = BudgetForm()
        try:
            wykres_spending()
            return render(request, 'budget.html', {"pozycje":pozycje, "form":form})
        except Exception:
            return render(request, 'budget.html', {"pozycje":pozycje, "form":form})

    def post(self, request):
        pozycje = Budget.objects.all()
        form = BudgetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            money = form.cleaned_data['money']
            monthly = form.cleaned_data['monthly']
            description = form.cleaned_data['description']
            Budget.objects.create(name=name, money=money, monthly=monthly, description=description)
            return render(request, 'budget.html', {"pozycje":pozycje, "form":form})
        additional = []
        counting = request.POST.getlist('counting')
        for element in pozycje:
            additional.append(request.POST.get(f'{element.id}'))
        my_sum = 0
        while counting != []:
            elem = float(counting.pop())
            my_sum += elem
        if additional != []:
            for el in additional:
                if el == '':
                    pass
                else:
                    add_to = float(el)
                    my_sum += add_to
        def set_session(request):
            request.session["suma_przekazana"] = my_sum
        set_session(request)
        return render(request, 'budget.html', {"counting": counting,
                                               "my_sum": my_sum,
                                               "pozycje": pozycje,
                                               "form": form})


class ModifyBudget(View):

    def get(self, request, id):
        pozycja = Budget.objects.get(id=id)
        form = BudgetForm(instance=pozycja)
        return render(request, 'modify-budget-pos.html', {"pozycja":pozycja, "form":form})

    def post(self, request, id):
        form = BudgetForm(request.POST)
        pozycja = Budget.objects.get(id=id)
        if form.is_valid():
            name = form.cleaned_data['name']
            money = form.cleaned_data['money']
            monthly = form.cleaned_data['monthly']
            description = form.cleaned_data['description']
            pozycja.name=name
            pozycja.money=money
            pozycja.monthly=monthly
            pozycja.description=description
            pozycja.save()
            return redirect('budget')


class DeleteBudget(DeleteView):
    model = Budget
    success_url = '/budget'


class MonthsBudgetView(View):

    def get(self, request):
        this_months_budget = MonthsBudget.objects.all()
        form = MonthsBudgetForm()
        try:
            wykres_month()
            return render(request, 'budget-months.html', {"this_months_budget":this_months_budget, "form":form})
        except Exception:
            return render(request, 'budget-months.html', {"this_months_budget":this_months_budget, "form":form})

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


class MonthsBudgetPropositionView(View):

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
        pozycja = MonthsBudget.objects.get(id=id)
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


class PiggyBanksView(View):
    def get(self, request):
        return render(request, 'piggy-banks.html')


class SavingAdd(View):

    def get(self, request):
        all_piggy_banks = PiggyBanks.objects.all()
        form = PiggyBanksForm()
        return render(request, 'add-new-piggy.html', {"all_piggy_banks":all_piggy_banks, "form":form})

    def post(self, request):
        all_piggy_banks = PiggyBanks.objects.all()
        form = PiggyBanksForm(request.POST)
        if form.is_valid():
            money_for = form.cleaned_data['money_for']
            m_min = form.cleaned_data['m_min']
            description = form.cleaned_data['description']
            PiggyBanks.objects.create(money_for=money_for, m_min=m_min, description=description)
            s1 = PiggyBanks.objects.get(money_for=money_for)
            a1 = AlreadyCollected.objects.create(collected=0)
            PaymentDay.objects.create(payment_piggybanks=s1, payment_collected=a1)
            return redirect('saving-goals')


class SavingGoals(View):

    def get(self, request):
        all_piggy_banks = PiggyBanks.objects.all()
        form = PiggyBanksForm()
        try:
            wykres_piggybanks_all()
            return render(request, 'saving-goals.html', {"all_piggy_banks":all_piggy_banks, "form":form})
        except Exception:
            return render(request, 'saving-goals.html', {"all_piggy_banks":all_piggy_banks, "form":form})

    def post(self, request):
        all_piggy_banks = PiggyBanks.objects.all()
        form = PiggyBanksForm(request.POST)
        if form.is_valid():
            money_for = form.cleaned_data['money_for']
            m_min = form.cleaned_data['m_min']
            description = form.cleaned_data['description']
            PiggyBanks.objects.create(money_for=money_for, m_min=m_min, description=description)
            s1 = PiggyBanks.objects.get(money_for=money_for)
            a1 = AlreadyCollected.objects.create(collected=0)
            PaymentDay.objects.create(payment_piggybanks=s1, payment_collected=a1)
            return render(request, 'saving-goals.html', {"all_piggy_banks":all_piggy_banks, "form": form})


class SavingCharts(View):

    def get(self, request):
        s2 = PiggyBanks.objects.values_list('money_for', flat=True).order_by('pk')
        try:
            wykres8()
            wykres9()
            wykres10()
            wykres15()
            wykres16()
            wykres24()
            wykres_innego_typu()
            return render(request, 'charts.html')
        except Exception:
            return render(request, 'charts.html')


class ModifySaving(View):

    def get(self, request, id):
        pozycja = PiggyBanks.objects.get(id=id)
        form = PiggyBanksForm(instance=pozycja)
        return render(request, 'modify-saving.html', {"pozycja":pozycja, "form":form})

    def post(self, request, id):
        form = PiggyBanksForm(request.POST)
        pozycja = PiggyBanks.objects.get(id=id)
        if form.is_valid():
            money_for = form.cleaned_data['money_for']
            m_min = form.cleaned_data['m_min']
            description = form.cleaned_data['description']
            pozycja.money_for = money_for
            pozycja.m_min = m_min
            pozycja.description = description
            pozycja.save()
            return redirect('saving-goals')


class SavingMistake(View):

    def get(self, request):
        all_piggy_banks = PiggyBanks.objects.all()
        piggy_mist_info = request.session.get("payment_info")
        return render(request, 'mistake.html', {"piggy_mist_info":piggy_mist_info, "all_piggy_banks":all_piggy_banks})

    def post(self, request):
        mistake_in = request.POST.get('mistake_in')
        mistake_id = int(mistake_in)
        mistake_value = request.POST.get('mistake_value')
        mistake_value_float = float(mistake_value)
        correct_value = request.POST.get('correct_value')
        correct_value_float = float(correct_value)
        last_mistake = PaymentDay.objects.filter(payment_piggybanks_id=mistake_id).last()
        last_to_change = AlreadyCollected.objects.get(id=last_mistake.payment_collected_id)
        last_mistake.value_of = correct_value_float
        last_mistake.save()
        last_to_change.collected -= mistake_value_float
        last_to_change.collected += correct_value_float
        last_to_change.save()
        return redirect('piggy-banks')

results_list = []

class SavingTime(View):

    def get(self, request):
        return render(request, 'saving-time.html')

    def post(self, request):
        amount_of1 = request.POST.get('amount_of')
        amount_month2 = request.POST.get('amount_month')
        res0 = float(amount_of1) / float(amount_month2)
        res1 = math.ceil(res0)
        results_list.append(f"{amount_of1} : {amount_month2} = {res1} miesięcy \n")
        results_list.reverse()
        return render(request, 'saving-time.html', {'res1':res1, "results_list":results_list})


results_list2 = []

class SavingAmount(View):

    def get(self, request):
        return render(request, 'saving-amount.html')

    def post(self, request):
        amount_of1 = request.POST.get('amount_of')
        amount_month2 = request.POST.get('amount_month')
        res0 = float(amount_of1) / float(amount_month2)
        res1 = Decimal("%.2f" % res0)
        results_list2.append(f"{amount_of1} : {amount_month2} = {res1} złotych \n")
        results_list2.reverse()
        return render(request, 'saving-amount.html', {'res1':res1, "results_list2":results_list2})


class DeleteSaving(DeleteView):
    model = PiggyBanks
    success_url = '/saving-goals'


class AlreadyCollectedView(View):

    def get(self, request):
        collected = AlreadyCollected.objects.all()
        all_piggy_banks = PiggyBanks.objects.all()
        return render(request, 'saving-collected.html', {"collected":collected,
                                                         "all_piggy_banks":all_piggy_banks})

    def post(self, request):
        collected = AlreadyCollected.objects.all()
        all_piggy_banks = PiggyBanks.objects.all()
        try:
            choose = request.POST.get('choose')
            chosen = int(choose)
            def set_session2(request):
                request.session["chosen_id"] = chosen # id all_piggy_banks
            set_session2(request)
            return render(request, 'saving-collected.html', {"chosen": chosen,
                                                            "collected": collected,
                                                            "all_piggy_banks": all_piggy_banks})
        except Exception:
            mine_x = request.session.get("chosen_id"),
            for e in mine_x:
                mine_new_x = e
            congrats = request.POST.get('congrats')
            congrats2 = float(congrats)
            mine_object = PaymentDay.objects.filter(payment_piggybanks_id=mine_new_x).last()

            try:
                PaymentDay.objects.get(payment_piggybanks_id=mine_new_x, date_of=date.today())
                piggy_mist_info = request.session.get("payment_info")
                msg = "Dziś już wpłacono na owy cel! Czyżby nastąpiła pomyłka przy wpisywaniu kwoty?"
                return render(request, 'mistake.html', {"piggy_mist_info":piggy_mist_info, "all_piggy_banks": all_piggy_banks, "msg":msg})
            except Exception:

                new_today=PaymentDay.objects.create(payment_piggybanks_id=mine_new_x, date_of=date.today(), payment_collected_id=mine_object.payment_collected_id, value_of=mine_object.value_of)
                def set_session4(request):
                    request.session["payment_info"] = congrats #
                set_session4(request)
                new_today.payment_piggybanks_id = mine_new_x
                new_today.payment_collected_id = mine_object.payment_collected_id
                new_today.save()
                already_c = AlreadyCollected.objects.get(id=new_today.payment_collected_id)
                already_c.collected += congrats2
                already_c.save()
                new_today.value_of += congrats2
                new_today.save()
                return render(request, 'saving-collected.html', {"collected": collected,
                                                                "all_piggy_banks": all_piggy_banks})


class StockView(View):
    def get(self, request):
        form = StockForm()
        ctx = Stock.objects.all()
        spolka = "cdr"
        p = {"s": spolka}
        spolka2 = "pzu"
        p2 = {"s": spolka2}
        answer = requests.get("http://stooq.pl/q/", params=p)
        soup = BeautifulSoup(answer.text, 'html.parser')
        answer2 = requests.get("http://stooq.pl/q/", params=p2)
        soup2 = BeautifulSoup(answer2.text, 'html.parser')
        cdr_kurs = soup.find("span", id=f"aq_{spolka}_c1")
        cdr_kurs2 = float(cdr_kurs.text)
        pzu_kurs = soup2.find("span", id=f"aq_{spolka2}_c2")
        pzu_kurs2 = float(pzu_kurs.text)
        # niekiedy zmienia się id - uwaga!

        if cdr_kurs2:
            cdr_interests = Stock.objects.get(name='CDR')
            jednostki_cdr = cdr_interests.interests
            value_of_cdr = jednostki_cdr * cdr_kurs2
        if pzu_kurs2:
            pzu_interests = Stock.objects.get(name='PZU')
            jednostki_pzu = pzu_interests.interests
            value_of_pzu = jednostki_pzu * pzu_kurs2

        return render(request, 'stock.html', {"cdr_kurs2":cdr_kurs2,
                                              "pzu_kurs2":pzu_kurs2,
                                              "value_of_cdr":value_of_cdr,
                                              "value_of_pzu":value_of_pzu,
                                              "ctx":ctx, "form":form,
                                              })

    def post(self, request):
        form = StockForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            enter_price = form.cleaned_data['enter_price']
            interests = form.cleaned_data['interests']
            value_of = form.cleaned_data['value_of']
            dividend = form.cleaned_data['dividend']
            type_of_market = form.cleaned_data['type_of_market']
            www = form.cleaned_data['www']
            Stock.objects.create(name=name, enter_price=enter_price, interests=interests, value_of=value_of,
                                 dividend=dividend, type_of_market=type_of_market, www=www)
            return redirect('stock')



class ModifyStock(View):

    def get(self, request, id):
        pozycja = Stock.objects.get(id=id)
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
            dividend = form.cleaned_data['dividend']
            type_of_market = form.cleaned_data['type_of_market']
            www = form.cleaned_data['www']
            pozycja.name = name
            pozycja.enter_price = enter_price
            pozycja.interests = interests
            pozycja.value_of = value_of
            pozycja.dividend = dividend
            pozycja.type_of_market = type_of_market
            pozycja.www = www
            pozycja.save()
            return redirect('stock')


class DeleteStock(DeleteView):
    model = Stock
    success_url = '/stock'


class CreditView(View):

    def get(self, request):
        credits_objects = Credits.objects.all()
        form = CreditsForm()
        return render(request, 'credit.html', {"credits_objects":credits_objects, "form":form})

    def post(self, request):
        credits_objects = Credits.objects.all()
        form = CreditsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            credit_amount = form.cleaned_data['credit_amount']
            should_end_on = form.cleaned_data['should_end_on']
            description = form.cleaned_data['description']
            Credits.objects.create(name=name, credit_amount=credit_amount, should_end_on=should_end_on, description=description)
            c1 = Credits.objects.get(name=name)
            r1 = Repayment.objects.create(collected_money=0)
            RepaymentDay.objects.create(repayment_credits=c1, repayment_collected=r1)
            return render(request, 'credit.html', {"credits_objects":credits_objects, "form":form})


class ModifyCredit(View):

    def get(self, request, id):
        credits_objects = Credits.objects.get(id=id)
        form = CreditsForm(instance=credits_objects)
        return render(request, 'modify-credit.html', {"credits_objects":credits_objects, "form":form})

    def post(self, request, id):
        credits_objects = Credits.objects.get(id=id)
        form = CreditsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            credit_amount = form.cleaned_data['credit_amount']
            should_end_on = form.cleaned_data['should_end_on']
            description = form.cleaned_data['description']
            credits_objects.name = name
            credits_objects.credit_amount = credit_amount
            credits_objects.should_end_on = should_end_on
            credits_objects.description = description
            credits_objects.save()
            return redirect('credits')


class DeleteCredit(DeleteView):
    model = Credits
    success_url = '/credits'


class CreditPayments(View):

    def get(self, request, id):
        credits_objects = Credits.objects.get(id=id)
        rep = RepaymentDay.objects.filter(repayment_credits_id=id).first()
        repaymentday_objects = RepaymentDay.objects.filter(repayment_credits_id=id)
        znajdz = rep.repayment_collected_id
        repayments_this_id = Repayment.objects.get(id=znajdz)
        return render(request, 'credit-payments.html', {"credits_objects": credits_objects,
                                                        "repayments_this_id":repayments_this_id,
                                                        "repaymentday_objects":repaymentday_objects})

    def post(self, request, id):
        credits_objects = Credits.objects.get(id=id)
        amount = request.POST.get('amount')
        amount2 = float(amount)
        credit_obj = Credits.objects.get(id=id)
        credits_objects = Credits.objects.all()
        last_payments = RepaymentDay.objects.filter(repayment_credits_id=credit_obj.id).last()
        try:
            if RepaymentDay.objects.get(repayment_credits_id=id, repayment_date=date.today()):
                cred_mist_info = request.session.get("repayment_info")
                msg = "Dziś już wpłacono na owy cel! Czyżby nastąpiła pomyłka przy wpisywaniu kwoty?"
                return render(request, 'credit-mistake.html', {"cred_mist_info":cred_mist_info,"credits_objects": credits_objects, "msg":msg})

        except Exception:
            new_paym = RepaymentDay.objects.create(repayment_credits_id=id,
                                                   repayment_date=date.today(),
                                                   repayment_collected_id=last_payments.repayment_collected_id,
                                                   repayment_value=amount2)
            def set_session3(request):
                request.session["repayment_info"] = new_paym.repayment_value
            set_session3(request)
            increasing = Repayment.objects.get(id=new_paym.repayment_collected_id)
            increasing.collected_money += amount2
            increasing.save()
            new_paym.repayment_value = amount2
            new_paym.save()
            return render(request, 'credit-payments.html', {"credits_objects": credits_objects})


class CreditMistake(View):

    def get(self, request):
        credits_objects = Credits.objects.all()
        cred_mist_info = request.session.get("repayment_info")
        return render(request, 'credit-mistake.html', {"cred_mist_info":cred_mist_info, "credits_objects": credits_objects})

    def post(self, request):
        credit_mistake = request.POST.get('credit-mistake')
        mistake_id = int(credit_mistake)
        mistake_value = request.POST.get('mistake_value')
        mistake_value_float = float(mistake_value)
        correct_value = request.POST.get('correct_value')
        correct_value_float = float(correct_value)

        credit_mistake = RepaymentDay.objects.filter(repayment_credits_id=mistake_id).last()
        last_to_change = Repayment.objects.get(id=credit_mistake.repayment_collected_id)
        credit_mistake.repayment_value = correct_value_float
        credit_mistake.save()
        last_to_change.collected_money -= mistake_value_float
        last_to_change.collected_money += correct_value_float
        last_to_change.save()
        return redirect('credits')


class StockViewWithoutScraper(View):

    def get(self, request):
        form = StockForm()
        ctx = Stock.objects.all()
        return render(request, 'stock2.html', {"ctx":ctx, "form":form})

    def post(self, request):
        form = StockForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            enter_price = form.cleaned_data['enter_price']
            interests = form.cleaned_data['interests']
            value_of = form.cleaned_data['value_of']
            dividend = form.cleaned_data['dividend']
            type_of_market = form.cleaned_data['type_of_market']
            www = form.cleaned_data['www']
            Stock.objects.create(name=name, enter_price=enter_price, interests=interests, value_of=value_of,
                                 dividend=dividend, type_of_market=type_of_market, www=www)
            return redirect('stock-without')


class ModifyStockWithout(View):

    def get(self, request, id):
        pozycja = Stock.objects.get(id=id)
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
            dividend = form.cleaned_data['dividend']
            type_of_market = form.cleaned_data['type_of_market']
            www = form.cleaned_data['www']
            pozycja.name = name
            pozycja.enter_price = enter_price
            pozycja.interests = interests
            pozycja.value_of = value_of
            pozycja.dividend = dividend
            pozycja.type_of_market = type_of_market
            pozycja.www = www
            pozycja.save()
            return redirect('stock-without')
