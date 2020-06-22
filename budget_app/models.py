from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse



class Budget(models.Model):
    name = models.CharField(max_length=64)
    money = models.FloatField()
    monthly = models.BooleanField(default=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('delete-budget', kwargs={'pk': self.pk})


class PiggyBanks(models.Model):
    money_for = models.CharField(max_length=64)
    m_min = models.FloatField()
    description = models.TextField(null=True)

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
    name = models.CharField(max_length=64)
    enter_price = models.FloatField()
    interests = models.IntegerField()
    value_of = models.FloatField(null=True)
    price = models.FloatField(null=True)
    dividend = models.NullBooleanField(default=False)
    type_of_market = models.CharField(max_length=64, null=True)
    www = models.CharField(max_length=256, null=True)

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
    should_end_on = models.DateField(null=True, verbose_name='Data planowanej końcowej spłaty')
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
