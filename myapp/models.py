from django.db import models
from datetime import datetime 

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    senha = models.CharField(max_length=8)
    data_nascimento = models.DateField()
    
class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)  
    contatos = models.ManyToManyField('self')

class Postagem(models.Model):
    texto = models.CharField(max_length=350)
    data = models.DateField(auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete = models.CASCADE)
    
class Comentario(models.Model):
    texto = models.CharField(max_length=150)
    data = models.DateField(auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete = models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete = models.CASCADE)

class Reacao(models.Model):
    tipo = models.CharField(max_length=10)
    data = models.DateField(auto_now_add=True)
    postagem = models.ForeignKey(Postagem, on_delete = models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete = models.CASCADE)
    peso = models.CharField(max_length=35)

# Create your models here.
