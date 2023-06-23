
from django import forms

from rol.models import Rol


class RolForm(forms.ModelForm):

    class Meta:
        model = Rol
        fields = ['typerol' ,]
