"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from budget_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('budget/', BudgetView.as_view(), name='budget'),
    path('modify-budget/<int:id>/', ModifyBudget.as_view(), name='modify-budget'),
    path('delete-budget/<int:pk>/', DeleteBudget.as_view(), name='delete-budget'),
    path('months-budget-proposition/', MonthsBudgetPropositionView.as_view(), name='months-proposition'),
    path('months-budget/', MonthsBudgetView.as_view(), name='months-budget'),
    path('modify-months/<int:id>/', ModifyMonths.as_view(), name='modify-months'),
    path('delete-months/<int:pk>/', DeleteMonths.as_view(), name='delete-months'),

    path('piggy-banks/', PiggyBanksView.as_view(), name='piggy-banks'),
    path('saving-goals/', SavingGoals.as_view(), name='saving-goals'),

    path('charts/', SavingCharts.as_view(), name='charts'),

    path('saving-time/', SavingTime.as_view(), name='saving-time'),
    path('saving-amount/', SavingAmount.as_view(), name='saving-amount'),
    path('saving-mistake/', SavingMistake.as_view(), name='saving-mistake'),
    path('saving-collected/', AlreadyCollectedView.as_view(), name='saving-collected'),
    path('modify-saving/<int:id>/', ModifySaving.as_view(), name='modify-saving'),
    path('delete-saving/<int:pk>/', DeleteSaving.as_view(), name='delete-saving'),

    path('stock/', StockView.as_view(), name='stock'),
    path('modify-stock/<int:id>/', ModifyStock.as_view(), name='modify-stock'),
    path('delete-stock/<int:pk>/', DeleteStock.as_view(), name='delete-stock'),

    path('credits/', CreditView.as_view(), name='credits'),
    path('credit-payments/<int:id>/', CreditPayments.as_view(), name='credit-payments'),
    path('modify-credit/<int:id>/', ModifyCredit.as_view(), name='modify-credit'),
    path('delete-credit/<int:pk>/', DeleteCredit.as_view(), name='delete-credit'),

    path('chart1/', ChartSaving1.as_view(), name='chart1'),
    path('chart2/', ChartSaving2.as_view(), name='chart2'),
    path('chart3/', ChartSaving3.as_view(), name='chart3'),
    path('chart4/', ChartSaving4.as_view(), name='chart4'),
    path('chart5/', ChartSaving5.as_view(), name='chart5'),
    path('chart6/', ChartSaving6.as_view(), name='chart6'),
    path('chart7/', ChartSaving7.as_view(), name='chart7'),

]
