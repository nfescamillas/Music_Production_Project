"""Smoke tests for the Django project foundation."""

import os


def test_django_settings_load() -> None:
    """The minimal Django configuration can initialize successfully."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    import django

    django.setup()
