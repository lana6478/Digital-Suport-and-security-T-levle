# Diagram and Notation Guide

*Digital Support and Security T Level → Appendices*

The specification expects students to be able to **read and draw** several standard types of technical diagram, particularly in Core Paper 1's problem-solving content and across the Occupational Specialisms. This page explains what each diagram type is for. The exact symbol keys (the literal shapes used) are set out as images in the official specification's Appendix 2 — see the link at the bottom of this page — this guide instead explains *when and why* you'd reach for each diagram type.

## Information flow diagrams

Used to show, at a glance, how information moves between a **source** and a **destination**, with the information itself labelled on the connecting arrow (e.g. `Source A —[Information]→ Destination B`). These are a lightweight way to express meaning without getting into full technical detail — useful early in problem-solving, when decomposing a problem, or when explaining how data moves around a simple system to a non-technical audience.

## Concept map symbols

A concept map links two **concepts** together via a **relationship**, and that relationship is always expressed as a verb (e.g. `Concept A —[requires]→ Concept B`). Concept maps are useful for showing how ideas, components or terms in a topic relate to each other — helpful for revision, and for demonstrating understanding of how different parts of a system or process interconnect rather than just listing them.

## Data flow diagrams (DFDs)

Data flow diagrams model how data moves through a system using a small set of standard symbols:

- **Data source or destination** — the entities data enters or leaves the system from/to (e.g. a user, an external system).
- **Process** — a step that transforms or acts on data.
- **Data store** — somewhere data is held (e.g. a database, a file).

Arrows connect these elements and are labelled with what data is flowing along them. DFDs are the standard way to describe how a piece of software or a business process actually handles data end-to-end, and are directly relevant to the "Data" content covered in the Core component.

## Flowchart symbols

Flowcharts describe the **logical flow of an algorithm or process**, step by step, using these standard symbols:

- **Terminator** — marks the start and end of the algorithm.
- **Process** — a processing step to be carried out.
- **Sub-process** — a self-contained group of steps, treated as a single step (often a call out to another defined process).
- **Decision** — a point where the flow branches based on a condition (a yes/no or true/false check).
- **Input/output** — a step where data enters or leaves the algorithm (e.g. reading user input, displaying a result).
- **Connector** — links two parts of a flowchart that can't easily be joined with a direct arrow (e.g. across a page break, or to avoid crossing lines).
- **Flow arrows** — show the order steps are executed in.

Flowcharts are core to the **algorithmic design** content in Core Paper 1: students need to both *interpret* a given flowchart (work out what it does, trace its output for a given input, spot and fix errors in it) and *draw* their own to represent a solution.

## Why this matters for assessment

Several command words in the [command word taxonomy](01-competency-frameworks.md#command-word-taxonomy) — particularly **Draw** and **Complete** — apply directly to these diagram types. A "Draw" question expects a fully-formed, correctly labelled diagram built from a given scenario; a "Complete" question gives a partially-finished diagram and expects the missing elements filled in correctly. Using the right symbol for the right purpose (e.g. not confusing a "process" box with a "decision" box in a flowchart) is part of what's being assessed, not just the overall logic.

## Key terms

- **DFD (Data Flow Diagram)** — a diagram modelling how data moves through a system via sources/destinations, processes and data stores.
- **Terminator** — the flowchart symbol marking the start or end of an algorithm.
- **Decomposition** — breaking a problem or solution into smaller, more manageable parts; often represented visually using these diagram types.

## Further reading

The actual symbol-shape keys (images) for each diagram type are published in Appendix 2 of the official specification:
[T Level Digital Support and Security — Specification (PDF)](https://qualifications.pearson.com/content/dam/pdf/TLevels/digital-support-and-security/2025/specification-and-sample-assessment-materials/digital-dss-specification.pdf)

## Related pages

- [Competency frameworks](01-competency-frameworks.md)
- [Core Paper 1](../01-core-component/01-core-paper-1.md)
- [Core Component overview](../01-core-component/00-overview.md)
