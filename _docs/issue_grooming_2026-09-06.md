# GitHub issue grooming draft — 2026-09-06

Repository: https://github.com/nfescamillas/Music_Production_Project

## Publication status

NOT PUBLISHED. The first issue update was rejected with `user rejected MCP tool call`; no reason beyond that was supplied. No issues were changed or created. This is a reviewable local draft, not evidence of completed GitHub grooming.

Reviewed all 48 existing issues individually in issue-number order, including their current bodies, states and comments. All are open; all have zero comments. Original descriptions are preserved in the proposed bodies below. Priority and readiness are planning recommendations, not claims that unfinished dependencies are complete. No labels, assignees or milestones are changed.

## Proposed backlog cleanup

- Close #11 as duplicate of #3; #12 of #4; #13 of #5; #14 of #6. Preserve original content and canonical links.
- Restore four missing tasks already present in _docs/tasks.md: backlog tasks 4, 6, 8 and 10. These are task ordinals, not GitHub issue numbers. Create them one at a time, then replace the descriptive prerequisite references with the returned GitHub issue numbers.
- Keep #1 open for completion review: existing smoke test passed (1 test) and Django system check passed on 2026-09-06; actual server startup was not checked.
- Start with #2 and #32 while foundation gaps are restored. #10, #4 and #23 require dependency/tooling choices and approval before additions.
- #21 accepts a local path independently of registration, enabling #20 without a cycle. #43 provides reusable progress data/display before #42. #32 provides central configuration before #45. #31 exposes optional context sections; #40 supplies profile/journal integration.
- Local safeguards apply from initial implementation; #44 is an audit, not permission to defer them. No remote fallback is allowed.

## Publication procedure after authorization

For each issue, re-fetch its current body and comments, reconcile any concurrent changes, apply its proposed body, verify the result, then move to the next issue. Create missing prerequisites sequentially and resolve their links before dependent issue updates. Close only the four verified duplicates, using a supported duplicate/not-planned closure reason and an explicit canonical link. Do not close #1 without remaining completion evidence.

## Proposed new prerequisite issues

### backlog-4: 4. Create the base application layout

## Goal

Provide a reusable Django domain app and template/static structure.

## Priority and dependencies

P0. Depends on #1. Enables #3, #6, #19 and #38.

## Acceptance criteria

- [ ] Register a dedicated domain app with conventional models, services, views, templates, static and test locations.
- [ ] Django discovers app templates/static assets without per-feature setup.
- [ ] A focused test confirms app loading and template rendering; the existing smoke test passes.
- [ ] No product models, speculative services or new dependencies are added.

Restores task 4 already defined in _docs/tasks.md.

### backlog-6: 6. Add placeholder navigation pages

## Goal

Give all eight navigation destinations working local routes.

## Priority and dependencies

P0. Depends on #3; route and shell implementation may be coordinated in sequence.

## Acceptance criteria

- [ ] Named routes exist for Dashboard, Projects, Coach, Analyze, References, Artist Profile, Production Journal and Settings.
- [ ] Each returns HTTP 200, identifies its destination and inherits the shared shell with active navigation.
- [ ] Route reversal and response tests cover every destination; no dead links.
- [ ] No product workflows or external assets are introduced.

Restores task 6 already defined in _docs/tasks.md.

### backlog-8: 8. Define the Project data model

## Goal

Persist core local production-project metadata in SQLite.

## Priority and dependencies

P0. Depends on the restored base application layout task. Enables #5, #17, #36 and #43.

## Acceptance criteria

- [ ] Store required trimmed name, optional ALS path, genre, tempo, key, timestamps and explicit import status.
- [ ] A project can exist without an ALS source; supplied tempo is positive and supplied path is validated as local.
- [ ] Define one shared path-validation contract; preserve user-selected source location and never copy media into SQLite.
- [ ] Add migrations and a development inspection path; test persistence, defaults, invalid values and path failures.
- [ ] No parsing or Ableton control.

Restores task 8 already defined in _docs/tasks.md.

### backlog-10: 10. Create a project detail page

## Goal

Show stored project metadata and processing state.

## Priority and dependencies

P0. Depends on the restored Project model task and #3. Enables #5 and later detail-page integrations.

## Acceptance criteria

- [ ] Named detail route displays name, optional source path, genre, tempo, key, timestamps and import state.
- [ ] Structure, audio analysis and coaching sections have clear empty states.
- [ ] Unknown project IDs return HTTP 404 and user-provided text is escaped.
- [ ] Focused view tests cover populated/missing optional data and unknown IDs.
- [ ] No parsing, DSP or model calls occur on this page.

Restores task 10 already defined in _docs/tasks.md.

## Existing issue edits

### [#1 — 1. Create the empty Django project](https://github.com/nfescamillas/Music_Production_Project/issues/1)

Proposed state: **open**.

## Goal

Establish a runnable local Django project with one passing automated test.

## Description

Create the project structure, dependency definition, and minimal Django configuration required to run locally. Add a deliberately small smoke test and document the single command that runs it successfully. Do not add product features, data models, or UI beyond what is necessary to prove the foundation works.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Implementation present; completion review

**Dependencies:** None

### Scope, acceptance criteria and validation

Verify committed configuration, SQLite, and documented smoke command. Record actual local server startup before closing. Smoke test passed (1 test) and manage.py check passed on 2026-09-06 using .venv/Scripts/python.exe. Commit 26b9e1d supplies the foundation.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#2 — 2. Define local development setup instructions](https://github.com/nfescamillas/Music_Production_Project/issues/2)

Proposed state: **open**.

## Goal

Make it possible for a new contributor to run the application and tests locally.

## Description

Write concise setup documentation covering the supported Python version, virtual environment creation, dependency installation, database initialization, app startup, and test execution. State that all data processing and model access must remain local-first. Keep the instructions specific to this repository and Windows-friendly.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Ready

**Dependencies:** #1

### Scope, acceptance criteria and validation

Document Python >=3.12 (3.12 verified), uv prerequisite, uv sync and its managed .venv, migrate, runserver on 127.0.0.1, uv run pytest, and the single-file test command. State that runtime processing is fully local, not merely local-first. Explain initial dependency downloads and that Ollama is unnecessary for the foundation. Validate commands on Windows; distinguish verified steps from untested ones.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#3 — 5. Build the local desktop-style shell](https://github.com/nfescamillas/Music_Production_Project/issues/3)

Proposed state: **open**.

## Goal

Display a consistent application frame with primary navigation.

## Description

Create a base template with the product name and navigation links for Dashboard, Projects, Coach, Analyze, References, Artist Profile, Production Journal, and Settings. Use a simple responsive layout suitable for a local desktop-sized browser window. The links may lead to placeholder pages at this stage.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisite

**Dependencies:** Missing backlog task 4: base app layout

### Scope, acceptance criteria and validation

Create reusable shell with product name, semantic main/navigation regions, keyboard focus, and responsive desktop/narrow layouts. Coordinate named destinations with missing task 6; keep route implementation there. Tests verify inherited layout and all eight navigation entries. Canonical issue for duplicate #11; styling integration belongs to #4.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#4 — 7. Add Tailwind CSS to the Django interface](https://github.com/nfescamillas/Music_Production_Project/issues/4)

Proposed state: **open**.

## Goal

Establish a maintainable styling workflow for the local interface.

## Description

Integrate Tailwind CSS with the Django static-asset pipeline and provide a documented development/build workflow. Apply a small neutral visual foundation to the base layout, including typography, spacing, colors, and accessible focus states. Do not design individual product dashboards in this task.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Dependency/tooling approval required

**Dependencies:** #3

### Scope, acceptance criteria and validation

Select and document a minimal Tailwind build approach before adding tools. Ask before adding dependencies; Python dependencies belong in pyproject.toml. Serve generated CSS locally with no CDN/runtime download. Document Windows build/watch commands and Django static discovery. Verify production CSS includes template classes and visible keyboard focus. No detailed dashboards. Canonical issue for duplicate #12.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#5 — 9. Create project list and creation screens](https://github.com/nfescamillas/Music_Production_Project/issues/5)

Proposed state: **open**.

## Goal

Let a user create and browse local production-project records.

## Description

Build server-rendered pages for listing projects and creating a new project record. Include clear validation feedback and a direct link from each listed project to its detail page. This task stores metadata only; it does not parse an ALS file.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisites

**Dependencies:** Missing backlog tasks 8 (Project model), 10 (detail); #3

### Scope, acceptance criteria and validation

Create project list and metadata form with required trimmed name, optional genre/tempo/key/ALS path, field errors, CSRF, and redirect after success. Empty list offers creation; each record links to valid detail route. Duplicate names may be allowed because records have separate IDs. Validate local paths without parsing or copying ALS. Test valid/invalid POST, persistence, empty list, and detail links. Canonical issue for #13.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#6 — 11. Design the normalized Ableton project schema](https://github.com/nfescamillas/Music_Production_Project/issues/6)

Proposed state: **open**.

## Goal

Define the internal data representation used after parsing an Ableton ALS file.

## Description

Document and implement Django models or a deliberately versioned structured representation for normalized project data. Cover project-level metadata, tracks, clips, MIDI notes, devices, arrangement information, and source-file references, while allowing fields to be unavailable. Do not parse real ALS files in this task.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisite

**Dependencies:** Missing backlog task 4; Project model only if persisted relationally

### Scope, acceptance criteria and validation

Define a versioned normalized contract for metadata, track IDs/types, clips/notes/devices, arrangement coordinates and source references. Specify beats versus seconds, optional/null versus empty, stable parent IDs, unsupported fields, parser version and source fingerprint. Choose models or structured serialization, document rationale and migrations if needed. Test round-trip/validation and absent values; no raw XML storage or parsing. Canonical issue for #14.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#7 — 13. Extract basic ALS project metadata](https://github.com/nfescamillas/Music_Production_Project/issues/7)

Proposed state: **open**.

## Goal

Obtain project name, tempo, and time signature from a valid ALS file.

## Description

Extend the ALS parsing service to extract only stable project-level metadata and return it through the normalized representation. Clearly distinguish missing source values from parser failures. Test against small ALS fixtures with both complete and incomplete metadata.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisites

**Dependencies:** #6, #15

### Scope, acceptance criteria and validation

Extract project name when present, tempo in BPM, time-signature numerator/denominator, and source format/version into normalized fields. If name comes from filename, label its provenance. Missing optional values remain unavailable; malformed values yield documented warnings or errors rather than invented defaults. Test minimal complete/missing/invalid fixtures and unsupported versions; no metadata persistence side effects.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#8 — 14. Extract ALS track metadata](https://github.com/nfescamillas/Music_Production_Project/issues/8)

Proposed state: **open**.

## Goal

Read named audio and MIDI tracks from an Ableton project.

## Description

Add parser support for track identifiers, names, track kinds, and basic enabled/muted state where present. Persist or expose the data through the normalized project schema without adding clip or device parsing. Include fixtures covering an audio track, a MIDI track, and absent optional values.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisites

**Dependencies:** #6, #15

### Scope, acceptance criteria and validation

Extract audio/MIDI track ID, name, kind and supported enabled/mute state in stable order. Distinguish unknown state from false; define handling of group/return/master/unknown tracks without claiming unsupported kinds are audio. Test mixed types, optional names/state, track identity and ordering. No clip/device extraction or source writes.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#9 — 15. Extract ALS MIDI clip and note data](https://github.com/nfescamillas/Music_Production_Project/issues/9)

Proposed state: **open**.

## Goal

Capture usable note-level composition information from MIDI tracks.

## Description

Add parsing for MIDI clips and their note timing, pitch, duration, and velocity where the ALS document provides them. Map values into the normalized schema and avoid assumptions about every Ableton version exposing identical XML. Cover empty clips and tracks with no MIDI clips in tests.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisite

**Dependencies:** #8

### Scope, acceptance criteria and validation

Map MIDI clips and notes to their parent track with stable IDs, pitch, velocity, start and duration in documented beat coordinates. Distinguish session and arrangement placement, clip-relative note time and loop offsets; unavailable arrangement position stays null. Test multiple clips, empty/no clips, boundary note values, loops and optional attributes. Document supported fixture versions; never silently coerce corrupt values.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#10 — 3. Configure project-wide quality checks](https://github.com/nfescamillas/Music_Production_Project/issues/10)

Proposed state: **open**.

## Goal

Provide repeatable formatting, linting, and test commands for the Django project.

## Description

Configure lightweight Python formatting and linting, document one command for all checks, and ensure the initial project passes. Exclude hosted CI and deployment automation.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Tooling approval required

**Dependencies:** #1, #2

### Scope, acceptance criteria and validation

Choose one lightweight formatter/linter approach and ask before adding dependencies to pyproject.toml. Define a Windows-friendly command that runs formatting checks, lint and pytest and returns nonzero if any fail. Exclude .venv, generated assets and caches appropriately. Verify success and an intentional temporary failure without committing the failing fixture. No hosted CI or deployment.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#11 — 5. Build the local desktop-style shell](https://github.com/nfescamillas/Music_Production_Project/issues/11)

Proposed state: **closed**; duplicate of #3.

## Goal

Display a consistent application frame with primary navigation.

## Description

Create a responsive base template with navigation for Dashboard, Projects, Coach, Analyze, References, Artist Profile, Production Journal, and Settings. Placeholder destinations are acceptable.

## Grooming — 2026-09-06

**Priority:** Duplicate

**Readiness:** Proposed close as duplicate

**Dependencies:** #3

### Scope, acceptance criteria and validation

Retain original description and add a canonical link to #3. Shell scope is already covered there; transfer any unique comments before closing. No implementation on this duplicate.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#12 — 7. Add Tailwind CSS to the Django interface](https://github.com/nfescamillas/Music_Production_Project/issues/12)

Proposed state: **closed**; duplicate of #4.

## Goal

Establish a maintainable styling workflow for the local interface.

## Description

Integrate Tailwind with Django static assets, document development/build commands, and establish accessible typography, spacing, colors, and focus states. Do not design detailed product pages.

## Grooming — 2026-09-06

**Priority:** Duplicate

**Readiness:** Proposed close as duplicate

**Dependencies:** #4

### Scope, acceptance criteria and validation

Retain original description and link to #4, which owns Tailwind/static build and accessible base styling. Transfer any unique discussion before closing.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#13 — 9. Create project list and creation screens](https://github.com/nfescamillas/Music_Production_Project/issues/13)

Proposed state: **closed**; duplicate of #5.

## Goal

Let a user create and browse local production-project records.

## Description

Build server-rendered list and creation pages with validation and project-detail links. Store metadata only; do not parse ALS here.

## Grooming — 2026-09-06

**Priority:** Duplicate

**Readiness:** Proposed close as duplicate

**Dependencies:** #5

### Scope, acceptance criteria and validation

Retain original description and link to #5, which owns metadata-only project creation/list screens. Transfer any unique discussion before closing.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#14 — 11. Design the normalized Ableton project schema](https://github.com/nfescamillas/Music_Production_Project/issues/14)

Proposed state: **closed**; duplicate of #6.

## Goal

Define the internal data representation used after parsing an Ableton ALS file.

## Description

Implement a versioned representation for project metadata, tracks, clips, MIDI notes, devices, arrangement information, and source references, allowing unavailable fields. Do not parse files yet.

## Grooming — 2026-09-06

**Priority:** Duplicate

**Readiness:** Proposed close as duplicate

**Dependencies:** #6

### Scope, acceptance criteria and validation

Retain original description and link to #6, which owns the versioned normalized ALS representation. Transfer any unique discussion before closing.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#15 — 12. Implement safe ALS file decompression and XML loading](https://github.com/nfescamillas/Music_Production_Project/issues/15)

Proposed state: **open**.

## Goal

Read a local Ableton ALS file into an XML document without modifying it.

## Description

Validate local paths, decompress gzip ALS content, load XML safely, and report useful errors. Never persist raw XML as LLM context; test valid and invalid fixtures.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisite

**Dependencies:** #6

### Scope, acceptance criteria and validation

Implement read-only local path validation, bounded gzip decompression and XML loading; reject URL/UNC/network inputs and unsupported or non-file paths with actionable errors. Define compressed/decompressed limits; reject DTD/external entity expansion. Report missing/unreadable/corrupt gzip/XML and unsupported ALS clearly. Test valid fixture and each failure, enforce unchanged source fingerprint, and retain no XML in DB, logs or model context. Ask before any parser dependency.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#16 — 16. Extract ALS device and effect summaries](https://github.com/nfescamillas/Music_Production_Project/issues/16)

Proposed state: **open**.

## Goal

Summarize instruments and effects used by each Ableton track.

## Description

Parse concise device names/types and associate them with tracks. Do not recreate presets or automate parameters; test associations.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisite

**Dependencies:** #8

### Scope, acceptance criteria and validation

Extract concise device name/type and supported rack nesting into the correct track, with stable order and unavailable/unknown values preserved. Bound nesting and output size. Test multiple tracks, nested racks, unknown devices and no devices. No presets, binary plugin state, parameter automation or plugin execution.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#17 — 17. Import parsed ALS data into a Project](https://github.com/nfescamillas/Music_Production_Project/issues/17)

Proposed state: **open**.

## Goal

Connect a selected ALS source file to persisted normalized project structure.

## Description

Add an import action that parses, persists supported data, records clear status, preserves relevant user metadata, and avoids partial corrupt data on failure.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisites

**Dependencies:** #5, #6, #7, #8, #9, #16

### Scope, acceptance criteria and validation

POST-only explicit import reads selected ALS, records source fingerprint and parser/schema versions, and atomically replaces normalized structure on success. Preserve user metadata; distinguish parsed and user values. Failure retains last successful structure and clear failed-attempt status without partial data. Test first import, unchanged reimport, changed source, parse failure and database rollback. Source must remain untouched.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#18 — 18. Display imported Ableton project structure](https://github.com/nfescamillas/Music_Production_Project/issues/18)

Proposed state: **open**.

## Goal

Let the user inspect tracks, clips, notes, and devices extracted from an ALS file.

## Description

Show normalized data on project details with track-level readability and good empty states, without raw XML dumps.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #17; missing backlog task 10

### Scope, acceptance criteria and validation

Display metadata and readable tracks with expandable/paginated clip, note and device details. Show supported/missing/unsupported data distinctly, source/parser versions and last import status. Escape source text; no raw XML dump. Test populated, failed, empty and large normalized fixture states; avoid loading every note into initial HTML.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#19 — 19. Define the audio-analysis result schema](https://github.com/nfescamillas/Music_Production_Project/issues/19)

Proposed state: **open**.

## Goal

Persist versioned, reproducible measurements for a local audio file.

## Description

Define analysis status, version, fingerprint, metrics, loudness, dynamics, spectral, stereo, silence, and error fields. Do not calculate metrics yet.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisite

**Dependencies:** Missing backlog task 4

### Scope, acceptance criteria and validation

Define shared audio-source/result models reusable by project mixes, stems and references. Results contain source fingerprint, algorithm/schema versions, parameters, timestamps, status and per-metric value/unit/unavailable reason. Preserve history across reruns. Define valid finite-value serialization and silence representation; store paths and derived data only. Test migrations, transitions, validation and history; no DSP yet.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#20 — 20. Add WAV file registration to a project](https://github.com/nfescamillas/Music_Production_Project/issues/20)

Proposed state: **open**.

## Goal

Allow a user to associate a local WAV mix or stem with a production project.

## Description

Store validated local WAV path, label, and source type without copying audio into the database; display registered files on the project.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisites

**Dependencies:** #5, #19, #21

### Scope, acceptance criteria and validation

Register local WAV path, label and full-mix/stem role using shared metadata inspection. Reject remote/missing/directory/unreadable/corrupt input; preserve original file in user-selected location. Record fingerprint and metadata and define duplicate registration handling. Show registered sources and changed/missing file status on detail. Test valid/invalid forms and unchanged source bytes; no automatic analysis.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#21 — 21. Implement WAV metadata inspection](https://github.com/nfescamillas/Music_Production_Project/issues/21)

Proposed state: **open**.

## Goal

Read fundamental technical properties from a registered WAV file.

## Description

Report duration, sample rate, channels, available bit depth, and frame count with useful corrupt/unsupported-file errors and fixture tests.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisite

**Dependencies:** #19

### Scope, acceptance criteria and validation

Implement path-based inspection independent of registration to avoid a #20 dependency cycle. Return frame count, sample rate, channels, duration and bit depth when meaningful. Document supported WAV encodings; reject unsupported and truncated files clearly. Test compact mono/stereo fixtures, duration=frames/rate, empty/truncated and unsupported formats. Reuse local path rules and ask before adding decoding libraries.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#22 — 22. Measure peak, RMS, and crest factor](https://github.com/nfescamillas/Music_Production_Project/issues/22)

Proposed state: **open**.

## Goal

Produce baseline dynamics measurements for an imported WAV file.

## Description

Implement deterministic peak, RMS, and crest factor calculations with documented units/channel handling and tolerance-based fixture tests.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisites

**Dependencies:** #19, #21

### Scope, acceptance criteria and validation

Define normalized sample amplitude, sample peak/RMS in dBFS and crest factor in dB; document channel aggregation and sample-peak versus true-peak distinction. Handle digital silence/zero RMS without invalid JSON, and use bounded-memory processing. Test known sine amplitude, constant samples, silence and unequal stereo channels with justified tolerances. Record algorithm version/parameters.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#23 — 23. Measure integrated loudness and true peak](https://github.com/nfescamillas/Music_Production_Project/issues/23)

Proposed state: **open**.

## Goal

Report mastering-relevant loudness metrics for a WAV file.

## Description

Use a local loudness library for integrated LUFS, practical short-term loudness, and true peak; handle unavailable results honestly.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Dependency approval required

**Dependencies:** #19, #21

### Scope, acceptance criteria and validation

Propose a local loudness library and obtain dependency approval before installation. Document the implemented loudness standard, channel support, true-peak method/oversampling and LUFS/dBTP units. Distinguish sample peak from true peak; label short/empty/silent inputs as unavailable where required. Validate against trusted controlled fixture values with tolerances, including intersample peaks. Short-term output needs explicit window/summary definition or documented unavailability.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#24 — 24. Measure frequency-band balance](https://github.com/nfescamillas/Music_Production_Project/issues/24)

Proposed state: **open**.

## Goal

Summarize low, mid, and high-frequency energy in a WAV file.

## Description

Derive a stable, documented frequency-band summary stored for comparison and coaching; focus on reliable metrics rather than visual interpretation.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #19, #21

### Scope, acceptance criteria and validation

Specify versioned frequency-band edges in Hz, spectral/window method and energy aggregation across frames/channels. Report reproducible numeric energy proportions with units, handling Nyquist limits and silence honestly. Test tones inside bands, boundary tones, mixed bands, multiple sample rates and silence with tolerances. No universal good/bad tonal judgments or new plotting UI.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#25 — 25. Measure stereo and silence characteristics](https://github.com/nfescamillas/Music_Production_Project/issues/25)

Proposed state: **open**.

## Goal

Identify basic stereo-image and silence information from a WAV file.

## Description

Calculate applicable stereo width/correlation and significant silent regions, report not-applicable for mono, and test mono/stereo fixtures.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #19, #21

### Scope, acceptance criteria and validation

Define correlation and any width formula, aggregation, silence threshold and minimum silent-region duration as versioned parameters. Mono stereo metrics are not applicable; constant/silent channels cannot yield fabricated correlation. Silence detection still applies to mono. Test identical/anti-phase/independent stereo, mono, all silence and leading/interior/trailing regions with documented time precision.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#26 — 26. Run and review an audio analysis](https://github.com/nfescamillas/Music_Production_Project/issues/26)

Proposed state: **open**.

## Goal

Let a user trigger a complete baseline analysis and inspect its results.

## Description

Run available measurements, persist status/version/timestamps/results/errors, and render objective results separately from AI interpretation.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisites

**Dependencies:** #20, #22, #23, #24, #25

### Scope, acceptance criteria and validation

Provide explicit POST analysis and objective results with source identity/fingerprint, versions, timestamp, units, missing-metric reasons and actionable failures. Recheck fingerprint to prevent stale/mixed-source results; preserve prior runs. Test successful/partial/failed run and repeat analysis. Keep service callable by #27; synchronous MVP path must have a documented bounded input/performance limit and cannot silently hang on large audio.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#27 — 27. Add background analysis job tracking](https://github.com/nfescamillas/Music_Production_Project/issues/27)

Proposed state: **open**.

## Goal

Keep the local interface responsive while audio analysis runs.

## Description

Add lightweight local job tracking with queued/running/completed/failed states and HTMX polling. Do not introduce Redis, cloud, or distributed workers.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisite

**Dependencies:** #26

### Scope, acceptance criteria and validation

Use a single-machine bounded execution mechanism with SQLite-backed queued/running/completed/failed state, atomic job claiming and duplicate submission control. Poll server-rendered status; stop polling on terminal state. Define restart recovery for orphaned running jobs, concurrency limits and safe database connections. Test transitions, failure/restart and duplicate submissions deterministically. No Redis, distributed workers or cloud; ask before new dependencies.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#28 — 28. Create the local reference-track library model](https://github.com/nfescamillas/Music_Production_Project/issues/28)

Proposed state: **open**.

## Goal

Organize locally stored reference-track metadata for comparison.

## Description

Add reference metadata for local WAV path, title, artist, genre, category, and analysis status; reuse shared audio analysis and provide list/create screens.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #19, #21, #3

### Scope, acceptance criteria and validation

Add reference metadata title/artist/genre/category linked to shared local WAV source, list and validated creation screen. Derive analysis status from shared result records; do not duplicate DSP. Test empty list, valid/corrupt/remote path input and persistence without media copying. Analysis execution belongs to #29.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#29 — 29. Analyze a reference track](https://github.com/nfescamillas/Music_Production_Project/issues/29)

Proposed state: **open**.

## Goal

Generate the same objective audio measurements for a reference track.

## Description

Connect references to the shared versioned audio-analysis flow, expose status/results, and retain metadata on failures.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #28, #26, #27

### Scope, acceptance criteria and validation

Run references through the same job/measurement pipeline and versions as project audio. Display status, timestamps and results while preserving reference metadata on failure. Test successful result equivalence for identical source/parameters, missing/changed file and failed rerun with prior result retained.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#30 — 30. Compare a project mix with a reference track](https://github.com/nfescamillas/Music_Production_Project/issues/30)

Proposed state: **open**.

## Goal

Produce an objective difference report between two completed analyses.

## Description

Calculate and label differences in loudness, peak, dynamics, frequency balance, and stereo characteristics; label all as measurements rather than judgments.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #26, #29

### Scope, acceptance criteria and validation

Select explicit project mix and reference analysis runs; define differences as project minus reference with metric units. Require compatible algorithm versions/parameters or explain why comparison is unavailable. Preserve both source fingerprints/result IDs; flag stale sources and exclude unavailable metrics. Test known positive/negative deltas, same-source zero, incompatible runs and mono/stereo gaps. Never label numeric differences as quality scores.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#31 — 31. Define structured coach context](https://github.com/nfescamillas/Music_Production_Project/issues/31)

Proposed state: **open**.

## Goal

Create a concise, safe representation of project information for local LLM prompts.

## Description

Select relevant metadata, ALS summaries, audio analyses, comparisons, and journal data with strict limits. Exclude raw XML, full audio, and unnecessary paths.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisites

**Dependencies:** #6, #19, #30

### Scope, acceptance criteria and validation

Build deterministic allowlisted structured context with source IDs/versions, normalized ALS summaries, measurements and comparison evidence. Define strict total/per-section budgets, deterministic truncation and explicit missing/stale sections. Provide optional extension points for profile/journal; implement their selection in #40 to avoid duplication/cycles. Exclude raw XML, audio and unnecessary paths. Test missing data, oversized inputs, ordering, version provenance and forbidden content.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#32 — 32. Add local Ollama availability checks](https://github.com/nfescamillas/Music_Production_Project/issues/32)

Proposed state: **open**.

## Goal

Detect whether a compatible local LLM service and model are ready to use.

## Description

Configure a local endpoint/model check and give clear remediation for unavailable service. Never silently use a cloud fallback; add mocked tests.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Ready; no Settings UI dependency

**Dependencies:** #1

### Scope, acceptance criteria and validation

Define central endpoint/model configuration defaults usable before #45. Validate loopback-only Ollama URLs and block remote redirects before any request. Set bounded timeouts and distinguish connection failure, missing model, malformed response and available service. Mock all network tests, including rejected remote endpoints. No automatic model download, account or fallback.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#33 — 33. Implement the local coach response service](https://github.com/nfescamillas/Music_Production_Project/issues/33)

Proposed state: **open**.

## Goal

Request a structured production-coaching response from the configured local model.

## Description

Combine question and structured context, require observations/recommendations/explanations/next actions, and gracefully handle malformed output or service failure.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Blocked by prerequisites

**Dependencies:** #31, #32

### Scope, acceptance criteria and validation

Accept bounded question/context; require structured observations with evidence IDs, subjective recommendations with explanations, and one highest-priority next action. Validate output shape/size and unknown evidence references. Treat imported/user text as data, not instructions. Bound timeout/retries and report malformed/unavailable model errors. Mock success/failure cases; no external fallback or executable Ableton instructions/actions.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#34 — 34. Build the project-aware Coach page](https://github.com/nfescamillas/Music_Production_Project/issues/34)

Proposed state: **open**.

## Goal

Let a user ask a coaching question in the context of a selected project.

## Description

Create a server-rendered interface to select a project, ask a question, receive structured local-model advice, and view source availability without raw prompt/XML exposure.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #3, #5, #33

### Scope, acceptance criteria and validation

Provide project selection and validated question POST, clear progress/error state and structured advice. Show available/missing evidence categories and distinguish observations from suggestions. Escape generated text and preserve question on error. Test no projects, unknown selection, empty/oversized question, success and unavailable model with mocks. No model requests on GET; history comes from #35.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#35 — 35. Store coaching conversations](https://github.com/nfescamillas/Music_Production_Project/issues/35)

Proposed state: **open**.

## Goal

Preserve project-specific questions and recommendations for later review.

## Description

Persist question, response, project link, context/analysis versions, timestamp, and failures; display readable chronological history.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisite

**Dependencies:** #34

### Scope, acceptance criteria and validation

Persist project-specific question, validated response or bounded error, timestamp, model name, context version and referenced analysis/source IDs/versions. Store bounded allowlisted context snapshot if needed for reproducibility; no raw XML/audio/unnecessary paths. Display ordered project-scoped history on Coach/detail. Test success/failure persistence, ordering and no cross-project leakage; no semantic memory.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#36 — 36. Define the production-session journal model](https://github.com/nfescamillas/Music_Production_Project/issues/36)

Proposed state: **open**.

## Goal

Record focused production sessions and planned follow-up work.

## Description

Add project-linked date, completed work, identified problems, and next actions, keeping editable user notes separate from AI observations.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisite

**Dependencies:** Missing backlog task 8

### Scope, acceptance criteria and validation

Create project-linked session date, completed work, problems and next actions with created/updated timestamps. Specify required fields, text length limits and deterministic date ordering. Keep user notes separate from future AI observations. Test migrations, validation, optional notes and project associations; no inference or editing UI.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#37 — 37. Build the production journal interface](https://github.com/nfescamillas/Music_Production_Project/issues/37)

Proposed state: **open**.

## Goal

Let a user create, edit, and review production-session entries.

## Description

Build project-scoped list, create, and edit pages; show latest session and next actions on the project detail page.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #36, #3; missing backlog task 10

### Scope, acceptance criteria and validation

Create project-scoped list/create/edit forms with CSRF and clear validation. Detail shows latest session and next actions with deterministic tie-breaking. Test create/edit/list, empty state, unknown entry/project and cross-project mismatches; escape user notes. No automatic AI rewriting.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#38 — 38. Define the Artist Profile model](https://github.com/nfescamillas/Music_Production_Project/issues/38)

Proposed state: **open**.

## Goal

Store editable long-term preferences and goals that personalize coaching.

## Description

Model local genres, BPM/key preferences, instruments/textures, references, goals, strengths, and weaknesses without automatic inference.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisite

**Dependencies:** Missing backlog task 4

### Scope, acceptance criteria and validation

Model one local editable Artist Profile with optional genres, preferred BPM range/keys, instruments/textures, reference preferences, goals, strengths and weaknesses. Enforce singleton semantics and valid ordered positive BPM range. Test empty profile, edits, invalid ranges and singleton behavior; no inferred personal facts or accounts.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#39 — 39. Build the Artist Profile interface](https://github.com/nfescamillas/Music_Production_Project/issues/39)

Proposed state: **open**.

## Goal

Let the user maintain the personal preferences used by the coach.

## Description

Build a form-based view/edit page explaining that data stays local; test creation, update, and display.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #38, #3

### Scope, acceptance criteria and validation

Build view/edit form that creates the singleton on first save, handles optional values and explains local personalization. Test initial empty state, valid update, invalid BPM/text limits, escaping and no duplicate profiles. No outbound requests or automatic inference.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#40 — 40. Incorporate profile and journal context into coaching](https://github.com/nfescamillas/Music_Production_Project/issues/40)

Proposed state: **open**.

## Goal

Make local coaching advice reflect declared preferences and recent project work.

## Description

Extend the context builder with bounded, clearly labeled profile and recent-session information while enforcing prompt-size limits.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #31, #36, #38

### Scope, acceptance criteria and validation

Add allowlisted profile preferences and a bounded recent-session selection for the active project, deterministic date ordering and existing context budget enforcement. Label user-authored preferences/notes separately from measured evidence and AI history. Test no profile/sessions, irrelevant-project exclusion, oversized histories and retained essential measurements.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#41 — 41. Generate a dashboard next-action summary](https://github.com/nfescamillas/Music_Production_Project/issues/41)

Proposed state: **open**.

## Goal

Answer “What should I work on next, and why?” for the current project.

## Description

Create a deterministic evidence-linked next-action service using incomplete project data, journal actions, and findings, including an honest insufficient-information state.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #19, #35, #36

### Scope, acceptance criteria and validation

Define an explicit deterministic precedence policy for user next actions, missing workflow prerequisites and current evidence-backed findings. Return one provisional action, reason, source IDs and missing-information state without an LLM call. Ignore stale/failed evidence and never invent a musical diagnosis. Test conflicts, stable tie-breaks, no data and cross-project isolation.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#42 — 42. Build the dashboard](https://github.com/nfescamillas/Music_Production_Project/issues/42)

Proposed state: **open**.

## Goal

Present the current project, progress areas, focus, and next action on launch.

## Description

Replace the placeholder with current metadata, production-stage progress, focus, and next-action states using real data or clear empty states.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #3, #41, #43

### Scope, acceptance criteria and validation

Define explicit current-project selection persisted locally and safe behavior when selection is missing/deleted. Show real project metadata, user stage progress, today's focus and one evidence-linked next action. Provide working detail/analyze links and honest empty/error states. Test zero/multiple projects, switching selection and missing analysis; no invented progress or background model calls.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#43 — 43. Add project production-progress tracking](https://github.com/nfescamillas/Music_Production_Project/issues/43)

Proposed state: **open**.

## Goal

Let a user track composition, sound design, arrangement, mixing, and mastering progress.

## Description

Add editable progress and notes per stage, then display accessible labels and visual bars on project details and dashboard.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** Missing backlog task 8 and task 10; #3

### Scope, acceptance criteria and validation

Persist user-editable 0–100 progress and optional notes for composition, sound design, arrangement, mixing and mastering. Define unset separately from zero. Add validated detail form and reusable display for #42; do not depend on dashboard completion. Test bounds, saves, unset states and project isolation. Provide numeric labels with bars; no automated progress inference.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#44 — 44. Add robust local-path privacy safeguards](https://github.com/nfescamillas/Music_Production_Project/issues/44)

Proposed state: **open**.

## Goal

Prevent project data from being sent outside the local application by default.

## Description

Audit imports, analysis, and LLM use; reject remote LLM endpoints by default, document the boundary, and test key safeguards.

## Grooming — 2026-09-06

**Priority:** P0

**Readiness:** Cross-cutting requirement; final audit later

**Dependencies:** Baseline safeguards in #15, #21, #32; final audit after #17, #26, #33, #45

### Scope, acceptance criteria and validation

Tighten goal from local 'by default' to local-only. Audit all file/model paths and forbid remote endpoints/fallbacks, remote redirects, cloud storage, telemetry and runtime asset CDNs. Test bypasses, unchanged source files and absent raw XML/audio in persistence/prompts. Verify loopback binding and CSRF protections. Safeguards are required from first implementation, not deferred until this audit.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#45 — 45. Create local settings for model and analysis behavior](https://github.com/nfescamillas/Music_Production_Project/issues/45)

Proposed state: **open**.

## Goal

Give the user a single place to configure local application behavior.

## Description

Create local settings for model endpoint/name, analysis defaults, and data locations; validate and flag non-local endpoints with no accounts/cloud features.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #32, #19, #3

### Scope, acceptance criteria and validation

Reuse central validated configuration; provide endpoint/model name and documented analysis defaults plus local application-data locations. Reject non-loopback endpoints rather than merely flagging them. Validate before persistence and preserve prior settings on failure; perform availability check only by explicit action. Store effective parameters with future runs; never rewrite history or move source media. Test valid/invalid settings and persistence; no accounts.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#46 — 46. Add end-to-end MVP workflow tests](https://github.com/nfescamillas/Music_Production_Project/issues/46)

Proposed state: **open**.

## Goal

Verify the primary local workflow works across project import, analysis, comparison, and coaching.

## Description

Add integration coverage for project creation, fixture ALS import, WAV analysis, reference comparison, journal creation, and mock coach-context assembly.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #17, #26, #29, #30, #35, #37, #39, #40, #42, #45

### Scope, acceptance criteria and validation

Add deterministic local integration tests spanning project creation, ALS import, WAV registration/analysis, reference comparison, profile/journal, bounded context and mocked coaching/history. Use temporary SQLite/files and generated or tiny committed fixtures. Cover corrupt/missing source, changed fingerprint, model unavailable and no partial writes. Assert source bytes unchanged and no external networking. Run full uv run pytest; avoid requiring a live model.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#47 — 47. Document MVP usage and known limitations](https://github.com/nfescamillas/Music_Production_Project/issues/47)

Proposed state: **open**.

## Goal

Provide an honest guide for using the completed local MVP.

## Description

Document inputs, Ableton read-only boundary, local-model setup, workflow, measurement versus judgment, parser limits, and common troubleshooting.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by prerequisites

**Dependencies:** #46 and implemented user workflows

### Scope, acceptance criteria and validation

Write Windows usage walkthrough for project/ALS/WAV/reference/profile/journal/coach workflows and loopback Ollama setup. Document actual supported ALS versions/WAV encodings, metric units/unavailability, stale sources, failure recovery and known limitations. Clearly separate measurements/advice and read-only producer control. Verify examples against delivered UI and commands; avoid claiming future features.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

### [#48 — 48. Prepare a local release package](https://github.com/nfescamillas/Music_Production_Project/issues/48)

Proposed state: **open**.

## Goal

Produce a repeatable local distribution artifact for the MVP.

## Description

Document and verify a Windows-focused package that launches Django locally with static assets and local defaults; exclude telemetry, cloud accounts, updates, and remote deployment.

## Grooming — 2026-09-06

**Priority:** P1

**Readiness:** Blocked by release prerequisites

**Dependencies:** #4, #10, #27, #44, #45, #46, #47

### Scope, acceptance criteria and validation

Choose smallest repeatable Windows local distribution (documented source bundle acceptable unless a packaged executable is separately required). Ask before new packaging dependencies. Include static assets, locked dependencies, startup/migration instructions and loopback binding; exclude personal DB/media/secrets/.venv. Verify clean install, launch/stop, data persistence, analysis job recovery and offline runtime after prerequisites. No cloud deployment, telemetry or automatic updates.

### Implementation boundaries

Follow Agents.md: fully local processing, SQLite and server-rendered Django; read/analyze/advise only. Original ALS/WAV/stem/reference files remain in user-selected locations. Ask before adding dependencies in pyproject.toml. Add focused tests appropriate to the behavior above.

---

