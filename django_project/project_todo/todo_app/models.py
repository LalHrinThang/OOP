from django.db import models

# Create your models here.

class Todo_app(models.Model):
    content = models.TextField()