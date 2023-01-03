from django.shortcuts import render, redirect
from .models import Task, SubTask
from .forms import TaskForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.

@login_required
def index(request):
    if request.GET:
        task = request.GET['get-task']
        tasks = Task.objects.filter(user = request.user, title__icontains = task)
    else:
        tasks = Task.objects.filter(user = request.user)
    return render(request, 'index.html', {'tasks': tasks})

@login_required
def add_taks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task = Task.objects.create(user = user, title = title, description = description)
            
            messages.success(request, 'Task added.')
            return redirect('core:list')
    form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def details_task(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'details.html', {'task':task})

@login_required
def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.save()
            return redirect('core:list')
        
    form = TaskForm()
    return render(request, 'add_task.html', {'form': form, 'task': task})


@login_required
def complete_task(request, id):
    task = Task.objects.get(id=id)
    if task.status == False:
        task.status = True
    else:
        task.status = False
    task.save()
    return redirect('core:list')


@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('core:list')


def login_hendler(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Wellcome {username}')
                return redirect('core:list')
    return render(request, 'login.html')


def logout_hendler(request):
    logout(request)
    return redirect('core:list')


def signup_hendler(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_conf = form.cleaned_data['password_conf']
            
            if password_conf == password:
                User.objects.create_user(
                    username = username,
                    password = password
                )
                return redirect('core:login')
    return render(request, 'signup.html')
