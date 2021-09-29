from django.db import models

# Create your models here.


class Brands(models.Model):
    name = models.TextField()
    logo = models.TextField()

    def __str__(self):
        return self.id
