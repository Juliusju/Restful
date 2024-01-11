from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Books


# Create your views here.

def home(request):
    return HttpResponse('Welcome Home')

class BookListView(ListView):
    model = Books
    template_name = 'books/book_list.html'
    
