from django.db import models


# Create your models here.
class Login(models.Model):
    name     = models.CharField(max_length=200)
    check    = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class contact(models.Model):
    name = models.CharField(max_length=200)
    email     = models.EmailField(default="", max_length=200)
    subject = models.CharField(default="" ,max_length=200)
    message = models.CharField(default="",max_length=200)

    def __str__(self):
        return self.name
