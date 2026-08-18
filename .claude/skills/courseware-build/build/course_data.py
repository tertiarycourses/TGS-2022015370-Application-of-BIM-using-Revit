"""
SINGLE SOURCE OF TRUTH — WSQ Application of BIM using Revit (TGS-2022015370).

Every artifact (PPT, LP, LG + LG.md, labs index) is generated from this module
plus data_domain1.py … data_domain4.py (one per course topic) and
data_teaching.py (the teaching slides carried over from the legacy v9 master
deck, including its graphics) so they stay 100% aligned.

Course: 2 training days = 16 hours (9:30am–6:30pm, 1-hour lunch, tea within).
Final assessment on Day 2: WA (SAQ) 1 hour + Practical Performance 1 hour.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Application of BIM using Revit"
SHORT_TITLE  = "Application of BIM using Revit"
COURSE_CODE  = "TGS-2022015370"
VERSION      = "v10"
VERSION_DATE = "18 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2

# Skills Framework alignment (Built Environment)
TSC_TITLE = "Building Information Modelling Application"
TSC_CODE  = "BEV-TEM-3027-1.1-1"
TSC_ABILITIES = [
    ("A1", "Identify BIM application and development in industry"),
    ("A2", "Identify BIM's interoperability with other analysis tools"),
    ("A3", "Maintain databases and information systems for BIM"),
    ("A4", "Develop models containing building elements and information"),
    ("A5", "Integrate the design of active systems in reference models"),
    ("A6", "Operate BIM applications and software"),
    ("A7", "Interpret data within BIM outputs"),
    ("A8", "Analyse the design performance and compliance of the relevant systems"),
    ("A9", "Develop BIM documentation"),
]
TSC_KNOWLEDGE = [
    ("K1",  "Principles of BIM"),
    ("K2",  "Value proposition of BIM"),
    ("K3",  "Requirements of BIM"),
    ("K4",  "Definition of BIM"),
    ("K5",  "Application of BIM"),
    ("K6",  "Technology used in BIM"),
    ("K7",  "BIM design processes"),
    ("K8",  "Documentation required for BIM"),
    ("K9",  "Databases and information systems required for BIM"),
    ("K10", "BIM e-submission documentation requirements and standards"),
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Apply Revit for Building Information Modelling (BIM)",
    "LO2: Develop models and integrate design for BIM",
    "LO3: Apply BIM and check the output",
    "LO4: Maintain BIM database and develop BIM documentation",
]

# ------------------------------------------------------------------ topics (= learning units)
TOPICS = [
    dict(num=1, code="01",
         title="Introduction to BIM and Revit",
         subtitle="What is BIM · principles of BIM · value proposition · requirements and applications · introduction of Revit for BIM",
         weighting="K1–K4 · A1, A2 · LO1",
         concepts=[
            ("BIM is a process, not a drawing", "An intelligent 3D model-based process giving AEC professionals the insight to plan, design, construct and manage buildings and infrastructure."),
            ("One model, whole lifecycle", "The BIM process — Plan, Design, Build, Operate — creates intelligent data that is used across the entire life of a built asset."),
            ("Dimensions beyond 3D", "3D geometry, 4D time, 5D cost, 6D sustainability, 7D facility management and 8D safety add information layers to the model."),
            ("The value proposition", "Greater efficiency, lower cost and wastage, better estimates, deeper insight, closer collaboration and better end results."),
            ("Requirements frame the work", "OIR, AIR, EIR, the BIM Execution Plan (BEP), PIM and AIM define what information is delivered, by whom and when."),
            ("Revit is a BIM authoring tool", "A single, integrated parametric model to conceptualise, design and document a project — used by architects, engineers and contractors."),
         ]),
    dict(num=2, code="02",
         title="BIM Modeling",
         subtitle="Develop models for building elements · walls, floors, ceilings, roofs, stairs, structure · site and topography · massing · BIM design integration",
         weighting="K6, K7 · A4, A5 · LO2",
         concepts=[
            ("Everything is parametric", "Each component has parametric qualities — change the model once and every related view, schedule and sheet updates automatically."),
            ("Model with the right tool", "Walls, curtain walls, floors, ceilings, roofs, stairs, railings — each element is created with its dedicated tool and family type."),
            ("Structure lives in the model", "Structural columns, beams, beam systems, trusses and braces carry the load path inside the same coordinated model."),
            ("Site gives context", "Toposurfaces, subregions, graded regions and building pads model the terrain the building sits on."),
            ("Mass first, detail later", "Conceptual masses and generative design (Dynamo) explore building volumes before committing to detailed elements."),
            ("Families drive integration", "System, loadable and in-place families — with materials and parameters — integrate design information into every element."),
         ]),
    dict(num=3, code="03",
         title="BIM Application",
         subtitle="Apply and operate BIM · technologies used in BIM · interpret output · schedules and quantity takeoffs · analyse performance and check compliance",
         weighting="K5 · A6, A7, A8 · LO3",
         concepts=[
            ("BIM manages the build", "Construction simulation, information statistics and real-time monitoring strengthen quality and process management on site."),
            ("Views interpret the model", "View range, view templates, callouts and section views turn one model into many purpose-built, readable outputs."),
            ("Schedules read the database", "Schedules and quantity takeoffs tabulate elements straight from the model — the model IS the quantity database."),
            ("Cost from the model", "Calculated-value formulas and material takeoffs produce preliminary cost estimates that update as the design changes."),
            ("Analyse before you build", "Revit Systems Analysis translates the model to EnergyPlus to simulate heating, cooling and annual energy performance."),
            ("Check, then comply", "Interference (clash) checks and analysis reports verify design performance and compliance before construction."),
         ]),
    dict(num=4, code="04",
         title="BIM Documentation",
         subtitle="Maintain BIM databases and information systems · documentation required for BIM · BIM e-submission requirements and standards",
         weighting="K8–K10 · A3, A9 · LO4",
         concepts=[
            ("Documents govern BIM", "BIM standards, BEP, BIP, PEP, EIR, MIDP and the Common Data Environment (CDE) govern how project information is produced and shared."),
            ("The BEP is the baseline", "The BIM Execution Plan records goals, roles, deliverables, level of detail and exchange protocols — agreed at project start."),
            ("Deliverables are agreed early", "Site, massing, architectural, structural and MEP models, schedules, shop drawings, as-builts and FM data — with dates."),
            ("Databases need discipline", "SVY21 geo-referencing, 1:1 metric scale, file/view naming formats, colour standards and federated file structures keep the database usable."),
            ("Worksharing maintains one truth", "A central model with worksets, linked files and phases lets the whole team maintain one coordinated information system."),
            ("e-Submission has rules", "BCA BIM e-submission: last-saved views, cover page, core information and discipline-specific requirements must all be checked."),
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "BIM fundamentals, Revit and BIM modeling",
    2: "BIM application, documentation and assessment",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — hands-on Revit modeling tasks, 1.5 hours, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)

# ------------------------------------------------------------------ links
PRACTICE_EXAM_URL = "https://exams.tertiaryinfotech.com"
LMS_URL = "https://lms-tms.tertiaryinfotech.com"

RECOMMENDED_COURSES = [
    "WSQ - Technical Drawing with AutoCAD",
    "WSQ - Architecture Drawing with Revit",
    "WSQ - Product Design with Fusion 360",
    "WSQ - AutoCAD Civil 3D for Infrastructure Design",
    "WSQ - Product Design with Autodesk Inventor",
]
