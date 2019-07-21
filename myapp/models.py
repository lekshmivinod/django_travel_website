# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class webpage(models.Model):
    name = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    class Meta:
        db_table = 'Web'
class contact(models.Model):
    fullname = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    msg = models.CharField(max_length=20)


    class Meta:
        db_table = 'contact'



class package(models.Model):
         title=models.CharField(max_length=100)
         description=models.CharField(max_length=500)
         price=models.CharField(max_length=50)
         summary=models.TextField(blank=True,null=True)


