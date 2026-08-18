"""Topic 1 — Introduction to BIM and Revit: hands-on activities (Labs 1–2).

Lab steps use the Revit ribbon path in the `command` slot (rendered as a UI
path, not a shell command). Lab project files are downloaded from the LMS
(https://lms-tms.tertiaryinfotech.com) or use the sample models installed
with Revit.
"""

DOMAIN1 = [
    dict(
        num=1, topic=1,
        title="Get Started with Revit",
        objective="LO1 — Apply Revit for Building Information Modelling (BIM)",
        desc="Tour the Revit environment on a real model: open the Autodesk sample "
             "architecture project, learn the ribbon, Properties palette, Project Browser "
             "and drawing area, then navigate plans, elevations, sections and the 3D view.",
        build="A guided tour of a complete BIM model — you can open any view, orbit the 3D model and inspect element properties.",
        services="Autodesk Revit 2024/2025, Autodesk sample project (rac_basic_sample_project.rvt)",
        steps=[
            ("Launch Revit. On the Home screen under Models click Open, browse to the Revit sample files and open the basic architecture sample project.",
             "Home ▸ Models ▸ Open ▸ rac_basic_sample_project.rvt"),
            ("Identify the four working zones: the ribbon (tools), the Properties palette (instance/type properties), the Project Browser (all views, schedules, sheets, families) and the drawing area.",
             ""),
            ("In the Project Browser expand Floor Plans and double-click Level 1. Zoom and pan with the mouse wheel; hover over a wall and read its description on the status bar.",
             "Project Browser ▸ Floor Plans ▸ Level 1"),
            ("Select a wall and inspect the Properties palette: note its Type (in the Type Selector), Base Constraint and Top Constraint. Click Edit Type to view (not change) the type parameters.",
             "Properties ▸ Type Selector / Edit Type"),
            ("Open the default 3D view and orbit the model with Shift + middle-mouse drag. Use the ViewCube to jump to Front, Top and corner views.",
             "Quick Access Toolbar ▸ Default 3D View"),
            ("Open an elevation and a section view from the Project Browser, and tile the windows to see the same model in several views at once.",
             "View ▸ Windows ▸ Tile Views"),
        ],
        test="You can name the four zones of the Revit UI, open any plan/elevation/section/3D view from the "
             "Project Browser, and read a selected element's type and constraints in the Properties palette — "
             "one model driving every view is the essence of BIM.",
    ),
    dict(
        num=2, topic=1,
        title="Convert 2D Information into a 3D Model",
        objective="LO1 — Apply Revit for Building Information Modelling (BIM)",
        desc="Turn a 2D PDF floor plan into an intelligent 3D model: create gridlines and "
             "walls to match the drawing, set the exterior walls to the 12\" Generic type and "
             "interior walls to the 6\" Generic type, constrain wall tops to Level 2 and give "
             "the corner a 30 ft radius — then add construction information to the model.",
        build="A 3D building model reproduced from a 2D plan, with correctly typed exterior/interior walls constrained to levels.",
        services="Autodesk Revit, 2D floor plan PDF (from the LMS lab files)",
        steps=[
            ("Start a new project from the Architectural template and link the 2D floor plan PDF into the Level 1 plan view as a reference underlay.",
             "File ▸ New ▸ Project ▸ Architectural Template · Insert ▸ Link PDF"),
            ("Place vertical and horizontal gridlines to match the grid intersections shown on the PDF.",
             "Architecture ▸ Datum ▸ Grid"),
            ("Draw the exterior walls over the PDF using the 12\" Generic wall type. In the Options Bar set Height to Level 2.",
             "Architecture ▸ Build ▸ Wall: Architectural ▸ Generic - 12\""),
            ("Draw the interior partition walls with the 6\" Generic wall type, also constrained to Level 2.",
             "Architecture ▸ Build ▸ Wall: Architectural ▸ Generic - 6\""),
            ("Create the curved corner wall with the Fillet Arc draw tool and set the radius to 30 ft (30' 0\").",
             "Modify | Place Wall ▸ Draw ▸ Fillet Arc ▸ Radius = 30'"),
            ("Open the default 3D view and verify the model: all walls rise from Level 1 to Level 2 and the plan matches the PDF. Select any wall and confirm its Top Constraint reads 'Up to level: Level 2'.",
             "Quick Access Toolbar ▸ Default 3D View"),
        ],
        test="The 3D view shows a closed building shell that matches the 2D PDF: exterior walls are Generic - 12\", "
             "interior walls are Generic - 6\", every wall's Top Constraint is Level 2, and the corner wall has a "
             "30 ft radius — 2D information has become an intelligent, parametric 3D model.",
    ),
]
