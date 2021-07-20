from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import *
from product.serializers import *


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

    pictures = ProductPicture.objects.filter(shoe=shoe)
    paths = []

    for pic in pictures:
        paths.append(request.build_absolute_uri(pic.picture.url))

    data = {
        "name": shoe.name,
        "price": shoe.price,
        "thumbnail": request.build_absolute_uri(shoe.thumbnail.url),
        "pictures": paths,
    }

    items = ShoeItem.objects.filter(shoe=shoe)
    serializer = ShoeItemSerializer(items, many=True, context={"request": request})

    data.update({"items": serializer.data})
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def takeOrders(request):
    user = None
    if request.user.is_authenticated:
        user = request.user

    items = []

    try:
        for itemdata in request.data.get('cart'):
            item = get_object_or_404(ShoeItem, id=itemdata.get("id"))
            items.append((item, itemdata.get("quantity")))

        newOrder = Order.objects.create(
            user=user,
            name=request.data.get('name'),
            phone=request.data.get('phone'),
            note=request.data.get('note'),
            address=request.data.get('address'),
            totalPrice=request.data.get('price'),
            status="pending",
        )

        for item, quantity in items:
            PurchaseItem.objects.create(
                order=newOrder,
                item=item,
                quantity=quantity
            )
    except Exception as e:
        print("[SERVER] Error creating order", str(e))
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"message": str(e)})

    print("[SERVER] New Order!!!\n")
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orders(request):
    user = request.user
    if user.is_authenticated:
        userOrders = Order.objects.filter(user=user)
        serializers = OrderSerializer(userOrders, many=True, context={"request": request})

        return Response(serializers.data)
    
    return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message", "Unauthorized"})