from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Project

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')


def home(request):
    projects = Project.objects.all()
    return render(request, 'cl_app/home.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'cl_app/project_detail.html', {'project': project})


def add_project(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        project = Project.objects.create(title=title, description=description, created_by=request.user)
        return redirect('project_detail', pk=project.pk)
    return render(request, 'cl_app/add_project.html')