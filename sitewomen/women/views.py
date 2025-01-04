
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [ {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
            {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
            {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True}, 
            
            ]

def index(requset):
    data = {'title': "главная страница", 'menu': menu, 'posts': data_db}
    return render(requset,'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {'title': "О сайте", 'menu': menu})

def categories(request, cat_id):
    return HttpResponse(f"<h1>Cтатьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug (request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Cтатьи по категориям</h1><p>slug: {cat_slug} </p>")

def archive(request, year):
     if year > 2025:
         uri = reverse('cats', args=('music', ))
         return redirect(uri)
     return HttpResponse(f"<h1>Архив по годам</h1><p> {year} </p>")

def padge_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def show_post(request, post_id):
    return HttpResponse(f"<h1>Отображение статьи с id = {post_id}")

def addpage(request):
    HttpResponse("Добавление статьи")

def contact(request):
    HttpResponse("Обратная связь")

def login(request):
    HttpResponse("Авторизация")




