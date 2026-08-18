"""Teaching slides per topic — content and graphics carried over from the
legacy v9 master deck (Tertiary Infotech's own courseware), refreshed into the
house visual components.

Slide kinds rendered by build_slides.py:
  ("tiles", title, kicker, items, cols, size)         items: str or (head, caption)
  ("pic",   title, kicker, bullets, image, imgw)      bullets left · image right (imgw inches, 0=auto)
  ("img",   title, kicker, image, caption)            full-width image slide
  ("banner",title, kicker, bullets, image)            wide ribbon-strip image on top, bullets below
  ("two",   title, kicker, left, right, lhead, rhead)
  ("flow",  title, kicker, steps)
  ("big",   line1, line2, kicker)
Images are looked up in courseware/assets/legacy/.
"""

TEACHING = {

# ------------------------------------------------------------------ TOPIC 1
1: [
 ("img","BIM in the Building Lifecycle","WHAT IS BIM","slide017_img4.png",
  "Building Information Modelling spans design, construction and operation."),
 ("pic","What is BIM?","DEFINITION · K4",[
   "An intelligent 3D model-based process that gives AEC professionals every detail needed to plan, design, construct and manage buildings and infrastructure.",
   "Design and construction teams work more efficiently while capturing the data they create — benefiting operations, maintenance and future planning.",
   "Used across architecture, civil engineering, construction, plant, MEP and structural engineering to make better design decisions and improve building performance.",
  ],"slide019_img5.png",5.6),
 ("tiles","The Process of BIM — Plan · Design · Build · Operate","BIM PROCESS · K1",[
   ("Plan","Combine reality capture and real-world data to generate context models of the existing built and natural environment."),
   ("Design","Conceptual design, analysis, detailing and documentation — BIM data informs scheduling and logistics before construction begins."),
   ("Build","Fabrication starts from BIM specifications; construction logistics are shared with trades and contractors for optimum timing."),
   ("Operate","BIM data carries over to operations and maintenance — and later to cost-effective renovation or efficient deconstruction."),
  ],2,14),
 ("img","Principles of BIM","PRINCIPLES · K1","slide023_img9.png",
  "The BIM principles: one shared, coordinated, data-rich model across the project lifecycle."),
 ("pic","BIM Dimensions — 3D Geometry","BIM DIMENSIONS · 1 OF 6",[
   "3D BIM is the most common model type — the three geographic dimensions (x, y, z) of a structure.",
   "Helps stakeholders visualise the structure before the project starts.",
   "Gives AEC professionals the insight and tools to plan, design, construct and manage more efficiently.",
  ],"slide024_img10.png",4.6),
 ("pic","BIM Dimensions — 4D Time","BIM DIMENSIONS · 2 OF 6",[
   "The 4th dimension adds project duration — timeline and scheduling information show how the project evolves over time.",
   "Extremely helpful for early-stage conflict detection, site planning and scheduling optimisation.",
   "Better communicates the next steps to stakeholders during every stage of construction.",
  ],"slide025_img11.png",3.8),
 ("pic","BIM Dimensions — 5D Cost","BIM DIMENSIONS · 3 OF 6",[
   "5D BIM visualises budget analysis and cost estimation — analysing project costs over time.",
   "Especially useful early on, to estimate costs of different design or construction scenarios.",
   "Tracks predicted vs actual cost with real-time notifications of cost overrun.",
  ],"slide026_img12.png",3.4),
 ("pic","BIM Dimensions — 6D Sustainability","BIM DIMENSIONS · 4 OF 6",[
   "6D BIM makes a structure self-sustainable and energy-efficient.",
   "Stakeholders analyse energy consumption and estimate energy usage during the initial design phase.",
   "Reduces energy consumption in the long run and improves operational management after construction.",
  ],"slide027_img13.png",4.2),
 ("pic","BIM Dimensions — 7D Facility Management","BIM DIMENSIONS · 5 OF 6",[
   "7D BIM improves operations and facility management for building owners and managers.",
   "Tracks asset data: status, warranty information, technical specifications, maintenance and operation manuals.",
   "Improves the maintenance process by listing all replacement parts and specifications.",
  ],"slide028_img14.png",4.2),
 ("tiles","BIM Dimensions — 8D Safety, and the Full Stack","BIM DIMENSIONS · 6 OF 6",[
   ("3D — Geometry","The shared x, y, z model every stakeholder visualises."),
   ("4D — Time","Schedule linked to the model; the build sequence becomes visible."),
   ("5D — Money","Cost estimation and budget tracking over time."),
   ("6D — Sustainability","Energy analysis from the design stage onwards."),
   ("7D — Facility Management","Asset data for operations and maintenance."),
   ("8D — Safety","Safety information added at design and execution — an overall picture of site risks and hazards for workers, before they occur."),
  ],2,13),
 ("tiles","Value Proposition — Advantages of BIM (1–4)","VALUE PROPOSITION · K2",[
   ("Maximised efficiency","Shorter project lifecycles; pre-construction and planning phases become easier to manage — everyone works off one up-to-date model, reducing errors and rework."),
   ("Reduced costs and wastage","Better material choices and streamlined construction work minimise human error and wasted materials — cutting cost."),
   ("Improved cost estimates","Model-based estimates from a detailed 3D model are more realistic and accurate, and quantity takeoffs become far easier."),
   ("Better insight into the project","A realistic 3D look at the eventual outcome helps contractors and clients feel the built asset — changes happen in pre-construction, not on site."),
  ],2,13),
 ("tiles","Value Proposition — Advantages of BIM (5–7)","VALUE PROPOSITION · K2",[
   ("Communication & collaboration","Cloud-based BIM lets everyone access up-to-date models anywhere, any time — estimates, models and design notes in one place."),
   ("Less risk","Closer collaboration reduces tender risk premiums, improves on-site safety and removes the risk of building from outdated information."),
   ("Better end results","Better planning and earlier visualisation produce a higher-quality build and a higher-quality built asset."),
   ("The common thread","Every advantage flows from one source: a single shared intelligent model that all stakeholders trust."),
  ],2,13),
 ("pic","The BIM Execution Plan (BEP)","REQUIREMENTS · K3",[
   "The BEP is the baseline document, approved by the Employer, that guides the project team in achieving the goals set — including BIM deliverables — throughout the project.",
   "It specifies the roles and responsibilities of project members when using BIM at different stages.",
   "It details how deliverables are created, coordinated, maintained and shared to satisfy the project goals.",
   "Defined at project start; updated (with the Employer's or BIM Manager's permission) when members or BIM uses change.",
  ],"slide038_img21.png",5.2),
 ("tiles","Typical Content of a BEP","REQUIREMENTS · K3",[
   "Project information","Project members",
   "Project goals & BIM uses for each project stage","BIM deliverables for each BIM use",
   "Model author and users for each deliverable","Model elements, level of detail and attributes",
   "Process for BIM creation, maintenance and collaboration","Exchange protocol, submittal format, technology infrastructure & software",
  ],2,13),
 ("tiles","Requirements of BIM — the Information Chain","REQUIREMENTS · K3",[
   ("OIR — Organisational Information Requirements","What the organisation needs to know to run its business."),
   ("AIR — Asset Information Requirements","What the organisation needs to know about the assets it is responsible for."),
   ("EIR — Employer Information Requirements","The information to be delivered, and the standards and processes to be adopted, for a construction project."),
   ("BEP — BIM Execution Plan","The overall vision and implementation details the project team follows throughout the project."),
   ("PIM — Project Information Model","The information model developed during the design and construction phase."),
   ("AIM — Asset Information Model","Graphical and non-graphical data, documents and metadata that support asset management."),
  ],2,12),
 ("pic","What is Revit?","INTRODUCING REVIT · A2",[
   "A BIM-based platform used by architects, engineers, contractors and designers to create one unified model of real-life information.",
   "A design and documentation platform: one integrated building information model to conceptualise, design and document a project.",
   "Virtual modelling — see the building or infrastructure before it is built on-site.",
   "Its tools are built for BIM: an intelligent model with data stored in it — helping you avoid rework, minimise cost, detect conflicts before construction and avoid delays.",
  ],"slide043_img22.png",5.2),
],

# ------------------------------------------------------------------ TOPIC 2
2: [
 ("tiles","Develop Models for Building Elements","WHY REVIT MODELING · K7",[
   ("Parametric objects","Each component has parametric qualities that drive its behaviour."),
   ("Quick changes, no repetition","One change updates every related component, view, detail and document automatically."),
   ("Construction documentation","High-quality documentation produced automatically from the 3D model."),
   ("Quantities & cost estimation","Generated automatically from the data inserted in the model."),
   ("Coordination & 3D visualisation","Shared models reduce conflicts and communicate design to client and team."),
   ("Interoperability","Revit imports, exports and links data in common formats such as IFC."),
  ],2,13),
 ("banner","Modeling Walls","WALLS · A4",[
   "Add instances of a wall type in a floor plan or 3D view: Architecture ▸ Build ▸ Wall ▸ Wall: Architectural (structural walls work the same way).",
   "Pick the wall type in the Type Selector; adjust instance properties in the Properties palette before placing.",
   "Options Bar: Level (base constraint), Height (top constraint), Location Line (which plane follows the cursor), Chain, Offset and Join Status.",
  ],"slide048_img23.png"),
 ("pic","Wall Placement Options","WALLS · A4",[
   "Location Line — align the wall's centreline, core face or finish face with the cursor as you draw.",
   "Chain — draw a series of wall segments connected at endpoints.",
   "Offset — place the wall's location line at a distance from the cursor or a picked line/face.",
   "Join Status — Allow creates a butt join where walls intersect; Disallow prevents joining.",
  ],"slide051_img24.png",4.6),
 ("pic","Stacked and Embedded Walls","WALLS · A4",[
   "Stacked walls: two or more subwalls of different thicknesses stacked at different heights — attached, with joined geometry.",
   "Embed a wall into a host wall (wall-in-wall, wall-in-curtain-wall or curtain-wall-in-wall).",
   "The embedded wall must be smaller than its host; use Cut Geometry, picking the HOST wall first, then the wall to embed.",
   "Resize an embedded wall with its drag controls after embedding.",
  ],"slide052_img25.png",3.8),
 ("pic","Modeling Curtain Walls","CURTAIN WALLS · A4",[
   "A curtain wall is placed like any wall — just select a curtain wall type (Curtain Wall 1, Exterior Glazing, Storefront) in the Type Selector.",
   "Divide the wall into panels with Curtain Grid; customise grids with Add/Remove Segments.",
   "Place mullions on grid lines; Tab-select any panel to change its type — even to a door panel.",
   "Doors and walls can be embedded within curtain panels.",
  ],"slide057_img28.png",5.2),
 ("banner","Modeling Floors and Openings","FLOORS · A4",[
   "Create a floor by picking walls or sketching its boundary — the boundary must be a closed loop; sketch a second loop inside to form an opening.",
   "Options Bar: Offset for floor edges; 'Extend into wall (to core)' measures the offset from the wall's core.",
   "Opening tools: By Face (perpendicular to the face), Vertical (perpendicular to a level), Shaft (cuts every level it spans), Wall Opening and Dormer.",
  ],"slide060_img29.png"),
 ("pic","Shaft Openings and View Range","FLOORS · A4",[
   "A Shaft cuts through roofs, floors and ceilings across its Base and Top Constraints — move it on one level and it moves on all levels.",
   "Every plan view has a View Range: Top, Cut Plane and Bottom planes define what is shown and how.",
   "View Depth adds a plane beyond the primary range to show elements below the bottom clip plane.",
  ],"slide063_img30.png",4.8),
 ("pic","Modeling Ceilings and Roofs","CEILINGS & ROOFS · A4",[
   "Ceilings are placed in a reflected ceiling plan — Automatic Ceiling fills a closed wall loop; Sketch Ceiling draws a custom boundary.",
   "Roof by Footprint: sketch/pick a closed loop in a plan view; slope-defining edges create hips and gables.",
   "A roof cannot cut through windows or doors.",
  ],"slide067_img33.png",4.8),
 ("pic","Roof by Extrusion","CEILINGS & ROOFS · A4",[
   "Create a roof by extruding an open-loop profile sketched in an elevation, 3D or section view.",
   "Set the Roof Reference Level and Offset — a reference plane controls the roof's position.",
   "After creating it, attach walls to the roof, rehost it or edit its work plane.",
  ],"slide070_img36.png",4.2),
 ("banner","Modeling Stairs and Railings","CIRCULATION · A4",[
   "Stairs assemble from components in edit mode: runs (straight, spiral, U-, L-shaped, sketched), landings, supports and railings.",
   "Railings: free-standing on levels, attached to hosts (floors, ramps, stairs), auto-created with stairs, or sketched with a custom path and Pick New Host.",
   "Tile plan + 3D views while assembling to see the full stair model as you work.",
  ],"slide072_img38.png"),
 ("pic","Site and Topography","SITE · A4",[
   "The Toposurface tool defines terrain from points placed at absolute or relative elevations, in 3D or site plan views.",
   "Subregion applies different properties (e.g. material) to an area; Split and Merge Surfaces divide and rejoin terrain; Graded Region develops the proposed site design.",
   "A Building Pad sketched on the toposurface cuts the terrain at a controlled level offset — with openings and slope if needed.",
  ],"slide075_img40.png",5.0),
 ("pic","Structural Columns and Framing","STRUCTURE · A5",[
   "Structural columns add vertical load-bearing elements: Structure ▸ Column, or At Grids for batch placement.",
   "Beams span supports; a Beam System fills a boundary with members per a layout rule; 3D option for sloped systems.",
   "Trusses place framing per the selected truss family's layout; braces sketch diagonally between structural elements in plan or framing elevations.",
  ],"slide083_img56.png",3.6),
 ("banner","Conceptual Masses","MASSING · A4",[
   "Mass modeling drafts conceptual volumes fast — as Conceptual Mass families (outside the project) or In-Place Masses (inside it).",
   "Use massing studies for design options, phase representation, zoning compliance (visually and numerically) and assembling complex forms from mass families.",
   "Generate floors, roofs, curtain systems and walls from mass instances — regenerating under control when the mass changes; schedule gross volume, floor area and surface area.",
  ],"slide092_img64.png"),
 ("pic","Generative Design and Dynamo","GENERATIVE DESIGN · K6",[
   "Generative design (AEC Collection) generates design alternatives from your inputs, constraints and goals.",
   "Dynamo is Revit's visual-programming add-in — open-source graphical programming for custom computational design and BIM automation.",
   "Workflow: build a Dynamo graph, declare Is Input / Is Output on nodes, export for generative design, then review the study's outcomes.",
  ],"slide094_img65.png",5.4),
 ("two","Families and Parameters","FAMILIES · K6",
  [("System families",0),("Walls, roofs, floors, ducts, pipes — predefined in Revit, never loaded from external files",1),
   ("Levels, grids, sheets and viewports are system families too",1),
   ("In-place families",0),("Unique, project-specific elements created with Family Editor tools",1),
   ("Reference other geometry and adjust when it changes",1)],
  [("Loadable families",0),("Windows, doors, casework, fixtures, furniture, boilers, plumbing — RFA files loaded via Insert ▸ Load Family",1),
   ("Combine into nested and shared families",1),
   ("Type catalogs",0),("Load only the types you need from large families (e.g. one C-Channel size, not dozens)",1),
   ("Keeps project size down and the Type Selector short",1)],
  "The three kinds","Loading & catalogs"),
 ("pic","Materials","MATERIALS · A5",[
   "Materials control how elements display in views and rendered images: Manage ▸ Settings ▸ Materials.",
   "They define Graphics, Appearance, Thermal and Physical information — for visualisation, analysis and scheduling.",
   "Apply by category or subcategory, by family, by element parameter, or by face with the Paint tool.",
  ],"slide080_img42.png",4.2),
],

# ------------------------------------------------------------------ TOPIC 3
3: [
 ("img","Technologies Used in BIM","TECHNOLOGY LANDSCAPE · K6","slide141_img76.png",
  "The technology stack around BIM: authoring, analysis, collaboration, field and FM tools."),
 ("pic","Application of BIM in Construction Management","APPLICATION · K5",[
   "BIM supports construction simulation and information statistics — management processes become visual and controllable.",
   "Quality management covers both the product and the technical process.",
   "Real-time monitoring of the construction process helps ensure construction quality on site.",
  ],"slide142_img77.png",5.6),
 ("pic","Interpreting the Model — View Range and Callouts","INTERPRET OUTPUT · A7",[
   "View Range (Top, Cut Plane, Bottom + View Depth) controls what a plan view shows and how elements are cut.",
   "Callouts enlarge part of a plan, section, detail or elevation — the callout tag links parent view to callout view.",
   "Delete the parent view and its callouts go with it; load a callout head to place callout tags.",
  ],"slide103_img68.png",4.4),
 ("banner","Section Views","INTERPRET OUTPUT · A7",[
   "Add a section line and crop region to define a new section view: View ▸ Create ▸ Section, drag through the model, resize the crop with the blue controls.",
   "Open the section by double-clicking its header or from the Project Browser's Sections group.",
   "The section view updates whenever the design changes or the section line moves.",
  ],"slide105_img69.png"),
 ("flow","Creating a Schedule or Quantity","SCHEDULES · A7",[
   "View ▸ Schedules ▸ Schedule/Quantities",
   "Pick the category and phase",
   "Select fields to report",
   "Filter, sort and group the data",
   "Format the schedule's appearance",
   "The schedule fills itself from the model",
  ]),
 ("tiles","Quantity Takeoffs and Cost Estimates","COST · A7",[
   ("Quantity takeoffs","Essential for accurate construction cost estimating — quantify elements from the model and track element-status changes with ongoing analysis."),
   ("Material takeoffs","Tabulate materials and areas across categories — more comprehensive than component schedules alone."),
   ("Calculated values","Formula-driven reporting fields for schedules and tag labels — e.g. Cost = Area × rate; the Name becomes the column header."),
   ("Massing studies","Mass floor schedules report gross volume, floor area and surface area — preliminary cost feedback that updates as the mass changes."),
  ],2,13),
 ("pic","Revit Systems Analysis — Workflow","ANALYSE PERFORMANCE · A8",[
   "Set up the model: building elements or masses, plus location; add analytical systems and define system zones; generate and revise analytical spaces.",
   "Revit translates the data to EnergyPlus, which runs the simulation — two default workflows: system sizing (heating/cooling loads) and annual energy simulation.",
   "Re-running with the same Building Type, Operating Schedule and Location groups results in the same folder; change them and a new folder is created.",
  ],"slide147_img78.png",4.6),
 ("pic","Reviewing Analysis Results","ANALYSE PERFORMANCE · A8",[
   "Reports: Project Browser ▸ Reports ▸ Analysis Reports — a time-stamped report per run; switch Report Style between Detailed and Loads.",
   "Compare runs: select multiple simulations and click Compare in Results & Compare.",
   "Peak heating, cooling and airflow demands are also set as properties on each analytical space — the numbers live on the model.",
  ],"slide147_img79.png",4.6),
 ("tiles","Check Your Understanding — BIM Application","QUIZ",[
   ("What is a 4D BIM model?","A 3D model with the addition of time or scheduling data."),
   ("Avoiding conflicts between systems?","Stakeholders use clash detection software on the shared model — not emailed copies."),
   ("Design authoring is…","The process by which 3D software is used to develop a building information model."),
   ("Interference Check","Revit's built-in clash detection: Collaborate ▸ Coordinate ▸ Interference Check."),
  ],2,13),
],

# ------------------------------------------------------------------ TOPIC 4
4: [
 ("tiles","Documentation Required for BIM","DOCUMENTATION · K8",[
   ("BIM Standard","The standards the project's BIM must follow."),
   ("BEP — BIM Execution Plan","Overall vision + implementation details the team follows throughout the project."),
   ("BIP — BIM Implementation Plan","How the organisation rolls BIM into its practice."),
   ("PEP — Project Execution Plan","The project-wide delivery plan BIM slots into."),
   ("EIR — Employer's Information Requirements","What information the employer requires, when and how."),
   ("MIDP & CDE","Master Information Delivery Plan schedules deliverables; the Common Data Environment is the single place information is shared."),
  ],2,12),
 ("tiles","BIM Deliverables — Agreed Early, With Dates","DOCUMENTATION · K8",[
   ("Models","Site model, massing model, architectural / structural / MEP models."),
   ("Model uses","Regulatory submissions, coordination and clash detection, visualisation, cost estimation."),
   ("Programme","Schedule and phasing programme — in BIM or spreadsheet."),
   ("Construction","Construction and fabrication models, shop drawings."),
   ("Handover","As-built model in native or open formats; data for facility management."),
   ("When agreed","At project start, and after the main project members are appointed."),
  ],2,12),
 ("two","Producing Drawings and Specifications","DRAWINGS & SPEC · A9",
  [("Architectural guidelines",0),
   ("Model in stages: Conceptual, Preliminary, Detailed, Construction, As-Built",1),
   ("Use the correct tool per element (Wall tool, Slab tool …); set 'Type' correctly when improvising",1),
   ("2D may complement the model for elements smaller than the agreed size (e.g. < 100 mm)",1),
   ("Model elements separately per storey",1)],
  [("Structural guidelines",0),
   ("Structural consultant produces an analysis model AND a physical model (Structural BIM)",1),
   ("Covers load-bearing concrete, wood and steel + non-load-bearing concrete",1),
   ("Rebar and joint details in Detailed Design stage, per tool capability",1),
   ("Required parameters: Type, Material, ID, Size — Type drives quantity takeoff",1)],
  "Architecture","Structure"),
 ("img","Databases and Information Systems for BIM","DATABASES · K9","slide161_img82.png",
  "The project information database: models, documents and structured data flowing through a common data environment."),
 ("tiles","Model Orientation, Site Configuration and Scale","SINGAPORE STANDARDS · K9",[
   ("SVY21 coordinates","Geo-reference the site model to SVY21 for Easting and Northing (x, y)."),
   ("Singapore Height Datum","Elevations set from SHD 0.000 m for height (z)."),
   ("True North","Present the site model layout in True North / real-world orientation."),
   ("Full-size metric","Model at 1:1 in metric; 2D views generated from the model must not use odd drawing scales."),
  ],2,13),
 ("pic","File Naming Format","SINGAPORE STANDARDS · K9",[
   "The e-submission file name consists of 6 fields: project, originator, volume/zone, level, file type and discipline.",
   "Consistent naming keeps the federated model navigable for every party and every agency.",
  ],"slide164_img83.png",6.2),
 ("pic","File Naming — Worked Examples","SINGAPORE STANDARDS · K9",[
   "Architectural, MEP and structural files each follow the same 6-field pattern with their discipline code.",
   "The examples show real project file names for each discipline.",
  ],"slide166_img85.png",6.2),
 ("pic","File Structure — Single vs Federated","SINGAPORE STANDARDS · K9",[
   "Single file: one BIM file holds everything — suitable for small projects with one main building.",
   "Federated / linked files: several BIM files linked together — for multi-building or large projects.",
   "Use UNC or relative paths for links; folders no more than two sub-folders deep.",
  ],"slide169_img88.png",5.6),
 ("pic","View Naming Format","SINGAPORE STANDARDS · K9",[
   "View names use 3–4 fields (one field is agency-specific).",
   "The View Name field describes the particular view: 1st Storey, North Elevation, Section AA, Fire Protection Legend, Door Schedule.",
   "Views used in a submission keep exactly their View Name.",
  ],"slide172_img91.png",5.4),
 ("pic","Colour Standards for Submissions","SINGAPORE STANDARDS · K10",[
   "Amendments to approved plans use the agencies' prescribed colours.",
   "Addition & Alteration (A&A) works have their own colour scheme.",
   "Correct colours let the regulatory officer read what changed at a glance.",
  ],"slide173_img92.png",5.6),
 ("tiles","e-Submission — Last Saved Views Checklist","E-SUBMISSION · K10",[
   ("Maximum extent","Each view is saved at its maximum extent — agencies check the Last Saved Model and Views."),
   ("Nothing hidden","No hidden objects or annotations remain in the submitted views."),
   ("External files load","Every external file that forms part of the submission loads; none missing or unreadable."),
   ("Purged","External references, irrelevant layers, drafting work and construction lines removed before submission."),
   ("Legible fonts","No proprietary fonts; all annotation fonts legible."),
   ("All phases display","Objects and annotations in each phase display in the last saved view."),
  ],2,12),
 ("pic","e-Submission Cover Page and Core Information","E-SUBMISSION · K10",[
   "The cover page carries: (1) submission authority and endorsements / QP's declaration, (2) project information, (3) the list of views, schedules and sheets for approval.",
   "All submissions carry the minimal Core Information (CI) specified by the respective regulatory agency.",
   "Discipline-specific requirements come from the Code of Practice for BIM e-Submission.",
  ],"slide179_img94.png",5.2),
 ("pic","Drawing Sheets","DOCUMENTATION · A9",[
   "A construction document set consists of sheets: View ▸ Sheet Composition ▸ Sheet.",
   "Drag a view or schedule onto the sheet — it becomes a viewport within the title block.",
   "Project templates capture sheet, view and family standards for future projects (File ▸ New ▸ Project template).",
  ],"slide106_img70.png",4.6),
 ("pic","Worksharing — One Central Model","MAINTAIN THE DATABASE · A3",[
   "Worksharing lets multiple team members work on the same project model at the same time, each on a functional area.",
   "Enable it via Collaborate ▸ Worksets: default worksets are created, then Save As publishes the central model.",
   "Team members edit local copies and synchronise with the central model.",
  ],"slide130_img72.png",5.2),
 ("pic","Phases and Design Options","MAINTAIN THE DATABASE · A3",[
   "Phases track stages of work (Existing, New Construction, +custom): Manage ▸ Phasing ▸ Phases; insert before/after and rename.",
   "Design options develop alternatives (entries, roofs, layouts) inside one project file while the team continues on the main model.",
   "Options become more focused and simplified as the project progresses.",
  ],"slide135_img73.png",5.0),
 ("tiles","Check Your Understanding — BIM Documentation","QUIZ",[
   ("BIM Level 1","The level using 2D and 3D modeling where only CAD/PDF versions are shared with other stakeholders."),
   ("LOD specifications","Level of Development is defined at the BEGINNING of a project."),
   ("Record model","An accurate 3D representation of the physical, environmental and informational assets of a facility."),
   ("Where it's governed","The BEP + the agencies' e-submission Code of Practice."),
  ],2,13),
],
}
