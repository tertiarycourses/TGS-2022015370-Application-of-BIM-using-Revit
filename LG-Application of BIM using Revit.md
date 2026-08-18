# Application of BIM using Revit — Learner Guide

**WSQ Course Code:** TGS-2022015370  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v10 · 18 August 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Skills Framework Alignment](#skills-framework-alignment)
- [Before You Start — Environment Setup](#before-you-start--environment-setup)
- [Topic 01 — Introduction to BIM and Revit  (K1–K4 · A1, A2 · LO1)](#topic-01--introduction-to-bim-and-revit--k1k4--a1-a2--lo1)
  - [Lab 1 — Get Started with Revit](#lab-1--get-started-with-revit)
  - [Lab 2 — Convert 2D Information into a 3D Model](#lab-2--convert-2d-information-into-a-3d-model)
- [Topic 02 — BIM Modeling  (K6, K7 · A4, A5 · LO2)](#topic-02--bim-modeling--k6-k7--a4-a5--lo2)
  - [Lab 3 — Modeling Walls — Reveals, Embedded and Curtain Walls](#lab-3--modeling-walls--reveals-embedded-and-curtain-walls)
  - [Lab 4 — Floors, Ceilings, Roofs and Openings](#lab-4--floors-ceilings-roofs-and-openings)
  - [Lab 5 — Stairs, Railings and Structural Elements](#lab-5--stairs-railings-and-structural-elements)
  - [Lab 6 — Terrain, Building Pad and Conceptual Mass](#lab-6--terrain-building-pad-and-conceptual-mass)
- [Topic 03 — BIM Application  (K5 · A6, A7, A8 · LO3)](#topic-03--bim-application--k5--a6-a7-a8--lo3)
  - [Lab 7 — View Templates, Schedules and Quantity Takeoffs](#lab-7--view-templates-schedules-and-quantity-takeoffs)
  - [Lab 8 — Energy Analysis and Design Compliance Checks](#lab-8--energy-analysis-and-design-compliance-checks)
- [Topic 04 — BIM Documentation  (K8–K10 · A3, A9 · LO4)](#topic-04--bim-documentation--k8k10--a3-a9--lo4)
  - [Lab 9 — Sheets, Worksharing and Linked Models](#lab-9--sheets-worksharing-and-linked-models)
  - [Lab 10 — BIM e-Submission Standards Check](#lab-10--bim-e-submission-standards-check)
- [Assessment Focus — How the Final Assessment Maps to This Guide](#assessment-focus--how-the-final-assessment-maps-to-this-guide)
- [Assessment Preparation](#assessment-preparation)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the WSQ course Application of BIM using Revit (TGS-2022015370), conducted by Tertiary Infotech Academy Pte Ltd. It provides step-by-step instructions for the 10 hands-on Autodesk Revit labs, organised by the four course topics, and is aligned to the Skills Framework TSC Building Information Modelling Application (BEV-TEM-3027-1.1-1). Every lab maps to a course learning outcome, and everything assessed in the final Written Assessment (K1–K10) and Practical Performance (A1–A9) is taught in these pages.

Use this guide alongside the course slides and the lab dataset files in the labs/ folder of the course repository (also downloadable from the LMS). Each lab has its own folder containing a README with the full steps plus the Revit project files (.rvt) it uses. The guide is your open-book companion during the final assessment.


## Course Learning Outcomes

- LO1: Apply Revit for Building Information Modelling (BIM)
- LO2: Develop models and integrate design for BIM
- LO3: Apply BIM and check the output
- LO4: Maintain BIM database and develop BIM documentation


## Skills Framework Alignment

This course maps to the Skills Framework for the Built Environment TSC: Building Information Modelling Application (BEV-TEM-3027-1.1-1).

**TSC Knowledge (assessed by the Written Assessment)**

- K1 — Principles of BIM
- K2 — Value proposition of BIM
- K3 — Requirements of BIM
- K4 — Definition of BIM
- K5 — Application of BIM
- K6 — Technology used in BIM
- K7 — BIM design processes
- K8 — Documentation required for BIM
- K9 — Databases and information systems required for BIM
- K10 — BIM e-submission documentation requirements and standards

**TSC Abilities (assessed by the Practical Performance)**

- A1 — Identify BIM application and development in industry
- A2 — Identify BIM's interoperability with other analysis tools
- A3 — Maintain databases and information systems for BIM
- A4 — Develop models containing building elements and information
- A5 — Integrate the design of active systems in reference models
- A6 — Operate BIM applications and software
- A7 — Interpret data within BIM outputs
- A8 — Analyse the design performance and compliance of the relevant systems
- A9 — Develop BIM documentation


## Before You Start — Environment Setup

**What you need**

- Autodesk Revit 2024 or 2025 installed on Windows (free 30-day trial, or an education licence from students.autodesk.com).
- The Revit sample projects installed with Revit (e.g. rac_basic_sample_project.rvt) for Labs 1 and 8.
- The course lab dataset files (.rvt, .pdf, .png) — in each lab's folder in the course repository, or downloadable from the LMS at https://lms-tms.tertiaryinfotech.com.
- A 3-button mouse (the middle button/wheel drives pan, zoom and orbit in Revit).

**Launch and verify Revit**

Start Revit and confirm you can open the basic sample architecture project from the Home screen. Check the ribbon shows the Architecture, Structure, Insert, Annotate, Analyze, Massing & Site, Collaborate, View and Manage tabs — the labs use all of them.

**Conventions used in every lab**

- Ribbon paths are written as Tab ▸ Panel ▸ Tool (e.g. Architecture ▸ Build ▸ Wall).
- Each lab folder contains the starter .rvt file(s) it needs; solution files (where provided) let you check your result.
- Save your work as <LabNN>_<YourName>.rvt so the trainer can review it.
- If a family or template is missing, load it via Insert ▸ Load Family or pick the closest available type.
- Imperial vs metric: the lab files use the units they were authored in — follow the values printed in the steps.


## Topic 01 — Introduction to BIM and Revit  (K1–K4 · A1, A2 · LO1)

What is BIM · principles of BIM · value proposition · requirements and applications · introduction of Revit for BIM

**Key concepts**

- BIM is a process, not a drawing — An intelligent 3D model-based process giving AEC professionals the insight to plan, design, construct and manage buildings and infrastructure.
- One model, whole lifecycle — The BIM process — Plan, Design, Build, Operate — creates intelligent data that is used across the entire life of a built asset.
- Dimensions beyond 3D — 3D geometry, 4D time, 5D cost, 6D sustainability, 7D facility management and 8D safety add information layers to the model.
- The value proposition — Greater efficiency, lower cost and wastage, better estimates, deeper insight, closer collaboration and better end results.
- Requirements frame the work — OIR, AIR, EIR, the BIM Execution Plan (BEP), PIM and AIM define what information is delivered, by whom and when.
- Revit is a BIM authoring tool — A single, integrated parametric model to conceptualise, design and document a project — used by architects, engineers and contractors.


### Lab 1 — Get Started with Revit

Objective: LO1 — Apply Revit for Building Information Modelling (BIM).

Goal: Tour the Revit environment on a real model: open the Autodesk sample architecture project, learn the ribbon, Properties palette, Project Browser and drawing area, then navigate plans, elevations, sections and the 3D view.

**What you'll build**

A guided tour of a complete BIM model — you can open any view, orbit the 3D model and inspect element properties.   (Tools: Autodesk Revit 2024/2025, Autodesk sample project (rac_basic_sample_project.rvt).)

**Step-by-step**

1. Launch Revit. On the Home screen under Models click Open, browse to the Revit sample files and open the basic architecture sample project.

   ```bash
   Home ▸ Models ▸ Open ▸ rac_basic_sample_project.rvt
   ```

2. Identify the four working zones: the ribbon (tools), the Properties palette (instance/type properties), the Project Browser (all views, schedules, sheets, families) and the drawing area.
3. In the Project Browser expand Floor Plans and double-click Level 1. Zoom and pan with the mouse wheel; hover over a wall and read its description on the status bar.

   ```bash
   Project Browser ▸ Floor Plans ▸ Level 1
   ```

4. Select a wall and inspect the Properties palette: note its Type (in the Type Selector), Base Constraint and Top Constraint. Click Edit Type to view (not change) the type parameters.

   ```bash
   Properties ▸ Type Selector / Edit Type
   ```

5. Open the default 3D view and orbit the model with Shift + middle-mouse drag. Use the ViewCube to jump to Front, Top and corner views.

   ```bash
   Quick Access Toolbar ▸ Default 3D View
   ```

6. Open an elevation and a section view from the Project Browser, and tile the windows to see the same model in several views at once.

   ```bash
   View ▸ Windows ▸ Tile Views
   ```


**Test it**

You can name the four zones of the Revit UI, open any plan/elevation/section/3D view from the Project Browser, and read a selected element's type and constraints in the Properties palette — one model driving every view is the essence of BIM.

> **Note:** The full lab, with its dataset files, is in labs/lab-01-*/ in the course repository.

---


### Lab 2 — Convert 2D Information into a 3D Model

Objective: LO1 — Apply Revit for Building Information Modelling (BIM).

Goal: Turn a 2D PDF floor plan into an intelligent 3D model: create gridlines and walls to match the drawing, set the exterior walls to the 12" Generic type and interior walls to the 6" Generic type, constrain wall tops to Level 2 and give the corner a 30 ft radius — then add construction information to the model.

**What you'll build**

A 3D building model reproduced from a 2D plan, with correctly typed exterior/interior walls constrained to levels.   (Tools: Autodesk Revit, 2D floor plan PDF (from the LMS lab files).)

**Step-by-step**

1. Start a new project from the Architectural template and link the 2D floor plan PDF into the Level 1 plan view as a reference underlay.

   ```bash
   File ▸ New ▸ Project ▸ Architectural Template · Insert ▸ Link PDF
   ```

2. Place vertical and horizontal gridlines to match the grid intersections shown on the PDF.

   ```bash
   Architecture ▸ Datum ▸ Grid
   ```

3. Draw the exterior walls over the PDF using the 12" Generic wall type. In the Options Bar set Height to Level 2.

   ```bash
   Architecture ▸ Build ▸ Wall: Architectural ▸ Generic - 12"
   ```

4. Draw the interior partition walls with the 6" Generic wall type, also constrained to Level 2.

   ```bash
   Architecture ▸ Build ▸ Wall: Architectural ▸ Generic - 6"
   ```

5. Create the curved corner wall with the Fillet Arc draw tool and set the radius to 30 ft (30' 0").

   ```bash
   Modify | Place Wall ▸ Draw ▸ Fillet Arc ▸ Radius = 30'
   ```

6. Open the default 3D view and verify the model: all walls rise from Level 1 to Level 2 and the plan matches the PDF. Select any wall and confirm its Top Constraint reads 'Up to level: Level 2'.

   ```bash
   Quick Access Toolbar ▸ Default 3D View
   ```


**Test it**

The 3D view shows a closed building shell that matches the 2D PDF: exterior walls are Generic - 12", interior walls are Generic - 6", every wall's Top Constraint is Level 2, and the corner wall has a 30 ft radius — 2D information has become an intelligent, parametric 3D model.

> **Note:** The full lab, with its dataset files, is in labs/lab-02-*/ in the course repository.

---


## Topic 02 — BIM Modeling  (K6, K7 · A4, A5 · LO2)

Develop models for building elements · walls, floors, ceilings, roofs, stairs, structure · site and topography · massing · BIM design integration

**Key concepts**

- Everything is parametric — Each component has parametric qualities — change the model once and every related view, schedule and sheet updates automatically.
- Model with the right tool — Walls, curtain walls, floors, ceilings, roofs, stairs, railings — each element is created with its dedicated tool and family type.
- Structure lives in the model — Structural columns, beams, beam systems, trusses and braces carry the load path inside the same coordinated model.
- Site gives context — Toposurfaces, subregions, graded regions and building pads model the terrain the building sits on.
- Mass first, detail later — Conceptual masses and generative design (Dynamo) explore building volumes before committing to detailed elements.
- Families drive integration — System, loadable and in-place families — with materials and parameters — integrate design information into every element.


### Lab 3 — Modeling Walls — Reveals, Embedded and Curtain Walls

Objective: LO2 — Develop models and integrate design for BIM.

Goal: Work with advanced wall modeling on the Embed Walls project: place brick-course wall reveals on an elevation, duplicate a wall type into a new Vertical Cladding type, embed the new walls into an existing wall with Cut Geometry, and add a curtain wall with grids and mullions.

**What you'll build**

A facade with three positioned reveals, embedded Vertical Cladding walls joined into the host wall, and a gridded curtain wall.   (Tools: Autodesk Revit, Embed Walls.rvt (LMS lab files).)

**Step-by-step**

1. Open Embed Walls.rvt. Start the Wall: Reveal tool, edit its type properties and change the profile to Reveal-Brick Course: 3 Bricks.

   ```bash
   Architecture ▸ Build ▸ Wall ▸ Wall: Reveal ▸ Edit Type
   ```

2. Place three reveals on the end elevation wall at the dimensions given in the drawing, each with Offset from Wall = 1".

   ```bash
   Modify | Place Reveal ▸ set Offset from Wall = 1"
   ```

3. Open the Floor 2 plan. Start a new wall, select the Stone on CMU type, duplicate it and name the new type Vertical Cladding; change Layer 1's material to Cladding, Vertical Ribbed.

   ```bash
   Architecture ▸ Wall ▸ Edit Type ▸ Duplicate ▸ 'Vertical Cladding'
   ```

4. Draw three lengths of the Vertical Cladding wall per the plan dimensions, with Base Constraint = Floor 2 and Top Constraint = Roof, then Align their tops/bottoms to the reveals.

   ```bash
   Modify ▸ Align
   ```

5. Use Cut Geometry to embed the Vertical Cladding walls into the existing host wall (pick the host first), then Join Geometry to remove the end edges in plan.

   ```bash
   Modify ▸ Geometry ▸ Cut / Join
   ```

6. Add a curtain wall: place a wall with a curtain wall type, divide it with Curtain Grid, and place mullions on the grid lines. Tab-select a panel and swap its type in the Type Selector.

   ```bash
   Architecture ▸ Wall ▸ Curtain Wall 1 · Architecture ▸ Build ▸ Curtain Grid / Mullion
   ```


**Test it**

The elevation shows three brick-course reveals at the specified dimensions; the Vertical Cladding walls sit flush inside the host wall with clean joins in plan; and the curtain wall shows a grid of panels with mullions — Tab-selection lets you re-type any single panel.

> **Note:** The full lab, with its dataset files, is in labs/lab-03-*/ in the course repository.

---


### Lab 4 — Floors, Ceilings, Roofs and Openings

Objective: LO2 — Develop models and integrate design for BIM.

Goal: Complete the horizontal envelope of the building: create a floor by picking walls, add a ceiling in a reflected ceiling plan, create a roof by footprint with slope-defining edges and a second roof by extrusion, then cut a vertical shaft opening through the levels.

**What you'll build**

A building with floors, ceilings, a footprint roof and an extruded roof, plus a shaft opening cutting through every level.   (Tools: Autodesk Revit, your Lab 2 model (or the LMS lab file).)

**Step-by-step**

1. Create the Level 1 floor: pick the exterior walls as boundaries (Extend into wall (to core)), and finish the sketch — the boundary must be a closed loop.

   ```bash
   Architecture ▸ Build ▸ Floor: Architectural ▸ Pick Walls
   ```

2. Open the Level 1 ceiling plan and place a ceiling with Automatic Ceiling by clicking inside the walls that form a closed loop.

   ```bash
   Architecture ▸ Build ▸ Ceiling ▸ Automatic Ceiling
   ```

3. Create the main roof by footprint on Level 2: pick the walls with an overhang, keep Defines Slope on for all edges, and finish — then open 3D to see the hips form.

   ```bash
   Architecture ▸ Build ▸ Roof ▸ Roof by Footprint
   ```

4. Create a porch roof by extrusion: in an elevation view sketch an open-loop profile and extrude it, then Attach the porch walls to the underside of the roof.

   ```bash
   Architecture ▸ Build ▸ Roof ▸ Roof by Extrusion · Modify Wall ▸ Attach Top/Base
   ```

5. Cut a shaft for the stair: sketch a closed loop with the Shaft tool, set Base Constraint = Level 1 and Top Constraint = Roof, and finish the opening.

   ```bash
   Architecture ▸ Opening ▸ Shaft
   ```

6. Verify in a section view that the shaft cuts the floor and ceiling on every intermediate level, and use By Face / Vertical openings where a duct or chimney penetrates the roof.

   ```bash
   Architecture ▸ Opening ▸ By Face / Vertical
   ```


**Test it**

The section view shows floor, ceiling and both roofs in place; the shaft opening cuts cleanly through every level it spans; and moving the shaft in one plan moves it on all levels — the model stays coordinated because every view reads the same database.

> **Note:** The full lab, with its dataset files, is in labs/lab-04-*/ in the course repository.

---


### Lab 5 — Stairs, Railings and Structural Elements

Objective: LO2 — Develop models and integrate design for BIM.

Goal: Add vertical circulation and the load path: assemble a stair from runs and landings, host a railing on a floor edge with Sketch Path, then place structural columns on the grid intersections and frame them with beams, a beam system and a brace.

**What you'll build**

A stair with railings connecting two levels, plus a structural frame of columns, beams, a beam system and a brace.   (Tools: Autodesk Revit, your Lab 2/4 model (or the LMS lab file).)

**Step-by-step**

1. Create a stair between Level 1 and Level 2: in stair assembly mode place a straight Run; a landing is created automatically between two runs. Finish and inspect it in 3D.

   ```bash
   Architecture ▸ Circulation ▸ Stair ▸ Run
   ```

2. Add a railing along the Level 2 floor edge: Sketch Path, draw the railing line, use Pick New Host to host it on the floor, and finish.

   ```bash
   Architecture ▸ Circulation ▸ Railing ▸ Sketch Path ▸ Pick New Host
   ```

3. Place structural columns at grid intersections from Level 1 to Level 2 (use At Grids to place several at once).

   ```bash
   Structure ▸ Structure ▸ Column ▸ At Grids
   ```

4. Draw beams between column tops on Level 2, snapping from column to column.

   ```bash
   Structure ▸ Structure ▸ Beam
   ```

5. Fill a bay with a Beam System: sketch its boundary with Pick Supports, set the Beam Type and Layout Rule (e.g. Fixed Distance), and finish.

   ```bash
   Structure ▸ Structure ▸ Beam System ▸ Sketch Beam System
   ```

6. Open a framing elevation and add a diagonal Brace between a column and a beam, snapping to their ends.

   ```bash
   Structure ▸ Structure ▸ Brace
   ```


**Test it**

The stair connects the two levels with automatically generated railings; columns stand on every chosen grid intersection; the beam system spaces its members per the layout rule; and the brace runs diagonally in the framing elevation — the architectural and structural elements coexist in one coordinated model.

> **Note:** The full lab, with its dataset files, is in labs/lab-05-*/ in the course repository.

---


### Lab 6 — Terrain, Building Pad and Conceptual Mass

Objective: LO2 — Develop models and integrate design for BIM.

Goal: Set the building into its site: create a toposurface by placing points at different elevations, add a building pad from the foundation footprint, frame the 3D view with a section box, apply a grass material — then explore an in-place conceptual mass and preview generative design with Dynamo.

**What you'll build**

A site terrain with a building pad cut into it, a realistic 3D view, and an in-place conceptual mass volume.   (Tools: Autodesk Revit, GSG_03_Terrain_Pad.rvt (LMS lab files), Dynamo.)

**Step-by-step**

1. Open GSG_03_Terrain_Pad.rvt and the Site plan. Start Toposurface and place points around the building at Elevation 0, then rings of points further out at higher elevations to slope the ground.

   ```bash
   Massing & Site ▸ Model Site ▸ Toposurface ▸ Place Point
   ```

2. Finish the surface and open the 3D view — the terrain now buries part of the building.

   ```bash
   Massing & Site ▸ Toposurface ▸ ✓ Finish Surface
   ```

3. Add a Building Pad: sketch its boundary with Pick Walls on the foundation walls, set the pad level, and finish — the pad cuts the terrain away from the building.

   ```bash
   Massing & Site ▸ Model Site ▸ Building Pad
   ```

4. Frame the model with a Section Box in the 3D view's properties and drag its grips to crop the terrain neatly around the building.

   ```bash
   3D View ▸ Properties ▸ Section Box
   ```

5. Select the toposurface, and in the Material parameter choose a grass material for a realistic render, then explore Subregion, Split Surface and Graded Region on the Massing & Site tab.

   ```bash
   Toposurface ▸ Properties ▸ Material ▸ Grass
   ```

6. Create an In-Place Mass: name it, sketch a profile and create a form, then Finish Mass — and open Manage ▸ Dynamo to see how a graph of nodes can drive such geometry for generative design.

   ```bash
   Massing & Site ▸ Conceptual Mass ▸ In-Place Mass · Manage ▸ Dynamo
   ```


**Test it**

The 3D view shows the building sitting in a grass-covered terrain with a clean pad cut into the slope, the section box crops the site tidily, and your in-place mass appears as a volume you could later turn into walls, floors and roofs — site, mass and building live in one model.

> **Note:** The full lab, with its dataset files, is in labs/lab-06-*/ in the course repository.

---


## Topic 03 — BIM Application  (K5 · A6, A7, A8 · LO3)

Apply and operate BIM · technologies used in BIM · interpret output · schedules and quantity takeoffs · analyse performance and check compliance

**Key concepts**

- BIM manages the build — Construction simulation, information statistics and real-time monitoring strengthen quality and process management on site.
- Views interpret the model — View range, view templates, callouts and section views turn one model into many purpose-built, readable outputs.
- Schedules read the database — Schedules and quantity takeoffs tabulate elements straight from the model — the model IS the quantity database.
- Cost from the model — Calculated-value formulas and material takeoffs produce preliminary cost estimates that update as the design changes.
- Analyse before you build — Revit Systems Analysis translates the model to EnergyPlus to simulate heating, cooling and annual energy performance.
- Check, then comply — Interference (clash) checks and analysis reports verify design performance and compliance before construction.


### Lab 7 — View Templates, Schedules and Quantity Takeoffs

Objective: LO3 — Apply BIM and check the output.

Goal: Operate BIM to produce controlled, quantified output: build a furniture-layout view with a scope box and visibility/graphic overrides and save it as a view template, then create a door schedule and a wall material takeoff, and add a calculated-value field for a preliminary cost estimate.

**What you'll build**

A styled Floor 2 Furniture Layout view template, a sorted door schedule, and a wall material takeoff with a calculated cost column.   (Tools: Autodesk Revit, Create View Template.rvt (LMS lab files).)

**Step-by-step**

1. Open Create View Template.rvt. Duplicate the Floor 2 plan view and rename it Floor 2 Furniture Layout, then apply the Main Zone scope box to set its crop region.

   ```bash
   Project Browser ▸ Floor 2 ▸ Duplicate View · Properties ▸ Scope Box = Main Zone
   ```

2. Open Visibility/Graphic Overrides (VG). Override the Walls Cut pattern to Solid Fill light grey with light-grey lines, and the Furniture projection lines/pattern to red Diagonal Down-Small.

   ```bash
   View ▸ Graphics ▸ Visibility/Graphics (VG)
   ```

3. On the Annotation Categories tab switch off Sections and set Grids to Halftone, then close VG and review the styled view.

   ```bash
   VG ▸ Annotation Categories
   ```

4. Save the styling as a template: right-click the view ▸ Create View Template From View, and apply it to another duplicate to prove the styling is reusable.

   ```bash
   Right-click view ▸ Create View Template From View
   ```

5. Create a door schedule: Schedule/Quantities, category Doors, add fields (Mark, Level, Width, Height, Count), and sort by Level — the schedule fills itself from the model.

   ```bash
   View ▸ Create ▸ Schedules ▸ Schedule/Quantities ▸ Doors
   ```

6. Create a Material Takeoff for Walls with Material: Name and Material: Area, then add a Calculated Value field (e.g. Cost = Area × unit rate) to produce a preliminary cost estimate.

   ```bash
   View ▸ Schedules ▸ Material Takeoff ▸ Calculated Value
   ```


**Test it**

Applying your view template restyles a fresh duplicate in one click; the door schedule lists every door sorted by level and updates when a door is deleted; and the wall takeoff's calculated column prices the walls from live model quantities — the model is the single quantity and cost database.

> **Note:** The full lab, with its dataset files, is in labs/lab-07-*/ in the course repository.

---


### Lab 8 — Energy Analysis and Design Compliance Checks

Objective: LO3 — Apply BIM and check the output.

Goal: Analyse design performance and check compliance: set the project location and energy settings, generate the energy analytical model, run a systems analysis (EnergyPlus), read the results and reports, and run an Interference Check between structural and architectural elements to find clashes.

**What you'll build**

An energy analysis run with its report, plus an interference-check report of clashes between element categories.   (Tools: Autodesk Revit, Revit Systems Analysis (EnergyPlus), your course model or the Autodesk sample project.)

**Step-by-step**

1. Open the sample architecture project. Set the project's geographic Location, then open Energy Settings and set the Mode and building type for analysis.

   ```bash
   Analyze ▸ Energy Optimization ▸ Location / Energy Settings
   ```

2. Generate the energy analytical model — Revit creates analytical spaces and surfaces from the building elements.

   ```bash
   Analyze ▸ Energy Optimization ▸ Create Energy Model
   ```

3. Run a systems analysis workflow: choose 'System sizing' (design heating/cooling loads) — Revit translates the model to EnergyPlus and runs the simulation.

   ```bash
   Analyze ▸ Energy Analysis ▸ Systems Analysis
   ```

4. Review the results: open Project Browser ▸ Reports ▸ Analysis Reports and double-click the time-stamped report; switch Report Style between Detailed and Loads.

   ```bash
   Project Browser ▸ Reports ▸ Analysis Reports
   ```

5. Select an analytical space and read its heating, cooling and airflow peak-demand properties — the same numbers as the report, attached to the model.

   ```bash
   Analytical Space ▸ Properties
   ```

6. Run an Interference Check between Structural Columns/Framing and Walls/Floors; export the clash report and resolve one clash, then Refresh to confirm it clears.

   ```bash
   Collaborate ▸ Coordinate ▸ Interference Check ▸ Run Interference Check
   ```


**Test it**

The Analysis Report opens with design heating and cooling loads for every zone, each analytical space carries its peak demands as properties, and the Interference Check lists each clash by element pair — after your fix and Refresh, the resolved clash disappears from the report.

> **Note:** The full lab, with its dataset files, is in labs/lab-08-*/ in the course repository.

---


## Topic 04 — BIM Documentation  (K8–K10 · A3, A9 · LO4)

Maintain BIM databases and information systems · documentation required for BIM · BIM e-submission requirements and standards

**Key concepts**

- Documents govern BIM — BIM standards, BEP, BIP, PEP, EIR, MIDP and the Common Data Environment (CDE) govern how project information is produced and shared.
- The BEP is the baseline — The BIM Execution Plan records goals, roles, deliverables, level of detail and exchange protocols — agreed at project start.
- Deliverables are agreed early — Site, massing, architectural, structural and MEP models, schedules, shop drawings, as-builts and FM data — with dates.
- Databases need discipline — SVY21 geo-referencing, 1:1 metric scale, file/view naming formats, colour standards and federated file structures keep the database usable.
- Worksharing maintains one truth — A central model with worksets, linked files and phases lets the whole team maintain one coordinated information system.
- e-Submission has rules — BCA BIM e-submission: last-saved views, cover page, core information and discipline-specific requirements must all be checked.


### Lab 9 — Sheets, Worksharing and Linked Models

Objective: LO4 — Maintain BIM database and develop BIM documentation.

Goal: Develop the construction documentation and maintain the shared model: compose a drawing sheet with a title block and viewports, add a callout and a section view, link a CAD file, enable worksharing to create a central model with worksets, and organise the project into phases.

**What you'll build**

A titled drawing sheet carrying plan + section + callout viewports, a workshared central model with worksets, and a phased project.   (Tools: Autodesk Revit, your course model, a DWG file (LMS lab files).)

**Step-by-step**

1. Create a sheet with a title block and drag the Level 1 plan and a schedule from the Project Browser onto it — each becomes a viewport.

   ```bash
   View ▸ Sheet Composition ▸ Sheet
   ```

2. Add a Section through the building and a Callout of the stair area in the plan view; open both views from their heads and place them on the sheet.

   ```bash
   View ▸ Create ▸ Section / Callout
   ```

3. Link a CAD file (e.g. a surveyor's DWG) into a site view, then compare Insert ▸ Link CAD (stays external, updates) with Insert ▸ Import CAD (embedded).

   ```bash
   Insert ▸ Link ▸ Link CAD
   ```

4. Enable worksharing: open Worksets — accept the default worksets to create the central model, then Save As the central file so team members can make local copies.

   ```bash
   Collaborate ▸ Manage Collaboration ▸ Worksets
   ```

5. Create a phase: open Manage ▸ Phases, insert a phase after New Construction, and assign an element to it; set a view's Phase and Phase Filter to see the effect.

   ```bash
   Manage ▸ Phasing ▸ Phases
   ```

6. Create a design option set for an entry alternative: Manage ▸ Design Options ▸ New, add a second option, and place variant geometry in each option.

   ```bash
   Manage ▸ Design Options
   ```


**Test it**

The sheet shows plan, section and callout viewports under a filled title block; the file is now a central model whose Worksets dialog lists your worksets; the phase filter hides/shows the phased element; and switching design options swaps the entry geometry — one database, fully documented.

> **Note:** The full lab, with its dataset files, is in labs/lab-09-*/ in the course repository.

---


### Lab 10 — BIM e-Submission Standards Check

Objective: LO4 — Maintain BIM database and develop BIM documentation.

Goal: Prepare a model for Singapore BCA BIM e-submission: apply the standard file and view naming formats, verify geo-referencing (SVY21 / SHD) and 1:1 metric scale, check the last-saved views, and assemble the submission cover page with the core information required by the regulatory agencies.

**What you'll build**

A submission-ready model: compliant file/view names, correct coordinates and scale, purged views and a complete cover page checklist.   (Tools: Autodesk Revit, your course model, BCA Code of Practice for BIM e-Submission.)

**Step-by-step**

1. Rename the model file to the 6-field e-submission format (project, originator, zone, level, type, discipline) and rename key views to the 3–4 field view naming format (e.g. A_1st Storey).

   ```bash
   File naming: <Project>-<Originator>-<Zone>-<Level>-<Type>-<Discipline>
   ```

2. Verify the site model is geo-referenced to SVY21 for Easting/Northing and to Singapore Height Datum (SHD 0.000 m) for elevation, with the layout in True North orientation.

   ```bash
   Manage ▸ Coordinates / Position ▸ True North
   ```

3. Confirm the model is built full-size 1:1 metric, and that no 2D view generated from it uses an odd drawing scale.

   ```bash
   Properties ▸ View Scale
   ```

4. Check every last-saved view: maximum extent saved, no hidden objects or annotations, all external files loadable, irrelevant layers/drafting purged, no proprietary fonts.

   ```bash
   Manage ▸ Purge Unused · VG ▸ Reveal Hidden Elements
   ```

5. Apply the colour standards for amendments and A&A works where the submission includes changes to approved plans.
6. Assemble the cover page: submission authority and QP's declaration/endorsements, project information, and the list of views, schedules and sheets for approval, with the agency's minimal Core Information.

   ```bash
   Sheet: Cover Page ▸ QP declaration · Project info · View list
   ```


**Test it**

Walking the e-submission checklist end-to-end passes: compliant file and view names, SVY21/SHD coordinates, 1:1 metric scale, clean last-saved views with nothing hidden or missing, correct amendment colours, and a cover page carrying the declaration, project information and view list — the model is ready for regulatory e-submission.

> **Note:** The full lab, with its dataset files, is in labs/lab-10-*/ in the course repository.

---


## Assessment Focus — How the Final Assessment Maps to This Guide

The final assessment on Day 2 has two open-book instruments. Everything they assess is taught in this guide:

**Written Assessment (SAQ) — 1 hour — assesses TSC Knowledge K1–K10**

- K1 Principles of BIM and K4 Definition of BIM — Topic 1 (What is BIM, the BIM process, BIM dimensions).
- K2 Value proposition of BIM — Topic 1 (the seven advantages of BIM).
- K3 Requirements of BIM — Topic 1 (OIR, AIR, EIR, BEP, PIM, AIM).
- K5 Application of BIM — Topic 3 (construction management, simulation, monitoring).
- K6 Technology used in BIM and K7 BIM design processes — Topics 2–3 (parametric modeling, Dynamo, analysis tools).
- K8 Documentation required for BIM — Topic 4 (BIM standard, BEP, BIP, PEP, EIR, MIDP, CDE, deliverables).
- K9 Databases and information systems — Topic 4 (SVY21/SHD, naming formats, file structures, worksharing).
- K10 BIM e-submission requirements and standards — Topic 4 (last saved views, cover page, core information, colour standards).

**Practical Performance (PP) — 1.5 hours — assesses TSC Abilities A1–A9**

- A1–A2 (identify BIM application and interoperability) — practised in Labs 1–2 and the PP's project set-up tasks.
- A4–A5 (develop models, integrate design) — practised in Labs 2–6 (walls, floors, roofs, structure, linked models).
- A6–A8 (operate BIM, interpret output, analyse performance) — practised in Labs 7–8 (schedules, energy settings, checks).
- A3 and A9 (maintain databases, develop documentation) — practised in Labs 9–10 (worksharing, sheets, e-submission).
- The PP uses the provided PP dataset (.rvt); take a snapshot at the end of each task and paste it into the answer document.

---


## Assessment Preparation

- First pass: complete every lab in Revit, checking each lab's Test-it criterion.
- Second pass: redo the labs from memory until the ribbon paths and workflows are automatic.
- Review the Key Concepts of each topic — the WA questions are scenario-based versions of them.
- Practise the PP workflow: link a model, Copy/Monitor levels, configure Energy Settings, and export a documented report.
- Sharpen readiness with the Tertiary Infotech practice exams portal: https://exams.tertiaryinfotech.com.
- The assessment is open book: bring this guide and the slides, and know your way around them quickly.


## Glossary

- **BIM (Building Information Modelling)** — An intelligent 3D model-based process for planning, designing, constructing and managing buildings and infrastructure.
- **BEP (BIM Execution Plan)** — The Employer-approved baseline document defining goals, roles, deliverables and processes for BIM on a project.
- **OIR / AIR / EIR** — Organisational, Asset and Employer Information Requirements — the chain of information needs BIM must satisfy.
- **PIM / AIM** — Project Information Model (design & construction) / Asset Information Model (operation & asset management).
- **CDE (Common Data Environment)** — The single shared place where project information is stored, managed and exchanged.
- **MIDP** — Master Information Delivery Plan — schedules who delivers which information, when.
- **LOD (Level of Development)** — How developed a model element's geometry and information are — defined at project start.
- **IFC (Industry Foundation Classes)** — The open, vendor-neutral exchange format BIM tools use for interoperability.
- **Parametric element** — A Revit component whose behaviour is driven by parameters — one change updates every related view and schedule.
- **Family (system / loadable / in-place)** — Revit's building blocks: predefined system elements, loadable RFA components, and unique in-project elements.
- **Toposurface / building pad** — Terrain modelled from elevation points, and the level cut into it that the building sits on.
- **Worksharing / central model** — Multiple team members editing local copies synchronised to one central model, divided into worksets.
- **Copy/Monitor** — The Collaborate tool that copies levels/grids from a linked model and warns when the source changes.
- **Interference (clash) check** — Revit's built-in detection of elements that occupy the same space — run before construction.
- **Quantity takeoff** — Extracting element counts, materials and areas from the model for cost estimating.
- **SVY21 / SHD** — The Singapore coordinate system and height datum a site model must be geo-referenced to for e-submission.
- **BIM e-submission** — Submitting the BIM model to Singapore's regulatory agencies per the BCA Code of Practice — last saved views, cover page and core information.
