import stripe
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView

from .forms import OrderPaymentForm
from .models import Item, Order, Currency, Discount


# Create your views here.


class ListItems(ListView):
    queryset = Item.objects.all()
    template_name = 'interviewPayment/list_items.html'
    context_object_name = 'items'


class DetailItem (DetailView):
    template_name = 'interviewPayment/detail_item.html'
    context_object_name = 'item'
    model = Item

    def get_context_data(self, **kwargs):
        contex = super(DetailItem, self).get_context_data(**kwargs)
        if order := Order.objects.filter(pk=self.request.session.get('order_id')).first():
            contex['order_items'] = order.items.all()

        return contex


class OrderPaymentView(FormView):

    form_class = OrderPaymentForm
    template_name = 'interviewPayment/list_order.html'

    def form_valid(self, form):
        order = Order.objects.get(pk=self.request.session['order_id'])
        order.currency = Currency.objects.filter(currency_code=form.cleaned_data['currency']).first()

        discounts = []

        if form.cleaned_data['discount']:
            discounts = [{
                'coupon': Discount.objects.first().stripe_id,
            }]

            order.discount = Discount.objects.first()

        order.save()

        line_items = [
            {
                'price_data': {
                    'currency': order.currency.currency_code,
                    'product_data': {
                        'name': item.name,
                        'description': item.description
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }
            for item in order.items.all()]

        session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            discounts=discounts,
            success_url=self.request.build_absolute_uri(reverse('interviewPayment:success_payment')),
            cancel_url=self.request.build_absolute_uri(reverse('interviewPayment:cancel_payment')),
        )

        self.request.session.clear()

        return redirect(session.url)

    def get_context_data(self, **kwargs):
        contex = super(OrderPaymentView, self).get_context_data(**kwargs)
        if order := Order.objects.filter(pk=self.request.session.get('order_id')).first():
            contex['order_items'] = order.items.all()

        return contex


def add_in_order(request, pk):
    order, _ = Order.objects.get_or_create(pk=request.session.get('order_id', default=None))
    request.session['order_id'] = order.pk

    order.items.add(Item.objects.get(pk=pk))
    return redirect(reverse('interviewPayment:list_items'))
