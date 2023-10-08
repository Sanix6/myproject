from django.shortcuts import render
from django.views.generic.base import View
from .models import Post, Main, Mentor


class PostView(View):
    """Что то новенькое"""

    def get(self, request):
        posts = Post.objects.all()


def index(request):
    data = Main.objects.all()
    context2 = {
        "data": data
    }
    return render(request, 'main/index.html', context2)


def lau(request):
    return render(request, "main/layout.html")


def about(request):
    data = Post.objects.all()
    context = {
        "data": data
    }
    return render(request, 'main/about.html', context)


def style(request):
    data = Mentor.objects.all()
    context1 = {
        "data": data
    }
    return render(request, 'main/style.html', context1)
