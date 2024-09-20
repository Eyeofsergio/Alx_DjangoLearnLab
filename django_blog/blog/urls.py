from django.urls import path
from blog import views as blog_views
from django.contrib.auth import views as auth_views


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
    path('post/<int:pk>/comments/new/', blog_views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', blog_views.CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', blog_views.CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', blog_views.search, name='search'),
    path('tags/<slug:tag_slug>/', blog_views.PostByTagListView.as_view(), name='posts-by-tag'),
    path('profile/edit/',auth_views.edit_profile, name='edit_profile')
]