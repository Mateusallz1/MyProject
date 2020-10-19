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

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"
        widgets = {
            'dt_nasc': forms.DateInput(
                attrs={
                    'type': 'date',
            }
        )
    }

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'