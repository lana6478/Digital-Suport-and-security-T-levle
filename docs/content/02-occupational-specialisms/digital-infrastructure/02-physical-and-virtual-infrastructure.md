# Digital Infrastructure - Physical and Virtual Infrastructure

*Digital Support and Security T Level → Occupational Specialisms → Digital Infrastructure → Physical and Virtual Infrastructure*

This page covers Content Area 2 of the Digital Infrastructure specialism: explaining, installing, configuring, testing and managing both physical and virtual infrastructure. It's the technical core of the specialism - networking, servers, virtualisation, cloud and service management. Subsection numbers mirror the specification.

## 2.1 Principles of network and infrastructure design

- **Resilience**: high availability (primary/secondary configurations), clustering (redundancy + scalability), load balancing (traffic distribution), segmentation (splitting network/systems/data/devices/services to limit risk impact).
- **Quality of Service (QoS)** - guarantees a specific level of network service.
- **Number systems** for subnetting/IP addressing: binary, hexadecimal, decimal, octal.
- Students must be able to explain the purpose, benefits and protocol/port usage of network infrastructure using correct technical language. *(E1, E4.)*

## 2.2 Transmitting digital information over copper, fibre and wireless

Signal types are electrical (copper), light-based (fibre) or wireless. Security risks include tampering and signal loss. Copper cabling needs segregating from electrical cabling because of interference (electromagnetic, static, crosstalk) - mitigated by shielding or parallel cable runs, in line with **BS EN 50174**. Wireless standards range from 802.11b/g/n through Wi-Fi 5, 6/6e and 7. Addressing covers **IPv4** (addressing schemes, subnetting, subnet masks) and **IPv6** (address types).

## 2.3 Elements of infrastructure and associated technologies

- **Network devices**: firewalls (including NGFW/UTM appliances), routers, switches, hubs, bridges, wireless access points, range extenders, modems, media converters.
- **End-user devices**: desktops/laptops, mobile devices, smart devices, removable media.
- **Storage**: HDD, SSD, removable media, **NAS**, **SAN**, block storage, object storage, and **RAID** levels - 0 (striping), 1 (mirroring), 5 (parity), 10 (mirroring + striping).
- **Wired/wireless tech**: UTP cabling (straight-through/crossover, TIA/EIA-568A/B), RJ11/RJ45 connectors, copper (Cat5e/Cat6) and fibre-optic cable, PPP, SDN, WPA1/2/3.
- **Antennas**: omni-directional, directional, patch, yagi, dipole.
- **Cloud service models**: IaaS, PaaS, SaaS, cloud storage.
- **Test equipment**: test plans, tone generator/probe, cable tester, tracing kit.
- Also: support scripting for automation/administration, network monitoring/logging, and capacity management (e.g. monitoring server load).

## 2.4 Electrostatic discharge (ESD) prevention and risk assessment (skill)

Mitigate ESD risk by limiting movement, checking temperature/humidity (higher humidity increases static build-up), and using anti-static equipment (e.g. wrist straps). Students apply the full risk-management process - identify risks and their effect on people, calculate probability/impact, prioritise, record findings, apply ESD protection, and comply with health & safety legislation. *(E1, E3, M2, M6, M10, D5.)*

## 2.5 Health and safety legislation in a digital infrastructure context

Health and Safety at Work etc. Act 1974 (PPE, employer duty of care); Manual Handling Operations Regulations 1992 (moving hardware); Health and Safety (Display Screen Equipment) Regulations 1999 (screen time, workspace setup); COSHH Regulations 2002 (e.g. printer maintenance); Control of Major Accident Hazards Regulations 2015 (e.g. earthing); WEEE Directive 2013 (disposal of hardware/network components).

## 2.6–2.8 Physical servers, virtual servers and containers

- **Physical servers** - full access to resources and full customisation, but expensive to buy/run, harder to maintain, storage is harder to scale, and they need physical space.
- **Self-hosted virtual servers** - lower setup expertise, better cost control, scalable, support HA/clustering, but high upfront cost and expensive resilience.
- **Cloud-hosted virtual servers** (e.g. Azure, AWS) - scale easily, built-in redundancy, third-party support, but higher subscription cost and a more complex initial setup.
- **Containers** - lightweight, portable, consistent and cheap to run and develop, but less secure if misconfigured, less OS flexibility, and need more expertise to set up.

## 2.9 Operating systems in digital infrastructure

Types: end-user/desktop (Windows, macOS), mobile (Android, iOS), server (Linux, Windows Server). Benefits: usability, no machine-language knowledge required, stronger data security. All OSs share a user interface, personalisation, resource management and an application platform - but differ in purpose-specific features, UX/UI, and supported functionality.

## 2.10 Client-server network services

- **Active Directory Domain Services (AD DS)** - centrally manages users, devices, security groups and distribution lists via **organisational units (OUs)**.
- **Group Policy** - **GPOs** applied to OUs to push settings/files to users and devices.
- **DHCP** - assigns IP addresses to clients.
- **LDAP** - directory-service authentication.
- **DNS** - hostname-to-IP translation.
- **File servers/DFS** - shared disk access. **Print servers** - shared printing. **Web/proxy/cache servers** - internet access, security, filtering. **Mail servers**, **application servers**, **database servers**, and security utilities (e.g. anti-virus) to protect data and systems.

## 2.11–2.12 Remote access and VPN setup

Remote access methods: **VPN** (private, encrypted connection), **RDP** (processing stays on the host machine), **LOM** - lights-out management (remote server administration), **SSH** (secure two-host connection). Setting up a simple VPN involves server-side configuration (enabling the service, setting IP/DNS, managing authentication and permissions) and client-side configuration (creating the connection, setting the destination IP/FQDN, setting permissions).

## 2.13–2.14 Installing, configuring, testing and maintaining networks (skill)

Install and configure servers (physical/virtual, OS, applications, database, security utilities), network infrastructure devices, firewalls, load balancers, end-user devices and network services (DNS, DHCP); select the right ports/protocols; implement scripting; apply back-up policy; and test functionality and performance, recording results to drive improvement. Ongoing maintenance repeats this for the same components, plus performance monitoring/logging, capacity management, and automation via scripting. *(D1, D6.)*

## 2.15 Making and testing UTP cable (skill)

Determine the cable's purpose and calculate the required length, then make a straight-through or crossover cable using the correct equipment (8P8C/RJ45 connectors, crimper, wire cutters), and test it against TIA/EIA standards. *(M2.)*

## 2.16–2.17 IT service management (ITSM) and ITIL

**ITSM** principles: co-creating value through service relationships, delivering a good customer experience, considering the broader impact of change, and working across departments.

**ITIL®** lifecycle stages: service strategy (aligning services to business objectives), service design, service transition (managed change), service operation (fulfilling requests, resolving failures, routine tasks), and continual service improvement.

## 2.18–2.19 DRPs and BCPs in digital infrastructure

Common principles: identify (risk, critical systems, resource requirements), analyse (business impact, maximum downtime), design (plan components), implement (communication plan), and measure (test, check compliance, review). A **BCP** is about keeping the business running during disruption (alternative premises, adaptive processes, alternative technology); a **DRP** is about restoring normal operations after a disaster (restoring access/functionality, replacing infrastructure).

## 2.20 Solution lifecycle (SLC)

Discover (requirements, planning, conceptual design, feasibility) → plan/design/develop (detailed design, prototyping, compliance, using existing architecture, development, integration) → test/QA (functional and performance testing) → pre-production (sandbox testing, sign-off) → deployment (release, staged rollout for high-impact changes) → monitor/evaluate (continuous improvement) → decommission → migrate. Every stage should be applied safely and documented. *(M2, M3.)*

## 2.21 DevOps

Principles: continuous integration/delivery, microservices, infrastructure as code, collaboration, automated testing, adapt-and-scale, monitoring/logging. Aims: deliver systems in an agile way; build, test and release changes quickly. Benefits: faster delivery, higher productivity, better cross-team process, scalability, fewer errors.

## 2.22 Solution architecture principles

Reuse and documentation matter; solution architecture applies to hardware; frameworks such as **TOGAF** provide structure; solutions should align to enterprise architecture; and architecture is described through system, view, viewpoint, concern and stakeholder.

## 2.23 Virtualisation concepts and applications

Concepts: creating multiple virtual resources from one physical resource (partitioning), or one virtual resource from several physical resources; isolation; encapsulation; hardware independence. Applications: network, server, desktop, OS and data virtualisation.

## 2.24 Continuous improvement of hardware/network (skill)

Identify the hardware affected by a change and assess current network performance; apply the appropriate SLC stage to respond; assess performance afterwards; process and review outcome data; and record findings clearly to inform future policy. *(E1, E2, E4, D4.)*

## Key terms

- **HA / clustering / load balancing** - resilience techniques for network design.
- **AD DS / GPO** - Active Directory Domain Services / Group Policy Object.
- **RAID 0/1/5/10** - striping, mirroring, parity, mirroring+striping.
- **IaaS/PaaS/SaaS** - Infrastructure/Platform/Software as a Service.
- **ITIL** - IT Infrastructure Library, a service-management framework.
- **SLC** - solution lifecycle.

## Related pages

- [Security Procedures and Controls](01-security-procedures-and-controls.md)
- [Discover, Evaluate and Apply Reliable Sources of Knowledge](03-sources-of-knowledge.md)
- [Network Cabling - Cabling Installation and Testing](../network-cabling/02-cabling-installation-and-testing.md)
- [Occupational Specialisms overview](../00-overview.md)
- [Scheme of Assessment](../05-scheme-of-assessment.md)
