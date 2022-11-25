from django.db import models

# Create your models here.


class Currency(models.Model):

    code = models.CharField(max_length=3, unique=True)


class Item(models.Model):

    name = models.CharField(max_length=200, unique=True)

    description = models.TextField()


class Amount(models.Model):

    amount = models.FloatField()

    currency = models.ForeignKey(
        Currency,
        on_delete=models.RESTRICT
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.RESTRICT
    )


class Order(models.Model):

    items = models.ManyToManyField(Item)

    currency = models.ForeignKey(
        Currency,
        on_delete=models.RESTRICT
    )


