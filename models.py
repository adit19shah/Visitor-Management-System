from django.db import models
from django.utils import timezone
from django import forms
#from django.conf.urls.defaults import *
import datetime

class Host(models.Model):
    NAME  =  models.CharField(max_length=32)
    EMAIL =  models.EmailField()
    Phone =  models.CharField(max_length=13)
    Pswd  =  models.CharField(max_length=32,default='')
    itime =  models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
         return self.NAME

class Checkin(models.Model):
    NAME  =  models.CharField(max_length=32)
    EMAIL =  models.EmailField()
    Phone =  models.CharField(max_length=13)
    itime =  models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.NAME

class Checkout(models.Model):
    Phone = models.CharField(max_length=13)
    otime = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.Phone

class Exites(models.Model):
    Phone = models.CharField(max_length=13, default='',null=True)
    Pswd = models.CharField(max_length=32, default='')
    otime=models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.Phone