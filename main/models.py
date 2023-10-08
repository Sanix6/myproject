from functools import reduce

from django.db import models


class Post(models.Model):
    """О новом посте:"""
    title = models.ImageField(upload_to='image/%Y/%m/%d', blank=True)
    author = models.CharField('Фио', max_length=20)

    class Meta:
        verbose_name = "New blog"

    def __str__(self):
        return f'{self.title},{self.author}'


class Mentor(models.Model):
    mentor = models.ImageField(upload_to='image/%Y/%m/%d', blank=True)
    image = models.CharField('Фио', max_length=20)

    class Meta:
        verbose_name = "New blog for mentor"

    def __str__(self):
        return f'{self.mentor},{self.image}'


class Main(models.Model):
    name = models.CharField("Название для вашей статьи", max_length=30)
    main = models.CharField("Для вашей статьи", max_length=300)


    class Meta:
        verbose_name = "New state"

    def __str__(self):
        return f'{self.name},{self.main},'
