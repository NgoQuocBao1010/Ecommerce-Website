from django.db.models import Count
from rest_framework import serializers
from .models import Shoe, ShoeItem, Color

class ShoeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoe
        fields = '__all__'


class ShoeItemSerializer(serializers.ModelSerializer):
    itemColor = serializers.SerializerMethodField()
    itemSizes = serializers.SerializerMethodField()
    
    class Meta:
        model = ShoeItem
        exclude = ('color', 'size') 
    
    def get_itemColor(self, obj):
        return obj.color.name
    
    def get_itemSizes(self, obj):
        result = []
        for size in obj.size.all():
            result.append(size.value)
        
        return result
        