from django import forms
from .models import Logro

class LogroForm(forms.ModelForm):
    class Meta:
        model = Logro
        fields = ('nombre', 'description', 'video')
