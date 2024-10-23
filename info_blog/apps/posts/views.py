from django.shortcuts import render
from .models import Post

def home(request):
    """
    Funcion que retorna la vista de index.html y carga en el documento los
    datos de las publicaciones traidas del modelo Post
    """
    posts = Post.objects.filter(activo=True)
    context = {'posts': posts}
    return render(request, 'index.html', context)
