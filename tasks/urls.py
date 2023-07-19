from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.view_all_tasks, name='view_all_tasks'),
    path('tasks/<int:task_id>', views.view_individual_task, name='view_individual_task'),
    path('search', views.search, name='search'),
    path('search/title/<str:task_title>', views.search_by_title, name='search_by_title'),
    path('search/tag/<str:tag>', views.search_by_tag, name='search_by_tag'),
]