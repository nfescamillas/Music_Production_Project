# Personal AI Music Production Coach — MVP Backlog

## 1. Create the empty Django project
Goal: Establish a runnable local Django project with one passing automated test.
Description: Create the project structure, dependency definition, and minimal Django configuration required to run locally. Add a deliberately small smoke test and document the single command that runs it successfully. Do not add product features, data models, or UI beyond what is necessary to prove the foundation works.

## 2. Define local development setup instructions
Goal: Make it possible for a new contributor to run the application and tests locally.
Description: Write concise setup documentation covering the supported Python version, virtual environment creation, dependency installation, database initialization, app startup, and test execution. State that all data processing and model access must remain local-first. Keep the instructions specific to this repository and Windows-friendly.

## 3. Configure project-wide quality checks
Goal: Provide repeatable formatting, linting, and test commands for the Django project.
Description: Choose and configure lightweight Python formatting and linting tools appropriate for the project. Add a single documented command or task for running checks and ensure the initial project passes them. Do not introduce CI hosting or deployment automation in this task.

## 4. Create the base application layout
Goal: Provide a reusable Django app and template structure for product features.
Description: Add a dedicated Django application for the music coach domain, with conventional locations for models, services, views, templates, static assets, and tests. Configure template and static-file discovery so later tasks can add pages without revisiting project setup. Include a test that confirms the app loads within Django.

## 5. Build the local desktop-style shell
Goal: Display a consistent application frame with primary navigation.
Description: Create a base template with the product name and navigation links for Dashboard, Projects, Coach, Analyze, References, Artist Profile, Production Journal, and Settings. Use a simple responsive layout suitable for a local desktop-sized browser window. The links may lead to placeholder pages at this stage.

## 6. Add placeholder navigation pages
Goal: Ensure every planned primary navigation destination has a working local route.
Description: Create minimal server-rendered pages and URL routes for each navigation item in the base shell. Each page should clearly identify itself and use the shared layout. Add route or view tests that verify all pages respond successfully.

## 7. Add Tailwind CSS to the Django interface
Goal: Establish a maintainable styling workflow for the local interface.
Description: Integrate Tailwind CSS with the Django static-asset pipeline and provide a documented development/build workflow. Apply a small neutral visual foundation to the base layout, including typography, spacing, colors, and accessible focus states. Do not design individual product dashboards in this task.

## 8. Define the Project data model
Goal: Persist the core metadata for a user music-production project.
Description: Add a Django model representing a local Ableton production project, including name, source ALS path, genre, tempo, key, timestamps, and import status. Add database migrations and model-level validation suitable for local file paths. Register the model in Django admin or provide an equivalent inspection path for development.

## 9. Create project list and creation screens
Goal: Let a user create and browse local production-project records.
Description: Build server-rendered pages for listing projects and creating a new project record. Include clear validation feedback and a direct link from each listed project to its detail page. This task stores metadata only; it does not parse an ALS file.

## 10. Create a project detail page
Goal: Show the stored metadata and processing state for one production project.
Description: Build a project detail route that displays the project name, source path, genre, tempo, key, timestamps, and import status. Provide clearly labeled empty states for project structure, audio analyses, and coaching history that later tasks will populate. Add tests for successful display and an unknown-project response.

## 11. Design the normalized Ableton project schema
Goal: Define the internal data representation used after parsing an Ableton ALS file.
Description: Document and implement Django models or a deliberately versioned structured representation for normalized project data. Cover project-level metadata, tracks, clips, MIDI notes, devices, arrangement information, and source-file references, while allowing fields to be unavailable. Do not parse real ALS files in this task.

## 12. Implement safe ALS file decompression and XML loading
Goal: Read a local Ableton ALS file into an XML document without modifying it.
Description: Create a focused service that validates a selected local ALS path, decompresses its gzip content, and loads XML safely with useful error messages. Preserve no raw XML in LLM context or database fields. Add fixture-based tests for a valid minimal ALS file and invalid or unreadable input.

## 13. Extract basic ALS project metadata
Goal: Obtain project name, tempo, and time signature from a valid ALS file.
Description: Extend the ALS parsing service to extract only stable project-level metadata and return it through the normalized representation. Clearly distinguish missing source values from parser failures. Test against small ALS fixtures with both complete and incomplete metadata.

## 14. Extract ALS track metadata
Goal: Read named audio and MIDI tracks from an Ableton project.
Description: Add parser support for track identifiers, names, track kinds, and basic enabled/muted state where present. Persist or expose the data through the normalized project schema without adding clip or device parsing. Include fixtures covering an audio track, a MIDI track, and absent optional values.

## 15. Extract ALS MIDI clip and note data
Goal: Capture usable note-level composition information from MIDI tracks.
Description: Add parsing for MIDI clips and their note timing, pitch, duration, and velocity where the ALS document provides them. Map values into the normalized schema and avoid assumptions about every Ableton version exposing identical XML. Cover empty clips and tracks with no MIDI clips in tests.

## 16. Extract ALS device and effect summaries
Goal: Summarize instruments and effects used by each Ableton track.
Description: Parse device names/types and associate them with their parent tracks, retaining only concise metadata useful to analysis and coaching. Do not attempt to recreate device presets or automate their parameters. Add tests that verify devices are attached to the correct normalized track.

## 17. Import parsed ALS data into a Project
Goal: Connect a selected ALS source file to persisted normalized project structure.
Description: Add a project-level import action that invokes the parser, saves supported normalized data, and records an explicit success or failure status. Preserve existing user-entered project metadata when appropriate and report friendly parsing errors in the interface. Test a successful import and a failed import with no partial corrupt data.

## 18. Display imported Ableton project structure
Goal: Let the user inspect tracks, clips, notes, and devices extracted from an ALS file.
Description: Add a structured section to the project detail page showing normalized project data with useful empty states. Prioritize track-level readability, then make clip/note/device details available without dumping raw XML. Ensure the page remains usable for projects with no parsed details.

## 19. Define the audio-analysis result schema
Goal: Persist versioned, reproducible measurements for a local audio file.
Description: Create models or a documented structured result format for an audio source, its analysis status, analysis version, file fingerprint, and measured metrics. Include fields needed for loudness, dynamics, spectral balance, stereo information, silence, and error reporting. Do not calculate audio metrics in this task.

## 20. Add WAV file registration to a project
Goal: Allow a user to associate a local WAV mix or stem with a production project.
Description: Build a validated form and service that store a local WAV path, user-friendly label, and source type such as full mix or stem. Validate path existence and WAV readability without copying the file into the application database. Display registered files on the project detail page.

## 21. Implement WAV metadata inspection
Goal: Read fundamental technical properties from a registered WAV file.
Description: Create an audio service that reports duration, sample rate, channel count, bit depth where available, and frame count. Store the result or expose it through the audio-source record, with actionable handling for unsupported or corrupt files. Add tests with a compact generated or checked-in WAV fixture.

## 22. Measure peak, RMS, and crest factor
Goal: Produce baseline dynamics measurements for an imported WAV file.
Description: Implement a deterministic analysis function for sample peak, RMS level, and crest factor, documenting the units and channel-handling approach. Save results under the versioned analysis schema rather than directly on the source file. Test known audio fixtures with expected approximate measurements.

## 23. Measure integrated loudness and true peak
Goal: Report mastering-relevant loudness metrics for a WAV file.
Description: Integrate a local loudness-analysis library to calculate integrated LUFS, short-term loudness where practical, and true peak. Clearly communicate unavailable measurements and avoid presenting estimates as definitive. Add tests with tolerance-based expected values from controlled audio fixtures.

## 24. Measure frequency-band balance
Goal: Summarize low, mid, and high-frequency energy in a WAV file.
Description: Implement an analysis service that derives a stable spectral summary, including defined frequency bands and a documented method for aggregation. Store concise numerical output that can support reference comparisons and coaching. Add visual interpretation later; this task focuses only on reliable measurements and tests.

## 25. Measure stereo and silence characteristics
Goal: Identify basic stereo-image and silence information from a WAV file.
Description: Add calculations for stereo width or correlation where applicable and identify significant silent regions using documented thresholds. Return clear not-applicable results for mono audio. Store results with the rest of the versioned audio analysis and test mono and stereo fixtures.

## 26. Run and review an audio analysis
Goal: Let a user trigger a complete baseline analysis and inspect its results.
Description: Add a project interface action that runs the available audio measurements for a registered WAV source and records status, timestamp, version, results, and failure details. Render an understandable results page that separates objective values from later AI interpretation. Keep processing synchronous only if the initial analysis is demonstrably fast enough.

## 27. Add background analysis job tracking
Goal: Keep the local interface responsive while audio analysis runs.
Description: Introduce a simple local job model and execution mechanism for analysis requests, with queued, running, completed, and failed states. Update the UI with HTMX polling or another lightweight server-rendered pattern. Do not introduce distributed workers, Redis, or cloud services.

## 28. Create the local reference-track library model
Goal: Organize locally stored reference-track metadata for comparison.
Description: Add a reference-track record containing local WAV path, title, artist, genre, personal category, and analysis status. Reuse the audio-source analysis capabilities rather than duplicating DSP logic. Include a browsable list and creation form with local-path validation.

## 29. Analyze a reference track
Goal: Generate the same objective audio measurements for a reference track.
Description: Connect reference-track records to the shared audio analysis workflow and expose their result status and measurements. Make failures visible without losing the reference metadata. Test that a reference analysis uses the same measurement versioning as project audio.

## 30. Compare a project mix with a reference track
Goal: Produce an objective difference report between two completed analyses.
Description: Implement a comparison service that calculates and labels differences in loudness, peak, dynamics, frequency-band balance, and stereo characteristics. Explicitly mark comparisons as measurements rather than quality judgments. Display a concise report from the project or reference interface.

## 31. Define structured coach context
Goal: Create a concise, safe representation of project information for local LLM prompts.
Description: Build a context-construction service that selects relevant project metadata, normalized ALS summaries, audio measurements, reference comparison results, and recent journal entries. Enforce limits and avoid including raw ALS XML, full audio data, or unnecessary local file-system details. Add tests proving the context remains concise and handles missing sources.

## 32. Add local Ollama availability checks
Goal: Detect whether a compatible local LLM service and model are ready to use.
Description: Add configuration and a service that checks a local Ollama endpoint, lists or validates the configured model, and returns human-readable remediation guidance when unavailable. Do not send data to remote services or silently fall back to a cloud model. Provide mocked tests for available and unavailable responses.

## 33. Implement the local coach response service
Goal: Request a structured production-coaching response from the configured local model.
Description: Create a service that combines a user question with the structured coach context and requests a response using a defined output shape. Require the output to distinguish evidence-based observations, subjective recommendations, explanations, and suggested next actions. Handle malformed model output and local-service failure gracefully.

## 34. Build the project-aware Coach page
Goal: Let a user ask a coaching question in the context of a selected project.
Description: Create a server-rendered Coach interface where the user selects a project, enters a question, and receives a structured local-model response. Show what source information was available to the coach, without exposing hidden prompt instructions or raw ALS XML. Add clear unavailable states when no local model is configured.

## 35. Store coaching conversations
Goal: Preserve project-specific questions and recommendations for later review.
Description: Add models for coaching exchanges, including question, response, project linkage, context/analysis versions, timestamp, and failure state. Display a chronological, readable history on the project page and Coach page. Do not implement cross-project semantic memory in this task.

## 36. Define the production-session journal model
Goal: Record focused production sessions and planned follow-up work.
Description: Add a model linked to a project for session date, completed work, identified problems, and next-session actions. Keep the text user-editable and separate direct user notes from later AI observations. Provide migrations and validation tests.

## 37. Build the production journal interface
Goal: Let a user create, edit, and review production-session entries.
Description: Add project-scoped list, creation, and editing pages for journal entries using the shared application layout. Show the latest session and next-session actions prominently on the project detail page. Include empty states and permission-free local operation.

## 38. Define the Artist Profile model
Goal: Store editable long-term preferences and goals that personalize coaching.
Description: Add a single local profile containing genres, preferred BPM ranges, preferred keys, favorite instruments/textures, reference preferences, production goals, strengths, and weaknesses. Design fields so users can revise them without losing historical project records. Do not infer profile facts automatically in this task.

## 39. Build the Artist Profile interface
Goal: Let the user maintain the personal preferences used by the coach.
Description: Create a form-based page for viewing and editing the local Artist Profile. Explain that the information personalizes advice and remains on the computer. Add tests for profile creation, editing, and display.

## 40. Incorporate profile and journal context into coaching
Goal: Make local coaching advice reflect declared preferences and recent project work.
Description: Extend the structured coach-context builder to include selected Artist Profile fields and a bounded summary of recent sessions for the active project. Preserve strict prompt-size limits and label user-authored information separately from analysis measurements. Test that irrelevant or excessive historical text is excluded.

## 41. Generate a dashboard next-action summary
Goal: Answer “What should I work on next, and why?” for the current project.
Description: Create a deterministic service that derives a provisional next action from incomplete project data, recent journal actions, and analysis or coach findings when available. It must identify the evidence used and return an honest insufficient-information state when needed. Do not require an LLM call for the initial summary.

## 42. Build the dashboard
Goal: Present the current project, progress areas, focus, and next action on launch.
Description: Replace the dashboard placeholder with a local overview resembling the planned launch experience: project metadata, production-stage progress, today’s focus, and next action. Use real stored data when available and readable empty states when no project has been selected. Keep charts and controls modest until the core data workflows are proven.

## 43. Add project production-progress tracking
Goal: Let a user track composition, sound design, arrangement, mixing, and mastering progress.
Description: Add editable progress values and optional notes for the five production stages on each project. Display them on the project detail page and dashboard using accessible labels in addition to visual bars. Do not infer progress automatically in this task.

## 44. Add robust local-path privacy safeguards
Goal: Prevent project data from being sent outside the local application by default.
Description: Audit file import, analysis, and LLM integration paths to ensure source audio, ALS files, parsed contents, and prompts remain local. Add explicit configuration defaults that reject remote LLM endpoints and document the boundary in the Settings page. Cover key safeguards with automated tests where feasible.

## 45. Create local settings for model and analysis behavior
Goal: Give the user a single place to configure local application behavior.
Description: Build the Settings page for configured local model endpoint/model name, chosen analysis defaults, and visible data-location information. Validate inputs and clearly flag non-local endpoints rather than silently accepting them. Keep settings scoped to one local user and avoid account or cloud features.

## 46. Add end-to-end MVP workflow tests
Goal: Verify the primary local workflow works across project import, analysis, comparison, and coaching.
Description: Add integration tests covering creation of a project, ALS import from a fixture, WAV registration and analysis, reference comparison, journal creation, and coach-context assembly. Mock local model transport so tests remain deterministic and do not need a running model. Focus on the user-visible MVP path, not exhaustive algorithm correctness.

## 47. Document MVP usage and known limitations
Goal: Provide an honest guide for using the completed local MVP.
Description: Write user-facing documentation covering supported inputs, the Ableton read-only boundary, how to run analysis and comparisons, local-model setup, and the difference between measurements and artistic judgment. List known parser limitations and unsupported Ableton features explicitly. Include troubleshooting for common invalid-path, malformed ALS, unsupported WAV, and unavailable-model errors.

## 48. Prepare a local release package
Goal: Produce a repeatable local distribution artifact for the MVP.
Description: Define and document a Windows-focused packaging process that launches the Django application locally and includes required static assets and configuration defaults. Verify the packaged result using a clean local test location if practical. Do not add telemetry, cloud accounts, automatic updates, or remote deployment.
