from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators omport permission_required 
from django.contrib.auth.decortors import user_passes_test

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    relationship_app/list_books.html
    relationship_app/library_detail.html
    
