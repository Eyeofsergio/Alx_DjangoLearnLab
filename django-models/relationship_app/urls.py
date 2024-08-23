from django.urls import path
from .views import list_books, LibraryDetailView
from relationship_app import views
from .views import view.register 
from django.contrib.auth import views as auth_views
from librarian_view import librarian_view
from member_view import member_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library_detail/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/'login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/'logout.html'), name='logout'),
    path('register/', views.register(), name='register'),
    path(admin/', views.admin_view, name='admin'),
]

from .views import views.register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register.as_view(), name='register'),
]
