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
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True)
    dateAdded = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="shoe-thumbnail/", default="shoe-thumbnail/default.png")

    # Manipulate (in this case, resizing image before saving)
    def makeThumbnail(self, size=(300, 300)):
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
        if "shoe-thumbnail/" in self.thumbnail:
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


class ShoeItem(models.Model):
    class Meta:
        unique_together = ['shoe', 'color', 'size']
    
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, null=True, on_delete=models.SET_NULL)
    size = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
    picture = models.ImageField(null=True, blank=True, upload_to="shoes/")

    def __str__(self):
        return f"{self.shoe}, color {self.color}, size {self.size} has {self.quantity} left"