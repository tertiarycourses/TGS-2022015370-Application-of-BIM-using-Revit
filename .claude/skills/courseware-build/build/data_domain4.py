"""Topic 4 — BIM Documentation: hands-on activities (Labs 9–10)."""

DOMAIN4 = [
    dict(
        num=9, topic=4,
        title="Sheets, Worksharing and Linked Models",
        objective="LO4 — Maintain BIM database and develop BIM documentation",
        desc="Develop the construction documentation and maintain the shared model: compose "
             "a drawing sheet with a title block and viewports, add a callout and a section "
             "view, link a CAD file, enable worksharing to create a central model with "
             "worksets, and organise the project into phases.",
        build="A titled drawing sheet carrying plan + section + callout viewports, a workshared central model with worksets, and a phased project.",
        services="Autodesk Revit, your course model, a DWG file (LMS lab files)",
        steps=[
            ("Create a sheet with a title block and drag the Level 1 plan and a schedule from the Project Browser onto it — each becomes a viewport.",
             "View ▸ Sheet Composition ▸ Sheet"),
            ("Add a Section through the building and a Callout of the stair area in the plan view; open both views from their heads and place them on the sheet.",
             "View ▸ Create ▸ Section / Callout"),
            ("Link a CAD file (e.g. a surveyor's DWG) into a site view, then compare Insert ▸ Link CAD (stays external, updates) with Insert ▸ Import CAD (embedded).",
             "Insert ▸ Link ▸ Link CAD"),
            ("Enable worksharing: open Worksets — accept the default worksets to create the central model, then Save As the central file so team members can make local copies.",
             "Collaborate ▸ Manage Collaboration ▸ Worksets"),
            ("Create a phase: open Manage ▸ Phases, insert a phase after New Construction, and assign an element to it; set a view's Phase and Phase Filter to see the effect.",
             "Manage ▸ Phasing ▸ Phases"),
            ("Create a design option set for an entry alternative: Manage ▸ Design Options ▸ New, add a second option, and place variant geometry in each option.",
             "Manage ▸ Design Options"),
        ],
        test="The sheet shows plan, section and callout viewports under a filled title block; the file is now a "
             "central model whose Worksets dialog lists your worksets; the phase filter hides/shows the phased "
             "element; and switching design options swaps the entry geometry — one database, fully documented.",
    ),
    dict(
        num=10, topic=4,
        title="BIM e-Submission Standards Check",
        objective="LO4 — Maintain BIM database and develop BIM documentation",
        desc="Prepare a model for Singapore BCA BIM e-submission: apply the standard file "
             "and view naming formats, verify geo-referencing (SVY21 / SHD) and 1:1 metric "
             "scale, check the last-saved views, and assemble the submission cover page "
             "with the core information required by the regulatory agencies.",
        build="A submission-ready model: compliant file/view names, correct coordinates and scale, purged views and a complete cover page checklist.",
        services="Autodesk Revit, your course model, BCA Code of Practice for BIM e-Submission",
        steps=[
            ("Rename the model file to the 6-field e-submission format (project, originator, zone, level, type, discipline) and rename key views to the 3–4 field view naming format (e.g. A_1st Storey).",
             "File naming: <Project>-<Originator>-<Zone>-<Level>-<Type>-<Discipline>"),
            ("Verify the site model is geo-referenced to SVY21 for Easting/Northing and to Singapore Height Datum (SHD 0.000 m) for elevation, with the layout in True North orientation.",
             "Manage ▸ Coordinates / Position ▸ True North"),
            ("Confirm the model is built full-size 1:1 metric, and that no 2D view generated from it uses an odd drawing scale.",
             "Properties ▸ View Scale"),
            ("Check every last-saved view: maximum extent saved, no hidden objects or annotations, all external files loadable, irrelevant layers/drafting purged, no proprietary fonts.",
             "Manage ▸ Purge Unused · VG ▸ Reveal Hidden Elements"),
            ("Apply the colour standards for amendments and A&A works where the submission includes changes to approved plans.",
             ""),
            ("Assemble the cover page: submission authority and QP's declaration/endorsements, project information, and the list of views, schedules and sheets for approval, with the agency's minimal Core Information.",
             "Sheet: Cover Page ▸ QP declaration · Project info · View list"),
        ],
        test="Walking the e-submission checklist end-to-end passes: compliant file and view names, SVY21/SHD "
             "coordinates, 1:1 metric scale, clean last-saved views with nothing hidden or missing, correct "
             "amendment colours, and a cover page carrying the declaration, project information and view list — "
             "the model is ready for regulatory e-submission.",
    ),
]
