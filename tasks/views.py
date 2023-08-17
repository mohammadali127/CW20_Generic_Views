from django.shortcuts import render, redirect
from .models import Task, Tag, Category
from django.contrib import messages
from datetime import datetime, time
from django.views.generic import ListView
from django.views.generic.edit import CreateView

class TaskListView(ListView):
    model = Task
    template_name = 'view_all_tasks_category.html'
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        Task.objects.create(category_name=request.POST['add_a_category'])
        messages.success(request, 'tag was added', 'success')
        return self.get(request, *args, **kwargs)


class AddCategoryView(CreateView):
    model = Category
    fields = ['category_name']
    template_name = 'base.html'
    def form_valid(self, form):
        messages.success(self.request, 'tag was added', 'success')
        return super().form_valid(form)


class ViewAllEmergencyTasks(ListView):
    model = Task
    template_name = 'view_all_emergency_tasks.html'
    context_object_name = 'tasks'


class TaskListView(ListView):
    model = Task
    template_name = 'view_all_tasks.html'
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        Task.objects.create( title=request.POST['title'],
                             body=request.POST['body'], due_date=request.POST['due_date'],
                             status=request.POST['status'], category=Category.objects.get(pk=int(request.POST['category'])))
        messages.success(request, 'new task was added', 'success')
        return self.get(request, *args, **kwargs)

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