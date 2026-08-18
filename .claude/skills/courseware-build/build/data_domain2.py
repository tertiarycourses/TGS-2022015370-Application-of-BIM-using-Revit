"""Topic 2 — BIM Modeling: hands-on activities (Labs 3–6)."""

DOMAIN2 = [
    dict(
        num=3, topic=2,
        title="Modeling Walls — Reveals, Embedded and Curtain Walls",
        objective="LO2 — Develop models and integrate design for BIM",
        desc="Work with advanced wall modeling on the Embed Walls project: place brick-course "
             "wall reveals on an elevation, duplicate a wall type into a new Vertical Cladding "
             "type, embed the new walls into an existing wall with Cut Geometry, and add a "
             "curtain wall with grids and mullions.",
        build="A facade with three positioned reveals, embedded Vertical Cladding walls joined into the host wall, and a gridded curtain wall.",
        services="Autodesk Revit, Embed Walls.rvt (LMS lab files)",
        steps=[
            ("Open Embed Walls.rvt. Start the Wall: Reveal tool, edit its type properties and change the profile to Reveal-Brick Course: 3 Bricks.",
             "Architecture ▸ Build ▸ Wall ▸ Wall: Reveal ▸ Edit Type"),
            ("Place three reveals on the end elevation wall at the dimensions given in the drawing, each with Offset from Wall = 1\".",
             "Modify | Place Reveal ▸ set Offset from Wall = 1\""),
            ("Open the Floor 2 plan. Start a new wall, select the Stone on CMU type, duplicate it and name the new type Vertical Cladding; change Layer 1's material to Cladding, Vertical Ribbed.",
             "Architecture ▸ Wall ▸ Edit Type ▸ Duplicate ▸ 'Vertical Cladding'"),
            ("Draw three lengths of the Vertical Cladding wall per the plan dimensions, with Base Constraint = Floor 2 and Top Constraint = Roof, then Align their tops/bottoms to the reveals.",
             "Modify ▸ Align"),
            ("Use Cut Geometry to embed the Vertical Cladding walls into the existing host wall (pick the host first), then Join Geometry to remove the end edges in plan.",
             "Modify ▸ Geometry ▸ Cut / Join"),
            ("Add a curtain wall: place a wall with a curtain wall type, divide it with Curtain Grid, and place mullions on the grid lines. Tab-select a panel and swap its type in the Type Selector.",
             "Architecture ▸ Wall ▸ Curtain Wall 1 · Architecture ▸ Build ▸ Curtain Grid / Mullion"),
        ],
        test="The elevation shows three brick-course reveals at the specified dimensions; the Vertical Cladding "
             "walls sit flush inside the host wall with clean joins in plan; and the curtain wall shows a grid of "
             "panels with mullions — Tab-selection lets you re-type any single panel.",
    ),
    dict(
        num=4, topic=2,
        title="Floors, Ceilings, Roofs and Openings",
        objective="LO2 — Develop models and integrate design for BIM",
        desc="Complete the horizontal envelope of the building: create a floor by picking "
             "walls, add a ceiling in a reflected ceiling plan, create a roof by footprint "
             "with slope-defining edges and a second roof by extrusion, then cut a vertical "
             "shaft opening through the levels.",
        build="A building with floors, ceilings, a footprint roof and an extruded roof, plus a shaft opening cutting through every level.",
        services="Autodesk Revit, your Lab 2 model (or the LMS lab file)",
        steps=[
            ("Create the Level 1 floor: pick the exterior walls as boundaries (Extend into wall (to core)), and finish the sketch — the boundary must be a closed loop.",
             "Architecture ▸ Build ▸ Floor: Architectural ▸ Pick Walls"),
            ("Open the Level 1 ceiling plan and place a ceiling with Automatic Ceiling by clicking inside the walls that form a closed loop.",
             "Architecture ▸ Build ▸ Ceiling ▸ Automatic Ceiling"),
            ("Create the main roof by footprint on Level 2: pick the walls with an overhang, keep Defines Slope on for all edges, and finish — then open 3D to see the hips form.",
             "Architecture ▸ Build ▸ Roof ▸ Roof by Footprint"),
            ("Create a porch roof by extrusion: in an elevation view sketch an open-loop profile and extrude it, then Attach the porch walls to the underside of the roof.",
             "Architecture ▸ Build ▸ Roof ▸ Roof by Extrusion · Modify Wall ▸ Attach Top/Base"),
            ("Cut a shaft for the stair: sketch a closed loop with the Shaft tool, set Base Constraint = Level 1 and Top Constraint = Roof, and finish the opening.",
             "Architecture ▸ Opening ▸ Shaft"),
            ("Verify in a section view that the shaft cuts the floor and ceiling on every intermediate level, and use By Face / Vertical openings where a duct or chimney penetrates the roof.",
             "Architecture ▸ Opening ▸ By Face / Vertical"),
        ],
        test="The section view shows floor, ceiling and both roofs in place; the shaft opening cuts cleanly through "
             "every level it spans; and moving the shaft in one plan moves it on all levels — the model stays "
             "coordinated because every view reads the same database.",
    ),
    dict(
        num=5, topic=2,
        title="Stairs, Railings and Structural Elements",
        objective="LO2 — Develop models and integrate design for BIM",
        desc="Add vertical circulation and the load path: assemble a stair from runs and "
             "landings, host a railing on a floor edge with Sketch Path, then place "
             "structural columns on the grid intersections and frame them with beams, a "
             "beam system and a brace.",
        build="A stair with railings connecting two levels, plus a structural frame of columns, beams, a beam system and a brace.",
        services="Autodesk Revit, your Lab 2/4 model (or the LMS lab file)",
        steps=[
            ("Create a stair between Level 1 and Level 2: in stair assembly mode place a straight Run; a landing is created automatically between two runs. Finish and inspect it in 3D.",
             "Architecture ▸ Circulation ▸ Stair ▸ Run"),
            ("Add a railing along the Level 2 floor edge: Sketch Path, draw the railing line, use Pick New Host to host it on the floor, and finish.",
             "Architecture ▸ Circulation ▸ Railing ▸ Sketch Path ▸ Pick New Host"),
            ("Place structural columns at grid intersections from Level 1 to Level 2 (use At Grids to place several at once).",
             "Structure ▸ Structure ▸ Column ▸ At Grids"),
            ("Draw beams between column tops on Level 2, snapping from column to column.",
             "Structure ▸ Structure ▸ Beam"),
            ("Fill a bay with a Beam System: sketch its boundary with Pick Supports, set the Beam Type and Layout Rule (e.g. Fixed Distance), and finish.",
             "Structure ▸ Structure ▸ Beam System ▸ Sketch Beam System"),
            ("Open a framing elevation and add a diagonal Brace between a column and a beam, snapping to their ends.",
             "Structure ▸ Structure ▸ Brace"),
        ],
        test="The stair connects the two levels with automatically generated railings; columns stand on every chosen "
             "grid intersection; the beam system spaces its members per the layout rule; and the brace runs diagonally "
             "in the framing elevation — the architectural and structural elements coexist in one coordinated model.",
    ),
    dict(
        num=6, topic=2,
        title="Terrain, Building Pad and Conceptual Mass",
        objective="LO2 — Develop models and integrate design for BIM",
        desc="Set the building into its site: create a toposurface by placing points at "
             "different elevations, add a building pad from the foundation footprint, frame "
             "the 3D view with a section box, apply a grass material — then explore an "
             "in-place conceptual mass and preview generative design with Dynamo.",
        build="A site terrain with a building pad cut into it, a realistic 3D view, and an in-place conceptual mass volume.",
        services="Autodesk Revit, GSG_03_Terrain_Pad.rvt (LMS lab files), Dynamo",
        steps=[
            ("Open GSG_03_Terrain_Pad.rvt and the Site plan. Start Toposurface and place points around the building at Elevation 0, then rings of points further out at higher elevations to slope the ground.",
             "Massing & Site ▸ Model Site ▸ Toposurface ▸ Place Point"),
            ("Finish the surface and open the 3D view — the terrain now buries part of the building.",
             "Massing & Site ▸ Toposurface ▸ ✓ Finish Surface"),
            ("Add a Building Pad: sketch its boundary with Pick Walls on the foundation walls, set the pad level, and finish — the pad cuts the terrain away from the building.",
             "Massing & Site ▸ Model Site ▸ Building Pad"),
            ("Frame the model with a Section Box in the 3D view's properties and drag its grips to crop the terrain neatly around the building.",
             "3D View ▸ Properties ▸ Section Box"),
            ("Select the toposurface, and in the Material parameter choose a grass material for a realistic render, then explore Subregion, Split Surface and Graded Region on the Massing & Site tab.",
             "Toposurface ▸ Properties ▸ Material ▸ Grass"),
            ("Create an In-Place Mass: name it, sketch a profile and create a form, then Finish Mass — and open Manage ▸ Dynamo to see how a graph of nodes can drive such geometry for generative design.",
             "Massing & Site ▸ Conceptual Mass ▸ In-Place Mass · Manage ▸ Dynamo"),
        ],
        test="The 3D view shows the building sitting in a grass-covered terrain with a clean pad cut into the slope, "
             "the section box crops the site tidily, and your in-place mass appears as a volume you could later turn "
             "into walls, floors and roofs — site, mass and building live in one model.",
    ),
]
