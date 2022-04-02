from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_page, name="register"),

    path('', views.home, name="home"),
    path('post/<str:pk>/', views.post, name="post"),
    path('profile/<str:pk>/', views.user_profile, name="user-profile"),

    path('create-post/', views.create_post, name="create-post"),
    path('like_post/', views.like_post, name="like_post"),
    path('update-post/<str:pk>/', views.update_post, name="update-post"),
    path('delete_post/<str:pk>/', views.delete_post, name="delete_post"),
    path('delete-message/<str:pk>/', views.delete_message, name="delete-message"),

    path('update-user/', views.update_user, name="update-user"),

    path('topics/', views.topics_page, name="topics"),
    path('activity/', views.activity_page, name="activity"),
]
