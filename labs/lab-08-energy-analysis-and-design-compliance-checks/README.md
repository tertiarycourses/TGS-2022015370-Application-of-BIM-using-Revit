# Lab 8 — Energy Analysis and Design Compliance Checks

**Course:** Application of BIM using Revit (TGS-2022015370)  ·  **Topic 03:** BIM Application  ·  **Alignment:** LO3 — Apply BIM and check the output

Analyse design performance and check compliance: set the project location and energy settings, generate the energy analytical model, run a systems analysis (EnergyPlus), read the results and reports, and run an Interference Check between structural and architectural elements to find clashes.

## What you'll build

An energy analysis run with its report, plus an interference-check report of clashes between element categories.

**Tools:** Autodesk Revit, Revit Systems Analysis (EnergyPlus), your course model or the Autodesk sample project

## Step-by-step

1. Open the sample architecture project. Set the project's geographic Location, then open Energy Settings and set the Mode and building type for analysis.

   > `Analyze ▸ Energy Optimization ▸ Location / Energy Settings`

2. Generate the energy analytical model — Revit creates analytical spaces and surfaces from the building elements.

   > `Analyze ▸ Energy Optimization ▸ Create Energy Model`

3. Run a systems analysis workflow: choose 'System sizing' (design heating/cooling loads) — Revit translates the model to EnergyPlus and runs the simulation.

   > `Analyze ▸ Energy Analysis ▸ Systems Analysis`

4. Review the results: open Project Browser ▸ Reports ▸ Analysis Reports and double-click the time-stamped report; switch Report Style between Detailed and Loads.

   > `Project Browser ▸ Reports ▸ Analysis Reports`

5. Select an analytical space and read its heating, cooling and airflow peak-demand properties — the same numbers as the report, attached to the model.

   > `Analytical Space ▸ Properties`

6. Run an Interference Check between Structural Columns/Framing and Walls/Floors; export the clash report and resolve one clash, then Refresh to confirm it clears.

   > `Collaborate ▸ Coordinate ▸ Interference Check ▸ Run Interference Check`


## Test it

The Analysis Report opens with design heating and cooling loads for every zone, each analytical space carries its peak demands as properties, and the Interference Check lists each clash by element pair — after your fix and Refresh, the resolved clash disappears from the report.

---
© 2026 Tertiary Infotech Academy Pte Ltd · UEN: 201200696W