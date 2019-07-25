from django.db import models
from django.utils import timezone

class Services(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255,default='')
    status = models.CharField(max_length=30,default='publish')
    created_at = models.DateTimeField('created',default = timezone.now)
    updated_at = models.DateTimeField('created',default = timezone.now)
    
class Partners(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255,default='')
    status = models.CharField(max_length=30,default='publish')
    created_at = models.DateTimeField('created',default = timezone.now)
    updated_at = models.DateTimeField('created',default = timezone.now)
    
class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    image = models.CharField(max_length=255,default='')
    status = models.CharField(max_length=30,default='publish')
    created_at = models.DateTimeField('created',default = timezone.now)
    updated_at = models.DateTimeField('created',default = timezone.now)
    
class Sliders(models.Model):
    title = models.CharField(max_length=400)
    subtitle = models.CharField(max_length=400,default='')
    image = models.CharField(max_length=255,default='')
    status = models.CharField(max_length=30,default='publish')
    created_at = models.DateTimeField('created',default = timezone.now)
    updated_at = models.DateTimeField('created',default = timezone.now)
    
class Homeservices(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    readmore = models.CharField(max_length=255,default='')
    image = models.CharField(max_length=255,default='')
    status = models.CharField(max_length=30,default='publish')
    created_at = models.DateTimeField('created',default = timezone.now)
    updated_at = models.DateTimeField('created',default = timezone.now)