from django import forms
from .models import Input

class InputForms(forms.ModelForm):
    class Meta :
        model = Input
        fields = ('kategory', 'body', 'image')
        widgets = {
            "kategory" : forms.Select(
                attrs={
                    'class': 'form-select',
                    'type':'text',
                    'required':True,
                    'data-style':'btn btn-danger btn-block',
                    #'title':'KTP, KK, STNK, dsb.',
                    'data-size':'7'
                }),
            "body" : forms.Textarea(
                attrs={
                    'class': 'form-control textarea-limited',
                    'type':'text',
                    'placeholder':"untuk memberikan catatan pada file",
                    'rows':'13',
                    'maxlength':'150',
                    'required':True,
                }),
           # <span class="btn btn-outline-default btn-round btn-file"><span class="fileinput-new">
            "image" : forms.FileInput(
                attrs={
                    'class' : 'btn btn-outline-default btn-round btn-file',
                    'type' : 'file',
                    'multiple' : True,
                    #'multiple name' : 'inputan'
                    
                }
                
            )
        }