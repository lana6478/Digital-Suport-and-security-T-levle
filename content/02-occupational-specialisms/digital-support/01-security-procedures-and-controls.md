# Digital Support — Security Procedures and Controls

*Digital Support and Security T Level → Occupational Specialisms → Digital Support → Security Procedures and Controls*

This is Content Area 1 of the Digital Support occupational specialism. It is one of three content areas every Digital Support student studies, and it is largely shared in spirit (though not word-for-word) with the equivalent content area in the other three specialisms — every T Level Digital Support and Security student, whichever specialism they choose, has to be able to apply procedures and controls to protect an organisation's digital security. In the Digital Support version, the emphasis sits on business controls, disaster recovery, risk management and network/device-level technical controls a digital support technician would apply day to day.

## 1.1 Preventative business control techniques

Preventative controls stop an incident happening in the first place. They fall into four broad groups:

- **Physical** — specialist anti-picking locks, barriers (fencing, bollards, gates, cages), flood defence systems, temperature control (e.g. air conditioning).
- **Combined/managed access** — card readers, biometric readers, video verification, PIN/passcodes.
- **Administrative** — separation of duties and role-based access, so no one person holds excessive privilege.
- **Technical** — domain and security policies such as allowlisting/denylisting, access control lists, sandboxing, device hardening and use of a certificate authority.

Practical skills built alongside this knowledge include setting up a domain services environment with security controls (group-based permissions, password complexity rules), deploying a certificate authority, and implementing the five NCSC Cyber Essentials controls — boundary firewalls, secure configuration (e.g. enabling MFA), access control, malware protection and patch management — plus configuring access control methods on end-user devices (authentication, MAC, DAC, ABAC, RBAC) and handling documents/data in line with data protection law.

## 1.2 Detective business control techniques

Controls that identify an incident once it has started: physical measures like CCTV and motion sensors, and administrative measures like temperature/error logs and periodic review or audit of who enters and leaves a facility.

## 1.3 Corrective business control techniques

Controls that act once an incident is confirmed, limiting damage: physical fire/gas suppression systems, and administrative standard operating procedures describing what to do when, for example, a fire is detected.

## 1.4 Deterrent business control techniques

Controls intended to discourage an incident before it is even attempted: visible security guards, alarms and surveillance, plus administrative measures such as alarm-setting procedures, fire drills, codes of conduct in employment contracts, and acceptable use policies.

## 1.5 Directive business control techniques

Controls that tell people what to do: signage, mandatory ID badge display, agreement types, general security policy documents, and compulsory staff training (including "human firewall" awareness training).

## 1.6 Compensating business control techniques

A safeguard used when a primary control isn't available or fails — e.g. environmental temperature controls as a physical example, or role-based awareness training and environmental-monitoring SOPs as administrative examples.

## 1.7 Applying and monitoring business controls

Students must be able to review an identified risk (gathering information from systems and users), then select, apply and monitor the appropriate control type — preventative, detective, corrective, deterrent, directive, compensating or recovery — while complying with relevant regulation and organisational procedure. *(Maps to assessment competencies D3.)*

## 1.8 Disaster recovery plan components

A Disaster Recovery Plan (DRP) covers:

- **Physical** elements — backups, off-site alternative server storage.
- **Administrative/procedural** elements sitting under a wider organisational Business Continuity Plan (BCP) — keeping systems functional, letting users access systems away from the main site, deploying backups to preserve data integrity, keeping digital systems aligned with business needs, tracking assets across the network (tagging/logging laptops), and reporting infrastructure changes to management.

## 1.9 Impacts of threats and vulnerabilities

Realised threats can cause: **danger to life** (health & safety breaches), **privacy** loss (data breaches, identity theft), **damage to property/resources**, **economic** loss, **reputational** damage and **legal** consequences (fines, prosecution).

## 1.10 Vulnerabilities in critical systems

Typical weak points include unauthorised physical access to network ports, weak user account control, single points of failure, open USB/network ports, and unsecured wireless networks.

## 1.11 Measures and procedures that mitigate threats

Key measures: Recovery Time Objective (RTO), Recovery Point Objective (RPO), Mean Time Between Failure (MTBF) and Mean Time to Repair (MTTR). Key procedures: standard operating procedures (installation, back-up, set-up) and service level agreements defining uptime and response/resolution times.

## 1.12 The risk management process

A five-step cycle: **identification** of risks/threats/vulnerabilities → **probability** (likelihood, e.g. high/medium/low) → **impact** (extent of possible damage, e.g. asset value) → **prioritisation** (ranking by probability × impact, with an owner assigned) → **mitigation** (reducing probability or impact).

## 1.13 Approaches and tools for analysing threats

- **Qualitative** (non-numeric) — RAG rating: red = high risk needing immediate action, amber = moderate risk to watch closely, green = low risk, no immediate action.
- **Quantitative** (numeric) — analysing effects such as cost overrun or resource consumption.
- **Tools** — fault tree analysis, impact analysis, failure mode effect critical analysis, Annualised Loss Expectancy (ALE), CRAMM (CCTA Risk Analysis and Management Method), SWOT analysis, and a risk register recording risks with a RAG rating.

## 1.14 Factors in threat assessment

- **Environmental** — extreme weather, natural disaster, pests, humidity, air quality.
- **Manmade internal** — malicious or accidental staff/contractor activity.
- **Manmade external** — malware, hacking, social engineering, third parties, terrorism.
- **Technological** — device/system failures (hard disk or RAM failure, damaged peripherals, software corruption, inaccessible sites) and the impact of technical change (downtime, upgrades, misconfiguration).
- **Political** — changes in legislation.

## 1.15 Purpose and process of risk assessment in a digital support context

The purpose is to identify and reduce risk — applying HSE guidance (e.g. ergonomic/accessible equipment), investigating project risks (e.g. a PESTLE analysis), identifying internal/external risk (e.g. system access for staff/contractors) and quantifying impact on asset value. Students conduct a security risk assessment for a scenario (e.g. a BYOD system): assess the system and its components, identify possible risks, calculate probability and impact, analyse and prioritise, and record findings accurately using correct technical terms. *(E4, M6, D4.)*

## 1.16 Types of risk response

**Accept** (impact judged acceptable), **avoid** (change scope to sidestep the risk), **mitigate** (reduce probability/impact) or **transfer** (contractually outsource the risk).

## 1.17 The penetration testing process

Customer engagement → information gathering → discovery and scanning → vulnerability testing → exploitation → final analysis and review → using the results to inform action (e.g. for a wireless network test).

## 1.18 Designing a risk mitigation strategy

Design considerations include the chosen risk response, the user profile (requirements, ability level), cost/benefit, and escalation routes to the appropriate authority. Students learn to gather and organise incident data, analyse trends to find underlying risks, apply mitigation techniques to threats found on end-user devices (e.g. installing RMM software, hardening a device), and treat this as a continuous-improvement loop: assign a risk owner, plan contingencies, keep security software current, and interpret penetration-test outputs.

## 1.19 Technical security controls as risk mitigation

Purpose: improving network security for users and systems. The five Cyber Essentials controls reappear here in more technical depth — access control (least privilege), patch management, malware protection, boundary firewalls/internet gateways, and secure configuration — alongside device hardening (removing unneeded programs/accounts/ports), remote monitoring and management (RMM), and vulnerability scanning (port/device scanning).

## 1.20 Continuous improvement through risk mitigation

The same continuous-improvement cycle as 1.18, extended with the requirement to record all findings and actions clearly using correct technical terms. *(E4, M5, D4.)*

## 1.21 Encryption as risk mitigation

- **Asymmetric encryption** — sends private data between users (e.g. encrypted email).
- **Symmetric encryption** — same key used to encrypt/decrypt (e.g. card payments).
- **Data-at-rest**: full disk encryption; a Hardware Security Module (HSM) safeguarding keys; a Trusted Platform Module (TPM) storing device-specific keys.
- **Data-in-transit**: SSL (encrypted link between browser and website) and TLS (end-to-end encryption for email, web and messaging).

## 1.22 Purpose, criteria and types of backup

Purpose: keep an up-to-date copy of data for recovery. Criteria: frequency, source, destination, and storage medium (e.g. LTO tape, cloud, disk). Types: full, incremental, differential, mirror.

## 1.23 Policies, procedures and risk mitigation

Organisational digital use policy SOPs cover network usage/monitoring, internet usage, BYOD, working from home (with DSE assessment), password renewal, and software update discipline. Health and safety policy SOPs cover lone working, manual handling, working at height, fire safety and RIDDOR 2013 reporting. A change procedure requires all changes to be approved, documented and periodically audited. Students must be able to explain each policy's purpose clearly and explain the security impact of non-adherence (e.g. danger to life, privacy loss). *(E5, D5.)*

## 1.24 Legislation, standards and best practice for information security

- **UK GDPR** — standardises how data is used/stored/transferred; key articles cover subject matter, material/territorial scope, definitions, processing principles, lawfulness and consent conditions.
- **Data Protection Act 2018** — the UK's implementation of GDPR: data must be used fairly/lawfully/transparently, for specified purposes, kept only as long as necessary, accurate, and secured against unlawful processing, loss or damage.
- **Computer Misuse Act 1990** — criminalises unauthorised access to computer material, unauthorised access with intent to commit further offences, and unauthorised acts intended (or reckless as to) impairing a computer's operation.
- **ISO 27001:2017** — certifiable information security management standard, applied to GDPR/DPA compliance, information security/management, penetration testing and risk assessment.
- **PCI DSS** — global card-payment security standard: secure network, protected cardholder data, vulnerability management, strong access control, regular monitoring/testing, and a documented security policy.
- **NCSC "10 Steps to Cyber Security"** — user education/awareness, home/mobile working, secure configuration, removable media control, managing user privileges, incident management, monitoring, malware protection, network security, risk management regime.
- **OWASP** — reviews and shares cyber security tools/resources, provides education for the public and professionals, and acts as a networking platform; applied in digital support to help users stay safe online and to improve software security.

## 1.25 Principles of network security

- **CIA triad** — confidentiality, integrity, availability — underpins security policy design.
- **IAAA** — identification, authentication, authorisation, accountability — applied via directory services, authentication processes, password practice, data protection/identification, and a current information asset register.

## 1.26 Managing and controlling access

Authentication restricts/grants access based on verified identity; firewalls restrict access to a defined set of services. Access-control models applied and monitored include: IDS (detects/monitors traffic for threats), IPS (blocks access on detected threats), NAC (enforces policy on devices/users joining the network), MAC (hierarchy of security levels), DAC (owner sets access), ABAC (attribute-based), RBAC (role-based) and RuBAC (rule-list based).

## 1.27 Managing and securing network traffic

- **Physical** — software-defined networking (using TLS, e.g. for banking sites), demilitarised zone (DMZ), air gapping.
- **Virtual** — VLAN (carrying VPN traffic for intranets/file systems), Virtual Routing and Forwarding (VRF), subnets, IPSec, and virtual air gapping.

## 1.28 Cyber security techniques for internet-connected devices

Wireless security (WPA2/WPA3 with end-to-end protection), device/password authentication, encryption, virtualisation, penetration testing, malware/anti-virus protection, patching, MFA and single logout. Practical skills: installing/configuring vulnerability-scanning software, anti-malware and firewall software on end-user devices; applying device hardening (change default passwords, correct file/service permissions, apply updates, remove unneeded software, apply security policy, disable unauthorised devices); and testing that the configuration was successful. *(E4, D1, D6.)*

## 1.29 The importance of cyber security to organisations and society

For **organisations**: protecting systems, devices, cloud availability, personal/commercially sensitive data, password policy, legal compliance and defence against cybercrime. For **society**: protecting privacy, preventing prejudice, ensuring equal opportunity and preventing identity theft — including the individual rights guaranteed under DPA 2018 (be informed, access data, correct inaccurate data, erasure, restrict processing, data portability, object to processing).

## 1.30 Techniques applied to cyber security for connected devices

The same technique list as 1.28 (wireless security, device security, encryption, virtualisation, penetration testing, malware/anti-virus protection, patching, MFA, single logout), covered here at knowledge level rather than as an installation skill.

## 1.31 Network topologies, referencing models and minimum standards

- **Topologies** — bus, star, ring, token ring, mesh, hybrid, client-server, peer-to-peer.
- **OSI model** — application, presentation, session, transport, network, data link, physical.
- **TCP/IP model** — application, transport, network, network interface.
- **Minimum cyber security standard principles**: **identify** (assign a lead, run risk assessments, document configurations/responses), **protect** (anti-virus/firewalls, reduce attack surface, trusted OS/apps, decommission legacy systems, security audits, encryption, least-privilege access, training), **detect** (security measures, audit/event logs, network monitoring), **respond** (contain and minimise impact) and **recover** (backups, maintenance plans, continuous-improvement review).

## 1.32 Common network/system/device vulnerabilities

Missing patches/firmware updates → mitigate with patch-manager software, traffic tracking and test devices. Password vulnerabilities (weak/default/no lockout) → NCSC-aligned minimum password rules and reset policy. Insecure BIOS/UEFI configuration → review/update settings. Misconfigured permissions → test and schedule audits (e.g. remove access for leavers). Missing protection software → anti-malware, updated/monitored security software, awareness of buffer overflow. Insecure disposal of data/devices → WEEE Directive 2013 compliance and data wiping. Inadequate backup management → correct frequency and backup type. Unprotected physical devices → install the correct protective software.

## Key terms

- **Preventative / detective / corrective / deterrent / directive / compensating control** — the six standard categories of business security control, each acting at a different stage of an incident.
- **DRP (Disaster Recovery Plan) / BCP (Business Continuity Plan)** — the DRP restores IT systems; the BCP keeps the wider business running.
- **RTO / RPO / MTBF / MTTR** — recovery-time, recovery-point, mean-time-between-failure and mean-time-to-repair metrics used to size resilience requirements.
- **RAG rating** — red/amber/green qualitative risk severity scale.
- **CIA triad** — confidentiality, integrity, availability.
- **IAAA** — identification, authentication, authorisation, accountability.
- **Cyber Essentials** — the NCSC's five baseline technical controls: boundary firewalls, secure configuration, access control, malware protection, patch management.

## Related pages

- [Digital Support: Software and OS Support](02-software-and-os-support.md)
- [Digital Support: Sources of Knowledge](03-sources-of-knowledge.md)
- [Cyber Security: Security Procedures and Controls](../cyber-security/01-security-procedures-and-controls.md)
- [Occupational Specialisms overview](../00-overview.md)
- [Scheme of Assessment](../05-scheme-of-assessment.md)
