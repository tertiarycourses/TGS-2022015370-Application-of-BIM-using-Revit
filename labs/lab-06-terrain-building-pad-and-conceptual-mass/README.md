# Lab 6 — Terrain, Building Pad and Conceptual Mass

**Course:** Application of BIM using Revit (TGS-2022015370)  ·  **Topic 02:** BIM Modeling  ·  **Alignment:** LO2 — Develop models and integrate design for BIM

Set the building into its site: create a toposurface by placing points at different elevations, add a building pad from the foundation footprint, frame the 3D view with a section box, apply a grass material — then explore an in-place conceptual mass and preview generative design with Dynamo.

## What you'll build

A site terrain with a building pad cut into it, a realistic 3D view, and an in-place conceptual mass volume.

**Tools:** Autodesk Revit, GSG_03_Terrain_Pad.rvt (LMS lab files), Dynamo

## Step-by-step

1. Open GSG_03_Terrain_Pad.rvt and the Site plan. Start Toposurface and place points around the building at Elevation 0, then rings of points further out at higher elevations to slope the ground.

   > `Massing & Site ▸ Model Site ▸ Toposurface ▸ Place Point`

2. Finish the surface and open the 3D view — the terrain now buries part of the building.

   > `Massing & Site ▸ Toposurface ▸ ✓ Finish Surface`

3. Add a Building Pad: sketch its boundary with Pick Walls on the foundation walls, set the pad level, and finish — the pad cuts the terrain away from the building.

   > `Massing & Site ▸ Model Site ▸ Building Pad`

4. Frame the model with a Section Box in the 3D view's properties and drag its grips to crop the terrain neatly around the building.

   > `3D View ▸ Properties ▸ Section Box`

5. Select the toposurface, and in the Material parameter choose a grass material for a realistic render, then explore Subregion, Split Surface and Graded Region on the Massing & Site tab.

   > `Toposurface ▸ Properties ▸ Material ▸ Grass`

6. Create an In-Place Mass: name it, sketch a profile and create a form, then Finish Mass — and open Manage ▸ Dynamo to see how a graph of nodes can drive such geometry for generative design.

   > `Massing & Site ▸ Conceptual Mass ▸ In-Place Mass · Manage ▸ Dynamo`


## Test it

The 3D view shows the building sitting in a grass-covered terrain with a clean pad cut into the slope, the section box crops the site tidily, and your in-place mass appears as a volume you could later turn into walls, floors and roofs — site, mass and building live in one model.

---
© 2026 Tertiary Infotech Academy Pte Ltd · UEN: 201200696W