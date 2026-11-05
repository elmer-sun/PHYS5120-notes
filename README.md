# PHYS5120 notes

Collaborative notes for **PHYS5120: Computational Energy Materials and Electronic Structure Simulations**, HKUST.

Imported from the [original Overleaf project](https://www.overleaf.com/project/6130625f9c31a759aa64b17b) on 2026-11-05. Credit for the original notes belongs to the original contributors. This repository is maintained separately; changes do not automatically synchronize with Overleaf.

## Read and edit by chapter

| Chapter | Source file |
| --- | --- |
| 1. Molecular dynamics | [01-molecular-dynamics.tex](chapters/01-molecular-dynamics.tex) |
| 2. Force fields and transport | [02-force-fields-and-transport.tex](chapters/02-force-fields-and-transport.tex) |
| 3. Monte Carlo simulation | [03-monte-carlo.tex](chapters/03-monte-carlo.tex) |
| 4. Adiabatic approximation | [04-adiabatic-approximation.tex](chapters/04-adiabatic-approximation.tex) |
| 5. Hartree and Hartree--Fock theory | [05-hartree-fock.tex](chapters/05-hartree-fock.tex) |
| 6. Electronic correlation beyond Hartree--Fock | [06-electronic-correlation.tex](chapters/06-electronic-correlation.tex) |
| 7. Density functional theory | [07-density-functional-theory.tex](chapters/07-density-functional-theory.tex) |
| 8. Exchange-correlation functionals | [08-exchange-correlation-functionals.tex](chapters/08-exchange-correlation-functionals.tex) |
| 9. Kohn--Sham eigenvalues and the band-gap problem | [09-kohn-sham-spectra.tex](chapters/09-kohn-sham-spectra.tex) |
| 10. Periodic solids, basis sets and pseudopotentials | [10-solids-and-basis-sets.tex](chapters/10-solids-and-basis-sets.tex) |
| 11. Frozen phonons | [11-frozen-phonons.tex](chapters/11-frozen-phonons.tex) |
| 12. Car--Parrinello molecular dynamics | [12-car-parrinello.tex](chapters/12-car-parrinello.tex) |

`main.tex` is the single compilation entry point and controls reading order. `preamble.tex` contains shared packages and definitions; `figures/` contains the original images. Chapter files are included with `\input` and do not need their own document preamble. Equation and figure references remain shared across chapters.

Compile from the repository root with `latexmk -pdf main.tex`, or select `main.tex` as the main document in Overleaf. The PDF includes a table of contents and linked bookmarks.

## Collaboration

- Work on one chapter per branch/pull request; describe the physical issue, the change and its evidence.
- Keep shared notation and macros in `preamble.tex`; discuss changes affecting multiple chapters.
- Use descriptive, chapter-prefixed labels for new equations and figures. Existing labels are retained for now so the restructuring does not break references.
- Keep the notes in English. Define symbols before use, explain assumptions and connect each derivation to its physical purpose. Expand omitted steps into readable arguments instead of copying slide bullets.
- Check the complete document after editing, including cross-chapter references. Do not commit temporary compilation files.

## Review status and lecture coverage

This revision reorganizes the inherited notes; it is **not a completed scientific review**. Original equations and prose are retained; one malformed cross-reference to Fick's equation has been repaired. DFT foundations, exchange-correlation approximations and spectral interpretation now have separate files. Effective mass and localized basis sets belong to Chapter 10 instead of the frozen-phonon chapter.

The local `Lectures_export.zip` supplied on 2026-11-05 contains Introduction, Lec1–Lec8, Lec9-Reproducibility in DFT and Martin-Fuchs. The instructor PDFs remain local reference material, separate from this repository.

- Chapters 1–3: Introduction and Lec1–Lec3.
- Chapters 4–6: Lec4–Lec6.
- Chapter 7: Lec7; Chapters 8–9: Lec8 and Martin-Fuchs, with topic-by-topic coverage to be checked.
- Chapters 10–12: inherited solid-state, phonon and Car–Parrinello material; correspondence with additional instructor slides still needs checking.
- Lec9 reproducibility currently lacks a dedicated chapter in the inherited notes; add it during the content expansion after checking the source.

Review chapter by chapter in reading order. Check definitions, dimensions, signs, assumptions, derivation steps and physical interpretations before extending examples. Initial issues identified for the review include the Verlet expansion and recurrence (Chapter 1), the scope and proof of the Hohenberg–Kohn theorem (Chapter 7), vibrational zero modes (Chapter 11), and the Car–Parrinello Lagrangian and equations of motion (Chapter 12). These issues are not corrected by this structural change.
