# Lab 2 — Convert 2D Information into a 3D Model

**Course:** Application of BIM using Revit (TGS-2022015370)  ·  **Topic 01:** Introduction to BIM and Revit  ·  **Alignment:** LO1 — Apply Revit for Building Information Modelling (BIM)

Turn a 2D PDF floor plan into an intelligent 3D model: create gridlines and walls to match the drawing, set the exterior walls to the 12" Generic type and interior walls to the 6" Generic type, constrain wall tops to Level 2 and give the corner a 30 ft radius — then add construction information to the model.

## What you'll build

A 3D building model reproduced from a 2D plan, with correctly typed exterior/interior walls constrained to levels.

**Tools:** Autodesk Revit, 2D floor plan PDF (from the LMS lab files)

## Dataset files in this folder

- `Planning Site.pdf`
- `Site Image.png`
- `Planning Site solution.rvt`

## Step-by-step

1. Start a new project from the Architectural template and link the 2D floor plan PDF into the Level 1 plan view as a reference underlay.

   > `File ▸ New ▸ Project ▸ Architectural Template · Insert ▸ Link PDF`

2. Place vertical and horizontal gridlines to match the grid intersections shown on the PDF.

   > `Architecture ▸ Datum ▸ Grid`

3. Draw the exterior walls over the PDF using the 12" Generic wall type. In the Options Bar set Height to Level 2.

   > `Architecture ▸ Build ▸ Wall: Architectural ▸ Generic - 12"`

4. Draw the interior partition walls with the 6" Generic wall type, also constrained to Level 2.

   > `Architecture ▸ Build ▸ Wall: Architectural ▸ Generic - 6"`

5. Create the curved corner wall with the Fillet Arc draw tool and set the radius to 30 ft (30' 0").

   > `Modify | Place Wall ▸ Draw ▸ Fillet Arc ▸ Radius = 30'`

6. Open the default 3D view and verify the model: all walls rise from Level 1 to Level 2 and the plan matches the PDF. Select any wall and confirm its Top Constraint reads 'Up to level: Level 2'.

   > `Quick Access Toolbar ▸ Default 3D View`


## Test it

The 3D view shows a closed building shell that matches the 2D PDF: exterior walls are Generic - 12", interior walls are Generic - 6", every wall's Top Constraint is Level 2, and the corner wall has a 30 ft radius — 2D information has become an intelligent, parametric 3D model.

---
© 2026 Tertiary Infotech Academy Pte Ltd · UEN: 201200696W