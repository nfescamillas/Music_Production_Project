Commands

- `uv sync` - install dependencies
- `uv run pytest` - the whole suite
- `uv run pytest tests/test_home.py` - one test file


Documents

- `_docs/process.md` - how work is organized


Rules

- This is a fully local, Django-based desktop-style application for personal
  Ableton Live production coaching. Do not add cloud storage, cloud audio
  processing, telemetry, accounts, or remote AI fallbacks.
- Dependencies are added in `pyproject.toml`. Do not add one without asking.
- Preserve the producer-in-control boundary: read, analyze, explain, and
  recommend; never modify, automate, or control Ableton Live projects.
- Treat ALS files as read-only gzip-compressed XML input. Normalize useful
  project data before persistence or AI use; never place raw ALS XML in an LLM
  prompt.
- Keep original ALS, WAV, stem, and reference files in user-selected local
  locations. Store paths, file fingerprints, metadata, and derived analysis
  results rather than copying large media files into the database.
- Keep objective measurements separate from subjective production advice.
  Explain the evidence behind recommendations and prioritize the most
  impactful next action rather than listing every possible improvement.
- Use SQLite and server-rendered Django pages for the MVP. Prefer Django
  templates, HTMX, and Tailwind over a separate frontend or distributed
  background-processing stack unless the task explicitly requires otherwise.
- Version audio-analysis results and retain their source fingerprint so reports
  are reproducible. Handle unsupported, missing, and corrupt local files with
  clear user-facing errors.
- Use only a configured local Ollama endpoint for coaching. Build concise,
  bounded structured context from project summaries, analysis, comparisons,
  profile preferences, and relevant journal entries.
- Keep each implementation task independently testable. Add focused tests for
  parser fixtures, DSP calculations, local-path validation, model-service
  failures, and user-visible workflow behavior as appropriate.
- Do not build MVP non-goals unless explicitly asked: autonomous song
  generation, automatic mastering, Ableton editing/control, plugin parameter
  control, voice control, mobile apps, or complex multi-agent systems.
