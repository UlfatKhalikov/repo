from django.db import models


class mobile(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    img = models.ImageField(upload_to="mysite/static/images/%d/%m/%y/")
    price = models.IntegerField()
    count = models.SmallIntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    

class stocks(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField(upload_to="mysite/static/images/%d/%m/%y/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)