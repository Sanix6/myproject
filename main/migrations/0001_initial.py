# Generated by Django 4.2.5 on 2023-10-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ImageField(upload_to='', verbose_name='Здесь должно храниться ваше фото!')),
                ('description', models.TextField(verbose_name='Tekcт для вашего фото...')),
                ('author', models.CharField(max_length=10, verbose_name='Фио')),
            ],
            options={
                'verbose_name': 'Новый блок',
            },
        ),
    ]
