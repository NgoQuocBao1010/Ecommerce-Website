from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Shoe, ShoeItem
from product.serializers import ShoeSerializer, ShoeItemSerializer

import json


@api_view(['GET'])
def shoeList(request):
    shoes = Shoe.objects.all()
    serializer = ShoeSerializer(shoes, many=True, context={"request": request})

    return Response(serializer.data)



@api_view(['GET'])
def shoesByBrand(request, brandName):
    shoes = Shoe.objects.filter(brand__name__iexact=brandName)
    serializer = ShoeSerializer(shoes, many=True, context={"request": request})

    return Response(serializer.data)


@api_view(['GET'])
def shoeDetail(request, id):
    shoe = get_object_or_404(Shoe, id=id)

    data = {
        "name": shoe.name,
        "price": shoe.price,
        "thumbnail": request.build_absolute_uri(shoe.thumbnail.url),
    }

    items = ShoeItem.objects.filter(shoe=shoe)
    serializer = ShoeItemSerializer(items, many=True)

    # test = list(serializer.data)
    # test.append(data)
    data.update({"items": serializer.data})
    return Response(data, status=status.HTTP_200_OK)
