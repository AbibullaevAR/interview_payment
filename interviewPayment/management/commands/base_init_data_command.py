from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from interviewPayment.models import Item, Discount, Currency


class Command(BaseCommand):
    help = 'Create base data for test project'

    UserModel = get_user_model()

    def handle(self, *args, **kwargs):
        Item.objects.get_or_create(name='Item 1', description='description item 1', price=1000)
        Item.objects.get_or_create(name='Item 2', description='description item 2', price=3000)
        Item.objects.get_or_create(name='Item 3', description='description item 3', price=5000)

        Currency.objects.get_or_create(currency_code='usd')
        Currency.objects.get_or_create(currency_code='chf')

        Discount.objects.get_or_create(stripe_id='tefPj9Tb', name='base coupon', percent_off=20)

        if not self.UserModel.objects.filter(username='Admin_test').exists():
            user = self.UserModel.objects.create_user('Admin_test', password='admin')
            user.is_superuser = True
            user.is_staff = True
            user.save()
