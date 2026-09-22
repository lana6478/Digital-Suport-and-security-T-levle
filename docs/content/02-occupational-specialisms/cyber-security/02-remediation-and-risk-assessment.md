# Cyber Security — Propose Remediation Advice for a Security Risk Assessment

*Digital Support and Security T Level → Occupational Specialisms → Cyber Security → Remediation and Risk Assessment*

This is Content Area 2 of the Cyber Security specialism — the specialism's second technical pillar, alongside Content Area 1. It covers computer forensics, recognising and categorising threats, vulnerability assessment, penetration testing, incident/event management, and the organisational policies that support risk mitigation. This is defensive, vocational curriculum content aimed at 16–19 year olds training to become cyber security technicians — it teaches how to recognise, assess and respond to security incidents, not how to carry out attacks.

## 2.1 Compliance principles in computer forensics

Purpose: investigate and analyse digital devices/networks to gather legitimate evidence for a body such as law enforcement. The five-stage compliance model: **identification** (what evidence exists, where, how it's stored), **preservation** (avoid tampering — isolate, secure and preserve evidence in chronological order, in line with legal retention periods), **analysis** (reconstruct data fragments, draw evidence-based conclusions), **documentation** (record all findings and the investigation itself), **presentation** (present findings to the appropriate body for further action).

## 2.2 Threats — social engineering, malware and password attacks

**Social engineering**: phishing (mass fraudulent messages — spoofed/misspelt domains, poor writing, infected attachments, urgency cues), spear phishing (targeted, harder to detect), vishing (fraudulent phone calls, often impersonating official bodies like HMRC, pressuring victims for personal details), smishing (fraudulent texts, often with suspicious links), shoulder surfing (observing someone entering credentials) and dumpster diving (retrieving discarded information).

**Denial-of-service**: DoS (overwhelms a service from one source) and DDoS (many devices attacking together) — both identified through degraded performance, spikes in traffic, repeated requests from the same source, and service outages. **Zero-day attacks** exploit a flaw before a patch exists, often only spotted via vendor statistics, unusual scanning, ML-based signature monitoring, or unusual interaction patterns.

**Malware**: virus (spreads and damages data/software), adware (unwanted ads, browser changes, slow performance), ransomware (blocks/deletes/encrypts data for payment), trojan (disguised as legitimate software), botnet (network of compromised devices under attacker control), spyware (hides and steals sensitive data). Most are spotted via scan reports, reduced device performance or unusual behaviour.

**Password attacks**: brute force (tries every combination), dictionary attack (tries common words/phrases) — both show up as increased network activity, repeated failed logins from one IP, unusual user behaviour. **Man-in-the-middle** attacks intercept communications, often flagged by browser security warnings or repeated unexpected disconnections.

**Skill**: identify potential threats/vulnerabilities/risks, calculate their likelihood and severity, and categorise them by priority.

## 2.3 Threat actors and threat intelligence

**Threat actors**: cyber criminals (financial gain via ransomware/social engineering/malware), insiders (current/past staff misusing authorised access for revenge or gain), terrorist organisations (disruption for a cause), nation states (political gain — stealing data, damaging infrastructure), hacktivists (expose wrongdoing "for good"), script kiddies (inexperienced attackers seeking a challenge). **Threat intelligence** — gathering critical information to analyse/prioritise threats — identifies previously unknown threats, reveals actor motivations, and supports fast, effective mitigation decisions.

## 2.4 Risk assessment stages and vulnerability assessment

Stages: **identify** vulnerability (scan/log analysis for anomalies) → **analyse** it (is it exploitable, how severe) → **identify risk** associated with it (prioritise) → **remediate** (update or remove the affected hardware/software) → **mitigate** (apply countermeasures, close down mitigated items, escalate anything still risky). Scoping a vulnerability assessment means defining in-scope systems/services/networks, access requirements and the vulnerabilities being tested for; evaluating it means classifying the risk of each finding and determining likely business impact, then documenting and organising the results.

## 2.5 Common Vulnerabilities and Exposures (CVE)

Identify published CVEs (from vendors, testers) → research each one, scoring it with the Common Vulnerability Scoring System (CVSS, 0–10 based on impact/exploitability/severity), identifying affected systems and possible mitigations → implement the mitigation.

## 2.6 Making mitigation recommendations from vulnerability evidence

Factors to weigh: potential business/operational/infrastructure impact, mitigating circumstances behind the vulnerability, cost of acting vs. not acting, type/severity of the vulnerability, available resources (people, finance, technology), reporting/response timeframes, CVE-based scope and priority, possible mitigation responses, and Proof-of-Concept (PoC) results confirming the flaw. Recommendations must be documented logically and communicated in appropriate technical language for the audience.

## 2.7 Impacts of an exploited vulnerability

Damage to property/resources, financial loss, reputational damage (loss of customer trust), fines/prosecution (e.g. an ICO fine after a data breach), operational disruption, harm to employees (physical or psychological), and identity theft.

## 2.8 Purpose of risk assessments on network infrastructure

**Host-based** — vulnerabilities in workstations/servers/hosts, plus configuration/patch visibility. **Network-based** — potential network attacks and vulnerable systems. **Wireless-based** — rogue access points, secure network configuration. **Application-based** — known software vulnerabilities/misconfigurations (e.g. SQL injection).

## 2.9 Strengths and weaknesses of vulnerability assessment tools

**Infrastructure scanners** (host/network/wireless): find missing patches, unsupported systems, weak passwords, exposed services, missing hardening and incorrect access controls — but don't stop active attacks, only catch previously known issues, can be slow for vendors to fix, may be inaccurate, and can affect live services while scanning. **Web application scanners**: automate scanning, find SQL injection, broken authentication, data exposure, incorrect access controls, vulnerable third-party components and weak/unencrypted communication — but can produce false positives/negatives, impact system resources while scanning, and again only catch known issue types. **Software scanners**: find missing updates/patches and run vendor-specific checks — but need regular updating, can also produce false positives/negatives, and make business impact hard to judge.

## 2.10 Types of organisational risk and management approaches

**Compliance risk** (not following policy) — managed via monitoring/updating processes, compliance controls and exception reports (flagging emerging issues, e.g. expiring software support). **Safety risk** (harm to people/property/environment) — managed via checks for human error and maintenance audits. **Information security risk** (data lost/stolen/copied/compromised) — managed via data controls (e.g. access control), network traffic monitoring, device management (e.g. restricted USB access) and regular security training.

## 2.11 Mitigating privacy-breach threats

Social engineering → raise awareness of current issues. Unmanaged devices → company policy restricting their use. Untrained staff → training and SOPs. Insider threats → access controls, monitoring unusual activity, segregation of duties. Unpatched applications → ensure updates are applied. Third-party risk → supplier due diligence. Improper device disposal → secure wiping and DPA 2018 compliance.

## 2.12 Measures used to assess threat/vulnerability impact

RTO (time to recover to an acceptable state), RPO (tolerable data loss), MTBF (likelihood/frequency of asset failure), MTTD (efficiency of detection), MTTR (average time to restore a failed system).

## 2.13 Identifying and classifying critical systems

**Single point of failure** — a design/implementation/configuration flaw where the whole system depends on one component. **Mission essential functions** — functions that must continue, or resume rapidly, after a disruption.

## 2.14 Factors in threat assessment for information security

Environmental (power failure/spikes, natural disasters, fire, equipment failure, flooding), manmade internal (malicious/accidental staff activity, human error, misconfigured firewalls), manmade external (malware, attack, social engineering, terrorism).

## 2.15 Qualitative and quantitative threat analysis

Qualitative: RAG rating (red/amber/green) applied to business risk. Quantitative: numeric methods — cost overrun, resource consumption, and calculations such as Single Loss Expectancy (SLE) × Annual Rate of Occurrence (ARO) = Annual Loss Expectancy (ALE), plus CVSS scoring. Tools: fault tree analysis, FMECA (Failure Mode, Effects and Criticality Analysis), CRAMM (scope → evaluate → recommend countermeasures) and FAIR (Factor Analysis of Information Risk).

## 2.16 Conducting a security risk assessment (e.g. on a LAN device)

Identify potential risks → assess each using a scoring matrix (likelihood × severity = risk score/RAG rating) → weigh asset value against mitigation cost → control the risk (proportionate response) → record findings → review/test controls regularly. Applied through regular internal/external audits covering in-house systems and third-party suppliers. *(E3, E4, M5, M6, M8.)*

## 2.17 Penetration testing stages

Planning and scoping (rules of engagement, timing, legal/contractual boundaries) → reconnaissance (gathering system information — topology, OS, applications) → scanning (finding open ports/services) → vulnerability assessment (identifying and testing exploitability) → exploitation (attempting to gain access) → reporting (documenting findings and remediation recommendations).

## 2.18 Risk response types

Accept (no further mitigation available, or residual risk remains after mitigation), transfer (outsource the risk to another party), avoid (change project/system scope to sidestep it), mitigate (reduce severity/likelihood through controls).

## 2.19 Incident/event management stages

Identify (via service desk, phone, email, SMS, chat) → log (manually, with contact/date/description, or automatically via a monitoring system) → manage (raise a ticket, assign to the right person by expertise/access/seniority, categorise by business impact) → prioritise (RAG-style urgency, SLA management and escalation, with crimes reported to police and data breaches reported to the ICO) → resolve (temporary workaround or permanent fix) → close (confirm resolution, complete an incident report covering an executive summary, discovery/investigation, impact, mitigation, recommendations and any ongoing risk) → document (gather relevant information, complete incident/exception reports per policy, store per data protection law).

## 2.20 Escalating a security incident while preserving evidence

Record the incident's date/time and description → take appropriate action (e.g. isolate the affected device from the network) → preserve digital evidence (copy relevant log files) → escalate as appropriate.

## 2.21 Applying NCSC Cyber Essentials controls

Boundary firewalls/internet gateways (restrict traffic flow), secure configuration (only necessary functionality enabled), malware protection (current anti-malware, regular scans), security update management (patch currency), access control and management (least privilege, with PAM for elevated access such as a super-user or privileged business account).

## 2.22 Encryption tools as risk mitigation

**Asymmetric encryption** — private data between users (e.g. encrypted email); underpins **data-in-transit** protection: TLS (end-to-end encryption for email/web/messaging) and SSL (legacy protocol for browser-to-website encryption). **Symmetric encryption** — same key encrypts/decrypts (e.g. card payments); underpins **data-at-rest encryption (DARE)**: Full Disk Encryption (FDE, protects against e.g. laptop theft) and File-Based Encryption (FBE, protects individual files/folders in transfer).

## 2.23 Purpose, criteria and types of backup

Purpose: keep data recoverable for full disaster recovery or partial loss. Criteria: frequency, source, destination, storage (medium and location), retention period, and regular restore testing. Types: full, incremental, differential, mirror, and **immutable** (cannot be changed, overwritten or deleted — a defence against ransomware tampering with backups).

## 2.24 Organisational digital use policies supporting risk mitigation

Data protection policy, acceptable use policy, access control policy, asset classification policy, information security policy, incident response procedure, mobile device policy, backup policy, BYOD policy, password policy, asset disposal policy, data retention policy.

## 2.25 Monitoring cyber security compliance

Audit processes/policies for currency (e.g. reviewing the information security policy) and improve them as needed; compare and check the accuracy of processes, logs and incident reports; comply with relevant ISO standards.

## Key terms

- **CVE / CVSS** — Common Vulnerabilities and Exposures (a published vulnerability record) scored by the Common Vulnerability Scoring System (0–10).
- **PoC (Proof of Concept)** — a controlled demonstration that a vulnerability is genuinely exploitable.
- **ALE (Annualised Loss Expectancy)** — SLE × ARO, a quantitative way to express expected yearly loss from a risk.
- **Immutable backup** — a backup that cannot be altered or deleted, protecting against ransomware and tampering.
- **SLA** — Service Level Agreement, defining expected response/resolution times for incidents.

## Related pages

- [Cyber Security: Security Procedures and Controls](01-security-procedures-and-controls.md)
- [Cyber Security: Sources of Knowledge](03-sources-of-knowledge.md)
- [Digital Support: Software and OS Support](../digital-support/02-software-and-os-support.md)
- [Occupational Specialisms overview](../00-overview.md)
- [Scheme of Assessment](../05-scheme-of-assessment.md)
