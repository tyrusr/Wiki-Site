from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path("entry", views.entry, name="entry"),
    path("wiki/<str:entry>", views.entrypage, name="entrypage"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search"),
    path("error_page", views.error_page, name="error_page"),
    path("new_page", views.new_page, name="new_page"),
    path("title_exists", views.title_exists, name="title_exists"),
    path("edit_page/<str:entry>", views.edit_page, name="edit_page")
]
