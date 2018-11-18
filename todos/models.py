from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey('category.Category',related_name='todo', on_delete=models.CASCADE,)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
