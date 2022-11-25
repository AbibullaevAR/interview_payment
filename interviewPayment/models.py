from django.db import models

# Create your models here.


class Currency(models.Model):

    code = models.CharField(max_length=3)

    amount = models.FloatField()


class Item(models.Model):

    name = models.CharField(max_length=200, unique=True)

    description = models.TextField()

    currency = models.ForeignKey(
        Currency,
        on_delete=models.RESTRICT
    )


class Order(models.Model):

    items = models.ManyToManyField(Item)

