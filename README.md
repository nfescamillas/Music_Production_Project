# Personal AI Music Production Coach

Fully local Django foundation for an Ableton Live production coaching tool.

## Verify the foundation

From the repository root, after dependencies are installed, check Django and run
the smoke test with:

```powershell
uv run python manage.py check
uv run pytest tests/test_home.py
```

The smoke test initializes Django and verifies that SQLite is configured to use
`db.sqlite3` in the repository root. Run the whole suite with `uv run pytest`.

Start the local development server with:

```powershell
uv run python manage.py runserver 127.0.0.1:8000
```

Open http://127.0.0.1:8000/ to see Django's development welcome page. Stop the
server with Ctrl+C. This empty foundation has no product pages, admin route or
accounts, and does not require Ollama. Full contributor setup is tracked in
GitHub issue #2.
