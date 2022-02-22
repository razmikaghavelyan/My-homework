from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.home),
    path('daytime/', views.daytime),
    path('intro/', views.introduction),
    path('task1/', views.square_keys),
]
