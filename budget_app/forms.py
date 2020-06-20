from django import forms
from .models import *
from .views import *


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(BudgetForm, self).__init__(*args, **kwargs)
        self.fields['opis'].required = False


class SkarbonkiForm(forms.ModelForm):
    class Meta:
        model = Skarbonki
        exclude = ['zapas']
    def __init__(self, *args, **kwargs):
        super(SkarbonkiForm, self).__init__(*args, **kwargs)
        self.fields['opis'].required = False
        self.fields['m_max'].required = False


class MonthsBudgetForm(forms.ModelForm):
    class Meta:
        model = MonthsBudget
        exclude = ['month_date']
    def __init__(self, *args, **kwargs):
        super(MonthsBudgetForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)
        self.fields['value_of'].required = False
        self.fields['price'].required = False
        self.fields['dividend'].required = False
        self.fields['type_of_market'].required = False
        self.fields['www'].required = False
