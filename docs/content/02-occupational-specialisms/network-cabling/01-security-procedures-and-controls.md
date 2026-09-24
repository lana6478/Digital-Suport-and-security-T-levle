# Network Cabling - Security Procedures and Controls

*Digital Support and Security T Level → Occupational Specialisms → Network Cabling → Security Procedures and Controls*

This page covers Content Area 1 of the Network Cabling occupational specialism: applying procedures and controls to maintain the digital security of an organisation and its data. It largely mirrors the Digital Infrastructure specialism's security content but is scoped to a cabling installer's world - physical site security, cabling-specific risk, and the legislation/standards that govern cabling work. Subsection numbers mirror the specification.

<figure>
<img src="assets/img/hero-network-cabling.svg" alt="A patch panel with cables plugged into numbered ports">
<figcaption>Network Cabling: running, terminating and testing cable to a professional standard.</figcaption>
</figure>

## 1.1 Preventative business controls

- **Physical** - anti-pick locks, barriers (fencing, bollards), gates, cages, lock-and-key (or equivalent).
- **Combined/managed access** - card readers, biometric scanners, video, PIN/passcodes.
- **Administrative** - separation of duties, relevance of role-based access.
- **Technical** - allowlists, denylists, access control lists, sandboxing, device hardening, certificate authorities.

Students also implement the five NCSC Cyber Essentials controls (boundary firewalls, secure configuration, access control, malware protection, patch management), apply access-control methods (authentication, MAC, DAC, ABAC, RBAC) to physical or virtual networks, and manage documents/data in line with data protection legislation. *(E5, D1, D6.)*

## 1.2–1.6 Detective, corrective, deterrent, directive and compensating controls

- **Detective** - CCTV, motion sensors; logs and site-access audits.
- **Corrective** - fire/gas suppression; SOPs for responding to an incident such as a fire.
- **Deterrent** - security guards, alarms, visible surveillance; SOPs (alarm-setting, fire drills), codes of conduct in employment contracts, acceptable-use policies.
- **Directive** - signage, mandatory ID badges; agreement types, general security policy, regular compulsory training.
- **Compensating** - temperature control; role-based awareness training, SOPs for environmental monitoring.

## 1.7 Applying and monitoring business controls (skill)

Review an identified risk (gather information from systems/users), then select, apply and monitor the right control type - preventative, detective, corrective, deterrent, directive, compensating or recovery - while complying with relevant policy. *(D3.)*

## 1.8 Disaster recovery plan components

Physical: back-ups, off-site alternate storage. Administrative (within a DRP supported by a wider BCP): keeping systems functional, enabling off-site access, deploying back-ups to preserve data integrity, keeping digital changes aligned to business need, tracking/logging assets across the network, and reporting infrastructure changes to management.

## 1.9–1.11 Impacts, vulnerabilities and mitigation measures

Impacts of realised threats: danger to life, privacy breaches, property/resource damage, economic loss, reputational damage, legal consequences. Vulnerabilities in critical systems: unauthorised network or physical port access, single points of failure, and open ports (USB, network ports, wireless). Mitigation measures: **RTO, RPO, MTBF, MTTR**; mitigation procedures: SOPs (installation, back-up, set-up) and SLAs (uptime, response/resolution times).

## 1.12–1.14 Risk management, analysis and threat assessment

The risk management process: identify → assess probability → assess impact → prioritise → mitigate. Analysis approaches: **qualitative** (RAG rating - red/amber/green) and **quantitative** (numeric cost/resource effects), using tools such as fault tree analysis, impact analysis, failure mode & effects critical analysis, ALE, CRAMM, SWOT analysis and a risk register.

Threat-assessment factors: environmental (weather, natural disaster, animals such as a rodent chewing cables, humidity, air quality), manmade (internal staff/contractor action; external malware, hacking, social engineering, third parties, terrorism), technological (Wi-Fi dropouts, inaccessible systems, device/firewall faults, signal interference, system/software upgrade impact), and political (legislative change).

## 1.15 Risk assessment in a network cabling context

Purpose: apply HSE guidance to projects, investigate the project environment (e.g. PESTLE analysis), identify internal/external risk (e.g. supply-chain assessment), and quantify impact on asset value. In practice: assess a system (e.g. a LAN cabling installation), identify its components, run the risk management process against it, and record findings clearly. *(E4, M6, D4.)*

## 1.16–1.18 Risk response, penetration testing and mitigation strategy design

Risk responses: accept, avoid, mitigate, transfer. Penetration testing follows the same stages as elsewhere in the qualification: customer engagement → information gathering → discovery/scanning → vulnerability testing → exploitation → final analysis/review → apply results. Designing a mitigation strategy weighs the chosen risk response, user profile, cost/benefit, risk ownership, escalation routes, contingency planning and ongoing review.

## 1.19 Technical security controls as risk mitigation

Purpose: strengthen network security for users and systems. Controls: the five Cyber Essentials controls, device hardening, remote monitoring & management (RMM), and anti-virus software to defend against known threats.

## 1.20 Continuous improvement through risk mitigation (skill)

Gather and organise incident information → analyse trends to surface underlying risk and understand the user profile → apply mitigation to identified threats/vulnerabilities/incidents (e.g. firewall placement) → monitor/review (assign risk owners, plan contingencies) → record findings clearly. *(E4, M5, D4.)*

## 1.21–1.23 Encryption, back-ups and organisational policy

Encryption (asymmetric, symmetric, data-at-rest via full-disk encryption/HSM/TPM, data-in-transit via SSL/TLS) and back-up (purpose, criteria - frequency, source, destination, storage - and types: full, incremental, differential, mirror) mirror the Digital Infrastructure content. Organisational policy covers a digital use policy (network/internet usage, BYOD, WFH, password renewal, software updates) and a health & safety policy (lone working, manual handling, working at height, fire safety, RIDDOR 2013), backed by a formal change procedure and regular policy audits. *(E5, D5 for the policy content.)*

## 1.24 Legislation, standards and best practice

Covers the same core framework as Digital Infrastructure, applied to cabling work: **UK GDPR**, the **Data Protection Act 2018**, the **Computer Misuse Act 1990**, **ISO 27001:2017**, **PCI DSS**, the **NCSC "10 Steps to Cyber Security"**, and **OWASP**. See the [Digital Infrastructure security page](../digital-infrastructure/01-security-procedures-and-controls.md#125-legislation-standards-and-best-practice) for the full breakdown of each.

## 1.25–1.30 Network security principles, access control, traffic security and vulnerabilities

- The **CIA triad** underpins security-policy design; **IAAA** (identification, authentication, authorisation, accountability) is applied through directory services, authentication, password policy, data protection and an information asset register.
- Access-control methods: authentication, firewalls, **IDS/IPS**, **NAC**, **MAC/DAC/ABAC/RBAC**.
- Traffic security: physical (SDN with TLS, DMZ, air gapping) and virtual (VLAN, VPN, VRF, subnets, IPSec).
- Cyber security techniques for connected devices: WPA2/WPA3, encryption, virtualisation, penetration testing, malware protection, patching, internet-gateway security, data-leakage protection, multi-factor authentication, single logout.
- Importance to organisations and society mirrors the Digital Infrastructure content - protecting systems/data/cloud availability for organisations, and privacy/identity/equal-opportunity protection (plus DPA 2018 rights) for society.

## 1.31 Network topologies, referencing models and minimum standards

Topologies (bus, star, ring, token ring, mesh, hybrid, client-server, peer-to-peer) and referencing models (OSI's seven layers; TCP/IP's four layers) underpin the **identify–protect–detect–respond–recover** cycle applied to network architecture.

## 1.32 Common vulnerabilities and cyber security controls

Missing patches/updates, weak or missing passwords, insecure BIOS/UEFI, misconfigured permissions, unprotected systems, insecure data/device disposal (WEEE Directive 2013), poor back-up management, and unprotected physical devices - each paired with a specific control (patch management, minimum password policy aligned to NCSC guidance, BIOS review, scheduled permission audits, malware protection, correct back-up frequency/type, correct software installation).

<!-- teaching-resources:start -->
## Teaching resources

Ready-made lesson slides for this topic. Each PowerPoint includes learning objectives, a starter, teaching slides, a quiz with answers, an activity and an exit ticket, with teacher notes on every slide. Download it and adapt it for your class.

| Lesson slides | Covers | Slides |
|---|---|---|
| [Business Security Controls (PowerPoint)](../../05-teaching-resources/slides/shared/01-business-security-controls.pptx) | 1.1 to 1.7 | 11 |
| [Disaster Recovery, Continuity and Backup (PowerPoint)](../../05-teaching-resources/slides/shared/02-disaster-recovery-and-backup.pptx) | DRP, BCP, RTO/RPO/MTBF/MTTR, SLAs, backups (1.8 to 1.12, 1.22 to 1.23; DI 2.18 to 2.19) | 10 |
| [Risk Management and Threat Assessment (PowerPoint)](../../05-teaching-resources/slides/shared/03-risk-management-and-threat-assessment.pptx) | Impacts, risk process, threat analysis, risk response, penetration testing (1.9 to 1.21) | 12 |
| [Technical Security and Network Protection (PowerPoint)](../../05-teaching-resources/slides/shared/04-technical-security-and-network-protection.pptx) | Technical controls, encryption, network security, access control, topologies and vulnerabilities (1.19 to 1.33) | 11 |
| [Security Law, Standards and Policy (PowerPoint)](../../05-teaching-resources/slides/shared/05-security-law-standards-and-policy.pptx) | Policies, legislation, standards and the importance of cyber security (1.23 to 1.31) | 10 |

See [all lesson slides](../../05-teaching-resources/01-lesson-slides.md) for every topic.
<!-- teaching-resources:end -->

## Key terms

- **DRP/BCP** - disaster recovery plan / business continuity plan.
- **RAG rating** - red/amber/green qualitative risk severity scale.
- **CIA triad** - confidentiality, integrity, availability.
- **DMZ** - demilitarised zone, an isolated network segment between internal and external networks.

## Related pages

- [Cabling Installation and Testing](02-cabling-installation-and-testing.md)
- [Discover, Evaluate and Apply Reliable Sources of Knowledge](03-sources-of-knowledge.md)
- [Digital Infrastructure - Security Procedures and Controls](../digital-infrastructure/01-security-procedures-and-controls.md)
- [Occupational Specialisms overview](../00-overview.md)
- [Scheme of Assessment](../05-scheme-of-assessment.md)
