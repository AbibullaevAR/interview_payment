from django.urls import path

from .views import ListItems
app_name = 'interviewPayment'

urlpatterns = [
    path('items/', ListItems.as_view(), name='list_items')
]
