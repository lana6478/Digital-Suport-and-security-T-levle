"""Explanations for the Digital Infrastructure specialism decks."""
from . import E

EXPLAIN = {
    "digital-infrastructure/01-network-design-addressing-and-transmission.pptx": {
        "Designing for resilience": E(
            "A resilient network keeps working when a part fails or demand spikes.\n\n"
            "High availability pairs a primary system with a secondary that takes over automatically if the primary fails.\n\n"
            "Clustering makes several servers act as one: if one fails the others carry on, and more can be added "
            "as demand grows.\n\n"
            "Load balancing spreads incoming traffic across several servers so none is overwhelmed.\n\n"
            "Segmentation splits the network, systems and data so a problem in one part stays there.\n\n"
            "Quality of Service (QoS) guarantees bandwidth for important traffic, such as voice calls.",
            "An online shop runs three web servers behind a load balancer. On Black Friday traffic is shared out, "
            "and when one server crashes customers don't notice.",
            [("What does a load balancer do?", "Spreads traffic across several servers."),
             ("What is high availability?", "A secondary system automatically taking over if the primary fails."),
             ("Why use QoS?", "To guarantee bandwidth for important traffic such as voice.")]),
        "Transmission media": E(
            "Data travels as electrical signals on copper, light pulses in fibre, or radio waves over wireless.\n\n"
            "Copper can pick up interference: electromagnetic interference from power cables and motors, static, "
            "and crosstalk between neighbouring pairs. BS EN 50174 sets how far data cabling must be kept from power "
            "cabling, or requires shielding.\n\n"
            "All media carry security risks: cables can be tapped and signals lost.\n\n"
            "Wireless has evolved through 802.11b, g and n, then Wi-Fi 5 (ac), Wi-Fi 6 and 6E (ax) and Wi-Fi 7 (be). "
            "Each generation adds speed and handles more devices at once.",
            "Running a data cable alongside a power cable in the same trunking causes intermittent errors; separating "
            "them or using shielded cable fixes it.",
            [("Name two sources of interference on copper.", "Any two: EMI, static, crosstalk."),
             ("Which standard covers segregating data and power cabling?", "BS EN 50174."),
             ("What is the IEEE name for Wi-Fi 6?", "802.11ax.")]),
        "IPv4 and IPv6": E(
            "IPv4 addresses are 32 bits, written as four decimal numbers such as 192.168.1.10. The subnet mask "
            "(such as 255.255.255.0, or /24) shows which part is the network and which part identifies the host.\n\n"
            "Subnetting splits one network into smaller ones, improving security and reducing broadcast traffic. The "
            "number of usable hosts is 2 to the power of the host bits, minus 2 (the network and broadcast addresses).\n\n"
            "IPv4 has run out of addresses, so IPv6 uses 128-bit addresses written in hexadecimal. Types include "
            "unicast (one device), multicast (a group) and anycast (the nearest of a group).",
            "192.168.10.0/26 leaves 6 host bits: 2 to the power 6 = 64, minus 2 = 62 usable addresses per subnet, "
            "giving four subnets from one /24.",
            [("How many bits in an IPv4 address?", "32."),
             ("How many usable hosts in a /24?", "254."),
             ("Why was IPv6 introduced?", "IPv4 addresses have run out.")]),
    },
    "digital-infrastructure/02-infrastructure-components-and-cabling.pptx": {
        "Network devices": E(
            "Each network device has a specific job.\n\n"
            "A firewall filters traffic; next-generation firewalls and UTM appliances add deeper inspection and "
            "extra services. A router forwards packets between networks. A switch connects devices within a LAN and "
            "sends each frame only to the right port. A hub, now rare, repeats everything to every port. A bridge "
            "joins two network segments.\n\n"
            "Wireless access points provide Wi-Fi and range extenders stretch it. A modem connects to the internet "
            "provider, and a media converter joins copper and fibre.",
            "A small office: modem to the ISP, then a firewall, a router, a switch for the wired PCs, and access "
            "points for Wi-Fi.",
            [("What does a switch do that a hub doesn't?", "Sends frames only to the correct port."),
             ("What does a router do?", "Forwards packets between networks."),
             ("What is a media converter for?", "Connecting copper to fibre.")]),
        "Storage": E(
            "Hard disk drives (HDD) are cheap per gigabyte; solid state drives (SSD) are much faster; removable "
            "media is portable.\n\n"
            "Network attached storage (NAS) is a file server box on the network. A storage area network (SAN) is a "
            "dedicated high-speed network of block storage for servers.\n\n"
            "Block storage offers raw blocks, ideal for databases. Object storage holds files with metadata, used "
            "for cloud storage.\n\n"
            "RAID 0 stripes data for speed, with no redundancy. RAID 1 mirrors data. RAID 5 stripes with parity "
            "across three or more disks and survives one failure. RAID 10 mirrors and stripes.",
            "A video editing team uses RAID 0 on scratch disks for speed, but keeps finished projects on a RAID 5 "
            "NAS that survives a drive failure.",
            [("Which RAID level has no redundancy?", "RAID 0."),
             ("What is object storage used for?", "Cloud storage of files with metadata."),
             ("What is the difference between NAS and SAN?", "NAS serves files over the network; a SAN is a dedicated block storage network.")]),
        "Making and testing a UTP cable": E(
            "Making a patch lead is a core practical skill.\n\n"
            "Decide what the cable is for and measure the length needed. Choose straight-through (the same standard "
            "at both ends, for connecting different devices such as a PC to a switch) or crossover (568A at one end, "
            "568B at the other).\n\n"
            "Strip the outer jacket, untwist and arrange the eight wires in the correct TIA/EIA-568 colour order, "
            "trim them evenly, push them fully into an 8P8C (RJ45) connector with the jacket inside, and crimp.\n\n"
            "Finally, test with a cable tester and check the wiremap against the standard.",
            "A lead fails the wiremap test with wires 3 and 6 swapped. The technician cuts off the connector, "
            "re-terminates it and retests: pass.",
            [("What is a straight-through cable?", "One with the same wiring standard at both ends."),
             ("What connector is used for Ethernet?", "8P8C (RJ45)."),
             ("What does a wiremap test check?", "That each wire is connected to the correct pin.")]),
    },
    "digital-infrastructure/03-servers-virtualisation-and-operating-systems.pptx": {
        "Server options": E(
            "There are four main ways to run server workloads.\n\n"
            "Physical servers give full access to hardware and full control, but are expensive to buy and run, "
            "harder to scale and need space.\n\n"
            "Self-hosted virtual servers run many VMs on your own hardware: good cost control and support for "
            "clustering, but a big upfront cost.\n\n"
            "Cloud-hosted virtual servers, on Azure or AWS, scale easily with built-in redundancy, but you pay "
            "ongoing subscriptions.\n\n"
            "Containers package just an application and what it needs. They're light and portable, but less secure "
            "if misconfigured and need expertise.",
            "A start-up with no server room runs its app in containers on a cloud platform, scaling up for busy "
            "periods and paying only for what it uses.",
            [("Give one disadvantage of physical servers.", "E.g. expensive, hard to scale, need space."),
             ("What is a container?", "A lightweight package holding an application and only what it needs."),
             ("Why might a business choose cloud-hosted servers?", "Easy scaling and built-in redundancy.")]),
        "Virtualisation concepts": E(
            "Virtualisation separates software from the physical hardware underneath.\n\n"
            "Partitioning creates many virtual resources from one physical resource, or one virtual resource from "
            "many. Isolation keeps each virtual machine separate, so a crash or infection in one doesn't affect the "
            "others. Encapsulation stores a whole VM as a set of files that can be copied, backed up or moved. "
            "Hardware independence means a VM runs on any host with a compatible hypervisor.\n\n"
            "Virtualisation can apply to networks, servers, desktops, operating systems and data.",
            "Because a VM is just files (encapsulation), a failing host's VMs can be moved to another host and "
            "restarted in minutes.",
            [("What is encapsulation in virtualisation?", "A whole VM stored as files that can be moved or copied."),
             ("What does isolation prevent?", "A problem in one VM affecting others."),
             ("Name two types of virtualisation.", "Any two: network, server, desktop, OS, data.")]),
    },
    "digital-infrastructure/04-network-services-remote-access-and-installation.pptx": {
        "Client-server network services": E(
            "Servers provide the services that make a network work.\n\n"
            "Active Directory Domain Services (AD DS) stores every user, device and group centrally, organised into "
            "organisational units (OUs). Group Policy applies settings to OUs through Group Policy Objects (GPOs).\n\n"
            "DHCP hands out IP addresses automatically. DNS turns names into IP addresses. LDAP is the protocol "
            "used to query the directory for authentication.\n\n"
            "File servers and DFS provide shared storage; print servers share printers; web, proxy and cache servers "
            "provide filtered internet access; mail, application and database servers run business systems.",
            "A new starter logs in: AD DS authenticates them, DHCP gives the PC an address, DNS finds the file "
            "server, and a GPO maps their drives.",
            [("What is an OU?", "An organisational unit grouping users and devices in Active Directory."),
             ("What does DHCP do?", "Assigns IP addresses automatically."),
             ("How is Group Policy applied?", "Through GPOs linked to OUs.")]),
        "Remote access methods": E(
            "Remote access lets staff and technicians use systems from elsewhere.\n\n"
            "A VPN creates an encrypted tunnel into the network, so remote users work as if they were in the office.\n\n"
            "RDP (Remote Desktop Protocol) shows a remote computer's desktop; the processing stays on that computer.\n\n"
            "Lights-out management (LOM) lets administrators control a server even when it's switched off or has "
            "crashed, through a separate management interface.\n\n"
            "SSH gives a secure encrypted connection between two hosts, usually for command-line administration.",
            "At 3am a server freezes. The admin uses LOM from home to power-cycle it, then SSH to check the logs.",
            [("What does a VPN create?", "An encrypted tunnel into the network."),
             ("Which method works even when a server is switched off?", "Lights-out management (LOM)."),
             ("What is SSH typically used for?", "Secure command-line administration.")]),
        "Install, configure, test, maintain": E(
            "Building a network follows the same cycle for every component.\n\n"
            "Install servers (physical or virtual), network devices, firewalls, load balancers and end-user devices.\n\n"
            "Configure them: operating systems, applications and services such as DNS and DHCP, choosing the "
            "correct ports and protocols, using scripts to automate repetitive tasks, and applying the backup policy.\n\n"
            "Test functionality and performance, and record the results.\n\n"
            "Maintain the network: monitor performance, keep logs, manage capacity so it doesn't run out, and "
            "automate routine jobs.",
            "A technician scripts the creation of 50 user accounts from a CSV file instead of making them one by one, "
            "then tests a sample can log in.",
            [("Why use scripting?", "To automate repetitive tasks quickly and consistently."),
             ("What is capacity management?", "Monitoring resources so they don't run out."),
             ("Why record test results?", "To prove it works and to drive improvements.")]),
    },
    "digital-infrastructure/05-health-safety-and-esd.pptx": {
        "Preventing electrostatic discharge": E(
            "Electrostatic discharge (ESD) is a sudden flow of static electricity, like the shock from a door handle. "
            "A discharge far too small to feel can destroy the tiny circuits in memory, processors and circuit boards.\n\n"
            "Damage isn't always obvious: a component may seem fine then fail weeks later.\n\n"
            "Reduce the risk by limiting movement while handling parts, checking temperature and humidity (static "
            "builds up more in dry air), wearing an anti-static wrist strap connected to earth, working on an "
            "anti-static mat, holding boards by their edges and keeping components in anti-static bags until needed.",
            "Upgrading RAM: power off and unplug, clip on the wrist strap, touch the case, then handle the module by "
            "its edges only.",
            [("Why is ESD damage hard to spot?", "Components can fail later rather than immediately."),
             ("Name two pieces of anti-static equipment.", "Any two: wrist strap, mat, anti-static bag."),
             ("How should circuit boards be held?", "By their edges.")]),
        "Health and safety legislation": E(
            "Infrastructure work is covered by several health and safety laws.\n\n"
            "The Health and Safety at Work etc. Act 1974 sets the employer's general duty of care, including PPE. The "
            "Manual Handling Operations Regulations 1992 cover lifting servers and network kit. The Display Screen "
            "Equipment Regulations cover workstation set-up and screen breaks.\n\n"
            "COSHH covers hazardous substances such as printer toner. The Control of Major Accident Hazards "
            "Regulations 2015 include earthing. The WEEE Directive 2013 covers disposing of old hardware responsibly.",
            "Replacing a UPS battery: manual handling (it's heavy), COSHH (battery acid) and WEEE (disposal) all apply.",
            [("Which regulations cover lifting heavy servers?", "The Manual Handling Operations Regulations 1992."),
             ("What does COSHH cover?", "Hazardous substances."),
             ("Which law covers disposing of old network kit?", "The WEEE Directive 2013.")]),
    },
    "digital-infrastructure/06-service-management-and-solution-lifecycle.pptx": {
        "ITSM and ITIL": E(
            "IT service management (ITSM) treats IT as a service delivered to customers, not just technology.\n\n"
            "Its principles: create value together with users, give a good customer experience, think about how a "
            "change affects the whole organisation, and work across departments.\n\n"
            "ITIL is the most widely used framework for ITSM. Its lifecycle runs from service strategy (aligning "
            "services with business goals) through service design, service transition (building and deploying with "
            "managed change) and service operation (running it day to day), to continual service improvement.",
            "Rather than just 'install a VPN', ITSM asks what remote staff actually need, designs the service, rolls "
            "it out with support, and measures satisfaction afterwards.",
            [("What does ITSM treat IT as?", "A service delivered to customers."),
             ("Name the ITIL lifecycle stages.", "Strategy, design, transition, operation, continual improvement."),
             ("Which ITIL stage involves managed change?", "Service transition.")]),
        "The solution lifecycle (SLC)": E(
            "The solution lifecycle takes an infrastructure solution from idea to retirement.\n\n"
            "Discover the requirements and check feasibility. Plan, design and develop the solution, prototyping and "
            "integrating it with existing systems. Test and quality-assure its function and performance. Try it in "
            "pre-production, such as a sandbox, and get sign-off. Deploy it, using a staged rollout for high-impact "
            "changes. Monitor and evaluate it. Eventually decommission it and migrate to its replacement.\n\n"
            "Every stage should be carried out safely and documented.",
            "A new Wi-Fi system is tested in one building (pre-production), rolled out floor by floor (staged "
            "deployment), then the old access points are decommissioned.",
            [("What happens in pre-production?", "Sandbox testing and sign-off."),
             ("Why stage a high-impact rollout?", "To limit the damage if something goes wrong."),
             ("What is the final stage?", "Decommission and migrate.")]),
        "DevOps": E(
            "DevOps brings development and operations teams together so changes can be built, tested and released "
            "quickly and reliably.\n\n"
            "Its principles include continuous integration and delivery (small changes merged and released "
            "frequently), microservices, infrastructure as code (servers and networks defined in scripts, so they can "
            "be rebuilt exactly), collaboration, automated testing, the ability to adapt and scale, and monitoring and "
            "logging.\n\n"
            "The benefits are faster delivery, higher productivity, smoother cross-team working, scalability and fewer errors.",
            "With infrastructure as code, a destroyed test environment is rebuilt identically in minutes by running a script.",
            [("What is infrastructure as code?", "Defining servers and networks in scripts so they can be rebuilt automatically."),
             ("What is continuous integration?", "Merging and testing small changes frequently."),
             ("Give two benefits of DevOps.", "Any two: faster delivery, productivity, collaboration, scalability, fewer errors.")]),
    },
}
