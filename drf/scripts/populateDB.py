from django.core.files import File
from product.models import Brand, Shoe, ShoeItem, Color, Size, ProductPicture

import os, random

# Generate random size, price and quantity
def randomGenerator(type=None):
    return {
        "size": random.sample(range(38, 45), random.randint(2, 6)),
        "quantity": random.randint(0, 7),
        "price": random.choice([1800, 2500, 2800, 2900, 3100, 3500, 3800, 4500, 5000, 5500])
    }.get(type)


#  =======================  Get or Create object in database    ======================= #
def getBrand(brandName):
    brand = Brand.objects.filter(name__iexact=brandName)

    if len(brand) > 0:
        return brand[0]
    
    newBrand = Brand.objects.create(name=brandName)
    return newBrand

def getColor(name):
    color = Color.objects.filter(name__iexact=name)

    if len(color) > 0:
        return color[0]
    
    newColor = Color.objects.create(name=name)
    return newColor

def getSize(value):
    size = Size.objects.filter(value__iexact=value)

    if len(size) > 0:
        return size[0]
    
    newSize = Size.objects.create(value=value)
    return newSize

def getShoe(name, brand, price, imgUrl):
    shoe = Shoe.objects.filter(name__iexact=name)

    if len(shoe) > 0:
        return shoe[0]
    
    newShoe = Shoe.objects.create(
        name=name, 
        brand=brand,
        price=price,
    )
    _, fileExtension = os.path.splitext(imgUrl)
    newShoe.thumbnail.save(f'{name}{fileExtension}', File(open(imgUrl, 'rb')))
    return newShoe

#  =======================  ***    ======================= #



def processing():
    # Get all shoes in image
    url = "F:\Project\Ecommerce Website\shoe_images"

    for brandUrl in os.listdir(url):
        shoesUrl = os.path.join(url, brandUrl)

        brand = getBrand(brandUrl)

        for shoe in os.listdir(shoesUrl):
            infoUrl = os.path.join(shoesUrl, shoe)

            imageUrl = os.path.join(infoUrl, os.listdir(infoUrl)[0])
            price = randomGenerator("price")

            shoeObj = getShoe(shoe, brand, price, imageUrl)
            
            sizes = randomGenerator("size")

            for image in os.listdir(infoUrl):
                color, fileExtension = os.path.splitext(image)
                colorObj = getColor(color)

                try:
                    pic = ProductPicture.objects.create(
                        shoe=shoeObj,
                        color=colorObj,
                    )
                    pic.picture.save(f'{shoe}{fileExtension}', File(open(os.path.join(infoUrl, image), 'rb')))
                except Exception as e:
                    print(str(e))
    
                for size in sizes:
                    quantity = randomGenerator("quantity")
                    try:
                        sizeObj = getSize(size)

                        item = ShoeItem.objects.create(
                            shoe=shoeObj,
                            color=colorObj,
                            size=sizeObj,
                            quantity=quantity,
                        )
                        print(f"{shoe}, {color}, {size}, {image}")

                    except Exception as e:
                        print(str(e))
            

def run():
    processing()