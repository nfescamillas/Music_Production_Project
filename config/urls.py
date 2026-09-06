"""Root URL configuration for the project foundation."""

from django.urls import URLPattern, URLResolver


# Product routes are introduced by later issues. DEBUG shows Django's welcome page.
urlpatterns: list[URLPattern | URLResolver] = []
