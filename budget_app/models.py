from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse



class Budget(models.Model):
    name = models.CharField(max_length=64)
    money_min = models.FloatField()
    money_max = models.FloatField(null=True)
    monthly = models.BooleanField(default=True)
    opis = models.TextField(null=True)
    zapasowa = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('delete-budget', kwargs={'pk': self.pk})


class Skarbonki(models.Model):
    money_for = models.CharField(max_length=64)
    m_min = models.FloatField()
    m_max = models.FloatField(null=True)
    month = models.BooleanField(default=True)
    opis = models.TextField(null=True)
    zapas = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.money_for

    def get_absolute_url(self):
        return reverse('delete-skarb', kwargs={'pk': self.pk})


class MonthsBudget(models.Model):
    chosen_name_of_month = models.CharField(max_length=64, verbose_name="Nazwa jaką chcesz wpisać dla tego miesiąca:")
    month_cost = models.FloatField()
    description = models.CharField(max_length=256, null=True)
    month_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.chosen_name_of_month

    def get_absolute_url(self):
        return reverse('months-budget', kwargs={'pk': self.pk})
