from django.urls import path
from . import views

urlpatterns = [
    path('',  views.get_routes),
    path('posts/', views.get_posts),
    path('post/<str:pk>/', views.get_post),
]
