from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  # Home page, list of tasks
    path('add/', views.add_todo, name='add_todo'),  # Add task
    path('update/<int:todo_id>/', views.update_todo, name='update_todo'),  # Update task
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),  # Delete task
]
