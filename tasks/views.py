from django.shortcuts import render, redirect
from .models import Task, Tag, Category
from django.contrib import messages

def view_all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'view_all_tasks.html', {'tasks':tasks})

def view_individual_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'view_individual_task.html', {'task': task})

def search(request):
    if request.method == 'POST':
        if 'search_by_tag' in request.POST:
            return redirect('search_by_tag', request.POST['search_by_tag'])
        elif 'search_by_title' in request.POST:
            return redirect('search_by_title', request.POST['search_by_title'])

    return render(request, 'search.html')

def search_by_title(request, task_title):
    tasks = Task.objects.filter(title__icontains = task_title)
    if tasks:
        return render(request, 'search_by_title.html', {'tasks':tasks})
    else:
        messages.error(request, 'Task Not Found.', 'danger')
    return redirect('search')

def search_by_tag(request, tag):
    tasks = Task.objects.filter(tags__tag_name__icontains = tag)
    if tasks:
        return render(request, 'search_by_tag.html', {'tasks': tasks})
    else:
        messages.error(request, 'Task Not Found.', 'danger')
    return redirect('search')