from django.contrib.auth import views as auth_views
from django.urls import path
from .views import register_view
from . import views
 

urlpatterns = [
    path('', views.post_list, name='post_list'), 
    path('register/', register_view, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    

    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/', views.post_update, name='update_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
]

