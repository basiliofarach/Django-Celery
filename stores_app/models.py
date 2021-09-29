from django.db import models

# Create your models here.


class Store(models.Model):
    brand = models.ForeignKey('brands_app.Brands', on_delete=models.CASCADE)
    identifier = models.TextField()
    name = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.id
