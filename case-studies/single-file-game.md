# Leap — Single-File Platformer Prompt Experiment

**Date:** 5 November 2026  
**Platform:** OpenAI Codex desktop (Windows)  
**Model/settings:** GPT-6.1 Sol, High reasoning  
**Deliverable:** One self-contained HTML file per version

## Summary

I tested how the detail of my instructions affected an AI-generated platformer. My first prompt, **"Make a HTML platformer game in a single file,"** produced *Lantern Leap*: a simple platformer with one level and seven collectibles.

For the second prompt, I specified a game called **Leap**, requiring retro pixel-art styling, at least ten levels lasting one minute or more, four difficulty modes, avatar customisation, menus, traps, weapons, secrets, and at least five tests per level plus menu/button checks. Codex produced a substantially larger single-file game with ten stages, difficulty selection, customisation and combat mechanics.

## Game files — inspect or play both versions

| | Prompt 1: Basic | Prompt 2: Detailed |
| --- | --- | --- |
| **Game** | **Lantern Leap** | **Leap** |
| **GitHub file** | [01 — Lantern Leap (HTML)](../games/01-lantern-leap-baseline.html) | [02 — Leap (HTML)](../games/02-leap-detailed-prompt.html) |
| **Scope** | One stage, seven sparks | Ten stages, four difficulties, avatar customisation, traps and weapons |
| **Original format** | Single self-contained HTML file | Single self-contained HTML file |

**How to play:** Open either HTML link, choose GitHub's **Download raw file** option, then open the downloaded `.html` file on your computer in a web browser. Both source files are also available to inspect directly on GitHub.

## What the comparison demonstrates

The more detailed prompt gave the model clearer requirements, creative direction, constraints and an explicit testing expectation. This is evidence of my **requirements specification and prompt design**, rather than proof that longer prompts always work better.

ChatGPT's **informal assessment** of the prompts was **3/10** for the basic prompt, **8/10** for the detailed prompt, and **7.5/10 overall** for demonstrated prompt-engineering performance in this experiment. These are subjective assessments, **not** professional certification or benchmark scores.

## Testing and limitations

The agent reported simulated checks across all stages and menus. **Actual Chrome/Firefox gameplay and rendering could not be verified in its isolated test sessions.** The model's reports therefore do not establish that the finished game is bug-free or that every level's real playtime meets the requested minimum.

## Evidence

Both original HTML builds are now published above, clearly labelled by prompt version. My prompt screenshots remain in my project records and have not yet been published in this repository.

