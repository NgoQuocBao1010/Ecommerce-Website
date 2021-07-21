from product.models import ProductPicture
from django.conf import settings

import os


def getAllUsedImages():
    pictureObj = ProductPicture.objects.all()

    imgPaths = []
    for obj in pictureObj:
        path = os.path.abspath(obj.picture.path)
        imgPaths.append(path)
    
    shoesImgFolder = os.path.join(settings.MEDIA_ROOT, "shoes")

    for image in os.listdir(shoesImgFolder):
        imagePath = os.path.abspath(os.path.join(shoesImgFolder, image))

        if imagePath not in imgPaths:
            print(imagePath)
    

def run():
    getAllUsedImages()