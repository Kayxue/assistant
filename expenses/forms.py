from django import forms
from .models import *

class MoneyForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = '__all__'
    widgets = {
      'item': forms.TextInput(attrs={'class': 'form-control'}),
      'category': forms.Select(attrs={'class': 'form-control'}),
      'amount': forms.NumberInput(attrs={'class': 'form-control'}),
    }