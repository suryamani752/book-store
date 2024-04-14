from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('book', views.book, name = 'book'),
    path('authors', views.authors, name = 'authors'),
    path('authordetail/<int:authorId>', views.authorDetail, name = 'authordetail'),
    path('about', views.about, name = 'about')
]