# Generated by Django 4.2.5 on 2023-10-06 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_image_main_image1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='image1',
        ),
    ]
