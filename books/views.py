from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author
from .models import Book
from django.http import Http404
# Create your views here.

def index(request):
    context = {
        'book_list' : Book.objects.all()
    }
    return render(request, 'index.html', context)

def authors(request):
    context = {
        'authors_list' : Author.objects.all()
    }
    return render(request, 'authors.html', context)

def book(request):
    context = {
            'book_list' : Book.objects.all(),
            'author_list' : Author.objects.all()
        }
    return render(request, 'book.html', context)

def authorDetail(request, authorId): 
    try:
        context = {
            'book_detail' : Book.objects.filter(author_id=authorId),
            'author_detail' : Author.objects.get(pk=authorId)
        }
    except Author.DoesNotExist:
        raise Http404("Writer does not exist") 
    return render(request, 'authorDetail.html', context)

def about(request):
    return render(request, 'about.html')

""" Examples
    from django.utils import timezone

     from books.models import Author,Book

    author = Author(name="J.K.Rowling",created = timezone.now())

    author
    <Author: J.K.Rowling>

    author.save()

    book = author.book_set.create(name="Harry Potter and the Half-Blood Prince",created = timezone.now(),price 
    ...: =20)

    book.save()

    book.save()

    Author.objects.all()

 Example for new project and sql 
 django-admin startproject bookstore
 python manage.py startapp books
 python manage.py sqlmigrate books 0001
 python manage.py makemigrations books
 python manage.py migrate """