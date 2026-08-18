# Lab 3 — Modeling Walls — Reveals, Embedded and Curtain Walls

**Course:** Application of BIM using Revit (TGS-2022015370)  ·  **Topic 02:** BIM Modeling  ·  **Alignment:** LO2 — Develop models and integrate design for BIM

Work with advanced wall modeling on the Embed Walls project: place brick-course wall reveals on an elevation, duplicate a wall type into a new Vertical Cladding type, embed the new walls into an existing wall with Cut Geometry, and add a curtain wall with grids and mullions.

## What you'll build

A facade with three positioned reveals, embedded Vertical Cladding walls joined into the host wall, and a gridded curtain wall.

**Tools:** Autodesk Revit, Embed Walls.rvt (LMS lab files)

## Dataset files in this folder

- `Embed Walls.rvt`
- `Embed Walls solution.rvt`

## Step-by-step

1. Open Embed Walls.rvt. Start the Wall: Reveal tool, edit its type properties and change the profile to Reveal-Brick Course: 3 Bricks.

   > `Architecture ▸ Build ▸ Wall ▸ Wall: Reveal ▸ Edit Type`

2. Place three reveals on the end elevation wall at the dimensions given in the drawing, each with Offset from Wall = 1".

   > `Modify | Place Reveal ▸ set Offset from Wall = 1"`

3. Open the Floor 2 plan. Start a new wall, select the Stone on CMU type, duplicate it and name the new type Vertical Cladding; change Layer 1's material to Cladding, Vertical Ribbed.

   > `Architecture ▸ Wall ▸ Edit Type ▸ Duplicate ▸ 'Vertical Cladding'`

4. Draw three lengths of the Vertical Cladding wall per the plan dimensions, with Base Constraint = Floor 2 and Top Constraint = Roof, then Align their tops/bottoms to the reveals.

   > `Modify ▸ Align`

5. Use Cut Geometry to embed the Vertical Cladding walls into the existing host wall (pick the host first), then Join Geometry to remove the end edges in plan.

   > `Modify ▸ Geometry ▸ Cut / Join`

6. Add a curtain wall: place a wall with a curtain wall type, divide it with Curtain Grid, and place mullions on the grid lines. Tab-select a panel and swap its type in the Type Selector.

   > `Architecture ▸ Wall ▸ Curtain Wall 1 · Architecture ▸ Build ▸ Curtain Grid / Mullion`


## Test it

The elevation shows three brick-course reveals at the specified dimensions; the Vertical Cladding walls sit flush inside the host wall with clean joins in plan; and the curtain wall shows a grid of panels with mullions — Tab-selection lets you re-type any single panel.

---
© 2026 Tertiary Infotech Academy Pte Ltd · UEN: 201200696W