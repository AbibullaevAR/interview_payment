from django.urls import path
from django.views.generic import TemplateView

from .views import ListItems, DetailItem, OrderPaymentView, add_in_order

app_name = 'interviewPayment'

urlpatterns = [
    path('items/', ListItems.as_view(), name='list_items'),
    path('item/<pk>', DetailItem.as_view(), name='detail_item'),
    path('order-items/', OrderPaymentView.as_view(), name='list_order'),

    path('add-in-order/<pk>', add_in_order, name='add_in_order'),

    path('success-payment/',
         TemplateView.as_view(template_name='interviewPayment/success_payment.html'),
         name='success_payment'),
    path('cancel-payment/',
         TemplateView.as_view(template_name='interviewPayment/cancel_payment.html'),
         name='cancel_payment'),
]
