from django.urls import path
from blog import views as blog_views
from django.contrib.auth import views as auth_views
from . import views
from blog import views 

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('register/', auth_views.register, name='register'),
    path('profile/', auth_views.profile, name='profile'),
    path('logout/', auth_views.Logout_view, name='logout'),
    path('', blog_views.HomePostListView.as_view(), name='home'),
    path('post/', blog_views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', blog_views.PostDetailView.as_view(), name='post-detail'),
    path("post/new/", auth_views.PostCreateView.as_view(), name='post-create'),
    path("post/<int:pk>/update/", auth_views.PostUpdateView.as_view(), name='post-edit'),
    path("post/<int:pk>/delete/", auth_views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id/comments/new/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('search/', auth_views.search_posts, name='search_posts'),
    path('tags/<slug:slug>/', blog_views.posts_by_tag, name='posts-by-tag'),
    path('profile/edit/',auth_views.edit_profile, name='edit_profile'),
    path('', views.index, name='home'),



]