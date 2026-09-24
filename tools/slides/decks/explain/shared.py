"""Explanations for the shared specialism decks."""
from . import E

EXPLAIN = {
    "shared/01-business-security-controls.pptx": {
        "When each control acts": E(
            "Business controls are measures that protect an organisation. They're grouped by when they act.\n\n"
            "Directive controls tell people what to do, such as policies and signs. Deterrent controls discourage an "
            "attempt, such as visible guards and alarms. Preventative controls stop an incident happening, such as "
            "locks and firewalls.\n\n"
            "Detective controls spot an incident while or after it happens, such as CCTV and logs. Corrective "
            "controls limit the damage and stop it recurring, such as fire suppression and restoring backups. "
            "Compensating controls step in when a main control fails or isn't available.\n\n"
            "Good security layers several types together.",
            "A server room: a 'Staff only' sign (directive), a visible camera (deterrent), a card lock "
            "(preventative), access logs (detective), gas fire suppression (corrective).",
            [("Which control type is CCTV footage reviewed after a break-in?", "Detective."),
             ("What does a corrective control do?", "Limits damage and stops the incident recurring."),
             ("When is a compensating control used?", "When a primary control fails or isn't available.")]),
        "Preventative controls": E(
            "Preventative controls stop incidents before they happen, and fall into four groups.\n\n"
            "Physical: anti-pick locks, fences, bollards, gates, cages, flood defences and air conditioning.\n\n"
            "Combined or managed access: card readers, biometric readers, video verification and PIN codes.\n\n"
            "Administrative: separation of duties and role-based access, so no one person has too much power.\n\n"
            "Technical: allowlists and denylists, access control lists, sandboxing untrusted software, device "
            "hardening and certificate authorities. Technicians put these in place by configuring domain policies, "
            "such as minimum password rules and group-based permissions.",
            "Separation of duties: the person who creates new supplier accounts can't also approve payments, so no "
            "single person can commit fraud unnoticed.",
            [("Give an example of a technical preventative control.", "E.g. allowlisting, access control lists, sandboxing, hardening."),
             ("What is separation of duties?", "Splitting tasks so no one person holds too much privilege."),
             ("Is a biometric door reader physical or managed access?", "Combined or managed access.")]),
        "NCSC Cyber Essentials: five controls": E(
            "Cyber Essentials is a government-backed scheme that protects against the most common attacks. It has "
            "five technical controls.\n\n"
            "Boundary firewalls and internet gateways control traffic in and out of the network.\n\n"
            "Secure configuration removes default passwords and unneeded software and turns on features such as MFA.\n\n"
            "Access control gives users only the access they need and limits admin accounts.\n\n"
            "Malware protection keeps anti-malware up to date or restricts which apps can run.\n\n"
            "Patch management applies security updates quickly, within 14 days for critical ones.",
            "Most attacks on small businesses exploit a default password, an unpatched system or a user with too "
            "many rights: exactly what these five controls close off.",
            [("Name the five Cyber Essentials controls.", "Firewalls, secure configuration, access control, malware protection, patch management."),
             ("What does secure configuration include?", "Removing defaults and unneeded software, enabling features like MFA."),
             ("Why limit admin accounts?", "Fewer accounts that attackers could use to take full control.")]),
        "Applying and monitoring controls": E(
            "Controls only work if they're chosen well and kept working.\n\n"
            "First, review the risk: gather information from systems (logs, alerts) and users (reports, interviews) "
            "to understand what could go wrong.\n\n"
            "Then select the right type or combination of controls, apply them following organisational procedure "
            "and the law, such as data protection requirements, and monitor them to check they keep working and "
            "adjust them when things change.\n\n"
            "This is a cycle, not a one-off job.",
            "Logs show repeated failed logins overnight. The technician adds account lockout (preventative) and an "
            "alert (detective), then checks the logs weekly.",
            [("What should you do before choosing a control?", "Review the risk by gathering information from systems and users."),
             ("Why monitor controls after applying them?", "To check they keep working and adjust when things change."),
             ("Give one source of information about a risk.", "E.g. logs, alerts, user reports.")]),
    },
    "shared/02-disaster-recovery-and-backup.pptx": {
        "DRP and BCP": E(
            "A business continuity plan (BCP) keeps the whole organisation running during a disruption: alternative "
            "premises, different ways of working, and letting staff work away from the main site.\n\n"
            "A disaster recovery plan (DRP) sits inside the BCP and focuses on IT: restoring systems and data after "
            "a disaster. It covers physical elements, such as backups and off-site server storage, and procedures, "
            "such as how to restore systems, keep data intact, track assets and report changes.\n\n"
            "The BCP asks 'how do we keep trading?'; the DRP asks 'how do we get IT back?'.",
            "After a flood, the BCP moves staff to work from home; the DRP restores the file server from the "
            "off-site backup onto cloud servers.",
            [("What is the difference between a BCP and a DRP?", "A BCP keeps the business running; a DRP restores IT systems."),
             ("Does the DRP sit inside the BCP or the other way round?", "The DRP sits inside the BCP."),
             ("Give one physical element of a DRP.", "E.g. backups or off-site server storage.")]),
        "Measures that size resilience": E(
            "Four measures help decide how resilient a system must be.\n\n"
            "Recovery Time Objective (RTO): the maximum time a system can be down before it seriously harms the business.\n\n"
            "Recovery Point Objective (RPO): the maximum amount of data, measured in time, the business can afford to "
            "lose. It sets how often backups must run.\n\n"
            "Mean Time Between Failures (MTBF): how long, on average, an asset runs before failing.\n\n"
            "Mean Time To Repair (MTTR): how long, on average, it takes to fix.\n\n"
            "Service level agreements (SLAs) turn these into promised uptime and response times.",
            "An online shop with an RPO of 1 hour must back up at least hourly. An RTO of 4 hours means it needs a "
            "restore plan that works in under 4 hours.",
            [("What does RPO decide?", "How often backups must run (maximum acceptable data loss)."),
             ("What does MTTR measure?", "The average time to repair a failed system."),
             ("What does an SLA define?", "Agreed uptime and response and resolution times.")]),
        "Backup types": E(
            "A full backup copies everything. It's simple to restore but slow and uses a lot of storage.\n\n"
            "An incremental backup copies only what changed since the last backup of any kind. It's fast and small, "
            "but a restore needs the last full backup plus every incremental since.\n\n"
            "A differential backup copies everything changed since the last full backup. It grows each day, but a "
            "restore needs only the full backup and the latest differential.\n\n"
            "A mirror is a live, exact copy. It's instant, but deleting a file deletes it in the mirror too.\n\n"
            "Choose frequency, source, destination and medium (tape, disk or cloud), and keep one copy off-site.",
            "Full backup on Sunday, incrementals Monday to Saturday. Thursday's crash needs Sunday's full plus "
            "Monday, Tuesday and Wednesday's incrementals.",
            [("Which backup type is quickest to make?", "Incremental."),
             ("What does a differential restore need?", "The last full backup and the latest differential."),
             ("Why isn't a mirror enough on its own?", "Deletions and corruption are copied too.")]),
    },
    "shared/03-risk-management-and-threat-assessment.pptx": {
        "The risk management process": E(
            "Risk management is a five-step cycle.\n\n"
            "Identify the risks, threats and vulnerabilities to systems and data.\n\n"
            "Assess probability: how likely is each one? High, medium or low.\n\n"
            "Assess impact: how much damage would it do, for example to the value of assets?\n\n"
            "Prioritise: rank risks by probability multiplied by impact, and give each an owner who is responsible for it.\n\n"
            "Mitigate: put controls in place to reduce the probability or the impact, starting with the highest "
            "priority. Then keep reviewing, because new risks appear all the time.",
            "Risk: a laptop with customer data is stolen. Probability medium, impact high, so priority high. Owner: IT "
            "manager. Mitigation: full disk encryption on all laptops.",
            [("Name the five steps.", "Identify, probability, impact, prioritise, mitigate."),
             ("How are risks prioritised?", "By probability multiplied by impact."),
             ("Why give each risk an owner?", "So someone is responsible for managing it.")]),
        "Analysing threats": E(
            "Threats can be analysed in words or in numbers.\n\n"
            "Qualitative analysis uses descriptions, most commonly a RAG rating: red means high risk and immediate "
            "action; amber means moderate risk, watched closely; green means low risk with no immediate action.\n\n"
            "Quantitative analysis puts numbers on risk, such as the cost or resources an incident would consume. "
            "Annualised Loss Expectancy (ALE) estimates how much a risk costs per year.\n\n"
            "Other tools include fault tree analysis, impact analysis, FMECA, CRAMM and SWOT. Results are recorded in a "
            "risk register with each risk's RAG rating.",
            "Two laptop thefts a year at 1,500 pounds each gives an ALE of 3,000 pounds a year: spending 500 pounds on "
            "cable locks is easily justified.",
            [("What does a red RAG rating mean?", "High risk needing immediate action."),
             ("What does ALE estimate?", "The expected cost of a risk per year."),
             ("Where are risks and their ratings recorded?", "In a risk register.")]),
        "Four risk responses": E(
            "Once a risk is understood, there are four ways to respond.\n\n"
            "Accept: the risk is small or too expensive to fix, so you live with it and monitor it.\n\n"
            "Avoid: change the plan so the risk no longer applies, for example by not storing card details at all.\n\n"
            "Mitigate: reduce the likelihood or impact with controls, the most common response.\n\n"
            "Transfer: pass the financial risk to another party through a contract, such as insurance or outsourcing "
            "to a specialist provider.\n\n"
            "A mitigation strategy weighs the response, the users, cost against benefit, who owns it and how to escalate.",
            "An online shop avoids card data risk by using a payment provider, mitigates phishing with training and "
            "MFA, and transfers breach costs with cyber insurance.",
            [("Buying cyber insurance is which response?", "Transfer."),
             ("When might you accept a risk?", "When it's small or too expensive to reduce."),
             ("What is avoiding a risk?", "Changing plans so the risk no longer applies.")]),
        "The penetration testing process": E(
            "A penetration test is an authorised, simulated attack to find weaknesses before real attackers do.\n\n"
            "It starts with customer engagement: agreeing the scope, rules and written permission. Testers then "
            "gather information about the target, discover and scan hosts and services, test for vulnerabilities, "
            "and carefully exploit some to prove the risk is real, within the agreed limits.\n\n"
            "Finally they analyse and report the findings, and the organisation acts on them.\n\n"
            "Without written permission, the same activities would break the Computer Misuse Act.",
            "A wireless pen test finds the guest Wi-Fi can reach the staff file server. The fix: separate the guest "
            "network onto its own VLAN.",
            [("What must be agreed before a pen test starts?", "Scope, rules and written permission."),
             ("Why exploit vulnerabilities during a test?", "To prove the risk is real."),
             ("Which law would unauthorised testing break?", "The Computer Misuse Act 1990.")]),
    },
    "shared/04-technical-security-and-network-protection.pptx": {
        "Technical security controls": E(
            "Technical controls are the settings and tools technicians apply to protect systems.\n\n"
            "Device hardening reduces the attack surface: remove unneeded programs, accounts and services, close "
            "unused ports and change default passwords.\n\n"
            "Remote monitoring and management (RMM) software lets technicians watch, patch and fix many devices from "
            "one console.\n\n"
            "Vulnerability scanning checks devices and ports for known weaknesses.\n\n"
            "Segmentation splits the network so an attack can't spread, and multi-factor authentication stops "
            "stolen passwords being enough on their own.",
            "Before handing over a new laptop: remove trial software, disable the guest account, apply updates, turn "
            "on the firewall and enrol it in RMM.",
            [("What is device hardening?", "Reducing the attack surface by removing unneeded software, accounts and ports."),
             ("What does RMM software let technicians do?", "Monitor, patch and fix many devices remotely."),
             ("Why segment a network?", "So an attack in one part can't spread.")]),
        "Encryption as risk mitigation": E(
            "Encryption scrambles data so only someone with the right key can read it.\n\n"
            "Symmetric encryption uses one shared key to encrypt and decrypt. It's fast, so it's used for large "
            "amounts of data and card payments.\n\n"
            "Asymmetric encryption uses a pair of keys: a public key to encrypt and a private key to decrypt. It's "
            "used for encrypted email and to set up secure connections.\n\n"
            "Data at rest is protected with full disk encryption, with keys stored in a Trusted Platform Module "
            "(TPM) chip or a Hardware Security Module (HSM). Data in transit is protected by TLS, which replaced SSL.",
            "A stolen laptop with full disk encryption is just a brick to the thief: without the key, the files are unreadable.",
            [("How many keys does asymmetric encryption use?", "Two: a public key and a private key."),
             ("What protects data in transit on the web?", "TLS."),
             ("What does a TPM store?", "Encryption keys specific to the device.")]),
        "Access control models": E(
            "Access control decides who can reach what.\n\n"
            "MAC (mandatory) uses security levels set centrally, like 'secret'. DAC (discretionary) lets the owner "
            "of a file decide who can use it. RBAC (role-based) grants access by job role. RuBAC (rule-based) uses "
            "rules such as time of day. ABAC (attribute-based) combines attributes of the user, resource and situation.\n\n"
            "Network tools enforce it: an IDS detects suspicious traffic and alerts; an IPS also blocks it; NAC checks "
            "devices meet policy before letting them join the network.\n\n"
            "All of this puts the CIA triad and IAAA into practice.",
            "In a hospital, RBAC gives all nurses access to patient records on their ward; RuBAC blocks remote "
            "access after 10pm.",
            [("What is the difference between an IDS and an IPS?", "An IDS detects and alerts; an IPS also blocks."),
             ("Which model grants access by job role?", "RBAC."),
             ("What does NAC do?", "Checks devices meet policy before they join the network.")]),
        "Securing network traffic": E(
            "Traffic can be protected physically and virtually.\n\n"
            "A DMZ (demilitarised zone) is a buffer network for public-facing servers, such as a web server, so "
            "attackers who breach it still can't reach the internal network. An air gap disconnects a system "
            "completely.\n\n"
            "VLANs split one physical network into separate virtual ones. VPNs and IPSec encrypt traffic between "
            "sites or remote users. VRF gives separate routing tables on one router, and subnets divide address ranges.\n\n"
            "Connected devices also need WPA2 or WPA3 Wi-Fi security, patching and MFA.",
            "A company puts its web server in a DMZ. When the site is hacked, the attacker is stuck there and can't "
            "reach the payroll server.",
            [("What is a DMZ for?", "Isolating public-facing servers from the internal network."),
             ("What does a VLAN do?", "Splits one physical network into separate virtual networks."),
             ("Which Wi-Fi security standards should be used?", "WPA2 or WPA3.")]),
        "Common vulnerabilities and their controls": E(
            "Most breaches exploit a short list of common weaknesses, each with a known fix.\n\n"
            "Missing patches: use patch management and test updates first. Weak or default passwords: enforce "
            "minimum rules and lockout. Insecure BIOS or UEFI: set a password and secure settings. Misconfigured "
            "permissions: audit them and remove leavers promptly. Missing protection software: install and monitor "
            "anti-malware.\n\n"
            "Insecure disposal: wipe data and follow WEEE. Poor backups: set the right frequency and test restores. "
            "Network attacks such as DHCP spoofing and VLAN hopping: use DHCP snooping and monitoring.",
            "An audit finds a leaver's account still active six months later: a misconfigured permissions "
            "vulnerability. The control: a leavers checklist and quarterly account audits.",
            [("How do you control weak passwords?", "Minimum password rules and account lockout."),
             ("Why test backups?", "To make sure they can actually be restored."),
             ("What must happen to old hard drives before disposal?", "Data must be securely wiped.")]),
    },
    "shared/05-security-law-standards-and-policy.pptx": {
        "Policies that reduce risk": E(
            "Policies turn good security into everyday rules.\n\n"
            "A digital use policy covers network and internet use and monitoring, bring your own device (BYOD), "
            "working from home (including a DSE assessment), password renewal and keeping software updated.\n\n"
            "A health and safety policy covers lone working, manual handling, working at height, fire safety and "
            "reporting incidents under RIDDOR 2013.\n\n"
            "A change procedure means every change is approved, documented and audited.\n\n"
            "You must be able to explain each policy's purpose and what could happen if it's ignored.",
            "Ignoring the BYOD policy by storing client files on a personal phone risks a data breach if the phone "
            "is lost: a privacy impact.",
            [("What does a BYOD policy cover?", "Using personal devices for work."),
             ("What is RIDDOR used for?", "Reporting injuries, diseases and dangerous occurrences."),
             ("Why have a change procedure?", "So changes are approved, documented and audited.")]),
        "Key legislation": E(
            "UK GDPR standardises how personal data is used, stored and transferred.\n\n"
            "The Data Protection Act 2018 is the UK's version: personal data must be used fairly, lawfully and "
            "transparently, for specified purposes, kept only as long as needed, kept accurate and kept secure. "
            "Individuals have rights to be informed, access, correct, erase and restrict their data, move it and "
            "object to its use.\n\n"
            "The Computer Misuse Act 1990 makes it a crime to access systems without permission, to do so intending "
            "further crimes, or to impair a computer's operation, for example with malware.",
            "A technician who restores a deleted customer file for a colleague who isn't entitled to see it breaks "
            "data protection law, even with good intentions.",
            [("Name three data protection principles.", "Any three: fair/lawful/transparent, specified purpose, minimised, accurate, not kept too long, secure."),
             ("Name two individual rights under DPA 2018.", "Any two: informed, access, rectify, erase, restrict, portability, object."),
             ("What are the three CMA offences?", "Unauthorised access; access with intent to commit further offences; unauthorised acts that impair a computer.")]),
        "Standards and best practice": E(
            "Standards give organisations a proven framework to follow.\n\n"
            "ISO 27001 is the international standard for an information security management system. Organisations "
            "can be certified against it, which reassures customers.\n\n"
            "PCI DSS protects card payments: a secure network, protected cardholder data, vulnerability management, "
            "strong access control, regular testing and a security policy.\n\n"
            "The NCSC's 10 Steps to Cyber Security is practical government guidance covering users, devices, "
            "networks and incident management.\n\n"
            "OWASP shares free tools and guidance on secure software.",
            "A shop taking card payments must follow PCI DSS; a cloud provider may get ISO 27001 certification to "
            "win contracts.",
            [("What is ISO 27001?", "A certifiable information security management standard."),
             ("Which standard applies to card payments?", "PCI DSS."),
             ("Who publishes the 10 Steps to Cyber Security?", "The NCSC.")]),
        "Why cyber security matters": E(
            "For organisations, cyber security protects systems, devices, cloud services, and personal and "
            "commercially sensitive data. It keeps them legally compliant and defends against cybercrime, which "
            "can cost money, customers and reputation.\n\n"
            "For society, protecting data preserves people's privacy, prevents prejudice and unfair treatment, "
            "supports equal opportunity and prevents identity theft.\n\n"
            "Data protection law gives individuals rights over their data. Good security is how organisations "
            "respect those rights in practice.",
            "When a retailer is breached, customers face phishing and identity theft, and the retailer faces fines "
            "and lost sales: both society and the organisation lose.",
            [("Give one reason cyber security matters to organisations.", "E.g. legal compliance, protecting data, defending against cybercrime."),
             ("How does cyber security protect society?", "E.g. privacy, preventing identity theft and prejudice."),
             ("Which law gives individuals rights over their data?", "The Data Protection Act 2018.")]),
    },
    "shared/06-sources-of-knowledge.pptx": {
        "Types of sources": E(
            "Technicians constantly look things up, so knowing where to look matters.\n\n"
            "Literature: textbooks, journals, manuals and supplier documentation. Detailed and usually accurate.\n\n"
            "Websites: wikis, forums such as Stack Overflow, and manufacturer sites. Fast and current, but of mixed quality.\n\n"
            "Media: social media, blogs, vlogs, podcasts and webinars. Good for tutorials and news.\n\n"
            "People: colleagues, managers, professional networks and conferences.\n\n"
            "Learning: MOOCs and vendor qualifications such as Cisco and CompTIA.\n\n"
            "Specialist sources: professional bodies, regulators such as the ICO, standards and databases such as CVE.",
            "Fixing a switch fault: check the manufacturer's manual first, then a vendor forum, then ask a colleague "
            "who has seen it before.",
            [("Name three types of source.", "Any three: literature, websites, media, people, e-learning, professional bodies."),
             ("Why start with manufacturer documentation?", "It's authoritative and specific to the product."),
             ("What is the CVE database?", "A public list of known vulnerabilities.")]),
        "Is the source reliable and valid?": E(
            "Not everything you read is true or up to date, so judge each source.\n\n"
            "Authority: is the author credible, qualified or linked to a recognised organisation? Evidence: does it "
            "cite its sources? Currency: is it recent enough, and does it match your software version? Relevance: "
            "does it fit your task, context and audience?\n\n"
            "Corroboration: do other independent sources agree? Bias: is opinion or self-interest shaping it?\n\n"
            "Industry accreditation, such as CCNA or CompTIA, suggests an author knows their subject.",
            "A 2015 forum post about Windows 7 is out of date for a Windows 11 fault, even if it was right at the time.",
            [("What does currency mean for a source?", "How recent it is and whether it matches the current version."),
             ("What is corroboration?", "Checking other independent sources agree."),
             ("Why might a vendor's own article be biased?", "It may promote its own products.")]),
        "Types of bias": E(
            "Bias is anything that makes a source, or your use of it, one-sided.\n\n"
            "Author or proprietary bias: the author's opinion or company interest shapes the content.\n\n"
            "Confirmation bias: you favour sources that agree with what you already think.\n\n"
            "Selection bias: sources are chosen to fit a conclusion decided in advance.\n\n"
            "Cultural bias: assumptions based on one society's norms.\n\n"
            "Availability bias (cyber security): judging by whatever is most recent or memorable.\n\n"
            "Signs of bias include partiality, prejudice and leaving things out. Reduce it by basing conclusions on "
            "evidence and deliberately looking at other views.",
            "After a big ransomware story, a manager wants all budget spent on ransomware, ignoring phishing, the "
            "bigger risk: availability bias.",
            [("What is confirmation bias?", "Favouring sources that agree with what you already think."),
             ("Give one sign of bias.", "E.g. partiality, prejudice, omission."),
             ("How can bias be reduced?", "Base conclusions on evidence and consider other views.")]),
        "Critical thinking process": E(
            "Critical thinking turns information into sound conclusions.\n\n"
            "Identify the relevant information: the arguments, views and opinions. Analyse it: spot bias, check how "
            "objective it is, and link the data together. Select suitable evaluation techniques and tools. Evaluate "
            "the findings and draw conclusions. Record them clearly.\n\n"
            "Techniques include formative evaluation (during a task) and summative (at the end), qualitative and "
            "quantitative methods, corroboration and triangulation. Tools include gap analysis, KPI analysis, "
            "scorecards, user diaries and maturity assessments.",
            "Deciding whether to upgrade to Wi-Fi 7: gather vendor claims, reviews and your own usage data, weigh "
            "bias, then compare current and needed performance with a gap analysis.",
            [("What is triangulation?", "Confirming a finding using three or more different sources or methods."),
             ("What does a gap analysis compare?", "The current state with the desired state."),
             ("What is the difference between formative and summative evaluation?", "Formative happens during a task; summative at the end.")]),
    },
}
