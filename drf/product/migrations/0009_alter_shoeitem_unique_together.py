# Generated by Django 3.2.5 on 2021-07-16 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210716_1918'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shoeitem',
            unique_together={('shoe', 'color', 'size')},
        ),
    ]