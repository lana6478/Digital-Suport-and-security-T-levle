"""Explanations for the Network Cabling specialism decks."""
from . import E

EXPLAIN = {
    "network-cabling/01-signal-theory-and-data-transmission.pptx": {
        "Principles of data transmission": E(
            "Networks carry data as bits, grouped into bytes and packets.\n\n"
            "Transmission can be synchronous, with sender and receiver sharing a clock, or asynchronous, with start "
            "and stop bits marking each chunk. Links must detect and correct errors, cope with limited bandwidth and "
            "noise, and may compress data.\n\n"
            "When several devices share a medium, an access method decides who sends. CSMA/CD (wired) listens, sends, "
            "and backs off if a collision is detected. CSMA/CA (wireless) tries to avoid collisions before sending.\n\n"
            "The network interface card wraps data into frames, packets and datagrams with addresses and sequence numbers.",
            "On Wi-Fi, devices can't hear every collision, so they wait for a clear channel and a short random time "
            "before sending: that's CSMA/CA.",
            [("What does CSMA/CD do when a collision happens?", "Stops and retries after a random delay."),
             ("Which access method does Wi-Fi use?", "CSMA/CA."),
             ("What do sequence numbers do?", "Let data be reassembled in the right order.")]),
        "How fibre carries light": E(
            "Fibre optic cable has a glass core surrounded by cladding with a slightly different refractive index.\n\n"
            "Light entering the core at a shallow enough angle hits the boundary with the cladding and reflects back "
            "inside instead of escaping. This total internal reflection keeps the light bouncing along the core for "
            "kilometres.\n\n"
            "Single-mode fibre has a very narrow core, so light travels in essentially one path. It goes much further "
            "and is used for long links. Multi-mode fibre has a wider core carrying many light paths; they arrive at "
            "slightly different times, which limits distance, so it's used within buildings.",
            "A campus uses multi-mode (OM4) between floors of one building, and single-mode (OS2) for the 3 km link "
            "to another site.",
            [("What keeps light inside a fibre core?", "Total internal reflection."),
             ("Which fibre type suits long distances?", "Single-mode."),
             ("Why is multi-mode limited in distance?", "Different light paths arrive at slightly different times.")]),
        "Attenuation: losing signal over distance": E(
            "Attenuation is the loss of signal strength as it travels, measured in decibels (dB).\n\n"
            "In fibre, absorption happens when impurities in the glass soak up light, getting worse with distance. "
            "Scattering happens when light hits tiny particles and is lost into the cladding. Bending the cable too "
            "tightly, whether a large macrobend or tiny microbends from pressure, lets light escape.\n\n"
            "Poor handling adds more loss: dirty or damaged connectors can cause an unreliable link or no link at "
            "all, and poor-quality cable or connectors add interference. Always clean and inspect fibre ends before connecting.",
            "A new fibre link fails its loss test. An inspection scope shows a fingerprint on one connector; cleaning "
            "it brings the loss within limits.",
            [("What unit is attenuation measured in?", "Decibels (dB)."),
             ("Name two causes of attenuation in fibre.", "Any two: absorption, scattering, bending."),
             ("What should you do before connecting fibre?", "Clean and inspect the connectors.")]),
        "Ohm's law and copper cabling": E(
            "Ohm's law links voltage (V), current (I) and resistance (R): V = I x R.\n\n"
            "For a given voltage, more resistance means less current. In a cable, resistance increases with length, "
            "and effectively with signal frequency; thinner conductors also have higher resistance.\n\n"
            "As a copper cable gets longer, the signal weakens until the receiver can't read it reliably. That's why "
            "copper Ethernet has a limit: 90 m for the permanent link plus up to 10 m of patch leads, 100 m in total.",
            "12 V across 4 ohms gives 12 / 4 = 3 A. Double the resistance to 8 ohms and the current halves to 1.5 A.",
            [("State Ohm's law.", "V = I x R."),
             ("What happens to current if resistance increases?", "It decreases."),
             ("What is the maximum copper Ethernet channel length?", "100 m.")]),
    },
    "network-cabling/02-cable-media-connectors-and-standards.pptx": {
        "Copper and fibre": E(
            "Copper is durable, easy to handle, cheap to install and can carry power (PoE) to devices such as "
            "cameras and access points. It's used for telephony and short LAN runs of up to 90 m permanent link and "
            "100 m channel. Types include UTP, STP, FTP and coaxial.\n\n"
            "Fibre goes further, carries more data, is lighter and suffers less degradation, but its performance is "
            "limited by the quality of the lasers at each end. Single-mode (OS1 and OS2) is for long distances; "
            "multi-mode (OM3 and OM4) for shorter runs.\n\n"
            "Plenum-rated cable gives off less smoke and fewer toxic fumes in a fire and meets the Construction "
            "Products Regulation (CPR).",
            "A wireless access point on the ceiling is powered and connected by one Cat6 cable using PoE, so no "
            "power socket is needed.",
            [("What does PoE allow?", "Power to be carried over the data cable."),
             ("Which is better for a 2 km link, copper or fibre?", "Fibre."),
             ("Why use plenum-rated cable?", "It produces less smoke and toxic fumes in a fire.")]),
        "Connectors and transceivers": E(
            "Copper connectors include RJ-45 for Ethernet, RJ-11 for telephones, BNC and F-type for coaxial, and "
            "DB-9 and DB-25 for older serial connections.\n\n"
            "Fibre connectors include LC (small, common in switches), SC, ST, MT-RJ and MPO (many fibres at once). "
            "Choose by mating type, locking method (latching, screw or bayonet, and UPC or APC polish), durability and size.\n\n"
            "Transceivers such as SFP, SFP+, GBIC and QSFP plug into switches to convert electrical signals to light. "
            "Choose by simplex or duplex, speed, wavelength, connector type and whether it's compatible with the host.",
            "A switch uplink uses an SFP+ transceiver with LC connectors on OM4 multi-mode fibre for 10 Gbps.",
            [("Which fibre connector is small and common in switches?", "LC."),
             ("What does a transceiver do?", "Converts electrical signals to light and back."),
             ("Which copper connector is used for telephones?", "RJ-11.")]),
        "Termination points": E(
            "Cables end at termination points, where they're connected in a structured way.\n\n"
            "A 66 block is an older punch-down terminal for telephone systems, used with Cat3 cable.\n\n"
            "A 110 block supports higher speeds (Cat5 to Cat6a) and replaced the 66 block for structured cabling.\n\n"
            "A patch panel is a rack-mounted panel where incoming cables are punched down at the back. Short patch "
            "leads at the front connect ports to switches, so changes can be made without touching the permanent "
            "cabling. Patch panels handle large numbers of copper and fibre connections.",
            "Moving a desk to a new switch port is just a matter of moving one patch lead at the front of the panel: "
            "no re-cabling needed.",
            [("Which punch-down block supports Cat6?", "The 110 block."),
             ("What is a patch panel for?", "Terminating cables so connections can be changed with patch leads."),
             ("Which cable category is used with a 66 block?", "Cat3.")]),
        "Termination methods and standards": E(
            "Copper is terminated on patch panels or with RJ-45 plugs. Fibre is terminated by splicing: fusion "
            "splicing melts two fibres together for a permanent, low-loss joint, mainly single-mode; mechanical "
            "splicing aligns them in a clamp and is quicker but not permanent.\n\n"
            "The TIA/EIA-568A and 568B standards set the order of the eight wires. A straight-through cable uses the "
            "same standard at both ends; a crossover uses 568A at one end and 568B at the other.\n\n"
            "Ethernet standards, from 100BASE-T to 10GBASE-T, define the speed each cable supports.",
            "A new building is wired to 568B throughout, so every outlet and patch lead matches, making faults far "
            "easier to trace.",
            [("What is fusion splicing?", "Melting two fibres together to make a permanent joint."),
             ("What makes a crossover cable?", "568A at one end and 568B at the other."),
             ("Why use one wiring standard throughout a building?", "So everything matches and faults are easier to trace.")]),
    },
    "network-cabling/03-structured-cabling-design-and-installation.pptx": {
        "Tools and equipment": E(
            "Cabling installers need the right tool for each job, used safely and to the manufacturer's guidance.\n\n"
            "Testing tools include multimeters, tone generators and probes (to trace a cable), continuity testers, "
            "OTDRs (to find faults along fibre), light sources and power meters, and spectrum analysers.\n\n"
            "Terminating tools include crimpers, strippers, cutters, punch-down tools, fusion splicers, fibre "
            "cleaning kits and cleavers.\n\n"
            "Access equipment such as step ladders, low-level towers and MEWPs is needed for high work, along with "
            "cabinets, racks, trunking and containment.",
            "Finding which unlabelled cable runs to room 12: the tone generator is clipped on in the room and the "
            "probe traces it at the patch panel.",
            [("What is a tone generator and probe used for?", "Tracing a cable."),
             ("What does an OTDR do?", "Finds faults and losses along a fibre."),
             ("What is a MEWP?", "A mobile elevating work platform.")]),
        "Installing a networking device": E(
            "Installing a device such as a switch, firewall or access point follows a checklist.\n\n"
            "Find its location in the design specification. Check the equipment supplied matches the specification. "
            "Confirm it physically fits, with enough space, power and cooling. Mount it in the rack securely. Test "
            "that it works. Then configure it to the requirements.\n\n"
            "Skipping checks causes expensive problems, such as a switch that overheats in a cabinet without enough airflow.",
            "Before racking a new PoE switch, the installer checks the cabinet's power supply can handle the extra "
            "load from 24 cameras.",
            [("Name three physical things to check before racking a device.", "Space, power and cooling."),
             ("Where do you find where a device goes?", "In the design specification."),
             ("What comes after mounting?", "Testing that it works, then configuring it.")]),
        "The network design specification": E(
            "A network design specification tells the installer exactly what to build.\n\n"
            "It includes the customer's statement of requirements, a bill of materials listing every component and "
            "quantity, design documents (floor plans, power and cooling, containment and cable routes), installation "
            "admin such as labelling, certification and warranty, installation procedures, contractual penalties, "
            "and a plan for future growth.\n\n"
            "Design depends on the topology, the standards to meet, the permanent links and channels, and whether "
            "the network spans a campus.",
            "The bill of materials lists 48 Cat6a outlets, 2 x 24-port patch panels and 2,400 m of cable, calculated "
            "from the floor plans plus slack.",
            [("What is a bill of materials?", "A list of every component and quantity needed."),
             ("Why plan for future growth?", "So the network can expand without re-cabling."),
             ("What does the statement of requirements describe?", "What the customer needs.")]),
    },
    "network-cabling/04-testing-certification-and-troubleshooting.pptx": {
        "Common failures": E(
            "Cabling faults are either physical or technical.\n\n"
            "Physical faults include the wrong cable type, incorrect pin-out, open circuits (a broken wire), shorts, "
            "bad ports, bent pins, cable damage, duplex or speed mismatches and the wrong containment.\n\n"
            "Technical faults include attenuation, latency, jitter, crosstalk, electromagnetic interference, "
            "mismatched transceivers, transmit and receive fibres reversed, bottlenecks and hardware errors.\n\n"
            "They show up as CRC errors, lost frames and packets, address conflicts and missing sequence numbers. "
            "Status LEDs are often the first clue.",
            "A desk only connects at 100 Mbps instead of 1 Gbps. A test shows one pair broken: gigabit needs all four "
            "pairs, 100 Mbps only two.",
            [("What is an open circuit?", "A break in a wire so current can't flow."),
             ("What might cause CRC errors?", "E.g. interference, damaged cable, bad connectors."),
             ("Why might a link fall back to 100 Mbps?", "E.g. a broken pair, since gigabit needs all four pairs.")]),
        "Certifying copper and fibre": E(
            "Certification proves an installation meets its standard, which the warranty depends on.\n\n"
            "Follow a test plan setting out the scope, approach, resources and schedule. For copper, use a "
            "continuity tester, performance tester or cable certifier, checking the wiremap, cable length and "
            "near-end crosstalk (NEXT). For fibre, use an optical loss test set (light source and power meter), an "
            "OTDR and an inspection scope, running tier 1 (loss) and tier 2 (OTDR) tests.\n\n"
            "Compare the results with the manufacturer's tolerances and record everything.",
            "A cable certifier reports one link at 94 m: over the 90 m permanent link limit, so it fails and the "
            "outlet must be moved or the route shortened.",
            [("What does NEXT stand for?", "Near-end crosstalk."),
             ("What is a tier 1 fibre test?", "A loss test with a light source and power meter."),
             ("Why does certification matter to customers?", "It proves the installation meets the standard and supports the warranty.")]),
        "Why poor workmanship matters": E(
            "Cutting corners always costs more later.\n\n"
            "For the network, poor workmanship means slower speeds, more interference, harder maintenance, shorter "
            "cable life and weaker security. Bad or missing labelling makes every future fault-find and change slower.\n\n"
            "For the business, it means paying for revisits, penalties under the service level agreement and "
            "warranty, reputational damage, delayed payment and failed audits.\n\n"
            "Not testing every cable risks equipment damage, early failures, disruption and errors nobody notices.",
            "An installer skips testing to finish early. Three months later, intermittent faults on six desks mean "
            "a return visit, unpaid, and an unhappy client.",
            [("Why does labelling matter?", "It makes fault-finding and changes much faster."),
             ("Give two business consequences of poor workmanship.", "Any two: revisit costs, penalties, reputation, delayed payment, failed audits."),
             ("Why test every cable, not a sample?", "Untested faults cause failures and disruption later.")]),
    },
    "network-cabling/05-health-safety-and-compliance-for-cabling.pptx": {
        "Protecting supporting media": E(
            "Cabling jobs often happen around other services: telecoms, CCTV and security systems, alarms, AV, "
            "wireless access points and IoT devices.\n\n"
            "Protect them by checking local records before starting, labelling service cables, avoiding shared "
            "containment routes where possible and following change management so nothing is disconnected by surprise.\n\n"
            "Data cables must be segregated from electrical cables, following BS EN 50174, to prevent interference "
            "and for safety.",
            "An installer cuts what looks like a spare cable in a ceiling void: it's the fire alarm. Checking records "
            "and labels first would have prevented it.",
            [("Why check local records before starting?", "To find other services and avoid damaging them."),
             ("Which standard covers segregating data and power cables?", "BS EN 50174."),
             ("Give two examples of supporting media.", "Any two: telecoms, CCTV, alarms, AV, access points, IoT.")]),
        "If you suspect asbestos": E(
            "Asbestos was widely used in buildings until 1999. Disturbing it releases fibres that can cause fatal "
            "lung diseases decades later.\n\n"
            "If you suspect asbestos-containing material (ACM), stop work immediately. Tell the relevant people: your "
            "supervisor and the site manager. Isolate the area so nobody else enters. Have it investigated by an "
            "asbestos-registered professional. Then act on their findings: removal, sealing, or air-quality checks.\n\n"
            "Never drill, cut or sweep suspect material to 'check'. The Control of Asbestos Regulations 2012 apply.",
            "Lifting a ceiling tile in a 1970s school reveals crumbly grey board. The installer stops, leaves the "
            "tile, keeps people out and calls the supervisor.",
            [("What is the first thing to do if you suspect asbestos?", "Stop work immediately."),
             ("Who should investigate suspected asbestos?", "An asbestos-registered professional."),
             ("Why is disturbing asbestos dangerous?", "It releases fibres that can cause fatal lung disease.")]),
        "Working at height and in confined spaces": E(
            "Before working at height, risk-assess the job and choose the safest equipment. Mobile elevating work "
            "platforms (MEWPs) must be used by trained operators. Low-level access towers must be assembled, "
            "inspected, used and dismantled following the manufacturer's instructions. The Work at Height "
            "Regulations 2005 apply.\n\n"
            "Confined spaces, such as ceiling voids, ducts and underfloor areas, bring risks of poor air, heat and "
            "difficulty escaping. The same risk management process applies, with the right PPE, properly maintained, "
            "and a rescue plan. The Confined Spaces Regulations 1997 apply.\n\n"
            "Record your findings clearly.",
            "Running cable through a raised floor void: check the air, plan how to get out, keep a colleague outside, "
            "and wear knee pads and gloves.",
            [("Who may operate a MEWP?", "Trained operators."),
             ("Which regulations cover confined spaces?", "The Confined Spaces Regulations 1997."),
             ("Why is a rescue plan needed for confined spaces?", "Escape may be difficult if something goes wrong.")]),
    },
}
