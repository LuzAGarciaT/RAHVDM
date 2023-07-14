from django import forms

from teacher.models import Teacher


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['typerol' , 'identification', 'names', 'lastnames', 'email', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})   
    
    