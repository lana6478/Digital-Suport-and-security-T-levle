# Core Paper 1: Problem Solving, Digital Support and Data

*Digital Support and Security T Level → Core Component → Core Paper 1*

Core Paper 1 is a 2 hour 15 minute written exam worth 90 marks (30% of the core, 15% of the total qualification). It covers three content areas: **Problem solving**, **Introduction to digital support**, and **Data**. This page summarises what students need to know and be able to do in each, following the specification's own numbering so you can cross-reference the official document.

## Content area 1: Problem solving

Students learn to solve digital support and security problems — whole solutions or parts of them — by analysing problems and expressing solutions as systems, processes, relationships or data structures.

### 1.1 Computational thinking

Students need to know what computational thinking is, when to use it, and its benefits and drawbacks, along with its four components: **decomposition**, **pattern recognition**, **abstraction** and **algorithmic design** (each also has its own benefits/drawbacks to weigh up).

- **Decomposition** — breaking a problem (or a solution) down into smaller, more manageable parts: identify the main features, characterise each one, then split into sub-parts. Students should be able to represent decomposition using block diagrams, information flow diagrams, flowcharts or written descriptions (see [Diagram notation](../03-appendices/02-diagram-notation.md)).
- **Pattern recognition** — spotting trends and similarities within/between problems and processes, finding common features between a new problem and existing solutions, and using identified patterns to make predictions.
- **Abstraction** — identifying the information that's actually needed, filtering out unnecessary detail, and hiding the internal workings of a system. In practice this means working out what inputs are needed, what outputs/outcomes are expected, what will vary vs. stay constant, and what key/repeated actions the solution must perform.
- Students should ultimately be able to judge how suitable each component of computational thinking is for a given digital support and security problem, and understand how the four components relate to each other.

### 1.2 Algorithmic design

Covers the definition, characteristics and purpose of algorithms, and two ways to express them: **flowcharts** (terminators, processes, sub-processes, decisions, inputs/outputs, arrows, labels) and **written descriptions** using hierarchical markers to show sequence — plus the benefits/drawbacks of each. Students need to understand the three control structures — **sequence, selection, iteration** — and be able to:

- work out what an algorithm does and trace its output for a given input;
- identify and correct errors in an algorithm; and
- design their own algorithms/solutions using these control structures.

### 1.3 Strategies

Three problem-solving approaches — **top-down, bottom-up, modularisation** — each with their own benefits and drawbacks depending on the problem.

**Root cause analysis** is used to find the underlying cause of a problem rather than just its symptoms, via approaches such as the **five whys**, **Failure Mode and Effects Analysis (FMEA)**, and **Event Tree Analysis (ETA)**. Once the root cause is found, the next action is to log it, close it, or escalate it to an appropriate manager, specialist or third party.

The **high-level problem-solving strategy** students should apply: define the problem → gather information → analyse the information → make a plan of action → implement a solution → review the solution.

**Incident management** definitions matter here too:
- A **digital incident** is a single unplanned event that disrupts service operations and negatively impacts service quality.
- A **digital problem** is the underlying *cause* of an incident.
- The incident management process has three stages: **detection** (report, record, prioritise) → **response** (identify owner, resolve and restore, record resolution) → **intelligence** (record lessons, identify cause, share lessons).

Students should be able to judge which strategy suits which type of problem.

## Content area 2: Introduction to digital support

Students analyse digital support and security problems that might involve hardware, software, people, processes and data, and use a range of tools and techniques to develop solutions.

### 2.1 Infrastructure

Understanding **routing table** data (static/dynamic addresses, network ID, subnet mask, next hop, interface designation) and being able to interpret it; using console tools like `ipconfig`/`ifconfig` to read TCP/IP configuration; and understanding what a **firewall** does, including securing its administrator access and setting ALLOW/BLOCK precedence rules.

### 2.2 Cabling

Cable types and where each is used: **UTP, STP, coaxial, fibre-optic**. What **Ethernet** is and where it's used, plus cable standards (**CAT 5e, CAT 6, CAT 7**) compared on bandwidth and maximum length, and the trade-offs between them.

### 2.3 Unified communications

**VoIP** and **SIP**, how they relate to each other, and the network metrics that affect call/communication quality: **speed, bandwidth, latency, jitter, packet loss**. **Codecs** compress/decompress data — students should know examples like MPEG-4 (video), MP3 (lossy audio) and FLAC (lossless audio).

### 2.4 Support

Understanding what users need when selecting/configuring/testing hardware (cores, memory, storage, clock speed, connectivity), operating systems (graphical/text-based, multi-tasking, single/multi-user, VM), and software (database, spreadsheet, word processor, presentation, communication, browser) — and being able to actually select, configure and test these components, judging what's suitable for the user's needs.

**Fault indicators** — error numbers, error messages, beep codes, blink codes — and the ability to interpret both these and technical documentation to diagnose hardware/software problems.

### 2.5 Testing

Why individual components (software, hardware, data, interfaces, the final service) are tested before integration, and a wide range of testing methods: concept, unit, boundary, integration, performance, system, acceptance, usability, regression, load/stress, closed box, open box.

Automation via **macros** and **scripts**; types of **test data** (valid, invalid, boundary, erroneous) and being able to create it; the structure of a **test plan** (identify tests → describe purpose → identify test data → describe expected results → record actual results); and methods for checking whether results are believable/accurate — logical reasoning (unbiased, relevant inputs; results that make sense), verification by a subject matter expert, and use of test plans.

### 2.6 Using data in digital support

How tabular data is organised (worksheet, row, column); **validation checks** — presence, length, range, type, format; techniques to interrogate data — ordering/sorting/filtering by field, arithmetic functions (SUM, MIN, MAX, AVERAGE), logical functions (IF, COUNTIF) — and using these in spreadsheets; and the purpose of saving/importing data via text-based files.

### 2.7 Using diagrams in digital support

**Data flow diagrams (DFDs)** — data sources, data destinations, processes, data stores, arrows, labels (symbol key in [Diagram notation](../03-appendices/02-diagram-notation.md)) — and **information flow diagrams** (boxes, arrows, labels). Students need to both interpret existing diagrams and create/complete their own to represent a system.

### 2.8 Risk and risk assessment

Risk is assessed using a **5×5 matrix** of Likelihood (improbable, remote, occasional, probable, frequent) against Severity (negligible, marginal, moderate, critical, catastrophic). Students should be able to interpret and build a risk matrix. Risk assessment documentation exists to ensure continuity of service, health and safety, and regulatory compliance, and should record: a description of the risk, who/what could be harmed, how the harm could occur, mitigations already in place, further mitigation needed, who's responsible, and the due date.

### 2.9 Project management methodologies and tools

**Waterfall** vs **Agile** project methodologies (components, benefits, drawbacks), and diagrammatic project-management techniques: **PERT**, precedence tables, **Gantt** charts, **Kanban**, **Critical Path Analysis (CPA)**. Students should be able to interpret/draw these diagrams and judge which methodology/technique suits a given project.

### 2.10 Strategies for responding to support issues

Reflective practice models: **Kolb's Experiential Learning Cycle** (concrete experience → reflective observation → abstract conceptualisation → active experimentation) and **Gibbs' Reflective Cycle** (description → feelings → evaluation → analysis → conclusion → action plan). **Concept mapping** (main idea, individual concepts — hardware, software, people, information, processes — linked by verb relationships) and the **design thinking process** (empathise → define → ideate → prototype → user feedback → repeat).

### 2.11 Sources of knowledge

Categories of source: literature (textbooks, manuals, supplier literature), professionals (conferences, managers, colleagues), websites (wikis, blogs, forums), media (social media, podcasts, video), and observation (dashboards, inspection). Reliability/validity should be judged on bias/subjectivity, evidence/expertise, publication date, and whether other sources corroborate it.

## Content area 3: Data

Students build fundamental knowledge of data as it relates to digital support and security, so they can communicate about it with other professionals — covering how data is stored, accessed, quality-assured, manipulated, analysed and processed.

### 3.1 Data, information and knowledge

The distinctions and relationships between **data**, **information** and **knowledge**. Sources that generate data: human (surveys, forms), AI/machine learning (including the danger of feedback loops), sensors (temperature, accelerometer, vibration, sound, light, pressure), IoT (smart thermostats, lights, security cameras, trackers), and transactions (customer data, membership, timing, basket). Data's value can be judged on quantity, timeframe, source and veracity — alongside ethical data practices. Organisations use data for pattern analysis, system performance monitoring (load, outage, throughput, status), user monitoring, targeted marketing, and threat/opportunity assessment.

### 3.2 Methods of transforming data

Data is transformed by **manipulating**, **analysing** and **processing** it.

### 3.3 Data taxonomy

Data is either **quantitative** (structured) or **qualitative** (unstructured). Quantitative data can be represented as discrete, continuous, or categorical values. Qualitative data is stored/retrieved as a single object, or codified into structured data.

### 3.4 Data types

Common data types and when each is used: **integer, real, character, string, Boolean, date, Blob** — and how data type interacts with structure and transformation choices.

### 3.5 Data formats

Common formats and their use cases: **JSON, text file, CSV, UTF-8, ASCII, XML**.

### 3.6 Structures for storing data

The role of **metadata** in describing and contextualising data; **file-based** and **directory-based** structures; **hierarchy-based** structures; and how storage structure relates to data transformation.

### 3.7 Data dimensions and maintenance

The **6 Vs of Big Data**: volume, variety, variability, velocity, veracity, value — and their impact on gathering, storing, maintaining and processing data. Data quality assurance methods: validation, verification, reliability, consistency, integrity, redundancy. Maintenance is also shaped by time, skills and cost.

### 3.8 Data systems

**Data wrangling** stages: structure → clean → validate → enrich → output. Core functions of a data system: input, search, save, integrate, organise (index), output, feedback loop. Data entry errors — **transcription** and **transposition** — and ways to reduce them: input validation, double-entry verification, drop-down menus, pre-filled fields. Implementation is shaped by the time/expertise needed to build data-entry screens and the time needed to enter data.

### 3.9 Data visualisation

Formats — graphs, charts, tables, reports, dashboards, infographics — chosen based on the type of data, the intended audience, and the brief.

### 3.10 Data models

Three ways to organise data: **hierarchical, network, relational** — chosen based on how efficiently individual items can be accessed, how efficient storage is, and implementation complexity. Students should be able to draw each: hierarchical/network models with blocks, arrows and labels; relational models with tables, rows, columns and labels.

### 3.11 Data access across platforms

**Permissions** (authorisation, privileges, access rights, rules) and **access mechanisms** — role-based access control (RBAC), rule-based access control (RuBAC), and APIs — with their respective benefits and drawbacks.

### 3.12 Data analysis tools

Storing Big Data for analysis: **data warehouse, data lake, data mart**. Analysing it: **data mining, reporting**. Using the resulting business intelligence: financial planning and analysis, and CRM (customer data analytics, communications) — and how the right tool depends on the scale of the data involved.

## Key terms

- **Decomposition / pattern recognition / abstraction / algorithmic design** — the four components of computational thinking.
- **Root cause analysis** — finding the underlying cause of a problem, not just treating symptoms.
- **DFD (Data Flow Diagram)** — see [Diagram notation](../03-appendices/02-diagram-notation.md).
- **6 Vs of Big Data** — volume, variety, variability, velocity, veracity, value.
- **RBAC / RuBAC** — role-based / rule-based access control.

## Related pages

- [Core Component overview](00-overview.md)
- [Core Paper 2](02-core-paper-2.md)
- [Core scheme of assessment](04-core-scheme-of-assessment.md)
- [Diagram notation](../03-appendices/02-diagram-notation.md)
