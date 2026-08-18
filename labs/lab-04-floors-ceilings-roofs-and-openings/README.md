# Lab 4 — Floors, Ceilings, Roofs and Openings

**Course:** Application of BIM using Revit (TGS-2022015370)  ·  **Topic 02:** BIM Modeling  ·  **Alignment:** LO2 — Develop models and integrate design for BIM

Complete the horizontal envelope of the building: create a floor by picking walls, add a ceiling in a reflected ceiling plan, create a roof by footprint with slope-defining edges and a second roof by extrusion, then cut a vertical shaft opening through the levels.

## What you'll build

A building with floors, ceilings, a footprint roof and an extruded roof, plus a shaft opening cutting through every level.

**Tools:** Autodesk Revit, your Lab 2 model (or the LMS lab file)

## Dataset files in this folder

- `Create Ceilings.rvt`
- `Create Ceilings Solution.rvt`

## Step-by-step

1. Create the Level 1 floor: pick the exterior walls as boundaries (Extend into wall (to core)), and finish the sketch — the boundary must be a closed loop.

   > `Architecture ▸ Build ▸ Floor: Architectural ▸ Pick Walls`

2. Open the Level 1 ceiling plan and place a ceiling with Automatic Ceiling by clicking inside the walls that form a closed loop.

   > `Architecture ▸ Build ▸ Ceiling ▸ Automatic Ceiling`

3. Create the main roof by footprint on Level 2: pick the walls with an overhang, keep Defines Slope on for all edges, and finish — then open 3D to see the hips form.

   > `Architecture ▸ Build ▸ Roof ▸ Roof by Footprint`

4. Create a porch roof by extrusion: in an elevation view sketch an open-loop profile and extrude it, then Attach the porch walls to the underside of the roof.

   > `Architecture ▸ Build ▸ Roof ▸ Roof by Extrusion · Modify Wall ▸ Attach Top/Base`

5. Cut a shaft for the stair: sketch a closed loop with the Shaft tool, set Base Constraint = Level 1 and Top Constraint = Roof, and finish the opening.

   > `Architecture ▸ Opening ▸ Shaft`

6. Verify in a section view that the shaft cuts the floor and ceiling on every intermediate level, and use By Face / Vertical openings where a duct or chimney penetrates the roof.

   > `Architecture ▸ Opening ▸ By Face / Vertical`


## Test it

The section view shows floor, ceiling and both roofs in place; the shaft opening cuts cleanly through every level it spans; and moving the shaft in one plan moves it on all levels — the model stays coordinated because every view reads the same database.

---
© 2026 Tertiary Infotech Academy Pte Ltd · UEN: 201200696W