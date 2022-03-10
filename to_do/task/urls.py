from django.urls import path
from task import views

urlpatterns = [
    path('', views.home),
    path('tasks/', views.list_task, name="list_task"),
    path('tasks/<int:task_id>/', views.task_view, name="task_view"),
    path('tasks/create/', views.task_create_view, name="task_create"),
    # path('tasks/<int:task_id>/delete', views.task_delete, name="task_delete"),
]
