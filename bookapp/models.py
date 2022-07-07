from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.CharField(max_length=64)
    eaddr = models.CharField(max_length=64)
