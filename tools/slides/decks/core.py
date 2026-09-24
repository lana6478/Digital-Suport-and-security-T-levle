"""Core Component decks: Core Paper 1, Core Paper 2 and the Employer Set Project."""

CP1 = "01-core-component/01-core-paper-1.md"
CP2 = "01-core-component/02-core-paper-2.md"
ESP = "01-core-component/03-employer-set-projects.md"
DIAGRAMS = "03-appendices/02-diagram-notation.md"

DECKS = [
    # ------------------------------------------------------------------ CP1
    {
        "area": "core",
        "file": "core/01-computational-thinking-algorithms-and-diagrams.pptx",
        "title": "Computational Thinking, Algorithms and Diagrams",
        "unit": "Core Paper 1",
        "spec": "1.1, 1.2, 2.7",
        "pages": [CP1, DIAGRAMS],
        "objectives": [
            "Describe the four components of computational thinking and when to use each.",
            "Trace, correct and design algorithms using sequence, selection and iteration.",
            "Draw flowcharts using the correct symbols.",
            "Interpret and create data flow and information flow diagrams.",
        ],
        "starter": "Write down every step you take to get to college in the morning. "
                   "Which steps could you group together? Which details could you leave out?",
        "slides": [
            {"type": "cards", "title": "The four components of computational thinking",
             "cards": [
                 ("Decomposition", "Break a problem or solution into smaller, manageable parts. "
                  "Identify the main features, then split each into sub-parts."),
                 ("Pattern recognition", "Spot trends and similarities within and between problems, "
                  "and reuse what worked before to make predictions."),
                 ("Abstraction", "Keep only the information you need. Work out the inputs, outputs, "
                  "what varies and what stays constant."),
                 ("Algorithmic design", "Express the solution as clear, ordered steps that a person "
                  "or computer can follow."),
             ],
             "notes": "Link back to the starter: grouping steps is decomposition, leaving details "
                      "out is abstraction. Ask students for a digital support example of each, e.g. "
                      "decomposing 'the network is slow' into device, cabling, switch and internet."},
            {"type": "compare", "title": "Weighing up computational thinking",
             "left": ("Benefits", [
                 "Large problems become manageable pieces",
                 "Parts can be shared across a team",
                 "Reusing patterns saves time",
                 "Abstraction focuses effort on what matters",
             ]),
             "right": ("Drawbacks", [
                 "Decomposing can take time up front",
                 "Over-abstraction can hide an important detail",
                 "A false pattern leads to the wrong fix",
                 "Parts still have to be joined back together",
             ]),
             "notes": "The specification expects students to judge how suitable each component is "
                      "for a given problem, so push for 'it depends' answers with a reason."},
            {"type": "cards", "title": "Three control structures",
             "cards": [
                 ("Sequence", "Steps run one after another in order. Example: log in, open the "
                  "ticket, record the fault."),
                 ("Selection", "A decision chooses a path. Example: IF the printer shows an error "
                  "code THEN look it up ELSE check the queue."),
                 ("Iteration", "Steps repeat until a condition is met. Example: ping the server "
                  "every 5 seconds UNTIL it replies."),
             ],
             "notes": "Every algorithm, however complex, is built from these three structures."},
            {"type": "table", "title": "Flowchart symbols",
             "header": ["Symbol", "Shape", "Used for"],
             "widths": [2, 2.4, 5],
             "rows": [
                 ["Terminator", "Rounded rectangle", "Start and end of the algorithm"],
                 ["Process", "Rectangle", "An action or calculation"],
                 ["Sub-process", "Rectangle with double sides", "A step defined in its own flowchart"],
                 ["Decision", "Diamond", "A yes/no question that splits the flow"],
                 ["Input / output", "Parallelogram", "Data entering or leaving the system"],
                 ["Arrow and label", "Line with arrowhead", "Direction of flow, with Yes/No labels on decisions"],
             ],
             "notes": "Algorithms can also be written as descriptions with hierarchical markers "
                      "(1, 1.1, 1.2). Flowcharts are easier to follow visually; written descriptions "
                      "are quicker to write and edit."},
            {"type": "bullets", "title": "Working with algorithms",
             "bullets": [
                 "Trace: follow the algorithm step by step with a given input and record the output.",
                 "Correct: find logic errors such as a wrong condition or a loop that never ends.",
                 "Design: build your own solution using sequence, selection and iteration.",
                 "Test: try normal, boundary and invalid inputs to check it behaves as expected.",
             ],
             "callout": "A trace table records the value of each variable after every step. "
                        "It is the fastest way to find where an algorithm goes wrong.",
             "notes": "Model a trace table on the board for a simple loop, e.g. adding up the "
                      "numbers 1 to 5, before students try one themselves."},
            {"type": "compare", "title": "Diagrams in digital support",
             "left": ("Data flow diagram (DFD)", [
                 "Data source and destination: external entities",
                 "Process: something that changes the data",
                 "Data store: where data is held",
                 "Arrows with labels: the data that moves",
             ]),
             "right": ("Information flow diagram", [
                 "Boxes: people, departments or systems",
                 "Arrows: the direction information travels",
                 "Labels: what the information is",
                 "Simpler: shows who talks to whom",
             ]),
             "notes": "The full symbol key is on the Diagram notation page of the wiki. Students "
                      "need to both interpret existing diagrams and complete or create their own."},
            {"type": "terms", "terms": [
                ("Decomposition", "breaking a problem into smaller parts."),
                ("Abstraction", "filtering out detail that is not needed."),
                ("Algorithm", "a precise, ordered set of steps to solve a problem."),
                ("Selection", "a decision that chooses between paths."),
                ("Iteration", "repeating steps until a condition is met."),
                ("DFD", "a diagram showing how data moves between entities, processes and stores."),
            ]},
        ],
        "quiz": [
            ("Name the four components of computational thinking.",
             "Decomposition, pattern recognition, abstraction, algorithmic design."),
            ("Which flowchart symbol is used for a decision?", "A diamond."),
            ("What is the difference between selection and iteration?",
             "Selection chooses a path once; iteration repeats steps until a condition is met."),
            ("Give one drawback of abstraction.",
             "Removing too much detail can hide something important to the solution."),
            ("What does a data store represent on a DFD?", "A place where data is held, such as a database or file."),
        ],
        "activity": {
            "title": "Flowchart a helpdesk fix",
            "time": "20 minutes",
            "format": "Pairs",
            "steps": [
                "Scenario: a user reports they cannot print.",
                "Decompose the problem into at least four possible causes.",
                "Draw a flowchart that checks each cause in a sensible order.",
                "Use at least one decision and one loop.",
                "Swap with another pair and trace their flowchart with a test case.",
            ],
            "success": [
                "Correct symbols throughout",
                "Every decision has labelled Yes and No paths",
                "The flowchart always reaches an end",
                "The trace gives the expected result",
            ],
            "notes": "Stretch: ask stronger students to add a sub-process for 'escalate to second line'.",
        },
        "exit": [
            "Which component of computational thinking do you use most without realising?",
            "Draw the symbol for an input or output.",
            "When would you choose a DFD over an information flow diagram?",
        ],
    },
]

# The remaining core decks live in their own modules to keep files readable.
from .core_cp1 import DECKS as _CP1  # noqa: E402
from .core_cp2 import DECKS as _CP2  # noqa: E402

DECKS = DECKS + _CP1 + _CP2
