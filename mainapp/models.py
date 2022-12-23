import datetime

from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=datetime.datetime.now())

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    enrollment = models.CharField(max_length=20, blank=True, null=True, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=datetime.datetime.now())
