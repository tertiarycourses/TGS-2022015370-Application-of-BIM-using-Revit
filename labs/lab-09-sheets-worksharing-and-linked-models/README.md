# Lab 9 — Sheets, Worksharing and Linked Models

**Course:** Application of BIM using Revit (TGS-2022015370)  ·  **Topic 04:** BIM Documentation  ·  **Alignment:** LO4 — Maintain BIM database and develop BIM documentation

Develop the construction documentation and maintain the shared model: compose a drawing sheet with a title block and viewports, add a callout and a section view, link a CAD file, enable worksharing to create a central model with worksets, and organise the project into phases.

## What you'll build

A titled drawing sheet carrying plan + section + callout viewports, a workshared central model with worksets, and a phased project.

**Tools:** Autodesk Revit, your course model, a DWG file (LMS lab files)

## Dataset files in this folder

- `CA-L15-01-Use PDF and Images.rvt`

## Step-by-step

1. Create a sheet with a title block and drag the Level 1 plan and a schedule from the Project Browser onto it — each becomes a viewport.

   > `View ▸ Sheet Composition ▸ Sheet`

2. Add a Section through the building and a Callout of the stair area in the plan view; open both views from their heads and place them on the sheet.

   > `View ▸ Create ▸ Section / Callout`

3. Link a CAD file (e.g. a surveyor's DWG) into a site view, then compare Insert ▸ Link CAD (stays external, updates) with Insert ▸ Import CAD (embedded).

   > `Insert ▸ Link ▸ Link CAD`

4. Enable worksharing: open Worksets — accept the default worksets to create the central model, then Save As the central file so team members can make local copies.

   > `Collaborate ▸ Manage Collaboration ▸ Worksets`

5. Create a phase: open Manage ▸ Phases, insert a phase after New Construction, and assign an element to it; set a view's Phase and Phase Filter to see the effect.

   > `Manage ▸ Phasing ▸ Phases`

6. Create a design option set for an entry alternative: Manage ▸ Design Options ▸ New, add a second option, and place variant geometry in each option.

   > `Manage ▸ Design Options`


## Test it

The sheet shows plan, section and callout viewports under a filled title block; the file is now a central model whose Worksets dialog lists your worksets; the phase filter hides/shows the phased element; and switching design options swaps the entry geometry — one database, fully documented.

---
© 2026 Tertiary Infotech Academy Pte Ltd · UEN: 201200696W