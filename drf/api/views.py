from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Shoe, ShoeItem
from product.serializers import ShoeSerializer, ShoeItemSerializer


@api_view(['GET'])
def shoeList(request):
    shoes = Shoe.objects.all()

    productName = request.GET.get("productName")
    shoeBrand = request.GET.get("brand")
    feature = request.GET.get("feature")
    sort = request.GET.get("sort")

    if productName:
        shoes = shoes.filter(name__icontains=productName)

    if shoeBrand:
        shoes = shoes.filter(brand__name__icontains=shoeBrand)
    
    if feature:
        pass
    
    if sort:
        querySet = {
            "a-z": shoes.order_by("name"),
            "z-a": shoes.order_by("-name"),
            "hight2low": shoes.order_by("-price"),
            "low2high": shoes.order_by("price"),
        }
        shoes = querySet.get(sort)

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

    data.update({"items": serializer.data})
    return Response(data, status=status.HTTP_200_OK)
