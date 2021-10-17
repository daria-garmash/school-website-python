from django.db import models
from datetime import datetime

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='first name', default='Мария')
    father_name = models.CharField(max_length=30, verbose_name='father name', null=True)
    last_name = models.CharField(max_length=30, verbose_name='last name', default='Иванова')
    address = models.TextField(max_length=100, verbose_name='address', default='address')
    birth_date = models.DateField(verbose_name='birth date', default='2000-01-01')
    tel = models.CharField(max_length=10, unique=True, verbose_name='tel')
    email = models.EmailField(unique=True, verbose_name='email')
    grade = models.IntegerField(verbose_name='grade', default='1')


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    creation_date = models.DateTimeField(auto_now_add=True)


class SchoolStaff(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='first name', default='Мария')
    father_name = models.CharField(max_length=30, verbose_name='father name', null=True)
    last_name = models.CharField(max_length=30, verbose_name='last name', default='Иванова')
    address = models.TextField(max_length=100, verbose_name='address', default='address')
    birth_date = models.DateField(verbose_name='birth date', default='1970-01-01')
    tel = models.CharField(max_length=10, unique=True, verbose_name='tel')
    email = models.EmailField(unique=True, verbose_name='email')
    position = models.TextField(max_length=50, verbose_name='position', default="учитель")

    def __str__(self):
        return self.first_name + " " + self.father_name + " " + self.last_name


class Event(models.Model):
    responsibleStaff = models.ForeignKey(SchoolStaff, on_delete=models.PROTECT)
    name = models.TextField(max_length=50, verbose_name="event name", default="event")
    date = models.DateTimeField(default=datetime.now())
    description = models.TextField(max_length=500, verbose_name="description", default="this is a description")
