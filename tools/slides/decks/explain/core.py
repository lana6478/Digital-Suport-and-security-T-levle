"""Explanations for the Core Component decks (Core Paper 1)."""
from . import E

EXPLAIN = {
    "core/01-computational-thinking-algorithms-and-diagrams.pptx": {
        "The four components of computational thinking": E(
            "Computational thinking is a way of tackling problems so that a person or a computer can solve them. "
            "It isn't programming: it's the thinking you do before you write code or fix a fault.\n\n"
            "Decomposition: breaking a big problem into smaller parts you can solve one at a time.\n\n"
            "Pattern recognition: spotting what this problem has in common with ones you've solved before, so you "
            "can reuse a solution.\n\n"
            "Abstraction: stripping away detail that doesn't matter. A network diagram shows devices and links, not "
            "the colour of the cables.\n\n"
            "Algorithmic design: writing the solution as clear, ordered steps anyone could follow.",
            "A user says 'my laptop is slow'. Decompose it (CPU, memory, disk, network), recognise the pattern (it's "
            "slow every Monday, when updates run), abstract (ignore the wallpaper), then write steps to diagnose it.",
            [("What is decomposition?", "Breaking a problem into smaller, more manageable parts."),
             ("Which component means ignoring detail that doesn't matter?", "Abstraction."),
             ("Why is pattern recognition useful for a support technician?",
              "It lets them reuse fixes from similar problems instead of starting from scratch.")]),
        "Three control structures": E(
            "Every algorithm, however complicated, is built from just three control structures.\n\n"
            "Sequence: instructions run one after another, in order. Changing the order can change the result.\n\n"
            "Selection: a condition is tested and the algorithm takes one path or another. In code this is an IF "
            "statement; in a flowchart it's a diamond with Yes and No arrows.\n\n"
            "Iteration: steps repeat, either a fixed number of times (count-controlled) or until a condition is met "
            "(condition-controlled). Every loop needs a way to stop, or it runs forever.",
            "Resetting 30 passwords: FOR each account (iteration), IF the account is disabled (selection) skip it, "
            "ELSE generate a password, then email the user (sequence).",
            [("Which control structure repeats steps?", "Iteration."),
             ("What flowchart symbol shows selection?", "A diamond (decision)."),
             ("What happens if a loop's stopping condition is never met?", "It runs forever (an infinite loop).")]),
        "Working with algorithms": E(
            "In the exam you'll be given algorithms to work out, fix and write yourself.\n\n"
            "To find an algorithm's purpose or output, trace it: follow each step with a sample input and write down "
            "every variable's value as it changes. This is what a trace table is for.\n\n"
            "Errors in algorithms are usually logic errors: a comparison the wrong way round (< instead of >), a "
            "counter that never increases, or steps in the wrong order. The algorithm still runs; it just gives the "
            "wrong answer.\n\n"
            "When you design your own, start from the inputs and outputs, then build the steps using sequence, "
            "selection and iteration.",
            "An algorithm should total the numbers 1 to 5. A trace shows the total reaching 10, not 15. The loop "
            "stops at 4 because it checks 'count < 5' instead of 'count <= 5'.",
            [("What is a trace table used for?", "Recording each variable's value step by step to find the output or an error."),
             ("Does a logic error stop an algorithm running?", "No. It runs but produces the wrong result."),
             ("Where should you start when designing an algorithm?", "With the inputs and the required outputs.")]),
        "Diagrams in digital support": E(
            "Diagrams let you explain a system quickly to colleagues and clients.\n\n"
            "A data flow diagram (DFD) shows how data moves through a system. External entities (people or systems "
            "outside it) send or receive data; processes change the data; data stores hold it; labelled arrows show "
            "exactly what data moves where.\n\n"
            "An information flow diagram is simpler. It uses boxes for people, departments or systems and arrows "
            "for the information passing between them. It shows who talks to whom, not how data is processed.\n\n"
            "You need to be able to read both and complete or draw your own.",
            "Helpdesk DFD: User (entity) sends 'fault report' to Log Ticket (process), which writes to the Tickets "
            "data store. Assign Technician (process) reads the ticket and sends 'job' to the Technician (entity).",
            [("What does a data store represent on a DFD?", "A place where data is held, e.g. a database or file."),
             ("What is an external entity?", "A person or system outside the system that sends or receives data."),
             ("When would an information flow diagram be enough?", "When you only need to show who passes information to whom.")]),
    },
    "core/02-problem-solving-strategies-and-reflective-practice.pptx": {
        "Three problem-solving approaches": E(
            "Top-down: start with the whole problem and keep breaking it into smaller sub-problems until each one is "
            "simple to solve. It gives a clear structure and suits new systems with a clear brief.\n\n"
            "Bottom-up: start with small parts that already work and combine them into a bigger solution. It suits "
            "situations where reliable components exist, but the final result can be less well organised.\n\n"
            "Modularisation: split the solution into self-contained modules with clear inputs and outputs. Each "
            "module can be built and tested separately, shared across a team and reused in future projects.",
            "Planning a new office network top-down: network, then floors, then rooms, then each desk point. "
            "Bottom-up: start from spare switches and routers already in the store room and build around them.",
            [("Which approach starts from the whole problem?", "Top-down."),
             ("Give one benefit of modularisation.", "Modules can be built, tested and reused separately."),
             ("When does bottom-up make sense?", "When reliable components already exist.")]),
        "Root cause analysis": E(
            "A quick fix that treats a symptom lets the problem come back. Root cause analysis finds the underlying "
            "cause so it can be fixed for good.\n\n"
            "Five whys: ask 'why?' about the problem, then about each answer, until you reach a cause you can act on.\n\n"
            "FMEA (Failure Mode and Effects Analysis): list every way a component could fail, what the effect would "
            "be and how serious it is, so the worst risks are tackled first.\n\n"
            "Event tree analysis: start from one event and map every outcome that could follow.\n\n"
            "Once found, the root cause is logged, closed, or escalated to someone who can fix it.",
            "The website is down. Why? The server crashed. Why? The disk was full. Why? Logs were never deleted. "
            "Why? No clean-up task exists. Fix: schedule log clean-up, not just a reboot.",
            [("Why isn't fixing the symptom enough?", "The underlying cause remains, so the problem comes back."),
             ("What does FMEA list?", "Every way a component could fail and the effect of each failure."),
             ("Name the three actions once a root cause is found.", "Log it, close it or escalate it.")]),
        "Incidents and problems": E(
            "In IT support, 'incident' and 'problem' mean different things.\n\n"
            "A digital incident is a single unplanned event that disrupts a service or lowers its quality, such as "
            "users being unable to log in this morning. The priority is to restore service quickly.\n\n"
            "A digital problem is the underlying cause of one or more incidents. The priority is to find and remove "
            "it so the incidents stop happening.\n\n"
            "The incident management process has three stages: detection (report, record and prioritise), response "
            "(identify an owner, resolve, restore and record) and intelligence (record lessons, identify the cause "
            "and share what was learned).",
            "Three separate login failures in a week are three incidents. The expired certificate on the login "
            "server that caused them is one problem.",
            [("Is 'the printer won't print today' an incident or a problem?", "An incident."),
             ("What are the three stages of incident management?", "Detection, response, intelligence."),
             ("Which stage stops the same incident happening again?", "Intelligence.")]),
        "Two reflective practice models": E(
            "Reflective practice means looking back at how you handled something so you do it better next time.\n\n"
            "Kolb's Experiential Learning Cycle has four stages: you have a concrete experience, reflect on what "
            "happened, draw general conclusions from it, then actively try out the new approach.\n\n"
            "Gibbs' Reflective Cycle has six stages: description, feelings, evaluation, analysis, conclusion and an "
            "action plan. Because it includes feelings, it's especially useful after a stressful or difficult job.\n\n"
            "Both models turn experience into improvement rather than repeating the same mistakes.",
            "After a tense call with an angry user, Gibbs: what happened; I felt rushed; what went well or badly; "
            "why it escalated; I could have listened first; next time I'll summarise their issue before acting.",
            [("How many stages does Gibbs' cycle have?", "Six."),
             ("What is the final stage of Kolb's cycle?", "Active experimentation."),
             ("Why is Gibbs useful after a difficult call?", "It includes reflecting on feelings.")]),
        "Concept mapping and design thinking": E(
            "Concept mapping: put the main idea in the centre and link related concepts to it. In digital support "
            "these are usually hardware, software, people, information and processes, joined by verb labels such as "
            "'stores' or 'uses'. It helps you see how a system fits together.\n\n"
            "Design thinking: a user-centred cycle for solving problems. Empathise with users, define the real "
            "problem, ideate possible solutions, prototype one, get user feedback, then repeat. It stops you "
            "building the wrong solution to the right problem.",
            "A concept map for email: User 'sends' Email 'via' Mail server 'protected by' Spam filter 'configured by' Technician.",
            [("What goes in the centre of a concept map?", "The main idea."),
             ("What is the first stage of design thinking?", "Empathise."),
             ("Why get user feedback on a prototype?", "To check the solution meets users' real needs before building it fully.")]),
    },
    "core/03-networks-cabling-and-unified-communications.pptx": {
        "Reading a routing table": E(
            "Routers use a routing table to decide where to send each packet. Each row is a route.\n\n"
            "The network ID and subnet mask together describe a destination network. The next hop is the address "
            "of the next router the packet should be sent to. The interface is the port it leaves through.\n\n"
            "Routes can be static (typed in by an administrator; simple but don't adapt to change) or dynamic "
            "(learned automatically from other routers using a routing protocol; adapt when links fail).\n\n"
            "If no specific route matches, the default route (0.0.0.0/0) sends the packet towards the internet.",
            "Route: 192.168.2.0 / 255.255.255.0, next hop 10.0.0.2, interface eth1. A packet for 192.168.2.45 "
            "leaves through eth1 towards the router at 10.0.0.2.",
            [("What does the next hop field show?", "The next router a packet is sent to."),
             ("What is the difference between static and dynamic routes?", "Static routes are entered manually; dynamic routes are learned automatically."),
             ("What is the default route for?", "Sending packets that match no other route, usually towards the internet.")]),
        "Console tools and firewalls": E(
            "ipconfig (Windows) and ifconfig (Linux and macOS) show a device's TCP/IP settings: IP address, subnet "
            "mask, default gateway and DNS servers. They're the first thing to check when a device can't connect. "
            "An address starting 169.254 means the device couldn't reach a DHCP server.\n\n"
            "A firewall filters traffic using rules that ALLOW or BLOCK traffic by address, port or application. "
            "Rules are usually checked from the top down and the first match wins, so order matters: specific "
            "rules go above general ones.\n\n"
            "Firewall admin access must itself be protected with strong credentials and limited to trusted locations.",
            "Rule 1 ALLOW TCP 443 from any. Rule 2 BLOCK all. Web traffic gets through. Swap the order and rule 1 "
            "is never reached, so everything is blocked.",
            [("What does an IP address starting 169.254 suggest?", "The device couldn't get an address from a DHCP server."),
             ("Why does firewall rule order matter?", "The first matching rule is applied, so later rules may never be reached."),
             ("Name two things ipconfig shows.", "Any two of: IP address, subnet mask, default gateway, DNS servers.")]),
        "Cable types": E(
            "Copper cables carry electrical signals. UTP (unshielded twisted pair) twists each pair of wires to "
            "cancel interference; it's cheap and flexible, so it's used in most offices. STP (shielded twisted pair) "
            "adds a foil or braid shield, which helps near motors, lifts or power cables.\n\n"
            "Coaxial cable has a single copper core inside a braided shield. It's used for broadband and TV.\n\n"
            "Fibre optic cable carries pulses of light through glass. It supports much higher bandwidth over much "
            "longer distances and isn't affected by electrical interference, but it costs more and needs specialist "
            "tools to terminate.",
            "A school links two buildings 400 m apart with fibre (copper is limited to 100 m) and wires each "
            "classroom with UTP.",
            [("Why are the pairs in UTP twisted?", "To reduce interference and crosstalk."),
             ("When would you choose STP over UTP?", "In electrically noisy areas, e.g. near motors or power cables."),
             ("Give two advantages of fibre.", "Higher bandwidth, longer distances, immune to electrical interference.")]),
        "Unified communications": E(
            "Unified communications combines voice, video, messaging and presence on one network.\n\n"
            "VoIP (Voice over IP) turns speech into data packets and sends them over the network instead of a phone line.\n\n"
            "SIP (Session Initiation Protocol) is the signalling that sets up, manages and ends a call: it rings the "
            "other phone and agrees the settings. VoIP carries the voice; SIP runs the call.\n\n"
            "Codecs compress and decompress media so it uses less bandwidth. Lossy codecs such as MP3 throw away "
            "detail you won't notice; lossless codecs such as FLAC keep everything. MPEG-4 is common for video.",
            "When you call a colleague on Teams, SIP-style signalling sets up the call, a codec compresses your voice, "
            "and VoIP packets carry it across the network.",
            [("What is the difference between VoIP and SIP?", "VoIP carries the voice; SIP sets up, manages and ends the call."),
             ("What does a codec do?", "Compresses and decompresses audio or video."),
             ("Is MP3 lossy or lossless?", "Lossy.")]),
        "What affects call quality": E(
            "Real-time voice and video are very sensitive to network conditions.\n\n"
            "Bandwidth is how much data the link can carry. If it's too low, calls break up. Speed is how fast data "
            "is transferred.\n\n"
            "Latency is the delay before data arrives. Above about 150 ms people start talking over each other.\n\n"
            "Jitter is variation in latency: packets arrive unevenly, making speech sound choppy or robotic.\n\n"
            "Packet loss is data that never arrives, heard as gaps and missing words.\n\n"
            "Quality of Service (QoS) settings can prioritise voice traffic over downloads.",
            "Calls are fine at 9am but choppy at lunchtime when everyone streams video. Jitter and packet loss rise "
            "with congestion; prioritising VoIP with QoS fixes it.",
            [("Which metric causes people to talk over each other?", "Latency."),
             ("What is jitter?", "Variation in latency between packets."),
             ("How can voice be protected from congestion?", "Using Quality of Service (QoS) to prioritise it.")]),
    },
    "core/04-supporting-and-testing-systems.pptx": {
        "Matching systems to user needs": E(
            "Good support starts with understanding what the user actually does.\n\n"
            "Hardware: more cores and a faster clock speed help with heavy processing such as video editing; more "
            "RAM lets more programs run at once; SSD storage makes everything feel faster; connectivity (Wi-Fi, "
            "Ethernet, ports) must match how they work.\n\n"
            "Operating system: graphical or text-based, single or multi-user, or a virtual machine if they need an "
            "isolated environment.\n\n"
            "Software: choose from databases, spreadsheets, word processors, presentation, communication tools and "
            "browsers based on their tasks. Always test the setup before handing it over.",
            "A receptionist needs email, a browser and a booking system: a modest PC is fine. A video editor needs a "
            "multi-core CPU, 32 GB RAM, a dedicated GPU and fast SSD storage.",
            [("Which component helps most when many programs run at once?", "RAM."),
             ("Why ask what the user does before choosing hardware?", "So the system matches their workload without overspending."),
             ("What should you do before handing over a new system?", "Test it.")]),
        "Fault indicators": E(
            "Computers tell you what's wrong if you know how to read them.\n\n"
            "Error numbers and error messages appear on screen. Search the exact code in the manufacturer's "
            "documentation rather than guessing.\n\n"
            "Beep codes sound at start-up before anything appears on screen. The pattern (for example one long, two "
            "short) points to a specific fault, often memory or graphics.\n\n"
            "Blink codes are patterns of flashing lights on laptops, printers and network devices.\n\n"
            "Codes differ between manufacturers, so always check the technical documentation for that model.",
            "A PC gives three short beeps and shows nothing. The motherboard manual lists three beeps as a memory "
            "error, so you reseat the RAM.",
            [("When do beep codes occur?", "At start-up, often before anything appears on screen."),
             ("Why check the manufacturer's documentation?", "Codes differ between manufacturers and models."),
             ("Give an example of a blink code.", "A flashing light pattern on a laptop, printer or router.")]),
        "Testing methods": E(
            "Components are tested on their own before being combined, because a fault is far easier to find in one "
            "part than in a whole system.\n\n"
            "Unit testing checks one component; integration testing checks components working together; system "
            "testing checks the whole thing; acceptance testing checks it meets the user's requirements.\n\n"
            "Boundary testing uses values at the edge of what's allowed. Performance, load and stress testing check "
            "speed under normal, heavy and extreme use. Regression testing checks a change hasn't broken anything "
            "that used to work.\n\n"
            "Closed box testing uses only inputs and outputs; open box testing uses knowledge of the internal code.",
            "Before a new booking system goes live: unit test each function, integration test booking plus payment, "
            "load test with 500 users, then users run acceptance tests.",
            [("Why test components before integration?", "Faults are easier to find in one part than in the whole system."),
             ("What does regression testing check?", "That a change hasn't broken existing features."),
             ("What is the difference between closed and open box testing?", "Closed box uses only inputs and outputs; open box uses knowledge of the code.")]),
        "Types of test data": E(
            "Good testing uses four types of data, so you see how the system behaves in every situation.\n\n"
            "Valid (normal) data should be accepted and processed correctly.\n\n"
            "Invalid data is the right type but outside the rules, so it should be rejected with a helpful message.\n\n"
            "Boundary data sits exactly at the edges of what's allowed. Bugs often hide here, because programmers "
            "mix up < and <=.\n\n"
            "Erroneous data is the wrong type altogether, such as letters where a number is expected. The system "
            "should reject it without crashing.",
            "A field accepts 1 to 8 guests. Valid: 4. Invalid: 12. Boundary: 1 and 8 (and 0 and 9 just outside). "
            "Erroneous: 'four'.",
            [("Why test boundary values?", "Errors are common at the edges, e.g. < instead of <=."),
             ("What should happen with erroneous data?", "It should be rejected without the system crashing."),
             ("An age field accepts 11 to 18. Give an invalid value.", "Any whole number outside the range, e.g. 25.")]),
        "Structure of a test plan": E(
            "A test plan makes testing organised and repeatable. Each test is a row with the same columns.\n\n"
            "Identify the test: what exactly is being tested. Describe its purpose: why it matters. Identify the "
            "test data: the exact values to use. Describe the expected result: written before running the test. "
            "Record the actual result: what really happened.\n\n"
            "If the actual result doesn't match the expected one, the test has found a fault to fix and retest. "
            "Repeated tests can be automated with macros or scripts.\n\n"
            "To judge whether results are believable, check the inputs were unbiased and relevant, the results make "
            "sense, and, where needed, ask a subject matter expert.",
            "Test 3: guests field boundary. Purpose: check the upper limit is accepted. Data: 8. Expected: accepted. "
            "Actual: rejected, so there is a bug in the range check.",
            [("Why write the expected result before running the test?", "So you can't convince yourself the actual result was correct."),
             ("What happens when actual and expected results differ?", "A fault has been found; fix it and retest."),
             ("How can repeated tests be run automatically?", "With macros or scripts.")]),
    },
    "core/05-project-management-and-risk-assessment.pptx": {
        "The 5 by 5 risk matrix": E(
            "A risk matrix puts a number on how serious a risk is, so you can decide what to deal with first.\n\n"
            "Rate the likelihood from 1 (improbable) to 5 (frequent) and the severity from 1 (negligible) to 5 "
            "(catastrophic). Multiply them to get a risk score from 1 to 25.\n\n"
            "High scores (often 15 and above) need action straight away. Medium scores need controls and "
            "monitoring. Low scores may be accepted.\n\n"
            "A risk assessment then records the risk, who or what could be harmed and how, existing and further "
            "mitigations, who is responsible and a due date.",
            "Server room overheating: likelihood 3 (occasional) x severity 4 (critical) = 12. Mitigation: add a "
            "temperature alarm and a second air-conditioning unit.",
            [("How is a risk score calculated?", "Likelihood x severity."),
             ("What is the highest possible score?", "25."),
             ("Name three things a risk assessment records.", "Any three: the risk, who/what is harmed and how, mitigations, owner, due date.")]),
        "Waterfall and Agile": E(
            "Waterfall runs a project in fixed stages: requirements, design, build, test, deploy. Each stage is "
            "finished and signed off before the next begins. It's easy to plan and cost, and produces thorough "
            "documentation, but changes late on are expensive.\n\n"
            "Agile delivers the project in short iterations (often two-week sprints). Each one produces a working "
            "piece that the customer reviews, and requirements can change as you learn. It copes well with change, "
            "but the final cost and date are harder to predict.\n\n"
            "Choose Waterfall when requirements are clear and fixed; choose Agile when they're likely to change.",
            "Installing cabling in a new building: Waterfall, because the plans are fixed. Building a new staff "
            "self-service portal: Agile, because users will want changes once they try it.",
            [("Which methodology delivers in short iterations?", "Agile."),
             ("Give one drawback of Waterfall.", "Changes late in the project are costly."),
             ("When is Waterfall a good choice?", "When requirements are clear and unlikely to change.")]),
        "Project management techniques": E(
            "Gantt charts show each task as a bar on a timeline, so you can see what happens when and what overlaps. "
            "They're easy to read and great for progress meetings.\n\n"
            "A precedence table lists each task, its duration and which tasks must finish before it can start.\n\n"
            "Critical Path Analysis (CPA) uses those dependencies to find the longest chain of tasks. That chain "
            "sets the shortest possible project length.\n\n"
            "PERT charts show tasks as a network and use optimistic, likely and pessimistic time estimates.\n\n"
            "Kanban boards move task cards through columns such as To do, Doing and Done.",
            "Rolling out 30 PCs: the Gantt chart shows imaging runs alongside desk installation, while the critical "
            "path runs through ordering, imaging, installing and testing.",
            [("What does a Gantt chart show?", "Tasks as bars on a timeline."),
             ("What does the critical path determine?", "The shortest possible length of the project."),
             ("What columns might a Kanban board have?", "E.g. To do, Doing, Done.")]),
        "Finding the critical path": E(
            "The critical path is the longest route through a project's dependent tasks.\n\n"
            "First, build a precedence table with every task, its duration and what must finish first. Then draw the "
            "tasks as a network in dependency order and add up the duration along every route from start to finish.\n\n"
            "The longest total is the critical path. Any delay to a task on it delays the whole project.\n\n"
            "Tasks off the critical path have float: spare time they can slip without delaying the finish. Managers "
            "watch critical tasks most closely.",
            "Route A: order kit (5) + image PCs (3) + install (2) + test (1) = 11 days. Route B: remove old PCs (1) + "
            "fit desks (2) + install (2) + test (1) = 6 days. Route A is critical; route B has float.",
            [("What is float?", "Time a task can slip without delaying the project."),
             ("What happens if a critical task is late?", "The whole project is delayed."),
             ("What do you need before you can find the critical path?", "Each task's duration and dependencies.")]),
    },
    "core/06-data-fundamentals.pptx": {
        "Data, information and knowledge": E(
            "These three words are often mixed up but mean different things.\n\n"
            "Data is raw facts and figures with no context, such as 37.8. On its own it tells you nothing.\n\n"
            "Information is data given context and meaning: 'the server room is 37.8 degrees C'. Now it can be understood.\n\n"
            "Knowledge is understanding applied to information so you can act: 'above 35 degrees the servers may "
            "shut down, so turn on the backup cooling'.\n\n"
            "Organisations collect data to produce information, and staff use knowledge to make decisions.",
            "Data: 120, 95, 210. Information: help tickets per day this week. Knowledge: Wednesday spikes after "
            "updates, so schedule extra helpdesk staff on Wednesdays.",
            [("What turns data into information?", "Adding context and meaning."),
             ("Give an example of knowledge from helpdesk data.", "E.g. tickets spike after updates, so add staff on those days."),
             ("Is 37.8 on its own data or information?", "Data.")]),
        "Where data comes from": E(
            "Data comes from many sources, and each has strengths and risks.\n\n"
            "Humans provide it through surveys and forms. It's rich but prone to typing mistakes.\n\n"
            "Sensors measure temperature, movement, vibration, sound, light and pressure automatically, and IoT "
            "devices such as smart thermostats and cameras send it over a network.\n\n"
            "Transactions record purchases, memberships and timings.\n\n"
            "AI and machine learning generate data too, but beware feedback loops, where an AI learns from its own "
            "biased output.\n\n"
            "Data's value depends on its quantity, timeframe, source and veracity (accuracy), and it must be used ethically.",
            "A gym collects data from sign-up forms (human), card entry logs (transactions) and treadmill sensors "
            "(IoT) to plan when to open extra classes.",
            [("Name two sources of data.", "Any two: humans, sensors, IoT devices, transactions, AI."),
             ("What is a feedback loop in AI?", "When an AI learns from its own output, reinforcing errors or bias."),
             ("What does veracity mean?", "How accurate and trustworthy the data is.")]),
        "Data taxonomy": E(
            "Data can be sorted into two main types.\n\n"
            "Quantitative data is structured: it's numbers or fixed categories that fit neatly into tables. It can "
            "be discrete (whole counts, like tickets logged), continuous (measured values, like CPU temperature) or "
            "categorical (fixed groups, like priority high, medium or low).\n\n"
            "Qualitative data is unstructured: free text, images, audio and video. It can only be stored and "
            "retrieved as a whole object, or codified into structured data, for example by tagging customer comments "
            "as positive or negative.\n\n"
            "The type of data decides how you can store, search and analyse it.",
            "A helpdesk records the number of calls (discrete), average wait time (continuous), priority "
            "(categorical) and the caller's description of the fault (qualitative).",
            [("Is 'CPU temperature' discrete or continuous?", "Continuous."),
             ("Is a customer's written complaint quantitative or qualitative?", "Qualitative."),
             ("How can qualitative data be made structured?", "By codifying it, e.g. tagging comments by category.")]),
        "Data types": E(
            "Every value stored in a system has a data type, which controls what it can hold and what you can do with it.\n\n"
            "Integers are whole numbers; reals hold decimals. Characters hold one symbol; strings hold text. "
            "Booleans hold only true or false. Dates hold calendar dates and times. Blobs (binary large objects) "
            "hold files such as images and PDFs.\n\n"
            "Choosing the right type saves storage, prevents errors and makes validation possible. A phone number "
            "is a string, not an integer, because it can start with 0 and you never do maths with it.",
            "A user account record: user ID (integer), name (string), locked (Boolean), last login (date), "
            "profile photo (Blob).",
            [("Which data type holds true or false?", "Boolean."),
             ("Why is a phone number stored as a string?", "It may start with 0 and isn't used in calculations."),
             ("What is a Blob used for?", "Storing binary files such as images or PDFs.")]),
        "Data formats": E(
            "Data formats decide how data is laid out when it's saved or sent between systems.\n\n"
            "CSV stores one record per line with values separated by commas. It's simple and opens in any spreadsheet.\n\n"
            "JSON stores key and value pairs that can be nested. It's the standard for web APIs.\n\n"
            "XML wraps data in named tags. It's more verbose but self-describing.\n\n"
            "Plain text files suit logs and notes.\n\n"
            "ASCII and UTF-8 are character encodings: ASCII has 128 basic English characters; UTF-8 can represent "
            "every language and emoji, so it's used on the web.",
            "The same ticket as CSV: 101,Printer,High. As JSON: {\"id\": 101, \"category\": \"Printer\", "
            "\"priority\": \"High\"}.",
            [("Which format is standard for web APIs?", "JSON."),
             ("Why is UTF-8 used on the web instead of ASCII?", "It supports characters from every language."),
             ("Give one advantage of CSV.", "Simple, and opens in any spreadsheet.")]),
    },
    "core/07-data-quality-systems-and-analysis.pptx": {
        "Validation checks": E(
            "Validation is an automatic check that data is sensible before it's accepted.\n\n"
            "A presence check makes sure a field isn't empty. A length check makes sure there are the right number of "
            "characters. A range check makes sure a number is between limits. A type check makes sure data is the "
            "right type. A format check makes sure data matches a pattern, such as an email address.\n\n"
            "Validation can't prove data is correct, only that it's reasonable. A valid date of birth can still be "
            "the wrong person's. Verification, such as typing a password twice, checks data was entered accurately.",
            "A booking form: name (presence), postcode (length and format), guests 1 to 8 (range and type), "
            "email (format). 31/02/2008 fails a date format check.",
            [("Which check makes sure a field isn't empty?", "Presence check."),
             ("Why can't validation prove data is correct?", "It only checks data is reasonable, not true."),
             ("What is verification?", "Checking data was entered accurately, e.g. typing it twice.")]),
        "Interrogating data in a spreadsheet": E(
            "Spreadsheets organise data in rows (records) and columns (fields) on worksheets.\n\n"
            "Sorting and filtering let you order data or show only rows that match, such as high-priority tickets.\n\n"
            "Arithmetic functions summarise data: SUM adds, AVERAGE finds the mean, MIN and MAX find the smallest "
            "and largest.\n\n"
            "Logical functions make decisions: IF returns one value or another depending on a condition; COUNTIF "
            "counts cells that match a condition.\n\n"
            "Data is often imported from text or CSV files exported by other systems, analysed, then saved back out.",
            "=COUNTIF(C2:C200,\"Printer\") counts printer faults. =IF(D2>48,\"Breach\",\"OK\") flags tickets that "
            "missed a 48-hour SLA.",
            [("Which function counts cells that match a condition?", "COUNTIF."),
             ("What does =AVERAGE(D2:D10) do?", "Calculates the mean of D2 to D10."),
             ("Why import data from CSV files?", "To analyse data exported from other systems.")]),
        "The 6 Vs of Big Data": E(
            "Big Data is data too large or complex for ordinary tools. The 6 Vs describe what makes it hard.\n\n"
            "Volume: the sheer amount. Variety: many types, from text to video to sensor readings. Variability: its "
            "meaning and flow change over time. Velocity: the speed it arrives and must be processed. Veracity: how "
            "trustworthy it is. Value: the useful insight it gives.\n\n"
            "Quality assurance keeps data usable: validation, verification, reliability, consistency, integrity "
            "and redundancy. How well data is maintained depends on time, skills and cost.",
            "A streaming service logs millions of plays a minute (volume, velocity), from TVs, phones and consoles "
            "(variety), to decide what to recommend (value).",
            [("Which V is about speed?", "Velocity."),
             ("Which V is about trustworthiness?", "Veracity."),
             ("Name two data quality assurance methods.", "Any two: validation, verification, reliability, consistency, integrity, redundancy.")]),
        "Data wrangling": E(
            "Raw data is rarely ready to use. Data wrangling prepares it in five steps.\n\n"
            "Structure it into a usable layout, such as consistent columns. Clean it by fixing errors and removing "
            "duplicates. Validate it against rules. Enrich it by adding useful data from other sources. Output it "
            "for analysis or another system.\n\n"
            "Data entry errors are a big source of problems. Transcription errors are copying mistakes ('Smtih'); "
            "transposition errors swap characters (1234 becomes 1243). Validation, double-entry verification, "
            "drop-down menus and pre-filled fields reduce them.",
            "A support log has 'UK', 'U.K.' and 'United Kingdom' in one column. Cleaning standardises them; a "
            "drop-down on the form stops it happening again.",
            [("What are the five data wrangling steps?", "Structure, clean, validate, enrich, output."),
             ("What is a transposition error?", "Swapping characters, e.g. 1234 becomes 1243."),
             ("How does a drop-down menu reduce errors?", "Users choose from fixed options instead of typing.")]),
        "Data models": E(
            "A data model decides how data is organised and linked.\n\n"
            "Hierarchical: a tree of parents and children, like folders on a drive. Fast when you follow one path, "
            "but awkward when a record belongs in two places.\n\n"
            "Network: records can have many links to many others, which is flexible but complex to build.\n\n"
            "Relational: data is split into tables of rows and columns, linked by keys. It avoids duplicating data, "
            "is easy to query with SQL and is the most common model today.\n\n"
            "The choice depends on access efficiency, storage efficiency and how complex it is to build.",
            "A relational helpdesk database: a Users table and a Tickets table, linked because each ticket stores the "
            "user's ID.",
            [("Which data model uses tables linked by keys?", "Relational."),
             ("What structure does a hierarchical model use?", "A tree of parents and children."),
             ("Why is the relational model popular?", "It avoids duplication and is easy to query.")]),
        "Access and analysis": E(
            "Permissions control who can read or change data. Role-based access control (RBAC) grants access by "
            "job role, such as all nurses. Rule-based access control (RuBAC) uses rules, such as no access outside "
            "working hours. APIs let other software request data in a controlled way.\n\n"
            "For Big Data analysis, a data warehouse stores cleaned, structured data from many sources; a data lake "
            "stores raw data in any format; a data mart is a smaller subset for one department.\n\n"
            "Data mining finds hidden patterns and reporting presents results. Together they produce business "
            "intelligence for planning and customer relationship management.",
            "A retailer's data lake holds raw web clicks; the warehouse holds cleaned sales; the marketing data mart "
            "feeds a weekly report.",
            [("What is the difference between RBAC and RuBAC?", "RBAC grants access by role; RuBAC by rules such as time of day."),
             ("What does a data lake store?", "Raw data in any format."),
             ("What is a data mart?", "A subset of data for one department.")]),
    },
    "core/08-health-and-safety-in-digital-work.pptx": {
        "Health and Safety at Work Act": E(
            "The Health and Safety at Work Act is the main law protecting people at work, including in IT.\n\n"
            "Employers must provide a safe working environment, train staff properly, provide adequate welfare "
            "facilities such as toilets and drinking water, and give the information, instruction and supervision "
            "people need to work safely.\n\n"
            "Employees have duties too: take reasonable care of themselves and others, follow training and safety "
            "procedures, and not misuse safety equipment.\n\n"
            "More specific regulations, such as those for display screens and manual handling, sit underneath it.",
            "A new technician must be trained before working in the server room, shown the fire exits and emergency "
            "power-off, and supervised until they're competent.",
            [("Name two employer duties under the Act.", "Any two: safe environment, training, welfare, information, instruction, supervision."),
             ("Do employees have duties too?", "Yes: take reasonable care and follow safety procedures."),
             ("How do other regulations relate to the Act?", "They sit under it and cover specific risks.")]),
        "Key regulations": E(
            "Manual handling regulations: avoid hazardous lifting where possible. Where you can't, assess the risk, "
            "tell staff about the load's weight and centre of gravity, and reduce the risk, for example with "
            "trolleys or team lifts.\n\n"
            "Work at height regulations: avoid it where you can. Otherwise plan and supervise the work, use competent "
            "people and suitable, stable equipment, protect against falling objects and plan for emergencies.\n\n"
            "Display screen equipment (DSE) regulations: employers must assess workstations, reduce risks including "
            "regular breaks from the screen, provide eye tests on request, and give training.",
            "Fitting a wireless access point on a 3 m ceiling: use a podium step or tower rather than a chair, have "
            "a second person present, and keep tools tethered.",
            [("What is the first rule of the work at height regulations?", "Avoid working at height where possible."),
             ("What must employers provide DSE users on request?", "An eye test."),
             ("Give one way to reduce manual handling risk.", "E.g. trolleys, team lifts, training.")]),
        "Risks in digital work and how to reduce them": E(
            "IT work has real physical risks.\n\n"
            "Long hours at a screen cause eye strain and back, neck and wrist pain. Workstation assessments, "
            "adjustable chairs, correct screen height and regular breaks reduce this.\n\n"
            "Cable installation risks trips, cuts from cable ties and trunking, and electric shock. Keep cables "
            "tidy, wear gloves and isolate power first.\n\n"
            "Lifting servers and boxes of equipment risks back injury. Use trolleys and team lifts.\n\n"
            "The four main mitigations are training, a safe environment and practices, safety equipment and supervision.",
            "A technician re-cabling a comms cabinet isolates power, wears gloves, uses a trolley for the new switch "
            "and routes cables away from walkways.",
            [("Name two health risks of DSE work.", "Any two: eye strain, back, neck or wrist pain."),
             ("How can cable installation be made safer?", "E.g. isolate power, wear gloves, keep cables tidy."),
             ("Name the four main mitigation themes.", "Training, safe environment, safety equipment, supervision.")]),
    },
    "core/09-digital-legislation-and-professional-guidelines.pptx": {
        "Data Protection Act and UK GDPR": E(
            "The Data Protection Act 2018 and UK GDPR control how organisations use personal data: any information "
            "about an identifiable living person.\n\n"
            "Data must be processed fairly, lawfully and transparently, collected for specified purposes, limited "
            "to what's needed, kept accurate, not kept longer than necessary, and kept secure. The organisation "
            "must be able to show it complies.\n\n"
            "People have rights over their data, including to see it, correct it and have it erased.\n\n"
            "Breaking the law can bring large fines from the Information Commissioner's Office (ICO) and lost trust. "
            "For IT staff it means securing systems and handling data carefully.",
            "A technician copying a customer database onto an unencrypted USB stick to 'work on it at home' breaches "
            "the security principle, even if nothing is lost.",
            [("What is personal data?", "Information about an identifiable living person."),
             ("Who enforces data protection law in the UK?", "The Information Commissioner's Office (ICO)."),
             ("Name one right people have over their data.", "E.g. access, correction, erasure.")]),
        "Computer Misuse Act 1990": E(
            "The Computer Misuse Act makes it a crime to use computers without permission.\n\n"
            "Unauthorised access: getting into a system or data you're not allowed to, even just to look.\n\n"
            "Unauthorised access with intent to commit further offences: breaking in to commit another crime, such "
            "as fraud.\n\n"
            "Unauthorised acts that impair a computer: for example spreading malware or deleting files.\n\n"
            "Employees can be prosecuted and dismissed, and companies can face liability, so staff awareness "
            "training matters. Having the technical ability to access something isn't the same as permission.",
            "An IT technician with admin rights reads the HR director's emails out of curiosity. They have the access "
            "but not the permission, so it's still unauthorised access.",
            [("Is it an offence to look at data you aren't authorised to see?", "Yes, unauthorised access is an offence."),
             ("Give an example of an act that impairs a computer.", "E.g. spreading malware or deleting files."),
             ("Why is staff awareness important?", "Employees and the company can face serious consequences.")]),
        "Other key legislation": E(
            "Equality legislation protects nine characteristics, including age, disability, race, religion and sex. "
            "It covers direct discrimination, indirect discrimination (a rule that disadvantages a group), "
            "harassment and victimisation. Claims have time limits.\n\n"
            "Intellectual property law protects creators' work through unregistered designs, registered designs and "
            "patents.\n\n"
            "The WEEE Regulations require electrical and electronic waste to be disposed of safely and responsibly, "
            "not sent to landfill. Data must be wiped first.\n\n"
            "International law applies to some offences, such as cybercrime and surveillance that cross borders.",
            "Old office PCs must go to a licensed WEEE recycler after their drives are securely wiped: this satisfies "
            "WEEE and data protection law together.",
            [("How many protected characteristics are there?", "Nine."),
             ("What do the WEEE Regulations cover?", "Safe disposal of electrical and electronic waste."),
             ("What is indirect discrimination?", "A rule that applies to everyone but disadvantages a protected group.")]),
        "Guidelines that shape professional behaviour": E(
            "Laws set the minimum; guidelines describe good professional practice.\n\n"
            "Codes of conduct come from employers, professional bodies such as BCS, the Institution of Analysts and "
            "Programmers and CIISec, and government. They expect you to follow policy and law, work competently and "
            "with integrity, minimise risk to the public, meet deadlines, communicate well and keep confidentiality.\n\n"
            "Industry standards make technology work together safely: ISO for quality and security, WCAG for "
            "accessible websites, W3C and IETF for web and internet standards, EIA/TIA and IEEE for cabling and "
            "networks, and PCI DSS for card payments.",
            "A BCS member asked to set up a system beyond their competence should say so and seek help, rather "
            "than risk a poor or unsafe job.",
            [("Name a professional body with a code of conduct.", "E.g. BCS, IAP or CIISec."),
             ("Which standard covers web accessibility?", "WCAG."),
             ("What is the difference between law and a code of conduct?", "Law sets legal minimums; codes describe good professional practice.")]),
        "Acceptable use and whistleblowing": E(
            "An acceptable use policy (AUP) sets the rules for using an organisation's IT. It lists permitted and "
            "prohibited activities, working practices such as confidentiality, communication etiquette, and the "
            "sanctions for breaking it. Staff usually sign it when they start.\n\n"
            "Whistleblowing procedures give staff a safe way to report wrongdoing, such as data being misused or "
            "safety being ignored. Whistleblowers are protected from being punished. This lets problems be fixed "
            "before they cause harm and keeps organisations legal and ethical.",
            "An AUP might ban installing unapproved software, using personal cloud storage for work files and "
            "sharing passwords, with disciplinary action for breaches.",
            [("What does an AUP set out?", "Rules for using IT: permitted and prohibited activities, etiquette and sanctions."),
             ("Why are whistleblowers protected?", "So people can report wrongdoing without being punished."),
             ("Give one thing an AUP might prohibit.", "E.g. installing unapproved software, sharing passwords.")]),
    },
}
