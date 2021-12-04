from django.urls import path
from django.urls.resolvers import URLResolver

from . import views

urlpatterns = [
    path("", views.index, name="index")
]