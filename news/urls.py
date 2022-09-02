from django.urls import path, include

from . import views

urlpatterns = [
  path("", views.HomeView.as_view(), name="home"),
  path("world/", views.world, name="world"),
  path("business/", views.business, name="business"),
  path("technology/", views.technology, name="technology"),
  path("entertainment/", views.entertainment, name="entertainment"),
  path("sport/", views.sport, name="sport"),
  path("health/", views.health, name="health"),
]