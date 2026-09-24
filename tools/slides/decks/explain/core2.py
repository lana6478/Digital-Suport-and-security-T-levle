"""Explanations for the Core Component decks (Core Paper 2 and the ESP)."""
from . import E

EXPLAIN = {
    "core/10-the-business-context.pptx": {
        "The business environment": E(
            "Every organisation exists to provide a product or a service, but they differ in why and how.\n\n"
            "Private sector organisations are owned privately and usually aim to make a profit. They range from "
            "small and medium enterprises (SMEs) to large enterprises, plus NGOs. The public sector is run by "
            "government, such as the NHS and councils. The voluntary or charity sector is not for profit.\n\n"
            "Business models describe who they sell to: B2C to consumers, B2B to other businesses, B2M to a mass market.\n\n"
            "Stakeholders are anyone affected: internal (owners, directors, employees) and external (customers, "
            "suppliers, shareholders, investors, government).",
            "A company selling laptops to schools is private sector and B2B. The schools, their pupils and the "
            "laptop manufacturer are all external stakeholders.",
            [("Which sector is the NHS in?", "The public sector."),
             ("What does B2B mean?", "Business to business."),
             ("Is an employee an internal or external stakeholder?", "Internal.")]),
        "Digital value across the business": E(
            "Digital systems add value to almost every part of an organisation.\n\n"
            "Sales and marketing use them for market research, social media, online selling, personalised offers "
            "and analytics. HR keeps staff records and training data. Operations use them to communicate, automate "
            "processes and support remote working. Managers watch key performance indicators (KPIs) in real time. "
            "Logistics automates stock control, and finance cuts costs and reports faster.\n\n"
            "To add value, systems must meet user needs: work well, remove pain points such as slow response, be "
            "accessible, compatible with other systems, available when needed and properly supported.",
            "A café's online ordering system increases sales, its stock system reorders milk automatically, and its "
            "dashboard shows the manager today's takings in real time.",
            [("How do digital systems help HR?", "Staff records, performance management and training records."),
             ("What is a pain point?", "Something that frustrates users, e.g. slow response or complex tasks."),
             ("What does real-time KPI monitoring let managers do?", "See performance as it happens and act quickly.")]),
        "Risks and impacts of digital systems": E(
            "Relying on digital systems brings risks as well as benefits.\n\n"
            "Security breaches can break confidentiality, integrity or availability. Privacy breaches expose "
            "personal or business information. Organisations can fall foul of the law or regulators. Poor design "
            "or biased systems can exclude some users. Rival technologies can make a system outdated, and systems "
            "can fail or turn out not fit for purpose.\n\n"
            "The impacts can be severe: legal action, fines, reputational damage, loss of a licence to operate and "
            "loss of business. That's why support and security roles matter so much.",
            "A dental practice's booking system is hit by ransomware. It can't see patients (lost business), must "
            "report the breach (regulator), and loses patients' trust (reputation).",
            [("Name two risks of using digital systems.", "Any two: security breach, privacy breach, non-compliance, exclusion, rival tech, technical failure."),
             ("Give two impacts of a serious breach.", "Any two: legal action, fines, reputational damage, loss of licence, loss of business."),
             ("How can a system exclude users?", "Through bias or poor, inaccessible design.")]),
    },
    "core/11-technical-change-management.pptx": {
        "Triggers for change": E(
            "Organisations change their systems when something pushes them to.\n\n"
            "Internal triggers come from inside: restructuring, expanding or downsizing, new strategic goals such as "
            "rebranding or new services, or crises like a cyber attack or system failure.\n\n"
            "External triggers come from outside, and PESTLE is a handy checklist: Political (a new government), "
            "Economic (recession, new competitors), Social (trends like remote working), Technological (new "
            "technology, obsolete systems, zero-day vulnerabilities), Legal (new laws) and Environmental "
            "(sustainability targets, pandemics).",
            "The pandemic (environmental and social) forced firms to roll out laptops, VPNs and video calls in weeks "
            "so staff could work from home.",
            [("What does PESTLE stand for?", "Political, Economic, Social, Technological, Legal, Environmental."),
             ("Give an internal trigger for change.", "E.g. expansion, restructuring, a cyber attack."),
             ("Which PESTLE factor is a new data protection law?", "Legal.")]),
        "The change management process (part 1)": E(
            "Changing a live system without a process causes outages, so organisations follow a change management process.\n\n"
            "First, identify the type of change: a new system or an amendment. The Change Advisory Board (CAB) then "
            "reviews, prioritises and approves requests and monitors progress.\n\n"
            "Next, set SMARTER objectives (specific, measurable, achievable, realistic, time-bound, evaluated, "
            "reviewed), forecast the impact, and allocate resources: budget, time, staff, hardware and software.\n\n"
            "Finally, communicate the risks and impact to stakeholders so they accept the change and comply with it.",
            "Moving email to the cloud: the CAB approves it; the objective is 'all 200 mailboxes migrated by 30 "
            "June with under one hour of downtime each'; staff are told what will change and when.",
            [("What does the CAB do?", "Reviews, prioritises and approves change requests and monitors progress."),
             ("What does SMARTER stand for?", "Specific, measurable, achievable, realistic, time-bound, evaluated, reviewed."),
             ("Why communicate with stakeholders before a change?", "To gain acceptance and make sure people comply.")]),
        "The change management process (part 2)": E(
            "Once planned, the change is configured, integrating with legacy systems while keeping services running, "
            "then fully tested in a proper test environment so results are reproducible.\n\n"
            "An implementation method is chosen: direct, parallel, phased or pilot.\n\n"
            "Everything is documented: decisions, requirements and updated manuals. A rollback plan, with backups "
            "and a recovery plan, means you can undo a failed change.\n\n"
            "Training needs are identified, progress is monitored with a post-implementation review, and version "
            "control keeps track of every change.",
            "A new firewall rule set is tested in a lab copy of the network, deployed on Saturday night, with the old "
            "configuration saved so it can be restored in minutes if anything breaks.",
            [("What is a rollback plan?", "A plan, with backups, to undo a change that fails."),
             ("Why test in a separate test environment?", "To find problems without affecting the live system."),
             ("What is a post-implementation review?", "Checking after go-live whether the change met its objectives.")]),
        "Implementation methods": E(
            "There are four ways to switch from an old system to a new one.\n\n"
            "Direct: switch the old one off and the new one on at once. Quick and cheap, but if the new system fails "
            "there's nothing to fall back on.\n\n"
            "Parallel: run both systems side by side for a while. Safe, but staff do the work twice.\n\n"
            "Phased: introduce the new system one part at a time. Lower risk, but slower.\n\n"
            "Pilot: one team or site uses it first, then everyone else follows. Problems are found early on a small "
            "scale, but the full rollout takes longer.",
            "A hospital moving to new patient records would never go direct. A pilot on one ward, followed by a "
            "phased rollout, keeps patients safe.",
            [("Which method runs old and new systems together?", "Parallel."),
             ("Which method is riskiest?", "Direct."),
             ("What is a pilot implementation?", "One team or site uses the new system first.")]),
        "Is the project feasible?": E(
            "Before committing, organisations check whether a change is feasible: worth doing and possible.\n\n"
            "Benefits and drawbacks: will it save money or earn more than it costs? How will it affect productivity, "
            "communication, security and reputation?\n\n"
            "Risks: staff may resist the change, misuse the new system or lack the knowledge to support it, and the "
            "rollout could disrupt the business.\n\n"
            "Constraints: the budget, the time available, and the people and technology on hand.\n\n"
            "If the risks and costs outweigh the benefits, the project may be changed or dropped.",
            "A small charity wants a new CRM. It would save 10 hours a week, but costs 8,000 pounds and no one can "
            "support it. The constraints make a cheaper hosted option more feasible.",
            [("Name three constraints on a project.", "Budget, time, human and technological resources."),
             ("Give one risk of introducing a new system.", "E.g. resistance to change, misuse, disruption."),
             ("What is a feasibility study for?", "Deciding whether a project is worth doing and possible.")]),
    },
    "core/12-digital-support-roles-and-communication.pptx": {
        "Four occupational areas": E(
            "Digital support and security work falls into four areas.\n\n"
            "Digital infrastructure: installing, testing and maintaining systems and networks, keeping them available, "
            "recovering from failures, optimising performance and applying security.\n\n"
            "Network cabling: installing, terminating, testing and certifying copper and fibre cable, fitting racks "
            "and cabinets, and producing cable route maps and records.\n\n"
            "Digital support: helping users with hardware and software, managing accounts and permissions, training "
            "users and keeping asset registers.\n\n"
            "Digital communications: installing and maintaining integrated communication systems such as VoIP.",
            "When a school opens a new block: cabling installers run the cable, infrastructure technicians set up "
            "the network, and support technicians set up the PCs and train the staff.",
            [("Which area certifies copper and fibre cable?", "Network cabling."),
             ("Which area trains end users?", "Digital support."),
             ("Name one infrastructure responsibility.", "E.g. keeping systems available, applying security, recovery.")]),
        "Communication techniques": E(
            "Technical skill is only half of support; the other half is communication.\n\n"
            "Written channels include incident tickets, system update notifications and forums. Keep them clear, "
            "concise and matched to the audience: how many people, how much they know and how much detail they need.\n\n"
            "In conversation, use a troubleshooting approach: ask open questions ('What happened just before it "
            "stopped?'), listen actively, and watch body language.\n\n"
            "When users are frustrated, stay calm, acknowledge the problem and de-escalate before explaining the fix. "
            "Negotiation helps when you can't give them exactly what they want.",
            "Instead of 'Your DNS cache was corrupt', say: 'Your computer had saved an old address for that website. "
            "I've cleared it, so it can find the right one now.'",
            [("Give an example of an open question.", "E.g. 'What happened just before it stopped working?'"),
             ("What is active listening?", "Fully concentrating on and responding to what the person says."),
             ("Why avoid jargon with users?", "They may not understand it.")]),
        "Meeting different interaction needs": E(
            "Different people need different kinds of support.\n\n"
            "Clients and end users want their problem fixed with minimal fuss: verbal help, written updates on "
            "progress, training, and remote support or screen sharing.\n\n"
            "Managers want the big picture: clear escalation routes, progress reports and presentations about "
            "risks, costs and decisions.\n\n"
            "Peers and colleagues benefit from shared best practice and knowledge, training, and collaboration on "
            "difficult problems.\n\n"
            "Adapting your approach to the audience makes you far more effective.",
            "The same outage: a text to users ('Email is down, fix expected by 11am'), a report to the manager "
            "(cause, impact, cost), and a knowledge-base article for colleagues (how it was fixed).",
            [("What do managers usually need from support staff?", "Escalation routes, progress reports, presentations."),
             ("How can users be supported remotely?", "E.g. remote support tools or screen sharing."),
             ("Why share fixes with colleagues?", "So the team can solve the same problem faster next time.")]),
    },
    "core/13-emerging-issues-and-technologies.pptx": {
        "Impact of digital technologies": E(
            "Technology changes how organisations work and how society lives.\n\n"
            "In organisations, communication has moved to email, chat and video; people are expected to be more "
            "productive and more available; staff are monitored more; remote and hybrid working are normal; and "
            "automation, including AI, takes over routine tasks.\n\n"
            "In society, some jobs disappear while new skills are needed. Fewer decisions involve humans, privacy is "
            "harder to protect, and behaviour changes. Access to information and services has improved for many, "
            "but people without skills, equipment or connectivity risk digital isolation.",
            "Self-service checkouts cut cashier jobs but created roles in maintenance and IT support, and left some "
            "older shoppers struggling.",
            [("Give two ways technology has changed organisational culture.", "E.g. remote working, staff monitoring, automation."),
             ("What is digital isolation?", "Being left out through lack of skills, equipment or connectivity."),
             ("Give one positive impact on society.", "E.g. better access to information and services.")]),
        "Digital inclusion": E(
            "Digital inclusion means everyone can access and use digital services fairly.\n\n"
            "That needs suitable hardware and software, reliable connectivity, and design that follows accessibility "
            "best practice. Public sector websites must meet accessibility regulations by law.\n\n"
            "Think about who the users are: their age, digital and literacy skills, whether they're staff or the "
            "public, cultural issues (including bias built into systems), and accessibility needs such as visual "
            "impairment or limited mobility.\n\n"
            "Professional development helps IT staff keep up with standards so they can build inclusive systems.",
            "A council moves applications online. Offering a phone line, large-text options and screen-reader-friendly "
            "forms keeps it inclusive.",
            [("What does digital inclusion mean?", "Everyone being able to access and use digital services fairly."),
             ("Name two user characteristics that affect inclusion.", "Any two: age, digital skills, literacy, culture, accessibility needs."),
             ("Must public sector websites be accessible?", "Yes, it is required by regulations.")]),
        "Emerging technologies (1)": E(
            "Several emerging technologies are changing digital support.\n\n"
            "Storage and processing: demand for storage keeps growing, and quantum computing could solve problems "
            "ordinary computers can't, which may one day break today's encryption.\n\n"
            "Internet of Things: billions of connected sensors and devices in factories, cities and homes. Edge "
            "computing processes their data close to where it's collected, cutting network load and delay.\n\n"
            "Artificial intelligence: machine learning finds patterns in data; generative AI creates text, images "
            "and code.\n\n"
            "Extended reality: augmented and virtual reality for training, design and remote support.",
            "An engineer wearing AR glasses sees repair instructions overlaid on a faulty server, while an expert "
            "watches remotely and guides them.",
            [("What is edge computing?", "Processing data close to where it's collected rather than centrally."),
             ("Why might quantum computing worry security experts?", "It could break current encryption."),
             ("What does generative AI do?", "Creates new content such as text, images or code.")]),
        "Emerging technologies (2)": E(
            "Open source software can be used and changed freely, with community support, which cuts licence costs.\n\n"
            "Blockchain is a shared ledger that's very hard to tamper with, used for cryptocurrency and supply-chain tracking.\n\n"
            "3D printing and drones create new ways to make and deliver things. Autonomous machines such as "
            "self-driving vehicles and robotic assembly lines replace human control.\n\n"
            "All of this has an environmental cost: devices use rare metals, data centres use huge amounts of "
            "energy, and old kit must be disposed of responsibly.\n\n"
            "These technologies often work together, which multiplies their impact.",
            "A warehouse uses IoT tags, AI to plan routes, autonomous robots to pick items and drones for stock "
            "checks: four technologies working together.",
            [("What is open source software?", "Software that can be used and changed freely."),
             ("Give one environmental impact of technology.", "E.g. rare metal use, energy use, disposal."),
             ("What makes blockchain useful?", "It is very hard to tamper with.")]),
    },
    "core/14-hardware-and-software.pptx": {
        "Types of computer": E(
            "Computers come in four broad types, each designed for different jobs.\n\n"
            "Personal computers (desktops and laptops) are general purpose machines for one user at a time.\n\n"
            "Mobile devices (phones and tablets) prioritise battery life, portability and touch input.\n\n"
            "Servers provide services, such as files, email or websites, to many users at once. They're built for "
            "reliability, often with redundant power supplies and drives, and run all the time.\n\n"
            "Embedded devices are computers built into other products, such as washing machines, cars and routers, "
            "and do one dedicated job.",
            "A smart thermostat is an embedded device; it sends data to a server in a data centre; you control it "
            "from a mobile app.",
            [("Which type of computer serves many users at once?", "A server."),
             ("What is an embedded device?", "A computer built into another product to do a dedicated job."),
             ("What do mobile devices prioritise?", "Battery life and portability.")]),
        "Hardware components": E(
            "The processor (CPU) runs instructions. More cores let it do several things at once; a higher clock "
            "speed does each faster; cache is small, very fast memory that keeps data close to hand.\n\n"
            "RAM is main memory: fast, holding programs and data in use, but volatile, so it's lost when power is "
            "off. ROM holds the start-up instructions and isn't lost.\n\n"
            "The motherboard connects everything. A GPU handles graphics and parallel work. Network interfaces "
            "connect via PCI slots or USB. Cooling, by air or liquid, stops components overheating. Input and "
            "output devices and sensors connect the computer to the world.",
            "A PC that slows down when many browser tabs are open is usually short of RAM; one that struggles "
            "rendering video needs a faster CPU or GPU.",
            [("What does volatile mean for RAM?", "Its contents are lost when the power is off."),
             ("What is cache?", "Small, very fast memory close to the processor."),
             ("What does a GPU do?", "Handles graphics and parallel processing.")]),
        "Secondary storage": E(
            "Secondary storage keeps data when the power is off.\n\n"
            "Magnetic hard disks are cheap per gigabyte but slow and fragile. Solid state drives are fast and "
            "robust but cost more. Optical discs are cheap and portable but hold little.\n\n"
            "RAID combines disks for speed or safety. RAID 1 mirrors data onto two disks. RAID 5 stripes data with "
            "parity across three or more disks, surviving one failure. RAID 10 mirrors and stripes, giving speed "
            "and resilience with four or more disks.\n\n"
            "NAS is a storage box on the network serving files. A SAN is a dedicated high-speed network of block "
            "storage for servers.",
            "A small office puts a NAS with two mirrored drives (RAID 1) on the network: if one drive fails, "
            "nobody loses their files.",
            [("What does RAID 1 do?", "Mirrors data onto two disks."),
             ("How many disk failures can RAID 5 survive?", "One."),
             ("What is the difference between NAS and SAN?", "NAS is a file server box on the network; a SAN is a dedicated high-speed storage network.")]),
        "Operating system types": E(
            "The operating system manages the hardware and runs programs. Different types suit different jobs.\n\n"
            "Batch systems run large jobs without user interaction, often overnight, such as payroll.\n\n"
            "Multitasking systems appear to run many programs at once by rapidly switching between them "
            "(time-slicing) and responding to interrupts. Desktop OSs work this way.\n\n"
            "Real-time systems respond instantly and predictably, for control and transactions such as traffic "
            "lights and card payments.\n\n"
            "Network OSs share resources and manage users across a network. Mobile OSs are designed for low power "
            "use and long battery life.",
            "An airbag controller must react within milliseconds, so it uses a real-time OS. A bank's overnight "
            "interest calculation is a batch job.",
            [("Which OS type runs large jobs without user interaction?", "Batch."),
             ("What is time-slicing?", "Rapidly switching the CPU between tasks so they appear to run at once."),
             ("Which OS type would control traffic lights?", "Real-time.")]),
        "Utility and application software": E(
            "Utility software looks after the computer itself. File managers organise files; defragmenters "
            "reorganise magnetic disks so files load faster; compression tools shrink files; package managers "
            "install and update software; protection software defends against malware; backup software copies "
            "data so it can be recovered.\n\n"
            "Application software lets users do their jobs: word processors, spreadsheets, databases, email and "
            "project management tools.\n\n"
            "Support technicians install, configure and troubleshoot both kinds.",
            "On Linux, a technician uses the apt package manager (a utility) to install LibreOffice (an application "
            "suite) on 30 PCs.",
            [("Is backup software a utility or an application?", "A utility."),
             ("What does a package manager do?", "Installs and updates software."),
             ("Why don't SSDs need defragmenting?", "They have no moving parts, so file layout doesn't slow access.")]),
    },
    "core/15-networks.pptx": {
        "Why network, and at what scale?": E(
            "Networking devices lets them share files, printers and internet access, and lets IT staff manage and "
            "back up everything centrally. The downsides are the cost of equipment and expertise, and that malware "
            "and faults can spread between devices.\n\n"
            "Networks are described by their size. A PAN (personal area network) links devices around one person, "
            "such as Bluetooth headphones. A LAN covers one building or site. A MAN covers a town or city. A WAN "
            "covers countries; the internet is the largest WAN.",
            "Your phone and smartwatch form a PAN; your school's network is a LAN; a university linking campuses "
            "across a city uses a MAN.",
            [("What does LAN stand for?", "Local area network."),
             ("Give one drawback of networking.", "E.g. equipment cost, malware can spread."),
             ("What is the largest WAN?", "The internet.")]),
        "Topologies and models": E(
            "A topology is the layout of a network. In a star, every device connects to a central switch, so one "
            "cable fault only affects one device; it's the standard in offices. A mesh connects devices to many "
            "others, so traffic can reroute around failures, but it's expensive. A tree links several stars in a "
            "hierarchy.\n\n"
            "The physical topology is how cables are laid out; the logical topology is how data actually flows.\n\n"
            "In a client-server model, servers provide services to clients. Thin clients rely on the server to do "
            "the processing. In peer-to-peer, every device is equal and shares resources directly.",
            "An office uses a star topology: every PC plugs into a switch in the comms cabinet, and the file server "
            "provides shared drives to clients.",
            [("Why is star topology popular?", "One cable fault only affects one device, and it's easy to manage."),
             ("What is a thin client?", "A device that relies on a server for processing."),
             ("What is the difference between physical and logical topology?", "Physical is the cable layout; logical is how data flows.")]),
        "The OSI and TCP/IP models": E(
            "Layered models split networking into jobs, so each layer can be designed and troubleshot separately.\n\n"
            "The OSI model has seven layers. From the top: application (services for programs), presentation "
            "(formatting and encryption), session (managing conversations), transport (reliable delivery and "
            "ports), network (logical addressing and routing), data link (frames and MAC addresses) and physical "
            "(cables and signals).\n\n"
            "The TCP/IP model used on the internet has four: application, transport, internet and network.\n\n"
            "When troubleshooting, work up from the physical layer.",
            "Can't reach a website: is the cable plugged in (physical)? Is there an IP address (network)? Does DNS "
            "resolve the name (application)?",
            [("How many layers does the OSI model have?", "Seven."),
             ("Which OSI layer handles routing?", "Layer 3, the network layer."),
             ("Which TCP/IP layer matches OSI's network layer?", "The internet layer.")]),
        "Data packets": E(
            "Data sent across a network is split into packets.\n\n"
            "Each packet has a header (source and destination addresses, packet number and protocol), a payload "
            "(the actual data) and a trailer with error-checking data.\n\n"
            "In packet switching, packets can take different routes and are reassembled in order using their numbers.\n\n"
            "Packets can be lost through congestion, faulty hardware or interference. A cyclic redundancy check "
            "(CRC) lets the receiver spot a damaged packet and ask for it again.\n\n"
            "Bandwidth is how much data can flow; latency is the delay.",
            "A 5 MB photo is split into thousands of packets. Some travel via London and some via Manchester, but "
            "your device reassembles them in order.",
            [("What does a packet header contain?", "Source and destination addresses, packet number and protocol."),
             ("What is a CRC used for?", "Detecting damaged packets."),
             ("How are packets put back in order?", "Using their packet numbers.")]),
        "Common protocols": E(
            "Protocols are agreed rules for communication.\n\n"
            "HTTP transfers web pages; HTTPS does the same but encrypted. SMTP sends email; POP downloads it to one "
            "device; IMAP keeps it on the server so it syncs across devices.\n\n"
            "RIP and OSPF are routing protocols that let routers share routes.\n\n"
            "FTP transfers files; SFTP does so securely. DHCP automatically gives devices an IP address. DNS turns "
            "names like bbc.co.uk into IP addresses.",
            "Opening a web page uses DHCP (to get an address), DNS (to find the server), and HTTPS (to fetch the "
            "page securely).",
            [("Which protocol gives devices IP addresses?", "DHCP."),
             ("What is the difference between POP and IMAP?", "POP downloads mail to one device; IMAP keeps it on the server and syncs."),
             ("Which protocol encrypts web traffic?", "HTTPS.")]),
    },
    "core/16-virtual-cloud-and-resilient-environments.pptx": {
        "Virtual environments": E(
            "Virtualisation runs several virtual machines (VMs) on one physical computer, each behaving like a "
            "separate PC, server, switch or router.\n\n"
            "A hypervisor manages them. A Type 1 hypervisor runs directly on the hardware and is used in data "
            "centres. A Type 2 runs on top of a normal OS, like VirtualBox on a laptop.\n\n"
            "VMs are isolated, portable and easy to copy, so they're cost-effective at scale, easy to manage, and "
            "great for disaster recovery, testing and training.\n\n"
            "The downsides: they put extra load on the hardware, run a little slower, and performance figures can "
            "be misleading.",
            "A college runs 40 student VMs on two physical servers. If a student breaks theirs, the technician "
            "restores it from a snapshot in minutes.",
            [("What does a hypervisor do?", "Creates and manages virtual machines."),
             ("Where does a Type 1 hypervisor run?", "Directly on the hardware."),
             ("Give one benefit of virtualisation.", "E.g. lower cost at scale, easy recovery, safe testing.")]),
        "Cloud delivery models: who manages what?": E(
            "Cloud computing rents computing resources over the internet. It can be public (shared provider "
            "infrastructure) or private (dedicated to one organisation). Its benefits are portability, elasticity "
            "(scaling up and down), fewer storage limits and cost.\n\n"
            "The three delivery models differ in who manages what.\n\n"
            "IaaS (Infrastructure as a Service): the provider supplies virtual hardware; you manage the OS and "
            "everything above it.\n\n"
            "PaaS (Platform as a Service): the provider also manages the OS and runtime; you manage your applications and data.\n\n"
            "SaaS (Software as a Service): the provider runs everything; you just manage users and data.",
            "Renting virtual servers on AWS is IaaS; deploying code to a managed app platform is PaaS; using "
            "Microsoft 365 is SaaS.",
            [("In SaaS, what does the client manage?", "User accounts and data."),
             ("Which model gives the client the most control?", "IaaS."),
             ("What is elasticity?", "Scaling resources up and down as demand changes.")]),
        "Making environments resilient": E(
            "A resilient environment keeps working, or recovers quickly, when something goes wrong. It improves "
            "security, protects reputation and reduces downtime.\n\n"
            "Methods include: applying software updates and patches; replacing hardware on a rolling plan and "
            "disposing of old kit securely; building in redundancy so no single failure stops the service; "
            "hardening devices by removing unneeded ports, apps and permissions; backing up onsite, offsite and to "
            "the cloud with tested recovery procedures; and standard operating procedures with training so staff "
            "handle incidents consistently.",
            "A shop's card system uses two internet connections and a backup router. When the main line fails, "
            "sales continue on the backup.",
            [("What is redundancy?", "Duplicate components so one failure doesn't stop the service."),
             ("What is device hardening?", "Removing unneeded ports, apps and permissions."),
             ("Why keep a backup offsite?", "So it survives a fire, flood or theft at the main site.")]),
        "Hot, warm and cold sites": E(
            "If the main site is lost, organisations can move to a backup site. There are three types.\n\n"
            "A hot site is fully equipped with up-to-date data, ready within minutes or hours. It's the most expensive.\n\n"
            "A warm site has equipment in place but data must be restored first, taking hours to days.\n\n"
            "A cold site is just space, power and connectivity, taking days or weeks to set up, but it's cheap.\n\n"
            "The choice depends on how long the business can survive without its systems.",
            "A bank needs a hot site because minutes of downtime cost millions. A small charity might accept a cold "
            "site or rely on cloud services.",
            [("Which site type is fastest to switch to?", "A hot site."),
             ("What does a warm site need before use?", "Data restored from backups."),
             ("Why would a business choose a cold site?", "It's the cheapest option if longer downtime is acceptable.")]),
    },
    "core/17-security-threats-and-vulnerabilities.pptx": {
        "Why confidentiality matters": E(
            "Organisations hold a lot of confidential information: HR data such as salaries and personal details; "
            "commercially sensitive data such as client lists, intellectual property, sales figures and contracts; "
            "and access information such as passwords, PINs and biometric data.\n\n"
            "Keeping it confidential protects people's privacy, protects intellectual property and client "
            "relationships, stops competitors poaching or undercutting, and prevents unauthorised access.\n\n"
            "If it leaks, the organisation faces regulatory penalties, loss of trust, reputational damage, fines and "
            "refunds, lost contracts, legal action and weaker security.",
            "A leaked price list lets a competitor undercut every quote. Leaked passwords let attackers into other systems.",
            [("Give an example of commercially sensitive data.", "E.g. client lists, sales figures, contracts, IP."),
             ("Why must access information be protected?", "It lets attackers into systems."),
             ("Name two consequences of a confidentiality breach.", "Any two: fines, lost trust, reputational damage, legal action, financial loss.")]),
        "Technical threats": E(
            "Technical threats attack systems directly.\n\n"
            "Malware includes viruses, worms, keyloggers, ransomware (encrypts files for a ransom), spyware and "
            "remote access trojans. Botnets are networks of infected devices used in DoS and DDoS attacks, which "
            "flood a service until it fails.\n\n"
            "Hackers use password cracking and brute force, SQL injection (tricking a database with crafted input), "
            "cross-site scripting and buffer overflows.\n\n"
            "Social engineering tricks people: phishing emails, spear phishing aimed at one person, smishing (texts), "
            "vishing (calls), pharming (fake websites), watering holes and USB baiting.\n\n"
            "DNS attacks and open Wi-Fi let attackers redirect or intercept traffic.",
            "An email 'from IT' asks staff to log in to a fake page to 'keep their mailbox'. That's phishing, and it "
            "steals passwords.",
            [("What does ransomware do?", "Encrypts files and demands payment."),
             ("What is spear phishing?", "Phishing aimed at a specific person or organisation."),
             ("What is a DDoS attack?", "Many devices flooding a service to make it unavailable.")]),
        "Human threats and responses": E(
            "People are often the weakest link, but also the best defence.\n\n"
            "Human error, such as deleting the wrong file, is reduced by confirmation boxes, file permissions and training.\n\n"
            "Malicious employees are dealt with by removing access immediately when they leave or are suspended.\n\n"
            "Disguised criminals posing as engineers or delivery drivers are stopped by ID checks and escorting visitors.\n\n"
            "Poor cyber hygiene, such as leaving PCs unlocked, writing passwords down or reusing them, is tackled "
            "with training, screen locks and password managers.",
            "A 'printer engineer' with no appointment asks to be let into the server room. Staff should check ID "
            "with the supplier and escort them.",
            [("How can human error be reduced?", "E.g. confirmation boxes, permissions, training."),
             ("What should happen to a leaver's accounts?", "They should be disabled immediately."),
             ("Give an example of poor cyber hygiene.", "E.g. leaving a PC unlocked, writing passwords down.")]),
        "Vulnerabilities": E(
            "A vulnerability is a weakness a threat can exploit.\n\n"
            "Technical vulnerabilities include weak encryption, a poor password policy, no multi-factor "
            "authentication, and out-of-date hardware, software and firmware. Old systems may no longer get "
            "security updates, and zero-day bugs are flaws attackers find before a patch exists.\n\n"
            "Physical vulnerabilities include poor access control (weak locks, shared door codes, tailgating), the "
            "location itself (shoulder surfing, vandalism, flood risk), equipment that isn't rugged enough, and "
            "natural disasters.\n\n"
            "The results can be data loss or leaks, unauthorised access, corruption and disruption.",
            "An unpatched Windows server (technical) in an unlocked cupboard (physical) is two vulnerabilities waiting to be exploited.",
            [("What is a zero-day vulnerability?", "A flaw exploited before a patch exists."),
             ("What is tailgating?", "Following an authorised person through a secure door."),
             ("Why is out-of-date software a vulnerability?", "It may have known flaws that are no longer patched.")]),
    },
    "core/18-threat-mitigation-cia-and-iaaa.pptx": {
        "Threat mitigation techniques": E(
            "Mitigation means reducing the chance or impact of a threat. Layering several techniques gives defence in depth.\n\n"
            "Protect devices with security settings, anti-malware, device hardening and regular software, firmware "
            "and driver updates.\n\n"
            "Control access with user access policies, software access control, multi-factor authentication and "
            "password managers.\n\n"
            "Protect data with encryption (hashing, symmetric and asymmetric) and backups (full, incremental or "
            "differential), stored safely.\n\n"
            "Protect networks with intrusion detection, VPNs, air gaps and certified APIs. Vet and train staff, and "
            "test defences with port scanning and ethical penetration testing.",
            "A firm with MFA, patched laptops and offline backups shrugs off a phishing attack that steals one "
            "password: the attacker can't log in without the second factor.",
            [("What is multi-factor authentication?", "Using two or more types of proof to log in."),
             ("What is an air gap?", "Keeping a system physically disconnected from other networks."),
             ("Why test defences with penetration testing?", "To find weaknesses before attackers do.")]),
        "Internet security processes": E(
            "A firewall controls traffic between networks using rules. Rules can filter inbound and outbound "
            "traffic, by traffic type, by application, and by IP address.\n\n"
            "Network segregation splits a network so an attack in one part can't spread. It can be virtual (VLANs), "
            "physical (separate hardware) or offline (air-gapped).\n\n"
            "Network monitoring watches traffic for unusual activity, such as a PC suddenly sending huge amounts of data.\n\n"
            "Port scanning checks which ports are open, so unneeded ones can be closed before attackers find them.",
            "A school separates staff, student and CCTV networks with VLANs. A student's infected laptop can't reach "
            "the staff file server.",
            [("What is network segregation?", "Splitting a network so problems can't spread between parts."),
             ("Why scan your own ports?", "To find and close ports attackers could use."),
             ("Give two things firewall rules can filter by.", "Any two: direction, traffic type, application, IP address.")]),
        "The CIA triad": E(
            "The CIA triad is the three goals of information security.\n\n"
            "Confidentiality: only authorised people can access data. Achieved with access control and encryption.\n\n"
            "Integrity: data is accurate and hasn't been tampered with. Achieved with permissions, hashing and audit "
            "logs. Keeping data confidential helps protect its integrity.\n\n"
            "Availability: data and systems are there when needed. Achieved with backups, redundancy and protection "
            "against DoS attacks. Intact data is what makes availability useful.\n\n"
            "The three support each other; weakening one usually weakens the others.",
            "Ransomware hits all three: attackers can read files (confidentiality), encrypt them (integrity) and "
            "lock staff out (availability).",
            [("Which part of the triad does a DDoS attack target?", "Availability."),
             ("What does integrity mean?", "Data is accurate and hasn't been tampered with."),
             ("How is confidentiality usually protected?", "Access control and encryption.")]),
        "The IAAA model": E(
            "IAAA describes how a system controls who does what.\n\n"
            "Identification: the user claims an identity, using something they know (a username), have (a card) or "
            "are (a fingerprint).\n\n"
            "Authentication: the system checks the claim, using a password, passphrase, biometrics or multi-factor "
            "authentication.\n\n"
            "Authorisation: the system decides what that user may access, using role-based access or access control lists.\n\n"
            "Accountability: actions are recorded in audit logs so they can be traced back to the user. Shared "
            "accounts break accountability, because you can't tell who did what.",
            "Logging in to the school network: typing your username (identification), entering your password "
            "(authentication), seeing only your folders (authorisation), and your file changes being logged (accountability).",
            [("Which IAAA stage checks a claimed identity?", "Authentication."),
             ("Which stage decides what a user can access?", "Authorisation."),
             ("Why do shared accounts break accountability?", "Actions can't be traced to one person.")]),
    },
    "core/19-employer-set-project-overview.pptx": {
        "What is the ESP?": E(
            "The Employer Set Project is worth 40% of the core and 20% of the whole qualification.\n\n"
            "It's set and marked externally, and taken under supervised conditions. Instead of testing topics "
            "separately, it checks you can bring the six core skills together on one realistic project: solving "
            "problems, communicating, working with stakeholders, building artefacts, troubleshooting logically, and "
            "working securely.\n\n"
            "There are three pathways, depending on your specialism: Digital Infrastructure and Network Cabling, "
            "Cyber Security, and Digital Support Technician. Each task is also linked to English, maths and digital "
            "competencies.",
            "The specimen project was set in the financial sector: students planned, fixed and designed IT for a "
            "fictional finance company.",
            [("What percentage of the whole qualification is the ESP?", "20%."),
             ("How many pathways are there?", "Three."),
             ("Is the ESP marked by your teacher?", "No, it's externally set and marked.")]),
        "The same shape for every pathway": E(
            "Every pathway follows the same sequence of tasks.\n\n"
            "The pre-task isn't assessed: you research the industry context of the brief.\n\n"
            "Task 1: plan the project with a Gantt chart, a resource and cost plan, and a written rationale.\n\n"
            "Task 2: find and fix defects in a simulation (usually Cisco Packet Tracer) or support tickets, "
            "documenting your testing.\n\n"
            "Task 3: design a solution clear enough for a client to approve and a third party to build.\n\n"
            "Task 4a: develop the solution. Task 4b: evaluate it against the brief and suggest improvements.",
            "In Task 2 you might find a PC with the wrong default gateway: you'd record the ping test that failed, "
            "the fix, and the ping test that then worked.",
            [("What three things does Task 1 produce?", "A Gantt chart, a resource and cost plan, and a rationale."),
             ("Is the pre-task assessed?", "No."),
             ("What happens in Task 4b?", "A reflective evaluation against the brief.")]),
        "What Task 4a looks for": E(
            "In Task 4a you build your solution, and markers look for four qualities.\n\n"
            "Robustness: will it survive failures? Think redundancy, backups, fallback routes and uninterruptible "
            "power supplies.\n\n"
            "Security: anti-malware and firewall configuration, appropriate user roles and permissions, device "
            "hardening and air gaps where needed.\n\n"
            "Organisation: well-configured servers, sensible placement of devices, the right connection media and "
            "correct subnetting.\n\n"
            "User experience: suitable end-user devices, reliable connections and good access to the systems people need.",
            "A strong solution adds a second link between switches (robustness), separates guest Wi-Fi on its own "
            "VLAN (security) and uses a clear IP scheme (organisation).",
            [("Name the four qualities markers look for in Task 4a.", "Robustness, security, organisation, user experience."),
             ("Give an example of improving robustness.", "E.g. redundant links, backups, UPS."),
             ("How does subnetting help organisation?", "It divides the network logically and makes it easier to manage.")]),
    },
}
