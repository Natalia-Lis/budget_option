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
    path('skarbonki/', SkarbonkiView.as_view(), name='skarbonki'),
    path('akc/', Akc.as_view(), name='akc'),
    path('skar-cele/', SkarbonkiCele.as_view(), name='skar-cele'),
    path('skar-nowy/', SkarbonkiNowy.as_view(), name='skar-nowy'),
    path('skar-czas/', SkarbonkiCzas.as_view(), name='skar-czas'),
    path('skar-kwota/', SkarbonkiKwota.as_view(), name='skar-kwota'),
    path('months-budget/', MonthsBudgetView.as_view(), name='months-budget'),
    path('modify-budget/<int:id>/', ModifyBudget.as_view(), name='modify-budget'),
    path('delete-budget/<int:pk>/', DeleteBudget.as_view(), name='delete-budget'),
    path('modify-skarb/<int:id>/', ModifySkarbonki.as_view(), name='modify-skarb'),
    path('delete-skarb/<int:pk>/', DeleteSkarbonki.as_view(), name='delete-skarb'),
    path('modify-months/<int:id>/', ModifyMonths.as_view(), name='modify-months'),
    path('delete-months/<int:pk>/', DeleteMonths.as_view(), name='delete-months'),

]
