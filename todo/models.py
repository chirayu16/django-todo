from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)  # Task title
    completed = models.BooleanField(default=False)  # Task status

    def __str__(self):
        return self.title
