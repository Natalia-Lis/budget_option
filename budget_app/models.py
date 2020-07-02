from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Budget(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa')
    money = models.FloatField(verbose_name='Kwota')
    monthly = models.BooleanField(default=True, verbose_name='Czy to koszt comiesięczny?')
    description = models.TextField(null=True, verbose_name='Opis zobowiązania')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('delete-budget', kwargs={'pk': self.pk})


class PiggyBanks(models.Model):
    money_for = models.CharField(max_length=64, verbose_name='Nazwa dla określonego celu')
    m_min = models.FloatField(verbose_name='Kwota potrzebna na ten cel')
    description = models.TextField(null=True, verbose_name='Opcjonalny opis dla celu')

    def __str__(self):
        return self.money_for

    def get_absolute_url(self):
        return reverse('delete-saving', kwargs={'pk': self.pk})


class MonthsBudget(models.Model):
    chosen_name_of_month = models.CharField(max_length=64, verbose_name="Nazwa jaką chcesz wpisać dla tego miesiąca:")
    month_cost = models.FloatField(verbose_name='Miesięczne koszty')
    description = models.CharField(max_length=256, null=True, verbose_name='Opcjonalny opis')
    month_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.chosen_name_of_month

    def get_absolute_url(self):
        return reverse('months-budget', kwargs={'pk': self.pk})


class Stock(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa dla określonej akcji')
    enter_price = models.FloatField(verbose_name='Cena w momencie zakupu')
    interests = models.IntegerField(verbose_name='Liczba zakupionych udziałów')
    value_of = models.FloatField(null=True, verbose_name='Wartość początkowa zakupu udziałów')
    dividend = models.NullBooleanField(default=False, verbose_name='Czy jest wypłacana dywidenda?')
    type_of_market = models.CharField(max_length=64, null=True, verbose_name='Nazwa dla rodzaju rynku akcji')
    www = models.CharField(max_length=256, null=True, verbose_name='Link do strony internetowej inwestora dla akcji')

    def __str__(self):
        return self.name


class AlreadyCollected(models.Model):
    collected = models.FloatField(default=0)
    target = models.ManyToManyField(PiggyBanks, through='PaymentDay')


class PaymentDay(models.Model):
    date_of = models.DateField(auto_now_add=True)
    value_of = models.FloatField(default=0)
    payment_piggybanks = models.ForeignKey(PiggyBanks, on_delete=models.CASCADE)
    payment_collected = models.ForeignKey(AlreadyCollected, on_delete=models.CASCADE)


class Credits(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa dla kredytu')
    credit_amount = models.FloatField(verbose_name='Kwota kredytu')
    should_end_on = models.DateField(null=True, verbose_name='Planowana końcowa spłata (YYYY-MM-DD)')
    description = models.TextField(null=True, verbose_name='Opcjonalny opis')

    def __str__(self):
        return self.name


class Repayment(models.Model):
    collected_money = models.FloatField(default=0)
    payment_target = models.ManyToManyField(Credits, through='RepaymentDay')


class RepaymentDay(models.Model):
    repayment_date = models.DateField(auto_now_add=True)
    repayment_value = models.FloatField(default=0)
    repayment_credits = models.ForeignKey(Credits, on_delete=models.CASCADE)
    repayment_collected = models.ForeignKey(Repayment, on_delete=models.CASCADE)


class Income(models.Model):
    name_of_income = models.CharField(max_length=128, verbose_name='Nazwa dla przychodu')
    value_of_income = models.FloatField(verbose_name='Kwota wpływu')
    income_description = models.TextField(null=True, verbose_name='Opcjonalny opis')

    def __str__(self):
        return self.name_of_income

    def get_absolute_url(self):
        return reverse('delete-income', kwargs={'pk': self.pk})


class AdditionalIncome(models.Model):
    chosen_name = models.CharField(max_length=64, verbose_name='Nazwa dla dodatkowego przychodu')
    amount_only = models.FloatField(null=True, verbose_name='Zapisywana kwota dodatkowa (*można pozostawić wolne)')
    amount_with_monthly = models.FloatField(null=True, verbose_name='Kwota dodatkowa wraz z miesięcznymi wpływami (*można pozostawić wolne)')
    income_description = models.CharField(null=True, max_length=128, verbose_name='Opis dla wpisywanego dodatkowego przychodu')
    income_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.chosen_name