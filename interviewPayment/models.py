from django.db import models
from django.db.models import CheckConstraint, Q


# Create your models here.


class Item(models.Model):

    name = models.CharField(max_length=200, unique=True)

    description = models.TextField()

    currency_code = models.CharField(max_length=3, unique=True)


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


class Order(models.Model):

    items = models.ManyToManyField(Item)

    discount = models.ForeignKey(Discount, on_delete=models.RESTRICT, blank=True, null=True)


