from django import forms
from .models import Canvas

class CanvasForm(forms.ModelForm):
  class Meta: 
    model = Canvas
    fields = ['size', 'material', 'form']   

    widgets = {
      'size': forms.Select(attrs={'class': 'form-select'}),
      'material': forms.Select(attrs={'class': 'form-select'}),
      'form': forms.Select(attrs={'class': 'form-select'})
    }
