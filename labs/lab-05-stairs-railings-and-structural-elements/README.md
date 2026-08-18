# Lab 5 — Stairs, Railings and Structural Elements

**Course:** Application of BIM using Revit (TGS-2022015370)  ·  **Topic 02:** BIM Modeling  ·  **Alignment:** LO2 — Develop models and integrate design for BIM

Add vertical circulation and the load path: assemble a stair from runs and landings, host a railing on a floor edge with Sketch Path, then place structural columns on the grid intersections and frame them with beams, a beam system and a brace.

## What you'll build

A stair with railings connecting two levels, plus a structural frame of columns, beams, a beam system and a brace.

**Tools:** Autodesk Revit, your Lab 2/4 model (or the LMS lab file)

## Dataset files in this folder

- `Studio Block.rvt`
- `Studio Block Structure.rvt`
- `Studio Block Finished.rvt`

## Step-by-step

1. Create a stair between Level 1 and Level 2: in stair assembly mode place a straight Run; a landing is created automatically between two runs. Finish and inspect it in 3D.

   > `Architecture ▸ Circulation ▸ Stair ▸ Run`

2. Add a railing along the Level 2 floor edge: Sketch Path, draw the railing line, use Pick New Host to host it on the floor, and finish.

   > `Architecture ▸ Circulation ▸ Railing ▸ Sketch Path ▸ Pick New Host`

3. Place structural columns at grid intersections from Level 1 to Level 2 (use At Grids to place several at once).

   > `Structure ▸ Structure ▸ Column ▸ At Grids`

4. Draw beams between column tops on Level 2, snapping from column to column.

   > `Structure ▸ Structure ▸ Beam`

5. Fill a bay with a Beam System: sketch its boundary with Pick Supports, set the Beam Type and Layout Rule (e.g. Fixed Distance), and finish.

   > `Structure ▸ Structure ▸ Beam System ▸ Sketch Beam System`

6. Open a framing elevation and add a diagonal Brace between a column and a beam, snapping to their ends.

   > `Structure ▸ Structure ▸ Brace`


## Test it

The stair connects the two levels with automatically generated railings; columns stand on every chosen grid intersection; the beam system spaces its members per the layout rule; and the brace runs diagonally in the framing elevation — the architectural and structural elements coexist in one coordinated model.

---
© 2026 Tertiary Infotech Academy Pte Ltd · UEN: 201200696W