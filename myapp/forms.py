from django.forms import ModelForm
from myapp.models import *
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post 
        fields = '__all__'

class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = ['nome']

class ArtigoForm(ModelForm):
    class Meta:
        model = Artigo
        fields = "__all__"
        widgets = {
            'data_pub': forms.DateInput(
                attrs = {
                    'type': 'date',
                }
            )
        }
