# Network Cabling - Installation and Testing

*Digital Support and Security T Level → Occupational Specialisms → Network Cabling → Installation and Testing*

This page covers Content Area 2 of the Network Cabling specialism: installing and testing cabling in line with technical and security requirements. This is the technical heart of the specialism - signal theory, cable types, termination, standards, testing and troubleshooting. Subsection numbers mirror the specification.

## 2.1 Principles of network cabling

Data is represented electronically as bits, bytes and packet structures. Transmission can be synchronous or asynchronous, and must handle error detection/correction, bandwidth limits and noise, and data compression, using access methods such as **CSMA/CD** and **CSMA/CA**. Data is encapsulated into frames, packets, datagrams, addresses and sequence numbers via the network interface card. Addressing covers **IPv4** (schemes, subnetting, subnet masks) and **IPv6** (address types).

## 2.2 Tools and equipment (skill)

- **Testing tools**: multimeter, tone generator and probe, **OTDR**, light source and power meter, spectrum analyser, continuity tester.
- **Terminating tools**: crimper, copper/fibre strippers, cable cutters, punch-down tool (IDC), screwdrivers, fusion splicer, fibre cleaning tools, cleave tool.
- **Physical access equipment**: MEWPs, low-level access towers, step ladders.
- **Fixtures/fittings**: prebuilt or flat-pack cabinets, racks, trunking/containment.

Students assess the job's requirements, select the correct tool, and use it safely per manufacturer guidance.

## 2.3–2.4 Networking devices, installation and configuration (skill)

Devices used when installing a network: firewalls, routers, switches (including SFP modules), hubs, bridges, modems, wireless access points, media converters, range extenders, VoIP endpoints, CCTV, servers, network interfaces and cabling itself.

Installing a device means: reading the design spec to find its location, checking the equipment matches spec, confirming physical fit (space, power, cooling), racking it, testing functionality, and configuring it to the requirement.

## 2.5–2.6 Structured cabling design

Design is shaped by network topology (logical and physical), compliance with physical-design standards, the relationship between **permanent links and channels**, campus distribution context, and the balance between passive and active network design.

A network design specification typically includes: a customer statement of requirement (SOR), a bill of materials, cabling design documentation (building/floor plans, power/cooling diagrams, containment layouts, cable routes), installation admin (labelling, documentation, certification, warranty, performance declarations), installation procedures, contractual penalties and a future-proofing strategy. Producing one means gathering requirements, designing the spec, analysing/interpreting it (resource quantities, material lengths, component placement), and flagging potential issues - all written using correct technical language and organised logically.

## 2.7–2.9 Fibre signal theory and handling faults

Light travels down fibre core via **total internal reflection (TIR)**, following **refraction** principles, in single-mode or multi-mode form. **Attenuation** is the loss of signal strength over distance (measured in dB), caused by absorption (light absorbed by particles, worsens with distance), scattering (light hitting particles and being lost into the cladding), and macro/microbending. Poor handling causes its own losses: dirty/faulty/contaminated connectors (unreliable or no connection), excessive bending (with or without tension), and poor-quality cable/connectors (interference).

## 2.10 Ohm's law and copper cabling

Ohm's law: **V = I × R**. Voltage and current are proportional (more voltage → more current); resistance opposes current (more resistance → less current). Applied to cabling, resistance varies with cable length, the resistors present in hardware, signal frequency and cable size - which is why there's a maximum cable length for reliable signal transmission.

## 2.11 Copper and fibre media types

**Copper**: durable, easy to handle, cheap to install, high bandwidth, can carry power (PoE). Used for telephony and short-run LAN (max 90m permanent link / 100m total channel). Types: twisted pair (TP), unshielded twisted pair (UTP, noise/EMI reduction via twisting), shielded/screened twisted pair (STP, insulating shield + grounding), foil twisted pair (FTP), coaxial (copper core, insulator, braided shield, outer coat).

**Fibre**: longer transmission distance, higher bandwidth, greater carrying capacity, lightweight, less data degradation, cheaper materials, but limited by laser quality at each end. Used for large data transfer and long-distance/inter-building links. Types: single-mode (OS1/OS2, one ray of light, long distance) and multi-mode (OM3/OM4, multiple rays of light, shorter distance).

## 2.12 Plenum-rated fire-resistant cable

Compared to non-fire-resistant cable, plenum cable emits lower toxicity and smoke, burns less, breaks down less, withstands higher heat while staying operational, and complies with the **Construction Products Regulation (CPR)**.

## 2.13–2.14 Connectors and transceivers

**Connectors** - copper: RJ-45, RJ-11, BNC, DB-9, DB-25, F-type. Fibre: LC, ST, SC, MT-RJ, MPO. Features to consider: mating type, locking method (latching, screw-down, bayonet, APC/UPC), durability, size and pin insulation.

**Transceivers** - physical forms: SFP, SFP+, GBIC, QSFP. Selection criteria: simplex/duplex, bidirectional capability, bandwidth, wave-division multiplex, dynamic range, transfer rate, connector type, and whether it's standalone or hosted in a switch/router.

## 2.15 Termination points

- **66 block** - punch-down terminal for telephone systems, terminates 22–26 gauge solid copper wire, RJ-21 female connector, used with Cat3.
- **110 block** - supports higher speeds (Cat5/Cat6/Cat6a), supersedes the 66 block, terminates on-premises structured cabling.
- **Patch panel** - mounted case where incoming wires terminate at punch-down blocks; patch cables interconnect via jacks; handles large volumes of copper and fibre.

## 2.16 Copper and fibre standards, termination and Ethernet deployment

**Copper cable standards:**

| Cable | Rated freq. (MHz) | Max length (m) | Ethernet data rate | Deployment standard |
|---|---|---|---|---|
| Cat3 | 16 | 100 | 10Mbps | 10BASE-T |
| Cat5 | 100 | 100 | 100Mbps | 100BASE-T / 100BASE-TX |
| Cat5e | 100 (up to 350) | 100 | 1Gbps | 1000BASE-T |
| Cat6 | 250 (up to 550) | 100 | 1Gbps/10Gbps | 1000BASE-TX |
| Cat6a | 500 (up to 550) | 100 | 10Gbps | 10GBASE-T |
| Cat7 | 600 | 100 | 10Gbps | - |
| RG59 | High bandwidth | 229 | 10Mbps | - |
| RG6 | Low bandwidth | 305 | 10Mbps | - |

**Fibre cable standards (max length, m, by wavelength):**

| Ethernet rate | Wavelength (nm) | OS1/OS2 | OM1 | OM2 | OM3 | OM4 |
|---|---|---|---|---|---|---|
| 100Mbps | 850 | 40,000 | 2,000 | 2,000 | 2,000 | 2,000 |
| 1Gbps | 850 | 100,000 | 275 | 550 | 550 | 1,000 |
| 10Gbps | 850 | 40,000 | 33 | 82 | 300 | 550 |
| 40 & 100Gbps | 850 | 40,000 | – | – | 100 | 150 |
| 1Gbps | 1300 | – | 550 | 550 | 550 | 550 |
| 10Gbps | 1300 | – | 300 | 300 | 300 | 300 |

**Termination methods**: patching (to a patch panel), RJ45 (Ethernet), splicing (fusion - permanent, single-mode; mechanical - non-permanent, single- or multi-mode).

**Termination standards**: TIA/EIA-568A (American pin-out) and TIA/EIA-568B (British/European pin-out) - a **crossover** cable uses 568A at one end and 568B at the other; a **straight-through** cable uses the same standard at both ends. Ethernet deployment standards range from 100BaseT/TX through 1000BaseT/T1/LX/SX to 10GBaseT.

## 2.17–2.18 Maintenance and troubleshooting

Troubleshooting follows: identify the problem (fault or routine monitoring) → diagnose (gather info, analyse against past data/similar systems, narrow down causes) → test the shortlist → resolve (implement the fix, document it, prevent recurrence). Maintenance also covers logging hardware/software changes and informing stakeholders, monitoring performance (user activity, traffic/load, benchmarking), and choosing between predictive maintenance (replacing before failure) and reactive maintenance (run-to-failure).

Common connectivity/performance failures - physical (wrong cable type, incorrect pin-out, open/short, bad port, cable damage, bent pins, duplex/speed mismatch, wrong containment) and technical (attenuation, latency, jitter, crosstalk, EMI, transceiver mismatch, TX/RX reverse, bottlenecks, hardware error, LED status) - are detected via cyclical redundancy checks, encapsulation errors, frame/packet/datagram loss, address conflicts and missing sequence numbers.

## 2.19–2.21 Transmission principles, supporting media and compliance

Signal types (electrical, light - laser/LED - or wireless) carry security risks (tampering, signal loss) and need segregation from electrical cabling per **BS EN 50174**. Supporting media to identify and protect around includes telecoms, security systems (CCTV), alarms, AV systems, WAPs and IoT devices - protected by avoiding shared containment routes, labelling service cables, checking local records, and applying change management.

Key standards: **BS EN 50173** (generic cabling), **BS EN 50174** (installation specification/QA), **BS EN 50310** (bonding/earthing), **BS EN 60825** (optical fibre safety), **BS 6701** and **BS 7671** (installation/wiring regulations), **IEEE 802.3** (Ethernet) and **802.16** (WiMAX), **IEC 60364** (electrical installations), **TIA/EIA-568-B** (cable categories), **ISO/IEC 11801** and **EN 50173** (generic cabling for customer premises). Related legislation: Health and Safety at Work etc. Act 1974, Electricity at Work Regulations 1989, Work at Height Regulations 2005, COSHH Regulations 2002, Confined Spaces Regulations 1997, PPE Regulations 2018, Control of Asbestos Regulations 2012.

## 2.22 Asbestos-containing materials (ACM)

If ACM is suspected during installation: stop work immediately, inform relevant personnel, isolate/restrict the area, get it investigated by an asbestos-registered professional, then act on the findings (removal, sealing, or air-quality checks) - all run through the standard risk-management process (identify → analyse → prioritise/mitigate → record).

## 2.23–2.24 Working at height and in confined spaces (skill)

Apply the risk-management process before working at height (using MEWPs safely per the Health and Safety at Work etc. Act 1974) and when assembling/inspecting/operating/dismantling prefabricated low-level access towers per manufacturer guidance. The same process applies to confined-space work, alongside correctly applied and maintained PPE, with findings recorded clearly.

## 2.25 Installing fixtures and fittings (skill)

Interpret the cabling design spec, compare the physical site against it (space, power, cooling), construct/install cabinets and racks per manufacturer guidance, add additional fixtures (trunking, containment), test everything for compliance, and arrange equipment within racks to meet the spec.

## 2.26–2.28 Inspection, certification and interpreting results

Testing standards include **TIA/EIA-568-B.2-1** (Cat6 transmission performance), **TIA/EIA-568-B.1-10** (Augmented Cat6), **TIA/EIA-TSB-155-A** (Cat6 support for 10GBASE-T), **TIA-1152** (field test instrument requirements) and **IEC 61935-1** (reference measurement procedures). Certification follows a test plan (scope, approach, resources, schedule) using appropriate copper (continuity tester, cable performance tester, cable certifier) or fibre (OLTS, light source, OTDR, fibre inspection tool) test equipment, checking parameters such as wiremap, cable length and near-end crosstalk (copper) or tier 1/2 testing and fibre inspection (fibre).

Failing to meet standards has network consequences (slower speeds, more interference, harder maintenance, shorter cable life, weaker security) and business consequences (revisit costs, SLA/warranty penalties, reputational damage, delayed payment, failed audits). In practice, students identify what's being tested (copper/fibre), pick the right cable spec and testing method, apply it per manufacturer/industry standards, and record results - then analyse and interpret those results against manufacturer tolerances to draw reasoned conclusions.

## 2.29 Impact of poor workmanship

Incorrect labelling makes troubleshooting, maintenance and reconfiguration harder. Failing to test all cabling risks equipment damage, premature breakdown, service disruption, and undetected system errors.

## Key terms

- **TIR** - total internal reflection, the principle that keeps light inside a fibre core.
- **Attenuation** - loss of signal strength over distance, measured in dB.
- **Permanent link / channel** - the fixed cabling segment vs. the full end-to-end connection including patch cords.
- **OTDR** - optical time domain reflectometer, used to test fibre cable.

## Related pages

- [Security Procedures and Controls](01-security-procedures-and-controls.md)
- [Discover, Evaluate and Apply Reliable Sources of Knowledge](03-sources-of-knowledge.md)
- [Digital Infrastructure - Physical and Virtual Infrastructure](../digital-infrastructure/02-physical-and-virtual-infrastructure.md)
- [Occupational Specialisms overview](../00-overview.md)
- [Scheme of Assessment](../05-scheme-of-assessment.md)
