from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ManHandle(models.Model):
    filename=models.CharField(max_length=50)
    filepath=models.CharField(max_length=200)
    result=models.IntegerField(default=-1)
    insertdata=models.DateTimeField('date published')