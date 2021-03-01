from django.urls import path
from . import views

urlpatterns = [
    path('',views.api_details),
    path('status/',views.status),
    path('task-create/',views.task_create),
    path('task-update/<int:pk>/',views.task_update),
    path('task-delete/<int:pk>/',views.task_delete),
    path('tasks/',views.get_all_tasks),
    path('task/<int:pk>/',views.get_task_by_pk)
]