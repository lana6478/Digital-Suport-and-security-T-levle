# Employer Set Projects (ESP)

*Digital Support and Security T Level → Core Component → Employer Set Projects*

The **Employer Set Project (ESP)** is the third and largest-weighted part of the Core Component (40% of the core, 20% of the total qualification). It's a substantial, externally set project taken under supervised/controlled conditions, and it's how the [six core skills](00-overview.md#the-core-skills) are assessed synoptically - pulling together problem-solving, communication, stakeholder work, artefact-building, logical troubleshooting, and security awareness into one connected piece of work, rather than testing them separately.

There are **three ESP pathways**, and which one a student sits depends on their chosen route: **Digital Infrastructure & Network Cabling**, **Cyber Security**, and **Digital Support Technician**. All three share the same overall shape but apply it to a different professional context.

## Common structure across all three ESPs

Every ESP follows the same task sequence, built around a single scenario (the specification's sample material is set in the financial sector):

1. **Pre-task - familiarisation with the industry context.** Not directly assessed, and not done under controlled conditions. Students research the scenario's industry context independently, share findings, and discuss as a group - this research then feeds into how well they handle the assessed tasks that follow.
2. **Task 1 - Planning a project.** Using a Pearson-provided template, students produce a **Gantt chart** and a **resource and cost plan**, then a written **rationale** justifying their planning decisions.
3. **Task 2 - Identifying and fixing defects/issues.** Students work with a simulation stimulus (a Cisco Packet Tracer file) or, for the Digital Support Technician route, a set of support tickets plus a simulation. They test to find the underlying issue, fix it, and document the whole testing process.
4. **Task 3 - Designing a solution.** Students decompose the problem and produce a design (a network design, a security plan, or a needs analysis, depending on the pathway) that clearly communicates the intended solution to a client and to a third party who might have to build it.
5. **Task 4a - Developing the solution.** Students build out their design into a working solution, applying the relevant technical skill, and addressing robustness/security/organisation and user experience.
6. **Task 4b - Reflective evaluation.** Students review the outcome against the original brief and success criteria, evidence that it meets user needs, and discuss how it could be improved if revisited.

Each task is signposted against specific [English, maths and digital competencies](../03-appendices/01-competency-frameworks.md) (e.g. `E4`, `M6`, `D2`) - the letter/number codes you'll see throughout the official spec show exactly which general competency each task is designed to develop.

## Digital Infrastructure & Network Cabling Employer Set Project

Built around a **network** scenario. After planning (Task 1) and fixing defects in a given network simulation (Task 2 - using testing tools like ping/tracer, correcting errors, following networking conventions), students move to:

- **Task 3 - Designing a network solution**: decompose the problem into hardware/software/settings/data-connection needs, group requirements by user type, and communicate the design via a network diagram plus annotations - correctly using IP addressing, network symbols and consistent entity names.
- **Task 4a - Developing the solution**: refine the network simulation, applying appropriate tools/devices/settings, while ensuring **robustness** (resilience, redundancy - backups, fallbacks, UPS), **security** (anti-malware/firewall configuration, user roles/permissions, hardening/air-gapping), sound **organisation** (server configuration, node deployment, connection media, subnetting), and good **user experience** (end-user devices, data connections, back-end systems, access/availability).
- **Task 4b - Reflective evaluation** as in the common structure above.

## Cyber Security Employer Set Project

Same overall shape, but the lens throughout is **security** rather than general network functionality. Task 2 is framed as identifying and fixing *security* defects, and the solution must specifically ensure the network *is secure*, not just functional.

- **Task 3 - Designing a solution**: produce a **security plan** by decomposing the scenario into physical, logical/software and user-based risks, then apply accepted security good practice and multiple layered mitigations (so no single control is a single point of failure), using industry-standard tools and procedures.
- **Task 4a - Developing the solution**: build a secure solution, ensuring resilience/redundancy as before, but with an explicit focus on mitigating **vulnerabilities** (security software configuration, user roles/permissions, hardening/air-gapping) and on **solution organisation** that also considers future scalability *without* compromising security.
- **Task 4b - Reflective evaluation** as in the common structure.

## Digital Support Technician Employer Set Project

Framed around **supporting end users and diagnosing problems**, rather than building network infrastructure from scratch.

- **Task 2 - Diagnosing issues and providing support**: respond to a set of support tickets alongside a simulation stimulus, applying testing and **root cause analysis** to identify likely causes and propose a range of possible solutions, then communicate the process and fix the issue.
- **Task 3 - Planning a solution**: carry out a **needs analysis** for a given organisation, decomposing the situation to cover both general and stakeholder-specific needs, describing the hardware/software/data-communication technologies needed, and assessing/mitigating relevant risks.
- **Task 4a - Developing the solution**: same robustness/security/organisation/user-experience considerations as the other two pathways, applied to a support context.
- **Task 4b - Reflective evaluation** as in the common structure.

<!-- teaching-resources:start -->
## Teaching resources

Ready-made lesson slides for this topic. Each PowerPoint includes learning objectives, a starter, teaching slides, a quiz with answers, an activity and an exit ticket, with teacher notes on every slide. Download it and adapt it for your class.

| Lesson slides | Covers | Slides |
|---|---|---|
| [The Employer Set Project (PowerPoint)](../05-teaching-resources/slides/core/19-employer-set-project-overview.pptx) | Employer Set Project, all pathways | 11 |

See [all lesson slides](../05-teaching-resources/01-lesson-slides.md) for every topic.
<!-- teaching-resources:end -->

## Key terms

- **ESP (Employer Set Project)** - the externally set, controlled-conditions project that synoptically assesses the six core skills.
- **Pre-release/pre-task material** - context released in advance so students can research before the controlled assessment; not itself marked.
- **Gantt chart** - a project-planning diagram showing tasks against a timeline (see also [Core Paper 1 §2.9](01-core-paper-1.md#29-project-management-methodologies-and-tools)).
- **Root cause analysis** - techniques (e.g. five whys, FMEA) for finding a problem's underlying cause rather than just its symptoms.

## Related pages

- [Core Component overview](00-overview.md)
- [Core scheme of assessment](04-core-scheme-of-assessment.md)
- [Core Paper 1](01-core-paper-1.md)
- [Core Paper 2](02-core-paper-2.md)
