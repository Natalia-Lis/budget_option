from django import forms
from .models import *
from .views import *


class BudgetForm(forms.ModelForm):
    # address = forms.CharField(required=False)
    class Meta:
        model = Budget
        exclude = ['zapasowa']
    def __init__(self, *args, **kwargs):
        super(BudgetForm, self).__init__(*args, **kwargs)
        self.fields['opis'].required = False
        self.fields['money_max'].required = False


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
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(MonthsBudgetForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False

