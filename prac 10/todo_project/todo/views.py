# todo/views.py
from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Todo.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'add_todo.html')
