# Generated by Django 3.2.5 on 2021-07-16 09:15

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_shoe_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(crop=None, default='shoe-thumbnail/default.png', force_format=None, keep_meta=False, quality=80, size=[300, 300], upload_to='shoe-thumbnail/'),
        ),
    ]
