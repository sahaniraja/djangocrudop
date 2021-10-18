from django.db import models

# Create your models here.

class Employee(models.Model):
    empno = models.IntegerField()
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    add = models.TextField(max_length=150)
