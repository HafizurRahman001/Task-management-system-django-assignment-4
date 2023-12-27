from django.db import models
from category.models import AddCategory

# Create your models here.
class AddTask(models.Model):
    task_title = models.CharField(max_length = 100)
    task_description = models.TextField()
    is_completed = models.BooleanField()
    task_assigned_date = models.DateField()
    select_task_category = models.ManyToManyField(AddCategory)


    def __str__(self):
        return f"{self.task_title}"
