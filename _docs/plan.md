# Personal AI Music Production Coach — Project Scope

## 1. Project Overview

A fully local AI-powered desktop application built with **Django** that acts as a personal electronic music production mentor and audio analysis system for **Ableton Live**.

The application is designed primarily to improve the user's production and mixing skills rather than replace the producer. It covers:

**Creative Development → Composition → Sound Design → Arrangement → Mixing → Mastering**

Target genres:
- Lo-fi
- Synthwave
- Ambient

Primary purposes:
1. Personal production tool
2. AI/software engineering portfolio project

## 2. Core Problem

The primary problem is improving the user's **music production and mixing skills through guidance, analysis, explanation and critique**.

The assistant should answer questions such as:
- What should I work on next?
- Why does this mix sound weak?
- What is wrong with my low end?
- Does this arrangement have enough contrast?
- How can I make this synth more atmospheric?
- How does my track compare with my reference?
- What are the biggest problems in this mix?
- What should I learn or practice to improve?

It should prioritize high-impact issues rather than overwhelm the user with endless recommendations.

## 3. Control Model

The application is intentionally limited to **Level 1 and Level 2 control**.

### Level 1 — Production Coach
The AI can:
- Give production advice
- Explain concepts
- Suggest creative directions
- Critique musical decisions
- Recommend workflow changes
- Teach composition, sound design, arrangement, mixing and mastering
- Recommend what to work on next
- Generate ideas such as chord, melody or bassline concepts
- Tell the user when an idea is weak and explain why

### Level 2 — Production Analyzer
The AI can:
- Read Ableton Live project information
- Analyze WAV files
- Analyze individual stems
- Analyze reference tracks
- Produce numerical measurements
- Compare the user's production against references
- Identify technical and musical issues
- Convert measurements into actionable recommendations

### Explicit Boundary

The assistant **must not automatically modify Ableton Live projects**.

It can:

**READ → UNDERSTAND → ANALYZE → ADVISE**

It cannot:

**MODIFY → AUTOMATE → CONTROL ABLETON**

## 4. Local-Only Requirement

The application must be **completely local/local-first**.

User data should remain on the user's computer, including:
- Ableton projects
- WAV files
- Stems
- Reference tracks
- Sample information
- Production history
- Project metadata
- Personal production profile
- AI memory

The core application should not depend on cloud storage or cloud processing.

"Hybrid intelligence" means different local components/models can handle different tasks rather than one model doing everything.

## 5. Technology Direction

### Framework
**Django**

Django should provide the main application/backend and local desktop-style web interface.

Potential supporting components:
- Python
- SQLite initially
- Local LLM inference
- Local audio/DSP processing
- Local vector/embedding storage if needed later

## 6. DAW Scope

The only supported DAW is:

**Ableton Live**

The user wants the assistant to **read Ableton projects directly**, not only exported audio.

Ableton `.als` files should be parsed into a normalized internal representation.

Conceptually:

```text
Ableton .als
     ↓
ALS Parser
     ↓
Normalized Project Model
     ↓
Database
     ↓
AI Context
```

The uploaded `.als` project confirms that Ableton project data can be treated as structured input. Ableton `.als` files are gzip-compressed XML documents containing structured project information.

The parser should investigate/extract, where available:
- Project name
- Tempo
- Time signature
- Tracks
- MIDI tracks
- Audio tracks
- Track names
- Clips
- MIDI notes
- Note timing
- Note pitch
- Instruments/devices
- Effects/devices
- Automation
- Sample/file references
- Arrangement/timeline information
- Markers and annotations
- Project metadata

Raw ALS XML should **not** be sent directly to the LLM. It should first be converted to concise structured context.

## 7. Audio Analysis Engine

Inputs:
- Full-mix WAV files
- Individual stems
- Reference WAV files

Example stems:

```text
Kick.wav
Bass.wav
Drums.wav
Pad.wav
Lead.wav
FX.wav
```

### Technical analysis
Potential measurements:
- BPM
- Peak level
- True peak
- RMS
- LUFS
- Short-term LUFS
- Dynamic range
- Crest factor
- Frequency spectrum
- Spectral centroid
- Spectral rolloff
- Stereo width
- Stereo correlation
- Clipping
- Silence
- Transient characteristics

### Musical analysis
Over time:
- Key
- Chord information
- Note density
- Rhythmic density
- Section changes
- Energy progression
- Repetition
- Arrangement density

The system should clearly distinguish **objective measurements** from **subjective artistic judgment**.

## 8. Production Workflow Coverage

### Creative Development
- Track concepts
- Mood
- Artistic direction
- Creative blocks
- Reference selection

### Composition
- Chord progressions
- Melodies
- Basslines
- Rhythms
- Harmonic development
- Musical structure

### Sound Design
Guidance on:
- Synth concepts
- Oscillators
- Filters
- Envelopes
- LFOs
- Modulation
- Layering
- Saturation
- Reverb
- Delay
- Stereo processing
- Texture creation

The user's primary hardware/controller is an **Akai MPC mini 3**, and the application should treat it as part of the user's normal production workflow where relevant.

### Arrangement
Analyze:
- Section length
- Repetition
- Variation
- Energy
- Transitions
- Instrumentation density
- Tension/release

### Mixing
Analyze:
- Frequency balance
- Low-end relationships
- Masking
- Dynamics
- Stereo image
- Loudness
- Gain staging
- Individual stems
- Transient behavior

### Mastering
Analyze:
- Integrated LUFS
- Short-term LUFS
- True peak
- Dynamics
- Spectral balance
- Stereo characteristics
- Clipping
- Frequency extremes
- Reference loudness and tonal differences

The application provides analysis and recommendations, not automatic mastering.

## 9. Reference Track System

A local reference library should be organized by:
- Genre
- Artist
- Track
- Personal category

Example:

```text
REFERENCE LIBRARY

LO-FI
├── Reference 01
├── Reference 02
└── Reference 03

SYNTHWAVE
├── Reference 01
└── Reference 02

AMBIENT
├── Reference 01
└── Reference 02
```

Comparisons may include:
- Loudness
- Peak level
- Frequency balance
- Low-end energy
- Midrange energy
- High-frequency energy
- Dynamics
- Stereo width
- Energy progression
- Arrangement
- Potential masking

The AI should translate numerical differences into useful musical guidance rather than merely displaying numbers.

## 10. Personal Artist DNA

A long-term core feature is a personalized production profile.

The application should gradually learn:
- Preferred genres
- Preferred BPM ranges
- Preferred keys
- Favorite instruments
- Favorite textures
- Typical arrangements
- Common effects
- Mixing tendencies
- Strengths
- Weaknesses
- Recurring technical problems
- Recurring creative patterns
- Favorite reference artists
- Favorite reference tracks

The objective is to help the user develop a **recognizable personal sound**, not simply imitate other artists.

## 11. Production Journal

The application should maintain production-session history.

Example:

```text
SESSION #17

Project:
Dreamscape

Today:
- Adjusted bass
- Changed pad
- Reduced reverb
- Added second section

Problems identified:
- Muddy low-mid
- Weak transition

Next session:
→ Fix transition
→ Compare against reference
```

This history becomes long-term AI context and allows recurring problems and progress to be identified.

## 12. AI Personality

The AI should combine three roles:

### Teacher
Explains concepts and teaches why something works.

### Producer
Provides creative recommendations and challenges creative decisions.

### Engineer
Provides objective technical analysis and measurements.

The assistant should be honest and willing to disagree.

It should not blindly praise ideas.

Example:

> "No, I wouldn't add another synth here. The problem is not a lack of content; it is a lack of contrast between sections."

## 13. Launch Experience

When the application opens, the dashboard should answer:

> **"What should I work on next, and why?"**

Recommended dashboard:

```text
PERSONAL MUSIC COPILOT

CURRENT PROJECT
────────────────────────────
Dreamscape

Genre: Synthwave
BPM: 112
Key: F#m

PRODUCTION STATUS

Composition       ███████░░░  70%
Sound Design      █████░░░░░  50%
Arrangement       ████░░░░░░  40%
Mixing            ██░░░░░░░░  20%
Mastering         ░░░░░░░░░░   0%

TODAY'S FOCUS
────────────────────────────
Finish the arrangement before
adding more sounds.

NEXT ACTION
────────────────────────────
Build the second main section.

[ OPEN PROJECT ]   [ ANALYZE AUDIO ]
```

Recommended navigation:
- Dashboard
- Projects
- Coach
- Analyze
- References
- Artist Profile
- Production Journal
- Settings

## 14. Typical User Workflow

```text
1. Open application
       ↓
2. Select Ableton project
       ↓
3. Application parses .als
       ↓
4. Project structure is displayed
       ↓
5. User optionally imports WAV/stems
       ↓
6. Audio analysis runs
       ↓
7. User selects reference track
       ↓
8. System performs comparison
       ↓
9. AI interprets results
       ↓
10. AI identifies highest-priority issues
       ↓
11. AI recommends next actions
       ↓
12. User returns to Ableton
       ↓
13. User makes changes manually
       ↓
14. User re-analyzes
       ↓
15. Production history is updated
```

## 15. MVP Definition

The MVP should prove:

> **The application can understand an Ableton project, analyze audio, and provide useful personalized production guidance.**

### MVP — Project
- Create project
- Import Ableton `.als`
- Parse project information
- Store project metadata
- Display project structure
- Track production progress

### MVP — Audio
- Import WAV
- Analyze full mix
- Analyze stems
- Calculate technical measurements
- Display analysis results

### MVP — AI
- Ask production questions
- Receive project-aware advice
- Mixing guidance
- Mastering guidance
- Creative guidance
- Explain technical concepts
- Identify problems
- Recommend next actions

### MVP — References
- Import reference track
- Analyze reference
- Compare user's track to reference
- Generate prioritized recommendations

### MVP — Personalization
- Store genre preferences
- Store artist/reference preferences
- Store production goals
- Store strengths/weaknesses
- Maintain production history

### MVP — Interface
- Django-based local desktop-style application
- Dashboard
- Projects
- Coach
- Analyzer
- References
- Profile

## 16. Explicit Non-Goals for MVP

Do NOT initially build:
- Autonomous complete song generation
- Automatic Ableton editing
- Automatic Ableton control
- Automatic mastering
- Plugin parameter control
- Fully autonomous production agents
- Voice control
- Mobile application
- Complex multi-agent architecture
- AI-generated complete tracks

## 17. Proposed Technical Architecture

```text
                    LOCAL COMPUTER
┌───────────────────────────────────────────────────┐
│                                                   │
│                 DJANGO APPLICATION                │
│                                                   │
│  ┌─────────────────────────────────────────────┐  │
│  │              Local/Desktop UI              │  │
│  └──────────────────────┬──────────────────────┘  │
│                         │                         │
│  ┌──────────────────────▼──────────────────────┐  │
│  │              Django Backend                 │  │
│  └─────────────┬──────────────┬───────────────┘  │
│                │              │                  │
│        ┌───────▼──────┐ ┌────▼─────────────┐   │
│        │ ALS Parser   │ │ Audio DSP Engine │   │
│        └───────┬──────┘ └────┬─────────────┘   │
│                │              │                 │
│                └──────┬───────┘                 │
│                       ▼                         │
│                Structured Context              │
│                       │                         │
│              ┌────────▼─────────┐               │
│              │ Local AI / LLM   │               │
│              └────────┬─────────┘               │
│                       │                         │
│              ┌────────▼─────────┐               │
│              │ Production Coach │               │
│              └────────┬─────────┘               │
│                       │                         │
│                ┌──────▼──────┐                  │
│                │  Database   │                  │
│                └─────────────┘                  │
│                                                 │
│  Local Files: ALS / WAV / Stems / References    │
└───────────────────────────────────────────────────┘
```

## 18. Development Roadmap

### Phase 1 — Django Foundation
- Django project
- Local database
- Local interface
- Project model
- User profile model
- Production session model

### Phase 2 — Ableton Intelligence
- Investigate `.als` format
- Build ALS parser
- Normalize Ableton data
- Store project structure
- Display tracks/clips/MIDI information

### Phase 3 — Audio Intelligence
- WAV ingestion
- Audio preprocessing
- DSP analysis
- Loudness analysis
- Frequency analysis
- Dynamics analysis
- Stereo analysis
- Stem analysis

### Phase 4 — Local AI Coach
- Local LLM integration
- Structured AI responses
- Production coaching
- Project-aware context
- Creative guidance
- Mixing guidance
- Mastering guidance

### Phase 5 — Reference Engine
- Reference library
- Reference analysis
- Track comparison
- Difference reports
- Prioritized recommendations

### Phase 6 — Personal Memory
- Production journal
- Long-term project history
- Artist DNA
- Recurring issue detection
- Personalized recommendations

### Phase 7 — Application Polish
- Dashboard
- Visualizations
- Production reports
- Search
- Settings
- Local packaging/deployment

## 19. Guiding Design Principles

1. Local first
2. Producer remains in control
3. AI teaches rather than replaces
4. Objective analysis + subjective musical judgment
5. Explain recommendations
6. Prioritize high-impact problems
7. Challenge weak decisions
8. Preserve artistic identity
9. Use project context instead of generic advice
10. Build incrementally
11. Avoid unnecessary agent complexity
12. Keep the system useful during actual music production

## 20. Final Product Definition

> **Personal AI Music Production Coach** is a fully local Django-based desktop application for Ableton Live that analyzes Ableton projects, WAV files, stems and reference tracks and provides personalized guidance throughout the electronic music production process, from creative development through mastering.
>
> The application specializes in Lo-fi, Synthwave and Ambient music and is designed primarily to improve the user's production and mixing skills.
>
> It operates at two levels: Level 1 provides production coaching, creative suggestions, explanations and critique; Level 2 provides project and audio analysis, numerical measurements and reference comparisons.
>
> The AI never automatically modifies or controls Ableton Live. The producer remains responsible for making all changes.
>
> Over time, the application maintains project history and develops an "Artist DNA" profile that allows it to identify recurring strengths, weaknesses, production patterns and opportunities for developing a recognizable personal sound.
>
> The first MVP will focus on three capabilities: **Ableton project intelligence, audio analysis, and project-aware AI production coaching.**
