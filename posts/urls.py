#!/usr/bin/env python3

from django.urls import path
from . import views


urlpatterns = [
    path("", views.post_list, name="list"),
    path("create/", views.post_create, name="home"),
    path("<int:id>", views.post_detail, name="detail"),
    path("update/", views.post_update, name="update"),
    path("delete/", views.post_delete, name="delete"),
]
