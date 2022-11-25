import stripe
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Item
# Create your views here.


class ListItems(ListView):
    queryset = Item.objects.all()
    template_name = 'interviewPayment/list_items.html'
    context_object_name = 'items'

