from django.urls import path, include
from django_app2 import views


urlpatterns = [
    path('', views.home),
    path('find/', views.find_movie),
    path('create/', views.create_film),
    path('delete/', views.delete_film),
]
