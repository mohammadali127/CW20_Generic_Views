from django.contrib import admin

from .models import Task, Category, Tag

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Category)
