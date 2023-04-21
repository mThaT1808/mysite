from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)

class Classroom(models.Model):
    number = models.IntegerField()

class Teacher(models.Model):
    name = models.CharField(max_length=50)

class Lesson(models.Model):
    name = models.CharField(max_length=50)

class Mark(models.Model):
    mark = models.IntegerField()


