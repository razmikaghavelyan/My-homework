from django.urls import path
from task.api import views

urlpatterns = [
    path("tasks/", views.task_list)
]
