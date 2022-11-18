from rest_framework import serializers
from .models import OnSaleItems

class OnSaleItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnSaleItems
        fields = '__all__'