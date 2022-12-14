from django.db import models
from django.db.models import CheckConstraint, Q


# Create your models here.

class Currency (models.Model):

    currency_code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.currency_code


class Item(models.Model):

    name = models.CharField(max_length=200, unique=True)

    description = models.TextField()

    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Discount (models.Model):

    name = models.CharField(max_length=30)

    stripe_id = models.CharField(max_length=8, unique=True)

    percent_off = models.FloatField()

    class Meta:
        constraints = (
            # for checking in the DB percent between 1 and 100
            CheckConstraint(
                check=Q(percent_off__gte=1.0) & Q(percent_off__lte=100.0),
                name='percent_off_range'),
        )

    def __str__(self):
        return self.name


class Order(models.Model):

    items = models.ManyToManyField(Item)

    discount = models.ForeignKey(Discount, on_delete=models.RESTRICT, blank=True, null=True)

    currency = models.ForeignKey(Currency, on_delete=models.RESTRICT, blank=True, null=True)
