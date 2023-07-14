
from django import forms

from rol.models import Rol


class RolForm(forms.ModelForm):

    class Meta:
        model = Rol
        fields = ['typerol' ,]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})   
