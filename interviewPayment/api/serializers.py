from rest_framework import serializers


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ('items', 'currency')


