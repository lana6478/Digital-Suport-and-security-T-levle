"""Explanations for the Cyber Security specialism decks."""
from . import E

EXPLAIN = {
    "cyber-security/01-governance-itsm-and-frameworks.pptx": {
        "Why governance?": E(
            "Information security governance is how an organisation directs and controls its security.\n\n"
            "It investigates, controls, communicates and reports cyber risk. It sets up a security framework: "
            "defined roles such as data controller and data processor, policies such as data retention and deletion, "
            "and regular activities such as evaluating new systems before they're bought.\n\n"
            "It manages compliance with law and standards such as ISO 27001, data protection and Freedom of "
            "Information requests, and it aligns business priorities with reducing cyber threats.\n\n"
            "Without governance, controls exist but nobody owns them or checks them.",
            "Governance decides that the IT manager owns patching, that data is deleted after six years, and that "
            "the board sees a security report every quarter.",
            [("What is a data controller?", "The organisation or person who decides how and why personal data is processed."),
             ("Give one thing governance manages compliance with.", "E.g. ISO 27001, data protection law, FOI requests."),
             ("Why does governance need defined roles?", "So every control has an owner who is accountable.")]),
        "Six IT governance principles": E(
            "Six principles guide good IT governance.\n\n"
            "Responsibility: everyone knows their security role. Strategy: systems are secure by design and planned "
            "for future needs such as cloud. Acquisition: every purchase is evaluated for risk, benefit and cost, with "
            "transparent decisions.\n\n"
            "Performance: enough preventative and remedial capability to guarantee confidentiality, integrity and "
            "availability. Conformance: IT use follows mandatory law and regulation. Human behaviour: policies and "
            "decisions consider people, not just technology.",
            "Before buying a new cloud CRM, the acquisition principle means checking its security certifications, "
            "data location and exit costs, not just the price.",
            [("Which principle covers evaluating purchases?", "Acquisition."),
             ("What does 'secure by design' mean?", "Security is built in from the start, not added later."),
             ("Why does human behaviour matter in governance?", "People's actions affect security as much as technology.")]),
        "IT service management (ITSM) processes": E(
            "ITSM is how an organisation manages the end-to-end delivery of IT services to its users.\n\n"
            "Service request management handles and tracks requests and incidents, such as a user reporting a "
            "suspicious email. Knowledge management keeps documentation current, such as standard hardened builds. "
            "IT asset management tracks hardware, software and configuration in a configuration management database "
            "(CMDB). Problem and incident management finds root causes and coordinates responses. Change management "
            "makes sure changes, like a new firewall rule, are agreed and recorded.",
            "A suspected phishing email is logged as a request, handled by the incident process, the root cause "
            "fixed by problem management, and a new mail filter rule approved through change management.",
            [("What is a CMDB?", "A configuration management database tracking IT assets and configuration."),
             ("Which ITSM process would approve a new firewall rule?", "Change management."),
             ("What does knowledge management do?", "Keeps documentation and support knowledge current.")]),
        "The ITIL service lifecycle": E(
            "ITIL is a widely used framework of best practice for ITSM. Its lifecycle has five stages.\n\n"
            "Service strategy aligns IT services with business objectives. Service design designs services and "
            "everything supporting them: people, processes, products and partners. Service transition builds and "
            "deploys services with coordinated change management. Service operation runs them day to day, fulfilling "
            "requests and resolving failures. Continual service improvement makes them steadily more efficient and "
            "effective.",
            "Introducing a new VPN service: strategy (support remote working), design (capacity, security), "
            "transition (pilot then rollout), operation (helpdesk support), improvement (review connection drop-outs).",
            [("Name the five ITIL stages.", "Strategy, design, transition, operation, continual improvement."),
             ("Which stage builds and deploys services?", "Service transition."),
             ("Which stage handles day-to-day requests?", "Service operation.")]),
        "Frameworks and standards for an ISMS": E(
            "An information security management system (ISMS) is the set of policies and processes that keep an "
            "organisation secure and compliant, including an information security policy and an acceptable use policy.\n\n"
            "Frameworks guide it: COBIT for governing and managing IT, SOC 2 for assessing security, availability, "
            "integrity, confidentiality and privacy controls, and NIST for managing cyber risk.\n\n"
            "Standards can be certified: ISO 27001 for establishing and improving an ISMS, ISO/IEC 38500 for IT "
            "governance, Cyber Essentials and Cyber Essentials Plus, and PCI DSS for payment cards.",
            "A software company wins a government contract only after gaining Cyber Essentials Plus and ISO 27001 certification.",
            [("What is an ISMS?", "An information security management system."),
             ("Which standard certifies an ISMS?", "ISO 27001."),
             ("What is the difference between Cyber Essentials and Cyber Essentials Plus?", "Plus includes independent technical testing.")]),
    },
    "cyber-security/02-secure-design-and-layered-protection.pptx": {
        "Protection methods by layer": E(
            "Defence in depth protects every layer so one failure doesn't expose everything.\n\n"
            "Hardware: physical controls such as locked cages, CCTV and key-card doors, plus device hardening.\n\n"
            "Operating system: install patches, with a system snapshot to roll back a bad update, and harden the OS "
            "by removing unneeded accounts, functions, apps and ports.\n\n"
            "Network: segmentation to limit how far an attacker can move, monitoring, hardening and firewalls.\n\n"
            "Software: anti-malware, single sign-on, MFA, privileged access management, application firewalls, "
            "vulnerability scanning and strong password policies.\n\n"
            "Cloud: audit logs, access controls and MFA, including location checks.",
            "An attacker who phishes a password still faces MFA (software), can't reach servers from the guest "
            "VLAN (network), and triggers an alert in the cloud logs.",
            [("What is defence in depth?", "Layered security so one failure doesn't compromise everything."),
             ("Why take a snapshot before patching?", "To roll back if the patch causes problems."),
             ("What does network segmentation limit?", "How far an attacker can move (lateral movement).")]),
        "Five secure design aims": E(
            "The NCSC's secure design principles have five aims.\n\n"
            "Establish the context: adopt zero trust, understand the requirements, users, suppliers and where "
            "sensitive data lives.\n\n"
            "Make compromise difficult: reduce the attack surface, use proven solutions and audit everything.\n\n"
            "Make disruption difficult: build in resilience and scalability and plan for supplier failure.\n\n"
            "Make compromise detection easier: collect logs, keep monitoring separate from operational systems, and "
            "learn what normal looks like.\n\n"
            "Reduce the impact of compromise: segment networks, separate duties, anonymise data and make recovery simple.",
            "Keeping logs on a separate server means an attacker who wipes the web server can't also wipe the evidence.",
            [("What is zero trust?", "Never trusting a user or device by default, even inside the network."),
             ("Why keep monitoring separate from operational systems?", "So logs survive if operational systems are compromised."),
             ("How does anonymising data reduce impact?", "Stolen data can't identify people.")]),
        "Operating systems and investigation": E(
            "Investigators need to know where operating systems store evidence.\n\n"
            "Windows keeps configuration in the registry; Linux in configuration files; macOS in library and "
            "preference files. Logs record network traffic, logins and system events. The file system (NTFS, FAT32, "
            "exFAT, APFS or ext4, depending on the OS) records files and their timestamps. Running processes show "
            "what's happening right now, including any malware.\n\n"
            "OS functions also help security: zero trust, device management that requires signed drivers, and "
            "processor management that protects against side-channel attacks.",
            "An investigator checks the Windows registry's Run keys and finds an unknown program set to start at "
            "every login: likely malware persistence.",
            [("Where does Windows store configuration?", "In the registry."),
             ("Why look at running processes?", "They show what's active now, including malware."),
             ("Name a file system used by macOS.", "APFS.")]),
    },
    "cyber-security/03-security-controls-and-disaster-recovery.pptx": {
        "Why have a DRP?": E(
            "A disaster recovery plan is a formal document setting out how to respond to unplanned incidents such as "
            "natural disasters, power cuts and cyber attacks.\n\n"
            "It minimises the time to repair and the interruption to normal work, limits the damage and cost, and "
            "sets up alternative ways of operating in advance, so service can be restored quickly.\n\n"
            "Writing and testing the plan also reveals gaps, such as untrained staff or missing backups, before a "
            "real disaster exposes them.",
            "During a ransomware attack, the DRP says who's in charge, which systems come back first, where the "
            "clean backups are and how to tell customers.",
            [("Give two reasons a DRP is important.", "E.g. reduces downtime, limits damage and cost, prepares alternatives, reveals gaps."),
             ("Name three incidents a DRP covers.", "E.g. natural disasters, power cuts, cyber attacks."),
             ("How can a DRP reveal gaps?", "Writing and testing it shows missing training, backups or resources.")]),
        "Implementing a DRP": E(
            "Implementing a DRP follows seven steps.\n\n"
            "Define its scope: the whole organisation, a department or individuals. Gather information: past "
            "outages, inventories of hardware, software, networks and data, and contact details. Risk-assess each "
            "threat's likelihood and impact.\n\n"
            "Create the plan and the resources it needs: systems, staff roles and budget. Get it approved. Test it "
            "regularly: decide scope and frequency, run it, review and amend.\n\n"
            "Keep improving it through internal and external audits and gap analysis.",
            "A tabletop exercise walks managers through 'the server room has flooded'. It reveals nobody knows the "
            "backup encryption password, so the plan is amended.",
            [("What comes after creating the plan?", "Getting it approved (signed off)."),
             ("Why test a DRP?", "To prove it works and find gaps."),
             ("What is a tabletop exercise?", "A discussion-based walk-through of a disaster scenario.")]),
        "Three control types in cyber security": E(
            "Cyber security uses three main types of control, each physical, technical or procedural.\n\n"
            "Preventative controls stop unauthorised access or tampering: locks, barriers, guards and biometrics; "
            "firewalls, allow and deny lists, sandboxing and device hardening; separation of duties and RBAC.\n\n"
            "Corrective controls limit damage and stop recurrence: fire and gas suppression; patching, disconnecting "
            "and quarantining infected systems; standard procedures and invoking the DRP.\n\n"
            "Compensating controls back up a failed primary control: segregation of duties and access logs; "
            "encryption; training, simulated attacks and monitoring procedures.",
            "If a door lock fails (preventative), key-code logs and CCTV review (compensating) still show who entered.",
            [("Is quarantining a virus preventative or corrective?", "Corrective."),
             ("Give a technical compensating control.", "Encryption."),
             ("What are the three forms each control can take?", "Physical, technical, procedural.")]),
    },
    "cyber-security/04-cryptography-and-digital-certificates.pptx": {
        "What cryptography provides": E(
            "Cryptography secures and authenticates data. It provides four things.\n\n"
            "Confidentiality: only the intended recipient can decrypt and read the data.\n\n"
            "Integrity: any change to the data in transit can be detected, for example with an HMAC.\n\n"
            "Authenticity: the recipient can check who sent the data, using a digital signature made with the "
            "sender's private key.\n\n"
            "Non-repudiation: the sender can't later deny sending it, because only they hold the private key.\n\n"
            "When sending data, first identify which of the CIA properties it needs.",
            "A signed software update proves it came from the vendor (authenticity) and wasn't altered in transit (integrity).",
            [("What does non-repudiation mean?", "The sender can't deny sending the message."),
             ("What provides authenticity?", "A digital signature."),
             ("What detects changes to data in transit?", "An integrity check such as an HMAC.")]),
        "Encryption and hashing": E(
            "Encryption is reversible: with the right key, you get the original data back.\n\n"
            "Symmetric encryption uses one shared key. It's fast, so it's used for large data and data at rest, but "
            "the key must be shared securely.\n\n"
            "Asymmetric encryption uses a key pair: anyone can encrypt with the public key, but only the private key "
            "decrypts. It solves key sharing and underpins TLS and email encryption.\n\n"
            "Hashing is one way: it turns data into a fixed-length fingerprint that can't be reversed. Any change to "
            "the input changes the hash completely, which makes it ideal for storing passwords and checking integrity.",
            "When you log in, your password is hashed and compared with the stored hash. The site never needs to "
            "store your actual password.",
            [("Can a hash be reversed?", "No, hashing is one way."),
             ("Which encryption type uses one shared key?", "Symmetric."),
             ("Why are passwords hashed rather than encrypted?", "Hashes can't be reversed, so stolen hashes don't reveal passwords directly.")]),
        "Digital certificates": E(
            "A digital certificate proves that a public key really belongs to a particular server, device or user.\n\n"
            "It contains the holder's name, a unique serial number, an expiry date, the holder's public key and the "
            "digital signature of the Certificate Authority (CA) that issued it. Your device trusts the certificate "
            "because it trusts the CA.\n\n"
            "Server certificates let clients check a website is genuine. Client certificates let a device prove its "
            "identity to a server. Code signing certificates let an operating system check software's author and integrity.",
            "The padlock in your browser means the site's certificate was signed by a trusted CA and matches the "
            "domain. It doesn't mean the site itself is honest.",
            [("Who issues digital certificates?", "A Certificate Authority (CA)."),
             ("Name three things a certificate contains.", "Any three: holder name, serial number, expiry, public key, CA signature."),
             ("What does a code signing certificate prove?", "The software's author and that it hasn't been altered.")]),
        "Generating a certificate": E(
            "Getting a certificate follows four steps.\n\n"
            "First, generate a public and private key pair. The private key never leaves the server.\n\n"
            "Next, create a Certificate Signing Request (CSR) containing the public key and the identity details.\n\n"
            "Then a trusted Certificate Authority checks the details and issues a signed certificate.\n\n"
            "Finally, install the certificate on the server or client.\n\n"
            "Certificate management tools then monitor expiry dates, renew certificates automatically, revoke "
            "compromised ones early, and help diagnose certificate errors.",
            "A company's website suddenly shows security warnings because its certificate expired over the weekend: "
            "exactly what auto-renewal tools prevent.",
            [("What is a CSR?", "A Certificate Signing Request."),
             ("Should the private key be sent to the CA?", "No, it never leaves the server."),
             ("Why revoke a certificate early?", "If its private key has been compromised.")]),
    },
    "cyber-security/05-cyber-law-and-ethics.pptx": {
        "Legislation for cyber security (1)": E(
            "Several laws shape cyber security work.\n\n"
            "The Data Protection Act 2018 requires organisations to protect personal data, detect security events "
            "and minimise the impact of incidents.\n\n"
            "The Computer Misuse Act 1990 criminalises unauthorised access, access intended to enable further "
            "crimes, unauthorised modification of data, and making or supplying tools for these offences.\n\n"
            "The Investigatory Powers Act 2016 sets how law enforcement and security agencies can obtain communications data.\n\n"
            "The Human Rights Act 1998 protects rights such as privacy and binds public authorities.\n\n"
            "The Telecommunications (Security) Act 2021 requires network providers to prevent, fix and disclose security compromises.",
            "Selling a password-cracking tool to someone you know will use it illegally is itself an offence under the Computer Misuse Act.",
            [("Which Act covers supplying hacking tools?", "The Computer Misuse Act 1990."),
             ("Which Act governs how agencies obtain communications data?", "The Investigatory Powers Act 2016."),
             ("Who must follow the Telecommunications (Security) Act?", "Network and service providers.")]),
        "Legislation for cyber security (2)": E(
            "The Freedom of Information Act 2000 lets the public request information from public bodies, but exempts "
            "some security bodies, such as the NCSC.\n\n"
            "The Network and Information Systems (NIS) Regulations 2018 set a security baseline for operators of "
            "essential services, such as energy and water, and for relevant digital service providers.\n\n"
            "The Official Secrets Act 1989 protects security and intelligence information.\n\n"
            "The Wireless Telegraphy Act 2006 regulates wireless devices and makes it an offence to intercept other "
            "people's wireless communications without authority.",
            "Capturing traffic from a neighbour's Wi-Fi 'just to see' breaks the Wireless Telegraphy Act, as well as the Computer Misuse Act if you access it.",
            [("Which regulations cover operators of essential services?", "The NIS Regulations 2018."),
             ("Which Act makes intercepting wireless communications an offence?", "The Wireless Telegraphy Act 2006."),
             ("Is the NCSC covered by FOI requests?", "No, it is exempt.")]),
        "UK Cyber Security Council Code of Ethics": E(
            "Cyber security professionals have powerful skills and access, so ethics matter.\n\n"
            "The UK Cyber Security Council's code has four principles. Credibility: be accountable and act "
            "ethically. Integrity: be honest and obey the law. Professionalism: share knowledge, base your work on "
            "evidence, promote public understanding and correct misinformation. Responsibility and respect: take "
            "ownership of your work, safeguard data, declare conflicts of interest, and champion equality, diversity "
            "and inclusion.",
            "A tester who finds a serious flaw reports it through the agreed channel rather than posting it online "
            "for attention: integrity and responsibility.",
            [("Name the four principles.", "Credibility, integrity, professionalism, responsibility and respect."),
             ("Why declare a conflict of interest?", "So others can trust your judgement is unbiased."),
             ("What does professionalism include?", "Sharing knowledge, evidence-based practice, correcting misinformation.")]),
    },
    "cyber-security/06-threats-threat-actors-and-intelligence.pptx": {
        "Social engineering": E(
            "Social engineering attacks people rather than technology.\n\n"
            "Phishing sends mass fraudulent messages. Warning signs: spoofed or misspelt addresses, poor writing, "
            "unexpected attachments and urgency. Spear phishing targets one person using personal details, so it's "
            "harder to spot.\n\n"
            "Vishing uses phone calls, often impersonating HMRC or a bank. Smishing uses texts with suspicious links.\n\n"
            "Shoulder surfing is watching someone type a password. Dumpster diving is searching bins for "
            "information. The defence is awareness training, a culture of checking, and MFA.",
            "An email 'from the CEO' asks finance to urgently pay a new supplier. A quick phone call to the CEO's "
            "known number exposes the spear phishing attempt.",
            [("What is the difference between phishing and spear phishing?", "Phishing is mass; spear phishing targets a specific person."),
             ("What is vishing?", "Social engineering by phone call."),
             ("Give two warning signs of phishing.", "Any two: spoofed address, poor writing, urgency, unexpected attachments.")]),
        "Malware": E(
            "Malware is software designed to cause harm.\n\n"
            "A virus spreads and damages data or software. Adware shows unwanted ads and changes browser settings. "
            "Ransomware blocks, deletes or encrypts data until a ransom is paid. A trojan disguises itself as "
            "legitimate software. A botnet is a network of infected devices controlled by an attacker, often used for "
            "DDoS attacks. Spyware hides and steals data.\n\n"
            "Most malware is spotted through anti-malware scan reports, devices slowing down, or unusual behaviour "
            "such as unexpected network traffic.",
            "A free 'PDF converter' (trojan) installs a keylogger (spyware) that captures banking passwords.",
            [("What is a trojan?", "Malware disguised as legitimate software."),
             ("What is a botnet used for?", "E.g. DDoS attacks, controlled by an attacker."),
             ("Give one sign of malware infection.", "E.g. slow performance, unusual behaviour, scan alerts.")]),
        "Threat actors": E(
            "Threat actors have different motives, which shape how they attack.\n\n"
            "Cyber criminals want money, using ransomware, phishing and malware. Insiders are current or former "
            "staff who misuse access out of revenge or for gain. Nation states seek political or military advantage, "
            "stealing data or damaging infrastructure. Terrorist groups want disruption for their cause. Hacktivists "
            "attack to expose what they see as wrongdoing. Script kiddies are inexperienced attackers using others' tools.\n\n"
            "Threat intelligence gathers information about actors and their methods, helping organisations "
            "prioritise defences and respond faster.",
            "A school is most likely to face criminals (ransomware) and insiders (students or staff), not nation states.",
            [("What motivates cyber criminals?", "Financial gain."),
             ("What is an insider threat?", "Current or former staff misusing their access."),
             ("How does threat intelligence help?", "It reveals threats and motives so defences can be prioritised.")]),
        "Critical national infrastructure": E(
            "Critical national infrastructure (CNI) is the systems a country depends on, which makes it a prime "
            "target for nation states and terrorists.\n\n"
            "Attacks on energy can cause power cuts and surges; on water, loss of supply or treatment; on finance, "
            "failed payments; on healthcare, compromised records and delayed treatment; on communications, loss of "
            "service and eavesdropping; on transport, disrupted travel and emergency dispatch; on government and "
            "defence, weakened decision-making and capability. Supply chains for food and raw materials can also be hit.",
            "In 2017 the WannaCry ransomware disrupted parts of the NHS, cancelling thousands of appointments: a "
            "real example of a CNI impact.",
            [("What is CNI?", "The essential systems a country depends on, e.g. energy, water, healthcare."),
             ("Why is CNI a target for nation states?", "Disrupting it causes widespread harm."),
             ("Give one impact of an attack on healthcare.", "E.g. compromised patient records, delayed treatment.")]),
    },
    "cyber-security/07-vulnerability-assessment-and-penetration-testing.pptx": {
        "Vulnerability assessment stages": E(
            "A vulnerability assessment systematically finds and fixes weaknesses.\n\n"
            "Identify vulnerabilities using scans and log analysis. Analyse each one: is it exploitable, and how "
            "severe? Identify the associated risk and prioritise. Remediate by updating or removing the affected "
            "hardware or software. Mitigate what can't be fixed with countermeasures, closing items off and "
            "escalating anything still risky.\n\n"
            "Before starting, scope it: which systems are included, what access testers need and what they're testing "
            "for. Afterwards, evaluate the business impact of each finding and document the results.",
            "A scan finds an old FTP server with a known flaw. It isn't needed, so it's switched off (remediate) "
            "rather than patched.",
            [("What is the first stage?", "Identify vulnerabilities."),
             ("What is the difference between remediate and mitigate?", "Remediate removes the flaw; mitigate reduces its risk."),
             ("What does scoping define?", "Which systems, what access, and what is being tested.")]),
        "CVEs and CVSS": E(
            "CVE (Common Vulnerabilities and Exposures) is a public list of known vulnerabilities, each with a unique "
            "ID, published by vendors and security researchers.\n\n"
            "CVSS (Common Vulnerability Scoring System) scores each one from 0 to 10 based on its impact, how easy it "
            "is to exploit and its severity. 9 or above is critical.\n\n"
            "When a new CVE affects you, research it, check which of your systems are affected, find the "
            "recommended mitigation and apply it. CVSS helps prioritise, but your own context matters too.",
            "A CVSS 9.8 flaw in an internet-facing VPN server is fixed tonight; a CVSS 7 flaw on an isolated test "
            "PC can wait for the normal patch cycle.",
            [("What is a CVE?", "A publicly listed known vulnerability with a unique ID."),
             ("What range do CVSS scores use?", "0 to 10."),
             ("Why isn't CVSS the only factor in prioritising?", "Your own context, such as exposure and business impact, also matters.")]),
        "Scanning tools: strengths and weaknesses": E(
            "Different scanners find different problems.\n\n"
            "Infrastructure scanners check hosts, networks and wireless for missing patches, unsupported systems, "
            "weak passwords, exposed services and poor hardening.\n\n"
            "Web application scanners look for SQL injection, broken authentication, exposed data, weak access "
            "control, vulnerable components and unencrypted communication.\n\n"
            "Software scanners check for missing updates and vendor-specific issues.\n\n"
            "All share limits: they only find known issues, can give false positives and false negatives, use system "
            "resources, and don't stop an attack in progress.",
            "A scanner flags a 'critical' flaw that turns out not to apply to your configuration: a false positive, "
            "which is why results must be checked by a person.",
            [("What is a false positive?", "A reported problem that doesn't really exist."),
             ("Can scanners find brand-new (unknown) vulnerabilities?", "No, only known issues."),
             ("Name one thing a web application scanner looks for.", "E.g. SQL injection, broken authentication.")]),
        "Penetration testing stages": E(
            "A penetration test simulates a real attack, with permission, in six stages.\n\n"
            "Planning and scoping: agree rules of engagement, timing, and the legal and contractual boundaries. "
            "Reconnaissance: gather information about the target's network, OS and applications. Scanning: find "
            "open ports and services. Vulnerability assessment: identify and test weaknesses. Exploitation: attempt "
            "to gain access, within the agreed limits. Reporting: document findings and remediation advice.\n\n"
            "A proof of concept demonstrates that a vulnerability can really be exploited.",
            "A tester gains access to a web server via an outdated plugin, stops there as agreed, and the report "
            "recommends updating it and removing unused plugins.",
            [("What is agreed during planning and scoping?", "Rules of engagement, timing and legal boundaries."),
             ("What happens during reconnaissance?", "Gathering information about the target."),
             ("What is a proof of concept?", "Evidence that a vulnerability can really be exploited.")]),
    },
    "cyber-security/08-risk-analysis-and-risk-response.pptx": {
        "Measures of impact": E(
            "Five time-based measures describe a threat's impact.\n\n"
            "RTO (Recovery Time Objective): how quickly a system must be back to an acceptable state.\n\n"
            "RPO (Recovery Point Objective): how much data loss is tolerable, which sets backup frequency.\n\n"
            "MTBF (Mean Time Between Failures): how often an asset is likely to fail.\n\n"
            "MTTD (Mean Time To Detect): how long, on average, before a threat is noticed. Attackers can do a lot of "
            "damage while undetected, so a lower MTTD is better.\n\n"
            "MTTR (Mean Time To Repair): how long, on average, to restore a failed system.",
            "If an attacker sits unnoticed for 200 days (MTTD), they have months to steal data. Better monitoring cuts "
            "that to hours.",
            [("What does MTTD measure?", "The average time to detect a threat."),
             ("Which measure sets backup frequency?", "RPO."),
             ("Why is a low MTTD important?", "Less time for attackers to cause damage.")]),
        "Qualitative and quantitative analysis": E(
            "Qualitative analysis describes risk in words, such as a RAG (red, amber, green) rating. It's quick and "
            "easy to communicate. Tools include fault tree analysis, FMECA, CRAMM (scope, evaluate, recommend "
            "countermeasures) and FAIR.\n\n"
            "Quantitative analysis uses numbers. Single Loss Expectancy (SLE) is the cost of one incident. Annual "
            "Rate of Occurrence (ARO) is how many times a year it's expected. SLE multiplied by ARO gives Annual Loss "
            "Expectancy (ALE), the expected yearly cost. CVSS scores are also quantitative.\n\n"
            "Comparing ALE with the cost of a control shows whether the control is worth it.",
            "A laptop theft costs 1,200 pounds (SLE) and happens twice a year (ARO). ALE = 2,400 pounds, so spending "
            "600 pounds a year on locks and tracking is justified.",
            [("What is the formula for ALE?", "SLE x ARO."),
             ("Give one qualitative tool.", "E.g. RAG rating, fault tree analysis, FMECA, CRAMM, FAIR."),
             ("How does ALE help decide on a control?", "If the control costs less than the ALE it saves, it's worth it.")]),
        "Conducting a security risk assessment": E(
            "A security risk assessment follows six steps.\n\n"
            "Identify potential risks to the asset. Score each with a matrix: likelihood multiplied by severity "
            "gives a risk score and RAG rating. Weigh the value of the asset against the cost of mitigation. Control "
            "the risk with a proportionate response. Record the findings clearly. Review and test the controls "
            "regularly.\n\n"
            "Regular internal and external audits keep assessments current and should include third-party "
            "suppliers, who can be a route in for attackers.",
            "A network printer stores scanned documents. Risks: default admin password, unencrypted storage. "
            "Controls: change the password, enable encryption, put it on a separate VLAN.",
            [("How is a risk score calculated?", "Likelihood x severity."),
             ("Why weigh asset value against mitigation cost?", "So the response is proportionate."),
             ("Why include suppliers in audits?", "They can be a route in for attackers.")]),
        "Risk responses": E(
            "There are four ways to respond to a risk.\n\n"
            "Accept: no further mitigation is possible or worthwhile, or some residual risk remains after controls. "
            "The risk is documented and monitored.\n\n"
            "Transfer: pass the financial risk to another party, such as an insurer or a managed service provider.\n\n"
            "Avoid: change the project or system so the risk disappears.\n\n"
            "Mitigate: reduce the likelihood or severity with controls.\n\n"
            "Most risks are mitigated first, and whatever residual risk remains is accepted or transferred.",
            "An organisation mitigates ransomware with backups and MFA, transfers the remaining cost with insurance, "
            "and accepts the small residual risk.",
            [("What is residual risk?", "The risk that remains after controls are applied."),
             ("Outsourcing email security to a specialist is which response?", "Transfer."),
             ("Which response changes the project so the risk disappears?", "Avoid.")]),
    },
    "cyber-security/09-incident-management-and-forensics.pptx": {
        "Forensic compliance model": E(
            "Digital forensics gathers evidence from devices and networks that can stand up in court or an "
            "investigation. It follows five stages.\n\n"
            "Identification: what evidence exists, where it is and how it's stored. Preservation: isolate and secure "
            "it without changing it, in chronological order and within legal retention periods. Analysis: rebuild "
            "fragments of data and draw conclusions based only on the evidence. Documentation: record every finding "
            "and every step taken. Presentation: report to the right body, such as the police.\n\n"
            "If evidence is altered or its handling isn't recorded, it may be unusable.",
            "An investigator makes a bit-for-bit copy of a hard drive and works only on the copy, so the original "
            "evidence is never changed.",
            [("What is the second stage?", "Preservation."),
             ("Why work on a copy of the evidence?", "So the original isn't altered."),
             ("Why document every step?", "To prove the evidence is reliable and wasn't tampered with.")]),
        "Incident and event management": E(
            "Incident management gets from 'something's wrong' to 'resolved and learned from'.\n\n"
            "Identify the incident, through the service desk, phone, email, SMS or chat. Log it, manually or "
            "automatically. Manage it: raise a ticket, assign the right person and categorise it by business impact. "
            "Prioritise it, using SLAs and escalation, reporting crimes to the police and personal data breaches to "
            "the ICO (within 72 hours). Resolve it with a workaround or a permanent fix. Close it with an incident "
            "report. Document everything and store it in line with data protection law.",
            "A monitoring alert shows mass file changes at 2am. It's logged automatically, escalated as critical, "
            "the server isolated, backups restored, and the ICO informed.",
            [("Who must be told about a personal data breach?", "The ICO."),
             ("What is the difference between a workaround and a fix?", "A workaround is temporary; a fix is permanent."),
             ("How is an incident categorised?", "By its business impact.")]),
        "Escalating while preserving evidence": E(
            "When you find a security incident, what you do first can destroy or protect evidence.\n\n"
            "Record the date, time and a description of what you saw. Take appropriate action, usually isolating the "
            "device from the network to stop the spread. Preserve digital evidence, for example by copying the "
            "relevant log files before they're overwritten. Escalate to the right person or team.\n\n"
            "Isolating rather than switching off matters: memory holds valuable evidence, such as running processes "
            "and encryption keys, that is lost at power-off.",
            "Spotting ransomware on a PC, you unplug the network cable (not the power), note the time and the ransom "
            "message, and call the security team.",
            [("Why isolate a device rather than turn it off?", "Evidence in memory is lost when it's powered off."),
             ("What should you record first?", "The date, time and a description."),
             ("Why copy log files quickly?", "They may be overwritten or deleted.")]),
    },
    "cyber-security/10-mitigation-backups-and-compliance.pptx": {
        "Mitigating privacy-breach threats": E(
            "Most privacy breaches come from predictable sources, each with a matching control.\n\n"
            "Social engineering is tackled by raising awareness of current scams. Unmanaged personal devices are "
            "restricted by policy. Untrained staff get training and clear procedures. Insider threats are limited by "
            "access controls, monitoring for unusual activity and separating duties. Unpatched applications are "
            "kept updated. Third-party suppliers are checked with due diligence before being trusted with data. "
            "Improperly disposed devices are prevented by secure wiping and following DPA 2018.",
            "A firm checks its new payroll provider's security certifications and contract terms before sending it "
            "any staff data: third-party due diligence.",
            [("How are insider threats reduced?", "Access controls, monitoring and separation of duties."),
             ("What is due diligence on a supplier?", "Checking its security before trusting it with data."),
             ("How should old devices be disposed of?", "Securely wiped and disposed of in line with the law.")]),
        "Backup types": E(
            "Backups are the last line of defence against ransomware and failure.\n\n"
            "Full backups copy everything; incremental copy changes since the last backup; differential copy changes "
            "since the last full backup; a mirror is a live exact copy.\n\n"
            "Immutable backups can't be changed, overwritten or deleted for a set period, even by an administrator. "
            "Ransomware often tries to destroy backups first, so immutable or offline copies are essential.\n\n"
            "A backup strategy sets frequency, source, destination, storage medium and location, how long copies are "
            "kept, and regular test restores.",
            "Ransomware encrypts a company's server and its connected backup drive, but the immutable cloud backup "
            "survives, so the company recovers without paying.",
            [("What is an immutable backup?", "One that can't be changed, overwritten or deleted."),
             ("Why does ransomware target backups?", "So victims can't recover without paying."),
             ("Why test restores?", "To prove the backups actually work.")]),
        "Monitoring compliance": E(
            "Policies only protect an organisation if people follow them and they stay up to date.\n\n"
            "Compliance monitoring audits processes and policies, such as reviewing the information security policy "
            "each year, and improves them where needed.\n\n"
            "It compares and checks the accuracy of processes, logs and incident reports: do the logs show what the "
            "procedures say should happen?\n\n"
            "It also checks the organisation meets the ISO standards it claims, such as ISO 27001.",
            "An audit finds the policy says leavers' accounts are disabled within 24 hours, but logs show some took "
            "three weeks. The process is fixed and rechecked next quarter.",
            [("Why audit policies regularly?", "To keep them current and check they're followed."),
             ("What does comparing logs with procedures show?", "Whether what actually happens matches what should happen."),
             ("Name an ISO standard compliance might check.", "ISO 27001.")]),
    },
}
