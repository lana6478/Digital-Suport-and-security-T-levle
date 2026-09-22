# Digital Infrastructure — Security Procedures and Controls

*Digital Support and Security T Level → Occupational Specialisms → Digital Infrastructure → Security Procedures and Controls*

This page covers Content Area 1 of the Digital Infrastructure occupational specialism: applying procedures and controls to maintain the digital security of an organisation and its data. It is the security foundation every Digital Infrastructure student needs before moving on to the technical infrastructure content in Content Area 2. Subsection numbers (1.1, 1.2 …) mirror the specification so you can cross-reference the official document.

<figure>
<img src="assets/img/hero-digital-infrastructure.svg" alt="A server rack connected to a cloud, representing physical and virtual infrastructure">
<figcaption>Digital Infrastructure: physical racks and virtual environments, working together.</figcaption>
</figure>

## 1.1 Preventative business controls

Preventative controls are proactive — their job is to stop an incident happening in the first place. They fall into four groups:

- **Physical** — specialist anti-pick locks, barriers/fencing/bollards, gates, cages, flood defences, temperature control (e.g. air conditioning).
- **Combined/managed access** — card readers, biometric scanners, CCTV, PIN/passcodes.
- **Administrative** — separation of duties and role-based access.
- **Technical** — allowlists, denylists, access control lists, sandboxing, device hardening, certificate authorities.

Students should also be able to configure a domain services environment with security controls (group policies, minimum password rules), deploy a certificate authority, implement the five NCSC Cyber Essentials controls (boundary firewalls, secure configuration, access control, malware protection, patch management), apply access-control methods (authentication, MAC, DAC, ABAC, RBAC) to physical or virtual networks, and manage documents/data in line with data protection law.

## 1.2 Detective business controls

Detective controls identify that an incident is happening or has already happened — CCTV and motion sensors (physical); logs (e.g. server-room temperature, error logs) and audits/reviews of who has entered or left a site (administrative).

## 1.3 Corrective business controls

Corrective controls are reactive: they limit damage and stop recurrence — fire/gas suppression systems (physical) and standard operating procedures such as a defined response when a fire is detected (administrative).

## 1.4 Deterrent business controls

Deterrent controls dissuade someone from acting in the first place — security guards, alarms and visible surveillance (physical); SOPs like alarm-setting and fire drills, employment contracts with codes of conduct, and acceptable-use policies (administrative).

## 1.5 Directive business controls

Directive controls promote a security-conscious culture — signage and mandatory ID badges (physical); agreement types, general security policy, and regular compulsory staff training such as "human firewall" training (administrative).

## 1.6 Compensating business controls

Compensating controls act as a backstop when a primary control fails — temperature controls (physical); role-based awareness training and SOPs for environmental monitoring (administrative).

## 1.7 Applying and monitoring business controls (skill)

Students must be able to review an identified risk (gathering information from systems and users), then select, apply and monitor the appropriate control type — preventative, detective, corrective, deterrent, directive, compensating or recovery — while complying with relevant regulatory and organisational policy.

## 1.8–1.9 Disaster recovery planning

A **disaster recovery plan (DRP)** exists to recover and maintain service after a disruption. It covers physical elements (back-ups, off-site storage) and administrative elements — often sitting inside a wider **business continuity plan (BCP)** — such as keeping systems functional, letting users work away from the main site, deploying back-ups to preserve data integrity, tracking asset/inventory changes, and reporting infrastructure changes to management.

Building a DRP follows a structured process: define its scope (site, organisation, department or individual level); gather information (past outages, hardware/software/network/data inventories, contacts); risk-assess assets, threats, vulnerabilities, probability and impact; create the plan and identify the resources it needs; get it signed off; then test it (identify resources, set a test frequency, run the test, review and document the outcome, amend as needed) and continuously improve it through internal/external audit.

## 1.10 Impacts of threats and vulnerabilities

Realised threats can cause harm across several categories: danger to life (health & safety breaches), privacy (data breaches, identity theft), property/resources (physical damage), economic (financial loss), reputational (brand damage) and legal (fines, prosecution).

## 1.11 Vulnerabilities in critical systems

Common weak points include unauthorised network or physical port access, single points of failure, system failure, and open ports such as USB and wireless.

## 1.12 Measures and procedures that mitigate threats

Key measures: **RTO** (recovery time objective), **RPO** (recovery point objective), **MTBF** (mean time between failure), **MTTR** (mean time to repair). Key procedures: SOPs (installation, back-up, set-up) and SLAs (uptime, response and resolution times).

## 1.13 The risk management process

A five-step cycle: **identify** potential risks/threats/vulnerabilities → **assess probability** (high/medium/low) → **assess impact** → **prioritise** based on probability × impact and assign ownership → **mitigate** to reduce probability or impact.

## 1.14 Approaches and tools for analysing threats

- **Qualitative** analysis uses a non-numeric **RAG rating** (red = act immediately, amber = monitor closely, green = no immediate action).
- **Quantitative** analysis assigns numbers to effects (e.g. cost overrun, resources consumed).
- Tools include fault tree analysis, impact analysis, failure mode & effects critical analysis, **annualised loss expectancy (ALE)**, **CRAMM**, **SWOT analysis**, and a risk register recording each risk's RAG rating.

## 1.15 Threat assessment factors

- **Environmental** — extreme weather, natural disaster, animals, humidity, air quality.
- **Manmade** — internal (malicious/accidental staff or contractor action) and external (malware, hacking, social engineering, third parties, terrorism).
- **Technological** — device/system failures and faults (misconfiguration, disk/component failure, power issues, dropouts, VPN/connectivity failure), firewall misconfiguration, software corruption, RAID failure, and the downstream impact of technical change.
- **Political** — legislative change.

## 1.16 Risk assessment in a digital infrastructure context

Purpose: reduce risk by applying HSE guidelines to projects, investigating the project environment (e.g. a PESTLE analysis), identifying internal/external risk (e.g. supply-chain assessment), and quantifying impact on asset value. In practice this means assessing a system, identifying its components, running the risk management process against it, and recording findings clearly using correct technical terms. *(Signposted competencies: E4, M6, D4.)*

## 1.17 Risk response types

**Accept** (impact judged tolerable), **avoid** (change scope to sidestep the risk), **mitigate** (reduce probability/impact), **transfer** (contractually outsource the risk).

## 1.18 Penetration testing process

Customer engagement → information gathering → discovery and scanning → vulnerability testing → exploitation → final analysis/review → act on the results (e.g. for a wireless network test).

## 1.19 Designing a risk mitigation strategy

Considerations: which risk response to use, the user profile (requirements, ability level), cost vs benefit, who owns the risk, escalation routes, contingency planning, and ongoing monitoring/review.

## 1.20 Technical security controls as risk mitigation

Purpose: strengthen network security for users and systems. Controls include the five Cyber Essentials controls (boundary firewalls, secure configuration, malware protection, patch management, access control), device hardening, network/system/data/device/service **segmentation**, hardware protection, **multi-factor authentication**, remote monitoring & management (RMM), and vulnerability/port scanning.

## 1.21 Continuous improvement through risk mitigation (skill)

Gather and organise incident information → analyse trends to find underlying risk and understand the user profile → apply mitigation techniques to identified threats (e.g. installing RMM, hardening devices) → monitor and review continuously (assign an owner, plan contingencies, keep security software current, interpret penetration-test output) → record findings clearly. *(E4, M5, D4.)*

## 1.22 Encryption as risk mitigation

Purpose: protect stored and transferred data using cryptography.

- **Asymmetric encryption** — sends private data between two parties (e.g. encrypted email).
- **Symmetric encryption** — encrypts/decrypts with the same key (e.g. card payments).
- **Data at rest**: full-disk encryption, a **hardware security module (HSM)**, or a **trusted platform module (TPM)**.
- **Data in transit**: **SSL** and **TLS**.

## 1.23 Back-up purpose, criteria and types

Purpose: keep an up-to-date copy of data for recovery. Criteria: frequency, source, destination, storage medium (LTO tape, cloud, disk). Types: full, incremental, differential, mirror.

## 1.24 Policies, procedures and risk mitigation

An organisational **digital use policy** typically covers network/internet usage, BYOD, working from home, password renewal and software updates. A **health & safety policy** covers lone working, manual handling, working at height, fire safety and RIDDOR 2013 reporting. All changes should go through a formal **change procedure**, and policies/SOPs should be routinely **audited**. Students must be able to explain each policy's purpose and the security impact of not following it (e.g. danger to life, privacy breach). *(E5, D5.)*

## 1.25 Legislation, standards and best practice

- **UK GDPR** — standardises how personal data is used, stored and transferred (key articles: subject matter/objectives, material scope, territorial scope, definitions, processing principles, lawfulness of processing, conditions for consent).
- **Data Protection Act 2018** — the UK's implementation of GDPR: data must be used fairly/lawfully/transparently, for specified purposes, kept to what's necessary, accurate, retained no longer than needed, and secured appropriately.
- **Computer Misuse Act 1990** — criminalises unauthorised access to computer material, unauthorised access with intent to commit further offences, and unauthorised acts intended (or reckless as to) impairing a computer's operation.
- **ISO 27001:2017** — certifiable information security management standard, covering GDPR/DPA compliance, information security/management, penetration testing and risk assessment.
- **PCI DSS** — protects card payments: secure network, protected cardholder data, vulnerability management, strong access control, regular monitoring/testing, and a documented security policy.
- **NCSC "10 Steps to Cyber Security"** — user education, home/mobile working, secure configuration, removable media control, user privilege management, incident management, monitoring, malware protection, network security, risk management.
- **OWASP** — promotes cyber security tools, training and a networking platform to support users and improve software security.

## 1.26 Principles of network security

The **CIA triad** (confidentiality, integrity, availability) underpins secure design. **IAAA** (identification, authentication, authorisation, accountability) is applied through directory services, authentication processes, password policy, data protection and an up-to-date information asset register.

## 1.27 Managing and controlling access

Authentication, firewalls, **IDS** (detects threats), **IPS** (blocks them), **NAC** (enforces policy per device/user), **MAC** (hierarchy of security levels), **DAC** (owner sets access), **ABAC** (attribute-based) and **RBAC** (role-based).

## 1.28 Physical and virtual traffic security

Physical: SDN with TLS, a **DMZ**, air gapping. Virtual: **VLANs**. Subnet-level: **VPN**, **VRF**, **IPSec**, air gapping.

## 1.29 Cyber security principles for connected devices

The CIA triad is applied to assess impact (e.g. a breach): prevent attacks through secure configuration, limit exposure, detect attacks through logging/auditing, and segregate devices/networks/resources to contain impact.

## 1.30 Installing and configuring security software (skill)

Techniques: WPA2/WPA3 wireless security, device authentication, encryption, virtualisation, penetration testing, malware/anti-virus protection, patching, multi-factor authentication, single logout. Students install and configure vulnerability scanners, anti-malware and firewall software, apply device hardening, and verify configuration on end-user devices. *(E4, D1, D6.)*

## 1.31 Importance of cyber security to organisations and society

Organisations must protect systems, cloud availability, company and personal data, enforce password policy, comply with legislation, and defend against cybercrime. For society, protecting personal data preserves privacy, prevents discrimination, supports equal opportunity, and prevents identity theft. DPA 2018 gives individuals rights to be informed, access their data, correct it, erase it, restrict its processing, port it, and object to certain processing.

## 1.32 Network topologies, referencing models and minimum standards

Topologies: bus, star, ring, token ring, mesh, hybrid, client-server, peer-to-peer. Referencing models: **OSI** (application, presentation, session, transport, network, data link, physical) and **TCP/IP** (application, transport, network, network interface). The **identify–protect–detect–respond–recover** cycle applies these principles to network architecture — from assigning a cyber security lead through to back-ups and continuous improvement.

## 1.33 Common vulnerabilities and controls

Missing patches, weak/default passwords, insecure BIOS/UEFI, misconfigured permissions, missing protection software, insecure disposal (WEEE Directive 2013), poor back-up management, DHCP spoofing, VLAN attacks/hopping, misconfigured firewalls or ACLs, poor topology design, and unprotected physical devices — each paired with a specific control (e.g. patch management software, minimum password policy, scheduled auditing, DHCP snooping, network monitoring).

## Key terms

- **DRP/BCP** — Disaster Recovery Plan / Business Continuity Plan.
- **RTO/RPO/MTBF/MTTR** — recovery-time, recovery-point, mean-time-between-failure and mean-time-to-repair measures.
- **CIA triad** — confidentiality, integrity, availability.
- **IAAA** — identification, authentication, authorisation, accountability.
- **RBAC/ABAC/MAC/DAC** — role-, attribute-, mandatory- and discretionary-based access control.
- **HSM/TPM** — hardware security module / trusted platform module.

## Related pages

- [Physical and Virtual Infrastructure](02-physical-and-virtual-infrastructure.md)
- [Discover, Evaluate and Apply Reliable Sources of Knowledge](03-sources-of-knowledge.md)
- [Network Cabling — Security Procedures and Controls](../network-cabling/01-security-procedures-and-controls.md)
- [Occupational Specialisms overview](../00-overview.md)
- [Scheme of Assessment](../05-scheme-of-assessment.md)
