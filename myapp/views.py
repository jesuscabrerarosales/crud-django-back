from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    title = "test"
    return render(request, 'index.html', {"title" :title })

def about(request):
    username= 'jesus'
    return render(request, 'about.html', {
        "username": username
    })

def hello(request,username):
    return HttpResponse("Hello world: %s" % username)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        "projects" : projects
    })

def task(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        "tasks" : tasks
        })