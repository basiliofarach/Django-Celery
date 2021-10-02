from django.db import models

# Create your models here.


class Deals(models.Model):
    name = models.TextField()
    store = models.ForeignKey(
        'stores_app.Store', blank=False, on_delete=models.CASCADE
    )
    image = models.TextField()
    price = models.CharField(max_length=150)

    def __str__(self):
        return self.name
