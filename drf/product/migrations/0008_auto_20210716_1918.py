# Generated by Django 3.2.5 on 2021-07-16 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_color_shoeitem_size'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='color',
            constraint=models.UniqueConstraint(fields=('name',), name='colorName'),
        ),
        migrations.AddConstraint(
            model_name='size',
            constraint=models.UniqueConstraint(fields=('value',), name='sizeValue'),
        ),
    ]