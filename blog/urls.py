from django.urls import path
from . import views
 

urlpatterns = [
    path('', views.home, name='home'), 
    path('post/', views.post_list, name='post_list'), 
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/update/', views.post_update, name='update_post'),
]

