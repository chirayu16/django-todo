from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Todo.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'todo/add_todo.html')

def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.completed = not todo.completed  # Toggle completion
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/update_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
