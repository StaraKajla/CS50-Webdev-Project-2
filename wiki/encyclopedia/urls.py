from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="wiki"),
    path("wiki/<str:name>", views.title, name="title"),
    path("query/", views.query, name="query"),
    path("new/", views.newPage, name="new"),
    path("save/", views.save, name="save"),
    path("randomSite/", views.randomSite, name="randomPage"),
    path("edit/", views.edit, name="edit")
]
