from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.task_add, name='task_add'),
    path('complete/<int:task_id>/', views.task_complete, name='task_complete'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
]
