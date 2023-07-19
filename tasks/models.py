from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name

class Task(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    due_date = models.DateTimeField()
    status = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title} + {self.due_date} + {self.category} + {self.tags}'
