from django.db import models

# Create your models here.


class Item(models.Model):

    name = models.CharField(max_length=200, unique=True)

    description = models.TextField()

    price = models.FloatField()

    currency = models.CharField(max_length=3)


class Order(models.Model):

    items = models.ManyToManyField(Item)

