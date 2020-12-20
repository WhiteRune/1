from django.db import models

# Create your models here.


class Student(models.Model):
    """
    Student data of all students in school
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    birthday = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    description = models.TextField()
    email = models.CharField(max_length=200)

