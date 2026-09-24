# Digital Support - Installing, Configuring and Supporting Software and Operating Systems

*Digital Support and Security T Level → Occupational Specialisms → Digital Support → Software and OS Support*

This is Content Area 2 of the Digital Support specialism - the specialism's distinctive technical core. It covers how digital support technicians work with agile delivery practices, business systems, domains, service/content management, end-user devices, operating systems, application deployment, remote access, and end-user support and training.

## 2.1 Agile values

The four values behind agile work: individuals and interactions over processes and tools; working software over comprehensive documentation; customer collaboration over contract negotiation; responding to change over following a plan.

## 2.2 Agile methodologies in practice

- **Scrum** - defined roles/events/artefacts/rules, daily scrums, work split into sprints.
- **Kanban** - balances demand against capacity, surfaces bottlenecks, uses a Kanban board and work-in-progress (WIP) limits.
- **DSDM** (Dynamic Systems Development Method) - fixes cost, quality and time; prioritises scope with MoSCoW.
- **Feature-driven development** - breaks work into small features, planned/designed/built feature by feature.
- **Crystal** - prioritises communication and interaction between people over process and tooling.
- **Lean** (7 principles) - eliminate waste, build in quality, create knowledge, defer commitment, deliver fast, respect people, optimise the whole.
- **Extreme Programming (XP)** - frequent short release cycles, checkpoints for new requirements, planning and feedback loops.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Agile Values and Methodologies](../../05-teaching-resources/slides/digital-support/01-agile-values-and-methodologies.pptx) (PowerPoint, 10 slides)
<!-- lesson-slide:end -->

## 2.3 Digital technologies across business operations

Digital systems now sit inside every business function: finance (budget dashboards, invoicing, expense tracking), sales/marketing (CRM, social media tools), operations (performance dashboards, ticketing), HR (personnel systems, digital training), communications (video conferencing, email, collaboration platforms) and R&D (CAD, IDEs). For digital support this means rising demand for support, greater staff training needs, more emphasis on CPD, and an ongoing requirement to keep information systems running so the organisation can collect, store, maintain and distribute information.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Digital Solutions and Training Users](../../05-teaching-resources/slides/digital-support/07-digital-solutions-and-training-users.pptx) (PowerPoint, 9 slides)
<!-- lesson-slide:end -->

## 2.4 Service functions that create a domain environment

- **Active Directory Domain Services (AD DS)** - centrally manages users/devices/security groups/distribution lists via organisational units (OUs); **Group Policy** applies Group Policy Objects (GPOs) to OUs to push settings/files.
- **DHCP** - assigns IP addresses and network configuration to clients.
- **DNS** - resolves hostnames to IP addresses.
- **File server / DFS** - shared disk access and permission management.
- **Print server** - shared printer access.
- **Mail server** - manages inbound/outbound client mail.
- **Certificate authority** - issues digital certificates to certify ownership of a public key.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Domains, Email and Remote Access](../../05-teaching-resources/slides/digital-support/02-domains-email-and-remote-access.pptx) (PowerPoint, 10 slides)
<!-- lesson-slide:end -->

## 2.5 Content management systems (CMS) and resolving user problems

CMS functions: **incident/request management** (logging, tracking, open/closed tickets), **knowledge management** (identifying training needs, collating support knowledge), **change management** (supporting new system rollout) and **configuration/asset management** (licence tracking, hardware/software requests, decommissioning). The troubleshooting method taught is: gather information (investigate the request and likely causes) → analyse the problem (eliminate known fixes/causes) → test remaining possibilities → resolve (back up data, implement and test the fix, repeat until resolved, document the cause/solution in the CMS, apply controls to stop recurrence).

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [End-User Support and Troubleshooting](../../05-teaching-resources/slides/digital-support/05-end-user-support-and-troubleshooting.pptx) (PowerPoint, 10 slides)
<!-- lesson-slide:end -->

## 2.6 End-user devices and systems supported via a CMS

Desktop (thick/thin clients), cloud workspaces (free or licensed), mobile devices (tablets, smartphones, wearables, e-readers), laptops, peripherals (mouse, keyboard, monitor, printer/scanner, speakers, projector, storage drive, card readers) and IoT (smart-building systems such as alarms/meters/lighting; smart devices such as autonomous vehicles and smart TVs).

## 2.7 Operating system types in a digital support environment

End-user OS (Windows/macOS/Linux - desktops and laptops), mobile OS (iOS/Android - tablets and phones), and server OS (Windows/Linux - client-server environments).

## 2.8 Application types used in digital support

Productivity software (word processing, spreadsheets, presentations, diagramming), web browsers, collaboration software (email client, conferencing, VoIP, instant messaging, online workspace, document sharing), business software (database, project management, bespoke apps, accounting, CRM, ticketing) and development software (CAD, IDE).

## 2.9 Application installation and configuration

System requirements to check before installing: storage, RAM, compatibility, processor, OS. Storage trade-offs: HDD (cheap, more capacity, but mechanically fragile and heat-prone) versus SSD (fast, no moving parts, but pricier with less capacity - useful where device size matters). Network card trade-offs: efficient and secure but at higher cost with a finite performance lifespan. Other considerations: resource setup for performance, permissions (file/folder access, user authorisation, least privilege) and security impact on the device, network, usability and data storage. Practical skill: remotely installing an OS and configuring settings - correct boot drive/partitioning/format, domain setup, time/date/region/language, drivers, updates, and upgrading an existing OS without losing user data - plus installing productivity software and applying network-based updates.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Devices, Operating Systems and Applications](../../05-teaching-resources/slides/digital-support/03-devices-operating-systems-and-applications.pptx) (PowerPoint, 10 slides)
<!-- lesson-slide:end -->

## 2.10 OS deployment considerations

System requirements and hardware configuration must be checked first. **Installation/deployment methods**: network-based, local (CD/USB), virtualised, cloud-based. **Boot methods**: internal drive (SSD/HDD), external media (USB/flash/hot-swappable), or network boot (PXE, Netboot). **Partitioning**: dynamic, basic, primary, extended, logical, GPT. **File systems**: exFAT, FAT32, NTFS, ReFS, NFS, ext3, ext4, HFS, and swap partitions. **Formatting**: quick format (faster, easier file recovery, no bad-sector scan) vs. full format (thorough scrub and bad-sector scan, harder to recover files, slower).

## 2.11 Deployment methods - advantages and disadvantages

- **Unattended installation** - minimal technician input via pre-set options.
- **Thin imaging** - scales well across varied devices and stays flexible, but needs more maintenance and is harder to configure.
- **Base image** - easy to create for a specific purpose at scale, but harder to maintain and less flexible.
- **In-place upgrade** - efficient, keeps user profiles, but risks compatibility issues and needs the full OS media/download.
- **Manual clean install** - gives the latest OS version simply, but may need a prior backup and takes time.
- **Repair installation** - fixes without data loss or a full upgrade, but is manual and may not resolve every instability.
- **Multi-boot** - runs multiple OSs on one device, but is fiddly to set up and maintain.
- **Remote network installation** - no physical access needed and scales efficiently, but is capped by network speed, needs specific configuration (e.g. PXE support) and significant setup.

## 2.12 Deploying software and OS remotely

Gather and analyse user requirements → select/configure the deployment method (thin imaging: gather installer/drivers and build a task sequence; base image: install and configure the OS/apps/drivers then capture the disk image) → deploy using the chosen method → apply updates to the OS/apps/drivers → test against business requirements → follow organisational safety/security policy throughout.

## 2.13 Creating and deploying disk images

Create the base image → create a customisation/answer file → add any extra drivers/software → distribute the image → deploy it → keep software versions and drivers updated to avoid introducing vulnerabilities.

## 2.14 Benefits of image-based deployment

Requires fewer resources through automation, keeps deployments consistent, reduces ongoing support cost, and allows quick system restoration.

## 2.15 System recovery vs. restoration

**Recovery** fixes the system in its current state, preserving files/folders. **Restoration** is used when recovery fails, and reverts the system to an earlier state. Process: ensure data is backed up → boot into recovery tools → follow on-screen steps → test to confirm the issue is resolved.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [OS Deployment, Imaging and Recovery](../../05-teaching-resources/slides/digital-support/04-os-deployment-imaging-and-recovery.pptx) (PowerPoint, 10 slides)
<!-- lesson-slide:end -->

## 2.16 Corporate and ISP email configuration

- **POP3** - pulls mail down to local software.
- **IMAP** - holds mail on the server, accessed by client software.
- **SMTP** - receives/sends mail over the internet.
- **S/MIME** - sends encrypted email.
- **SSL / port settings** - encrypted connection between mail/web server and client.
- **TLS** - SSL's successor, providing data security.

## 2.17 Configuring on-premises and cloud email services

Align configuration with corporate policy, set up user profiles (usernames, passwords, signatures), and select the provider (e.g. Google Workspace, Microsoft 365), protocol (SMTP/IMAP/POP3), MX record, and inbound/outbound mail domains.

## 2.18 Remote access - purpose and applications

Purpose: lets someone work from a remote location as though connected to the physical network (e.g. supporting home working during an office closure as part of a BCP). Applications: desktop sharing, remote support (fault diagnosis, correcting user issues remotely), off-site working.

## 2.19 VPNs for secure remote access

Role: encrypts network traffic and masks the client's IP address to increase privacy. Configuration factors: settings, client/server configuration, port and security protocol (e.g. TLS, SSL), encryption settings/certificates, and authentication.

## 2.20 Configuring a simple VPN

**Server side**: enable the VPN service, configure IP address/DNS hostnames for the VPN interface, manage user access (authentication, permissions). **Client side**: create the connection, set the destination IP/FQDN, set permissions and conditions.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Domains, Email and Remote Access](../../05-teaching-resources/slides/digital-support/02-domains-email-and-remote-access.pptx) (PowerPoint, 10 slides)
<!-- lesson-slide:end -->

## 2.21 Support processes for end users and customers

User management (add/remove users, access hours), password management (complexity, expiry, forced reset), permissions/privileges (resource access, group policy, shared resource configuration), software installation/deployment, remote resource connection, fault identification, escalation from first to third line, knowledge management/documentation, known fixes, SOPs, asset management and auditing.

## 2.22 Applying troubleshooting methods

The same structured method as 2.5: gather information → analyse the problem → test remaining possibilities → apply resolution (back up, implement, test, repeat, document in the fault-logging system) → apply actions to stop the cause recurring.

## 2.23 Monitoring and operating information systems

Analyse the performance of hardware, software, database, network and people. Monitor the appropriate security controls (firewalls, anti-virus) and network performance/traffic. Operate and maintain assets (track licences, respond to hardware/software requests, log/tag assets correctly). Support users face-to-face or remotely (training, recording issues in the CMS, password management, fault ID, escalation). Record and summarise findings logically, using correct technical terms, to inform future policy.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [End-User Support and Troubleshooting](../../05-teaching-resources/slides/digital-support/05-end-user-support-and-troubleshooting.pptx) (PowerPoint, 10 slides)
<!-- lesson-slide:end -->

## 2.24 Version control management

Fresh installation covers OS, application software, utility software and licensing. Patching/updating covers system, driver/firmware, anti-virus/anti-malware and application updates. "Updates" also covers rollback procedures (e.g. rolling back a device driver or a failed OS update). Deployment uses network tools such as Group Policy, spanning local install, network deployment, testing and release control.

## 2.25 Asset management process

Identification and planning (user/organisational needs, constraints, deployment strategy) → acquisition and implementation (sourcing hardware/software, integrating into the current system) → operation and maintenance (tracking licences, responding to requests) → decommissioning and redeployment (removing unused assets, retiring out-of-date systems, managing joiner/leaver profiles).

## 2.26 Mobile Device Management (MDM)

Purpose: track/locate, secure, and manage the use and configuration (wireless/cellular data, hotspot, tethering, airplane mode, Bluetooth, email) of mobile devices. Applications include segregating personal/professional profiles and enforcing policy compliance. Remote management covers remote wipe, disabling features, restricting devices/app stores/calling-data use, and controlling backup/sync. Security features: screen lock, device encryption, password enforcement, login-attempt restrictions, MFA, and authenticator apps (e.g. Google Authenticator, FIDO). Practical skill: applying MDM to configure the settings listed under "purpose" above.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Asset, Version and Mobile Device Management](../../05-teaching-resources/slides/digital-support/06-asset-version-and-mobile-device-management.pptx) (PowerPoint, 9 slides)
<!-- lesson-slide:end -->

## 2.27 Explaining the benefits of digital solutions

Analyse the requirement (access to information/services/products, or transactions), identify the best-fit solution (digital systems, productivity software, or wider digital technology), then explain the benefit clearly and concisely, pitched to the audience and using correct technical terminology.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Digital Solutions and Training Users](../../05-teaching-resources/slides/digital-support/07-digital-solutions-and-training-users.pptx) (PowerPoint, 9 slides)
<!-- lesson-slide:end -->

## 2.28 Operating digital information systems and tools

Operate systems to collect/store/maintain/distribute information supporting service delivery; process and critically review user feedback; maintain service delivery (create/action/update tickets, communicate ticket status, monitor/record system performance, support users remotely); record and summarise findings clearly to inform future policy.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [End-User Support and Troubleshooting](../../05-teaching-resources/slides/digital-support/05-end-user-support-and-troubleshooting.pptx) (PowerPoint, 10 slides)
<!-- lesson-slide:end -->

## 2.29 Training methods and tools for digital systems

**Methods**: shadowing, desk-side support, remote support, e-learning, VR, AR, smart boards, gamified apps (e.g. Kahoot!, Padlet), simulation. **Tools**: crib sheets, smart sheets, webinars, screencasts, managed/virtual learning environments (MLE/VLE), sandboxed environments, MOOCs.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Digital Solutions and Training Users](../../05-teaching-resources/slides/digital-support/07-digital-solutions-and-training-users.pptx) (PowerPoint, 9 slides)
<!-- lesson-slide:end -->

<!-- teaching-resources:start -->
## Teaching resources

Ready-made lesson slides for this topic. Each PowerPoint includes learning objectives, a starter, teaching slides, a quiz with answers, an activity and an exit ticket, with teacher notes on every slide. Download it and adapt it for your class.

| Lesson slides | Covers | Slides |
|---|---|---|
| [Agile Values and Methodologies (PowerPoint)](../../05-teaching-resources/slides/digital-support/01-agile-values-and-methodologies.pptx) | 2.1, 2.2 | 10 |
| [Domains, Email and Remote Access (PowerPoint)](../../05-teaching-resources/slides/digital-support/02-domains-email-and-remote-access.pptx) | 2.4, 2.16 to 2.20 | 10 |
| [Devices, Operating Systems and Applications (PowerPoint)](../../05-teaching-resources/slides/digital-support/03-devices-operating-systems-and-applications.pptx) | 2.6 to 2.9 | 10 |
| [OS Deployment, Imaging and Recovery (PowerPoint)](../../05-teaching-resources/slides/digital-support/04-os-deployment-imaging-and-recovery.pptx) | 2.10 to 2.15 | 10 |
| [End-User Support and Troubleshooting (PowerPoint)](../../05-teaching-resources/slides/digital-support/05-end-user-support-and-troubleshooting.pptx) | 2.5, 2.21 to 2.23, 2.28 | 10 |
| [Asset, Version and Mobile Device Management (PowerPoint)](../../05-teaching-resources/slides/digital-support/06-asset-version-and-mobile-device-management.pptx) | 2.24 to 2.26 | 9 |
| [Digital Solutions and Training Users (PowerPoint)](../../05-teaching-resources/slides/digital-support/07-digital-solutions-and-training-users.pptx) | 2.3, 2.27, 2.29 | 9 |

See [all lesson slides](../../05-teaching-resources/01-lesson-slides.md) for every topic.
<!-- teaching-resources:end -->

## Key terms

- **AD DS / GPO** - Active Directory Domain Services and Group Policy Objects, the core Windows domain management tools.
- **DHCP / DNS** - protocols that assign IP addresses and resolve hostnames respectively.
- **Thin imaging / base image** - two contrasting approaches to building deployment images, trading flexibility against maintenance effort.
- **MDM** - Mobile Device Management, used to secure and control mobile devices remotely.
- **VPN** - Virtual Private Network, encrypting traffic and masking IP address for secure remote access.

## Related pages

- [Digital Support: Security Procedures and Controls](01-security-procedures-and-controls.md)
- [Digital Support: Sources of Knowledge](03-sources-of-knowledge.md)
- [Cyber Security: Remediation and Risk Assessment](../cyber-security/02-remediation-and-risk-assessment.md)
- [Occupational Specialisms overview](../00-overview.md)
- [Scheme of Assessment](../05-scheme-of-assessment.md)
