from django import forms

from .models import Currency


class OrderPaymentForm (forms.Form):

    discount = forms.BooleanField(required=False)

    currency = forms.ChoiceField(
        choices=lambda: [(currency.currency_code, currency.currency_code) for currency in Currency.objects.all()],
        required=True
    )
