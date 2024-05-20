from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import TodosUserModel
from .forms import CreateTodoForm


# Create your views here.
@login_required(login_url='accounts:login')
def authenticated(request):
    todos = TodosUserModel.objects.filter(user=request.user, status='pendiente').order_by('due_date')
    if todos.exists():
        return render(request, template_name='todos/authenticated.html', context={'todos': todos})
    else:
        error_message = "No hay tareas pendientes"
        return render(request, template_name='todos/authenticated.html', context={'error_message': error_message})


@login_required(login_url='accounts:login')
def create_todo(request):
    if request.method == 'POST':
        print("estoy aca 1")
        todos_form = CreateTodoForm(request.POST)
        if todos_form.is_valid():
            print("estoy aca 2")
            todo = todos_form.save(commit=False)
            todo.user = request.user
            print(request.user)
            todo.save()
            todos_form.save_m2m()
            messages.success(request, 'Tarea creada correctamente')
            return redirect('todos:authenticated')
        else:
            print(todos_form.errors)
    else:
        todos_form = CreateTodoForm()
    return render(request, template_name='todos/create.html', context={'todos_form': todos_form})


@login_required(login_url='accounts:login')
def view_todo(request, todo_id):
    return render(request, template_name='todos/view.html')


@login_required(login_url='accounts:login')
def modify_todo(request):
    return render(request, template_name='todos/modify.html')


@login_required(login_url='accounts:login')
def complete_todo(request):
    pass


@login_required(login_url='accounts:login')
def delete_todo(request):
    pass
