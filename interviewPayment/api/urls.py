from django.urls import path

from .views import OrderCreate

app_name = 'api'

urlpatterns = [
    path('create-order/', OrderCreate.as_view(), name='create-order'),
]
