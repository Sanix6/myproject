# Generated by Django 4.2.5 on 2023-10-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/Y%', verbose_name='Для вашего совместного фото'),
        ),
    ]