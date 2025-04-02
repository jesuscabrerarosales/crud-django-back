from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def hello(request,username):
    return HttpResponse("Hello world: %s" % username)

def projects(request):
    all_projects = list(Project.objects.values())
    return render(request, 'projects.html')

def task(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    return render(request, 'task.html')