from django.db import models

# Create your models here.
class AddCategory(models.Model):
    add_category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.add_category}"