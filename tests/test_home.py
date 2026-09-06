"""Smoke tests for the Django project foundation."""


def test_django_settings_load(monkeypatch) -> None:
    """The foundation initializes with a project-local SQLite database."""
    monkeypatch.setenv("DJANGO_SETTINGS_MODULE", "config.settings")

    import django
    from django.apps import apps
    from django.conf import settings

    django.setup()

    assert apps.ready
    assert settings.DATABASES["default"]["ENGINE"] == "django.db.backends.sqlite3"
    assert settings.DATABASES["default"]["NAME"] == settings.BASE_DIR / "db.sqlite3"
