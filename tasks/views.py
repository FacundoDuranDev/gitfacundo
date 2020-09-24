from django.shortcuts import render

tasks = ["Tarea1","Tarea2","Tarea3"]
# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
        "tasks": tasks
    })
