from django.urls import path
from reddit_user import views


urlpatterns = [
    path('register/', views.user_register, name="reddit_register"),
    path('login/', views.user_login, name="reddit_login"),
    path('logout/', views.user_logout, name="reddit_logout"),
]