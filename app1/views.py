from django.shortcuts import render, redirect,get_object_or_404
from .models import Todo
from .forms import TodoForm
#CREATE
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})


#RETRIVE
def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})


#UPDATE
def update_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')   # go back to list page
        else:
            print(form.errors)  # debug if needed
    else:
        form = TodoForm(instance=todo)

    return render(request, 'update_todo.html', {'form': form})
#delete
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)#id=7
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'delete_todo.html', {'todo': todo})