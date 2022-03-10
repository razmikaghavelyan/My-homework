from django.urls import path
from user import views

urlpatterns = [
    path('', views.user_register, name="user_register"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_log_out, name="user_logout"),
]