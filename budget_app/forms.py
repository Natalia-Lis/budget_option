from django import forms
from .models import *
from .views import *


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(BudgetForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False


class PiggyBanksForm(forms.ModelForm):
    class Meta:
        model = PiggyBanks
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(PiggyBanksForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False



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


class CreditsForm(forms.ModelForm):
    class Meta:
        model = Credits
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CreditsForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['should_end_on'].required = False
#
# class AlreadyCollectedForm(forms.Form): #?
#     date_of = models.DateField(auto_now_add=True)
#     payment_skarbonki = models.ForeignKey(Skarbonki, on_delete=models.CASCADE)
#     payment_collected = models.ForeignKey(AlreadyCollected, on_delete=models.CASCADE)
#     value_of = models.FloatField(default=0)
#
#     collected = models.FloatField(default=0)
#     target = models.ManyToManyField(Skarbonki, through='PaymentDay')
