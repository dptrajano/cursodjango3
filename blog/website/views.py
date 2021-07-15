from django.shortcuts import render
from .models import Post, Contact

def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Html']

    list_posts = Post.objects.all() # váriavel list_posts = recebe classe Post do models e pega todos os campos do banco de dados

    data = {
        'name': 'Curso de Django 3',
        'lista_tecnologias': lista,
        'posts': list_posts}

    return render(request, 'index.html', data) # vai renderizar o template index.html e carregar as informações de data

def post_detail(request, id):
    post = Post.objects.get(id=id) # váriavel post = recebe classe Post do models e pega (get) o id do banco de dados
    return render(request, 'post_detail.html', {'post': post}) # vai renderizar o template post_detail.html com base na variavel post (linha de cima)

def save_form(request):
    name=request.POST['name']
    Contact.objects.create(
        name=name,
        email=request.POST['email'],
        message=request.POST['message']
    )
    return render(request, 'contact_success.html', {'name_contact': name})