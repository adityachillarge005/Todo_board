from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django .shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from datetime import date
# Create your views here.
@login_required
def home(request):
    return HttpResponse("hello adi")
@login_required
def todo_list(request):
    priority = request.GET.get('priority')
    search_query = request.GET.get('search')

    todos = Todo.objects.filter(user=request.user)

    if priority:
        todos = todos.filter(priority=priority)

    if search_query:
        todos=todos.filter(title__icontains=search_query)

    pending_todos = todos.filter(is_completed = False)
    completed_todos = todos.filter(is_completed = True)

    return render(request, 'app1/todo_list.html', {
        'pending_todos': pending_todos,
        'completed_todos': completed_todos,
        'today': date.today(),
        'current_priority': priority,
    })

@login_required
def create_todo(request):
    if request.method== 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('Todo_list')
        else:
            print(form.errors)
    else:
        form = TodoForm()
    
    return render(request,'app1/todo_form.html',{'form':form})

@login_required
def delete_todo(request,id):
    todo=get_object_or_404(Todo,id=id,user=request.user)
    todo.delete()
    return redirect('Todo_list')
@login_required
def update_todo(request,id):
    todo = get_object_or_404(Todo,id=id,user=request.user)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('Todo_list')
    
    else:
        form = TodoForm(instance=todo)

    return render(request,'app1/todo_form.html',{'form':form})
@login_required
def toggle_complete(request,id):
    todo = get_object_or_404(Todo, id=id,user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('Todo_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html',{'form':form})