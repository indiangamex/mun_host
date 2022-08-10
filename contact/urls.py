from django.contrib import admin
from django.urls import path
from contact import views
urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    path("idelegate", views.idelegate, name="idelegate"),
    path("sdelegate", views.sdelegate, name="sdelegate"),
    path("unga", views.unga, name="unga"),
    path("unhrc", views.unhrc, name="unhrc"),
    path("aippm", views.aippm, name="aippm"),
    path("crisis", views.crisis, name="crisis"),
    path("ip", views.ip, name="ip"),
    path("letter", views.letter, name="letter")
]