from django.db.models.signals import pre_save
import os
from .models import Shoe

# def removeOldImage(sender, instance, **kwargs):
#     if Shoe.objects.filter(id=instance.id).exists():
#         try:
#             oldImg = Shoe.objects.get(id=instance.id).thumbnail.path
#             newImg = instance.thumbnail.path

#             print(oldImg, newImg)

#             if newImg != oldImg and "default" not in os.path.basename(oldImg):
#                 if os.path.exists(oldImg):
#                     os.remove(oldImg)
#                     # print(f"[SERVER]: Image removed successfully\n")
                    
#         except Exception as e:
#             print(f"[SERVER]: Error on removing old image: {e}\n")

# pre_save.connect(removeOldImage, sender=Shoe)