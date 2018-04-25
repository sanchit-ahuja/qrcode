# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    bitsid=models.CharField(max_length=15)
    name=models.CharField(max_length=20,null=True)
    qrcode=models.CharField(max_length=10,null=True)


    def __unicode__(self):
        return self.bitsid

class Profshow(models.Model):
    name=models.CharField(max_length=25)
    def __unicode__(self):
        return self.name


class Tickets(models.Model):
    student=models.ForeignKey(Student)
    profshow=models.ManyToManyField(Profshow)
    number=models.IntegerField(default=0)

    def __unicode__(self):
        return self.student.name


#Done