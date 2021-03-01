from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
# Create your views here.

@api_view(['GET'])
def status(request):
    return Response({"status":"up"})

@api_view(['GET'])
def api_details(request):
    api_endpoints = {
        "All Tasks": "tasks/",
        "Task by pk": "task/<int:pk>/",
        "Create": "task-create/",
        "Read": "task/<int:pk>/",
        "Update": "task-update/<int:pk>/",
        "Delete": "task-delete/<int:pk>/"
    }
    return Response(api_endpoints)

@api_view(['GET'])
def get_all_tasks(request):
    task_list = []
    tasks = Task.objects.all()
    for task in tasks:
        result = {
            "pk":task.pk,
            "title":task.title,
            "completed":task.completed
        }
        task_list.append(result)

    return Response(task_list)

@api_view(['GET'])
def get_task_by_pk(request,pk):
    try:
        task = Task.objects.get(pk=pk)
    except:
        return Response({"message":"task not found"},status=404)
    result = {
        "pk":task.pk,
        "title":task.title,
        "completed":task.completed
    }
    return Response(result)

@api_view(['POST'])
def task_create(request):
    title = request.data['title']
    task = Task.objects.create(title=title)
    task.save()
    return Response({"message":"Task added successfully"})

@api_view(['PUT'])
def task_update(request,pk):
    task = Task.objects.get(pk=pk)

    if 'title' in request.data:
        title = request.data['title']
        task.title = title

    if 'completed' in request.data:
        completed = request.data['completed']
        task.completed = completed
    
    task.save()
    return Response({"message":"Task updated successfully"})

@api_view(['DELETE'])
def task_delete(request,pk):
    task = Task.objects.filter(pk=pk).delete()
    return Response({"message":"Task deleted successfully"})
