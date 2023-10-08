from django.contrib import admin
from .models import Post, Mentor, Main


@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ("title", 'author')
    list_display_links = list_display


@admin.register(Mentor)
class Postadmin1(admin.ModelAdmin):
    list_display = ('image', 'mentor')
    list_display_links = list_display


@admin.register(Main)
class Postadmin2(admin.ModelAdmin):
    list_display = ("name", "main",)
    list_display_links = list_display
