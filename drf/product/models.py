from django.db import models
from django.contrib.auth import get_user_model
from django.core.files import File
from io import BytesIO
from PIL import Image

from django_resized import ResizedImageField

User = get_user_model()

class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Brand {self.name}"


class Shoe(models.Model):
    class Meta:
        ordering = ['-dateAdded']
        constraints = [
            models.UniqueConstraint(fields=["name"], name="shoeName")
        ]


    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    dateAdded = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="shoe-thumbnail/", default=None, null=True, blank=True)

    # Manipulate (in this case, resizing image before saving)
    def makeThumbnail(self, size=(300, 300)):
        # print("[SERVER] Making thumbnail ...")
        im = Image.open(self.thumbnail)
        im = im.convert('RGB')

        # im.thumbnail(size)  ## Resizing method that keep the original aspect ration
        im = im.resize(size)  ## Resizing method that ignore the original aspect ration
        thumb_io = BytesIO()
        im.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=self.thumbnail.name)

        return thumbnail
    
    # Override save method
    def save(self, *args, **kwargs):
        if self.thumbnail:
            self.thumbnail = self.makeThumbnail()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Color(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name"], name="colorName")
        ]
        
    
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Size(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["value"], name="sizeValue"),
        ]

    value = models.IntegerField()

    def __str__(self):
        return str(self.value)


class ProductPicture(models.Model):
    class Meta:
        unique_together = ['shoe', 'color']
    
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    picture = models.ImageField(default="shoe-thumbnail/default.png", upload_to="shoes/", null=True, blank=True)

    def __str__(self):
        return f"Picture of {self.color} {self.shoe}"


class ShoeItem(models.Model):
    class Meta:
        unique_together = ['shoe', 'color', 'size']
    
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, null=True, on_delete=models.SET_NULL)
    size = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.shoe}, color {self.color}, size {self.size} has {self.quantity} left"


class Order(models.Model):
    class Meta:
        ordering = ['-dateCreated']

    STATUS = (
        ('pending', 'pending'),
        ('delivering', 'delivering'),
        ('delivered', 'delivered'),
    )

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=STATUS)
    totalPrice = models.PositiveIntegerField(default=0)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} on {self.dateCreated} by {self.user}"

 
class PurchaseItem(models.Model):
    class Meta:
        unique_together = ['order', 'item']


    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(ShoeItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Item from {self.order}"