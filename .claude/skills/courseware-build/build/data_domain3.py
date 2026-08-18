"""Topic 3 — BIM Application: hands-on activities (Labs 7–8)."""

DOMAIN3 = [
    dict(
        num=7, topic=3,
        title="View Templates, Schedules and Quantity Takeoffs",
        objective="LO3 — Apply BIM and check the output",
        desc="Operate BIM to produce controlled, quantified output: build a furniture-layout "
             "view with a scope box and visibility/graphic overrides and save it as a view "
             "template, then create a door schedule and a wall material takeoff, and add a "
             "calculated-value field for a preliminary cost estimate.",
        build="A styled Floor 2 Furniture Layout view template, a sorted door schedule, and a wall material takeoff with a calculated cost column.",
        services="Autodesk Revit, Create View Template.rvt (LMS lab files)",
        steps=[
            ("Open Create View Template.rvt. Duplicate the Floor 2 plan view and rename it Floor 2 Furniture Layout, then apply the Main Zone scope box to set its crop region.",
             "Project Browser ▸ Floor 2 ▸ Duplicate View · Properties ▸ Scope Box = Main Zone"),
            ("Open Visibility/Graphic Overrides (VG). Override the Walls Cut pattern to Solid Fill light grey with light-grey lines, and the Furniture projection lines/pattern to red Diagonal Down-Small.",
             "View ▸ Graphics ▸ Visibility/Graphics (VG)"),
            ("On the Annotation Categories tab switch off Sections and set Grids to Halftone, then close VG and review the styled view.",
             "VG ▸ Annotation Categories"),
            ("Save the styling as a template: right-click the view ▸ Create View Template From View, and apply it to another duplicate to prove the styling is reusable.",
             "Right-click view ▸ Create View Template From View"),
            ("Create a door schedule: Schedule/Quantities, category Doors, add fields (Mark, Level, Width, Height, Count), and sort by Level — the schedule fills itself from the model.",
             "View ▸ Create ▸ Schedules ▸ Schedule/Quantities ▸ Doors"),
            ("Create a Material Takeoff for Walls with Material: Name and Material: Area, then add a Calculated Value field (e.g. Cost = Area × unit rate) to produce a preliminary cost estimate.",
             "View ▸ Schedules ▸ Material Takeoff ▸ Calculated Value"),
        ],
        test="Applying your view template restyles a fresh duplicate in one click; the door schedule lists every door "
             "sorted by level and updates when a door is deleted; and the wall takeoff's calculated column prices the "
             "walls from live model quantities — the model is the single quantity and cost database.",
    ),
    dict(
        num=8, topic=3,
        title="Energy Analysis and Design Compliance Checks",
        objective="LO3 — Apply BIM and check the output",
        desc="Analyse design performance and check compliance: set the project location and "
             "energy settings, generate the energy analytical model, run a systems analysis "
             "(EnergyPlus), read the results and reports, and run an Interference Check "
             "between structural and architectural elements to find clashes.",
        build="An energy analysis run with its report, plus an interference-check report of clashes between element categories.",
        services="Autodesk Revit, Revit Systems Analysis (EnergyPlus), your course model or the Autodesk sample project",
        steps=[
            ("Open the sample architecture project. Set the project's geographic Location, then open Energy Settings and set the Mode and building type for analysis.",
             "Analyze ▸ Energy Optimization ▸ Location / Energy Settings"),
            ("Generate the energy analytical model — Revit creates analytical spaces and surfaces from the building elements.",
             "Analyze ▸ Energy Optimization ▸ Create Energy Model"),
            ("Run a systems analysis workflow: choose 'System sizing' (design heating/cooling loads) — Revit translates the model to EnergyPlus and runs the simulation.",
             "Analyze ▸ Energy Analysis ▸ Systems Analysis"),
            ("Review the results: open Project Browser ▸ Reports ▸ Analysis Reports and double-click the time-stamped report; switch Report Style between Detailed and Loads.",
             "Project Browser ▸ Reports ▸ Analysis Reports"),
            ("Select an analytical space and read its heating, cooling and airflow peak-demand properties — the same numbers as the report, attached to the model.",
             "Analytical Space ▸ Properties"),
            ("Run an Interference Check between Structural Columns/Framing and Walls/Floors; export the clash report and resolve one clash, then Refresh to confirm it clears.",
             "Collaborate ▸ Coordinate ▸ Interference Check ▸ Run Interference Check"),
        ],
        test="The Analysis Report opens with design heating and cooling loads for every zone, each analytical space "
             "carries its peak demands as properties, and the Interference Check lists each clash by element pair — "
             "after your fix and Refresh, the resolved clash disappears from the report.",
    ),
]
