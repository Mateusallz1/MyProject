from django.shortcuts import render, redirect
from myapp.forms import *
from myapp.models import *
# Create your views here.

def index(request):
    return render(request, 'bemvindo.html')

def list_posts(request):
    posts = Post.objects.all() # Se fossem muitos registros é interessante que seja por demanda...
    return render(request, "list_posts.html", {'posts': posts})

def list_reporters(request):
    reporters = Reporter.objects.all()
    return render(request, "list_reporters.html", {'reporters': reporters})

def list_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, "list_artigos.html", {'artigos': artigos})

def list_autores(request):
    autores = Autor.objects.all() # Se fossem muitos registros é interessante que seja por demanda...
    return render(request, "list_autores.html", {'autores': autores})

def list_livros(request):
    livros = Livro.objects.all() # Se fossem muitos registros é interessante que seja por demanda...
    return render(request, "list_livros.html", {'livros': livros})

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid(): 
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_posts')
    else:
        form = PostForm()
        return render(request, "add.html", {'form': form})

def add_reporter(request):
    if request.method == "POST":
        form = ReporterForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_reporters')
    else:
        form = ReporterForm()
        return render(request, "add.html", {'form': form})
    
def add_artigo(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST)
        if form.is_valid(): 
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_artigos')
    else:
        form = ArtigoForm()
        return render(request, "add.html", {'form': form})

def add_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid(): 
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_autores')
    else:
        form = AutorForm()
        return render(request, "add.html", {'form': form})
    
def add_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid(): 
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_livros')
    else:
        form = LivroForm()
        return render(request, "add.html", {'form': form})