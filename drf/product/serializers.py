from django.db.models import Count
from rest_framework import serializers
from .models import *

class ShoeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoe
        fields = '__all__'


class ShoeItemSerializer(serializers.ModelSerializer):
    itemColor = serializers.SerializerMethodField()
    itemSize = serializers.SerializerMethodField()
    
    class Meta:
        model = ShoeItem
        exclude = ('color', 'size') 
    
    def get_itemColor(self, obj):
        return obj.color.name
    
    def get_itemSize(self, obj):
        return obj.size.value


class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = '__all__'


class OrderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    phone = serializers.CharField(max_length=20, required=True)
    address = serializers.CharField(max_length=255, required=True)
    price = serializers.IntegerField()
    cart = serializers.ListField()
    

    def validate_data(self, data):
        pass
    
    def save(self, user=None, *args, **kwargs):
        pass
        