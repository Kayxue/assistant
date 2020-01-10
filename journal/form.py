from django import forms
from .models import *

class DiaryForm(forms.ModelForm):
  class Meta:
    model = Journal
    fields = ['content']
    widgets = {
      'content': forms.Textarea(attrs={'class': 'form-control'}),
    }