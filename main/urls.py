from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('Главная страница', views.about, name="about"),
    path('lay', views.lau, name="layout"),
    path("Страница для ментора", views.style, name='style')
]
