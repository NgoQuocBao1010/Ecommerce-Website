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
    name = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = PurchaseItem
        exclude = ('order', 'item')
    
    def get_name(self, obj):
        return obj.item.shoe.name
    
    def get_color(self, obj):
        return obj.item.color.name

    def get_size(self, obj):
        return obj.item.size.value
    
    def get_thumbnail(self, obj):
        shoe = obj.item.shoe
        color = obj.item.color
        thumbnail = ProductPicture.objects.get(shoe=shoe, color=color)

        return thumbnail.picture.url
    
    



class OrderSerializer(serializers.ModelSerializer):
    cart = PurchaseItemSerializer(read_only=True, many=True)
    domain = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields =  '__all__'
    
    def get_domain(self, obj):
       request = self.context.get('request')
       return request.build_absolute_uri('/')[:-1]
    

        