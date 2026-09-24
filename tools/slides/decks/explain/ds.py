"""Explanations for the Digital Support specialism decks."""
from . import E

EXPLAIN = {
    "digital-support/01-agile-values-and-methodologies.pptx": {
        "The four agile values": E(
            "Agile is a way of working that delivers value in small, frequent steps and adapts to change. It rests "
            "on four values.\n\n"
            "Individuals and interactions over processes and tools: people talking solve problems faster than forms. "
            "Working software over comprehensive documentation: something that works matters most. Customer "
            "collaboration over contract negotiation: work with the customer throughout, not just at the start. "
            "Responding to change over following a plan: adjust when needs change.\n\n"
            "The items on the right still matter; agile just values the left more.",
            "A support team rolling out a new ticketing system shows users a working version every two weeks and "
            "changes it based on their feedback.",
            [("Complete: working software over...", "Comprehensive documentation."),
             ("Does agile mean no documentation?", "No, it just values working software more."),
             ("Why collaborate with customers throughout?", "So the result meets their real, changing needs.")]),
        "Agile methodologies (1)": E(
            "Scrum organises work into sprints, usually two to four weeks, each delivering something usable. It has "
            "defined roles (product owner, scrum master, team), events such as the daily scrum, and artefacts such as "
            "the backlog.\n\n"
            "Kanban shows work as cards moving across a board (To do, In progress, Done). Work-in-progress (WIP) "
            "limits stop too much being started at once and make bottlenecks visible. It suits the steady flow of "
            "support tickets.\n\n"
            "DSDM fixes cost, quality and time, and flexes the scope instead, prioritising features with MoSCoW.",
            "A helpdesk's Kanban board shows 12 tickets stuck in 'Waiting for parts': the bottleneck is supply, not the technicians.",
            [("What is a sprint?", "A short fixed period delivering a usable increment."),
             ("What does a WIP limit do?", "Caps how much work is in progress to expose bottlenecks."),
             ("What does DSDM keep fixed?", "Cost, quality and time.")]),
        "MoSCoW prioritisation": E(
            "MoSCoW sorts requirements into four groups so the most important are delivered first.\n\n"
            "Must have: essential; without them the project fails. Should have: important but not vital; could be "
            "delayed if needed. Could have: nice extras if time allows. Won't have (this time): agreed to be left out "
            "for now, which prevents scope creep.\n\n"
            "When time or money runs short, the 'could haves' are dropped first, protecting the 'must haves'.",
            "New helpdesk system. Must: log and track tickets. Should: email updates. Could: chatbot. Won't (this "
            "time): mobile app.",
            [("What does the W in MoSCoW mean?", "Won't have (this time)."),
             ("What is dropped first if time runs out?", "Could haves."),
             ("How does 'won't have' help a project?", "It prevents scope creep by agreeing what's out.")]),
    },
    "digital-support/02-domains-email-and-remote-access.pptx": {
        "Service functions in a domain": E(
            "A domain lets an organisation manage all its users and computers centrally.\n\n"
            "Active Directory Domain Services (AD DS) stores accounts and groups in organisational units (OUs); "
            "Group Policy pushes settings to them. DHCP assigns IP addresses; DNS resolves names to addresses. File "
            "servers and DFS share storage with permissions; print servers share printers; mail servers handle "
            "email. A certificate authority issues digital certificates that prove identity.\n\n"
            "Together they mean a user can log in on any domain PC and get the same files, printers and settings.",
            "A teacher logs in on a classroom PC: AD DS checks their password, Group Policy maps their drive and "
            "printer, and DNS finds the servers.",
            [("What does Group Policy do?", "Pushes settings to users and computers in OUs."),
             ("What does a certificate authority issue?", "Digital certificates."),
             ("Why use a domain?", "To manage users and computers centrally.")]),
        "Email protocols": E(
            "Email uses different protocols for sending and receiving.\n\n"
            "SMTP sends mail between servers and from your client to your server.\n\n"
            "POP3 downloads mail to one device and usually removes it from the server: fine for one computer, poor "
            "for several.\n\n"
            "IMAP keeps mail on the server and syncs it, so your phone, laptop and webmail all match.\n\n"
            "S/MIME encrypts and signs individual messages. TLS (the successor to SSL) encrypts the connection "
            "between client and server. Configuration also needs the provider, the right ports and the domain's MX "
            "record, which tells the internet which server receives its mail.",
            "A user complains emails read on their phone don't show as read on their laptop: they're set up with "
            "POP3 and need IMAP.",
            [("Which protocol sends email?", "SMTP."),
             ("Why use IMAP for several devices?", "It keeps mail on the server and syncs it."),
             ("What is an MX record?", "A DNS record saying which server receives a domain's email.")]),
        "Remote access and VPNs": E(
            "Remote access lets someone work away from the office as if they were connected to it: desktop sharing, "
            "remote support and off-site working. It's a key part of business continuity plans.\n\n"
            "A VPN protects remote access by encrypting all traffic between the device and the organisation's network "
            "and hiding the device's own IP address.\n\n"
            "Setting one up means choosing the security protocol and port, encryption settings and certificates, "
            "and how users authenticate, on both the server and the client.",
            "When snow closes the office, staff connect through the VPN from home and carry on working securely, as "
            "planned in the BCP.",
            [("What does a VPN encrypt?", "All traffic between the device and the organisation's network."),
             ("How does remote access support business continuity?", "Staff can keep working when they can't reach the office."),
             ("Name one thing to configure for a VPN.", "E.g. protocol, port, encryption, certificates, authentication.")]),
    },
    "digital-support/03-devices-operating-systems-and-applications.pptx": {
        "End-user devices": E(
            "Support technicians look after a wide range of devices.\n\n"
            "Desktops can be thick clients, which process locally, or thin clients, which rely on a server. Cloud "
            "workspaces provide a whole desktop over the internet. Mobile devices include laptops, tablets, phones, "
            "wearables and e-readers. Peripherals include keyboards, monitors, printers, scanners, projectors, "
            "drives and card readers.\n\n"
            "IoT devices are growing fast: smart building systems such as alarms, meters and lighting, and smart "
            "devices such as smart TVs. Each needs setting up, securing and supporting.",
            "A call centre uses thin clients: cheap, easy to replace, and all the software runs centrally, so one "
            "update fixes every desk.",
            [("What is a thin client?", "A device that relies on a server for processing."),
             ("Give two examples of IoT devices in a building.", "E.g. smart alarms, meters, lighting."),
             ("What is a cloud workspace?", "A desktop provided over the internet.")]),
        "Checking requirements: storage": E(
            "Before installing software or an OS, check the device meets the system requirements: storage, RAM, "
            "processor and OS compatibility.\n\n"
            "Storage choice matters. Hard disk drives are cheaper and hold more, but have moving parts that can fail "
            "and generate heat. Solid state drives are much faster, have no moving parts and suit small devices, "
            "but cost more per gigabyte.\n\n"
            "Also consider permissions: give users only the access they need (least privilege), and think about the "
            "security impact of what you install on the device, the network and the data.",
            "A new design app needs 16 GB of RAM and 50 GB free. The laptop has 8 GB, so it needs an upgrade before installation.",
            [("Name three system requirements to check.", "Any three: storage, RAM, processor, OS compatibility."),
             ("Give one advantage of an SSD.", "E.g. faster, no moving parts, compact."),
             ("What is least privilege?", "Giving users only the access they need.")]),
        "Installing an operating system": E(
            "Installing an OS follows a clear sequence.\n\n"
            "Choose the boot drive, then partition and format it. Join the device to the domain so it's managed "
            "centrally. Set the time, date, region and language. Install drivers so the hardware works properly. "
            "Apply updates, including over the network. Finally, install the applications the user needs.\n\n"
            "When upgrading an existing OS, back up and migrate the user's data first so nothing is lost.",
            "After a fresh install, the Wi-Fi doesn't work: the network driver hasn't been installed yet. Installing "
            "it from the manufacturer's site fixes it.",
            [("What must you do before upgrading a user's OS?", "Back up and migrate their data."),
             ("Why install drivers?", "So the hardware works properly."),
             ("Why join the device to the domain?", "So it's managed centrally.")]),
    },
    "digital-support/04-os-deployment-imaging-and-recovery.pptx": {
        "Deployment considerations": E(
            "Deploying an OS involves several choices.\n\n"
            "Installation method: over the network, locally from USB, virtualised, or cloud-based. Boot method: from "
            "the internal drive, external media, or the network using PXE.\n\n"
            "Partitioning: GPT is the modern standard; older disks use MBR with primary, extended and logical "
            "partitions. File system: NTFS for Windows, ext4 for Linux, exFAT for USB sticks shared between systems.\n\n"
            "Formatting: a quick format is fast and data can still be recovered; a full format scans for bad sectors "
            "and makes recovery much harder.",
            "Before giving an old laptop to a new user, a full format (plus secure wipe) makes sure the previous "
            "user's files can't be recovered.",
            [("What does PXE allow?", "Booting a device over the network."),
             ("Which file system suits a USB stick used on Windows and macOS?", "exFAT."),
             ("What does a full format do that a quick format doesn't?", "Scans for bad sectors and makes data harder to recover.")]),
        "Deployment methods": E(
            "Different deployment methods suit different situations.\n\n"
            "An unattended installation answers setup questions automatically from a file. Thin imaging installs a "
            "basic OS and adds drivers and apps per device: flexible but more work to manage. A base image captures a "
            "complete, configured system: quick at scale but less flexible.\n\n"
            "An in-place upgrade keeps user profiles but can hit compatibility problems. A clean install gives a "
            "fresh system but needs a backup first. A repair install fixes the OS without losing data. Multi-boot "
            "runs several OSs. Remote network installation needs no physical access but depends on network speed.",
            "Deploying 200 identical laptops: a base image. Upgrading one manager's laptop without losing their "
            "settings: an in-place upgrade.",
            [("What is an unattended installation?", "One that answers setup questions automatically from a file."),
             ("Give one advantage of a base image.", "Quick and consistent at scale."),
             ("Which method keeps user profiles?", "An in-place upgrade.")]),
        "Creating and deploying a disk image": E(
            "A disk image is a complete copy of a configured system, used to set up many devices identically.\n\n"
            "Install and configure the OS, applications and drivers on one reference machine and capture it as the "
            "base image. Create an answer (customisation) file for things like the computer name and region. Add any "
            "extra drivers or software. Distribute the image to a deployment server, then deploy it to the target devices.\n\n"
            "Keep the image updated, or every new device starts with old software and known vulnerabilities.\n\n"
            "Imaging saves time, keeps builds consistent, cuts support costs and allows fast restoration.",
            "When a laptop gets malware, the technician simply reimages it in 20 minutes instead of spending hours cleaning it.",
            [("What is a disk image?", "A complete copy of a configured system."),
             ("Why keep images updated?", "So new devices don't start with old, vulnerable software."),
             ("Give two benefits of imaging.", "Any two: saves time, consistency, lower support cost, fast restoration.")]),
        "Recovery and restoration": E(
            "When a system has problems, try recovery before restoration.\n\n"
            "System recovery repairs the system in its current state, keeping the user's files and folders, for "
            "example with startup repair.\n\n"
            "System restoration is used when recovery fails. It returns the system to an earlier state, such as a "
            "restore point or backup image, so recent changes may be lost.\n\n"
            "Either way: make sure data is backed up first, boot into the recovery tools, follow the steps, then test "
            "that the problem is really fixed.",
            "After a bad driver update, Windows won't start. Startup repair (recovery) fails, so the technician rolls "
            "back to yesterday's restore point (restoration).",
            [("Which should you try first, recovery or restoration?", "Recovery."),
             ("What might be lost in a restoration?", "Recent changes since the restore point."),
             ("What should you do before either?", "Make sure data is backed up.")]),
    },
    "digital-support/05-end-user-support-and-troubleshooting.pptx": {
        "What the CMS does": E(
            "A service or content management system (CMS) is the support team's central tool.\n\n"
            "Incident and request management logs, tracks, opens and closes tickets. Knowledge management collects "
            "fixes and spots training needs. Change management supports the rollout of new systems. Configuration "
            "and asset management tracks licences, hardware and software requests, and decommissioning.\n\n"
            "Because everything is recorded, the team can see trends, share fixes and prove they met their service levels.",
            "The CMS shows 40 tickets about the same VPN error this week: the team writes one knowledge article and "
            "fixes the root cause.",
            [("Name two CMS functions.", "Any two: incident/request, knowledge, change, configuration/asset management."),
             ("Why record every ticket?", "To see trends, share fixes and prove service levels."),
             ("What does asset management track?", "Licences, hardware, software requests and decommissioning.")]),
        "The troubleshooting method": E(
            "A structured method stops you guessing.\n\n"
            "Gather information: what exactly happened, when, and what changed? Analyse the problem: rule out known "
            "fixes and common causes. Test the remaining possibilities one at a time. Resolve it: back up data, "
            "apply the fix, test it and repeat until it's solved. Document the cause and fix in the CMS. Prevent it "
            "recurring with a lasting control.",
            "'The internet is broken' turns out, after questions, to be one website failing on one PC. Clearing the "
            "DNS cache fixes it; the cause is documented.",
            [("What is the first step?", "Gather information."),
             ("Why test one possibility at a time?", "So you know which change fixed it."),
             ("Why document the fix?", "So the team can solve it faster next time.")]),
        "Support processes": E(
            "Day-to-day support covers a lot of routine work.\n\n"
            "User management: adding and removing accounts and setting access hours. Password management: "
            "complexity, expiry and forced resets. Permissions: access to resources, Group Policy and shared folders. "
            "Software installation and connecting users to remote resources.\n\n"
            "Fault identification and escalation: first line handles common issues, second line deeper technical "
            "problems, third line specialists and suppliers.\n\n"
            "Plus documentation, known fixes, standard operating procedures, and asset management and auditing.",
            "A first-line technician resets a password (routine). A corrupted database goes to second line, and a "
            "suspected hardware fault under warranty to the supplier (third line).",
            [("What does first-line support handle?", "Common, routine issues."),
             ("When should a ticket be escalated?", "When it's beyond the current line's skills or access."),
             ("Why remove accounts promptly when staff leave?", "To stop former staff accessing systems.")]),
    },
    "digital-support/06-asset-version-and-mobile-device-management.pptx": {
        "Version control management": E(
            "Keeping software versions under control stops chaos.\n\n"
            "Fresh installations cover the OS, applications, utilities and licensing. Patching and updating covers "
            "system updates, drivers and firmware, anti-malware definitions and applications.\n\n"
            "Every update needs a rollback procedure, such as rolling back a device driver or uninstalling a failed "
            "OS update, in case it causes problems.\n\n"
            "Updates are deployed with network tools such as Group Policy, tested first, and released in a "
            "controlled way rather than all at once.",
            "A graphics driver update makes screens flicker on 30 PCs. The technician rolls back the driver through "
            "Group Policy and pauses the update.",
            [("Why have a rollback procedure?", "To undo an update that causes problems."),
             ("Name two things that get patched.", "Any two: OS, drivers, firmware, anti-malware, applications."),
             ("Why test updates before releasing them?", "To catch problems before they affect everyone.")]),
        "The asset management process": E(
            "Asset management tracks every piece of hardware and software through its life.\n\n"
            "Identification and planning: what do users and the organisation need, within what constraints, and how "
            "will it be deployed? Acquisition and implementation: source it and integrate it into current systems. "
            "Operation and maintenance: track licences and respond to requests. Decommissioning and redeployment: "
            "retire old systems, reuse what's still good, and manage the profiles of people joining and leaving.",
            "An asset register shows 20 unused software licences. They're reassigned to new starters instead of "
            "buying more, saving money.",
            [("Name the four stages.", "Identify and plan, acquire and implement, operate and maintain, decommission and redeploy."),
             ("Why track licences?", "To stay legal and avoid paying for unused ones."),
             ("What happens at decommissioning?", "Old assets are retired, reused or disposed of.")]),
        "Mobile Device Management (MDM)": E(
            "MDM software lets IT manage phones and tablets centrally.\n\n"
            "It can track and locate devices, secure them and configure Wi-Fi, mobile data, hotspots, Bluetooth and "
            "email. It can separate work and personal profiles, so company data stays in the work area, and enforce "
            "policies such as a screen lock, encryption, password rules, login attempt limits and MFA.\n\n"
            "Remotely, it can wipe a lost device, disable features, restrict app stores and control backup and sync.",
            "A manager leaves their phone on a train. IT locates it, then remotely wipes the work profile before "
            "anyone can access company email.",
            [("What can MDM do if a phone is lost?", "Locate it and remotely wipe it."),
             ("Why separate work and personal profiles?", "To keep company data apart and protected."),
             ("Name two security features MDM can enforce.", "Any two: screen lock, encryption, password rules, login limits, MFA.")]),
    },
    "digital-support/07-digital-solutions-and-training-users.pptx": {
        "Explaining a digital solution": E(
            "Support staff often have to recommend and explain technology to people who aren't technical.\n\n"
            "First analyse the requirement: what do they need to do, such as access information, use a service or "
            "complete transactions? Then identify the best-fit solution: a digital system, productivity software or "
            "wider digital technology. Finally explain the benefit clearly and concisely, pitched at your audience, "
            "using the correct technical terms but explaining any jargon.\n\n"
            "Focus on what it does for them, not how clever it is.",
            "Not 'SharePoint provides versioned document libraries', but 'everyone edits the same up-to-date file, "
            "and you can always get an older version back'.",
            [("What should you analyse first?", "The user's requirement."),
             ("Why focus on benefits rather than features?", "Users care about what it does for them."),
             ("How should jargon be handled?", "Avoided or explained.")]),
        "Training users": E(
            "Good training helps people use systems confidently and cuts support calls.\n\n"
            "Methods include shadowing and desk-side support, remote support, e-learning and simulation, VR and AR, "
            "smart boards, and gamified apps such as Kahoot! and Padlet.\n\n"
            "Tools include crib sheets and quick-reference guides, webinars and screencasts, virtual and managed "
            "learning environments (VLEs and MLEs), sandboxed practice environments where mistakes don't matter, and MOOCs.\n\n"
            "Choose based on the audience, the task, the time available and how many people need training.",
            "Rolling out MFA to 300 staff: a two-minute screencast, a one-page crib sheet, and drop-in desk-side help "
            "on launch day.",
            [("What is a sandboxed environment for?", "Safe practice where mistakes don't affect live systems."),
             ("What is a crib sheet?", "A short quick-reference guide."),
             ("Why might a screencast suit a large rollout?", "Many people can watch it whenever they need it.")]),
    },
}
