from django.db import models
from datetime import datetime 


class Reporter(models.Model):
    nome = models.CharField(max_length=70)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    data_pub = models.DateTimeField()
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.title

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    titulo = models.CharField(max_length=3, choices=TITLE_CHOICES)
    dt_nasc = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    
    def __str__(self):
        return self.nome

'''
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
'''

# Create your models here.
