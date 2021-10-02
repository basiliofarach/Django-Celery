from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Store(models.Model):
    brand = models.ForeignKey('brands_app.Brands', on_delete=models.CASCADE)
    identifier = models.TextField()
    name = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    username = models.TextField()
    email = models.TextField()
    store = models.ForeignKey('Store', on_delete=models.CASCADE)

    def __str__(self):
        return self.username
