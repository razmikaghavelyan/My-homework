from django.urls import path
from reddit_wall import views

urlpatterns = [
    path('post/', views.reddit_post, name="reddit_posts"),
]