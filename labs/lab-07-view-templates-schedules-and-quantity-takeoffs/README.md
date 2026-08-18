# Lab 7 — View Templates, Schedules and Quantity Takeoffs

**Course:** Application of BIM using Revit (TGS-2022015370)  ·  **Topic 03:** BIM Application  ·  **Alignment:** LO3 — Apply BIM and check the output

Operate BIM to produce controlled, quantified output: build a furniture-layout view with a scope box and visibility/graphic overrides and save it as a view template, then create a door schedule and a wall material takeoff, and add a calculated-value field for a preliminary cost estimate.

## What you'll build

A styled Floor 2 Furniture Layout view template, a sorted door schedule, and a wall material takeoff with a calculated cost column.

**Tools:** Autodesk Revit, Create View Template.rvt (LMS lab files)

## Dataset files in this folder

- `Create View Template.rvt`
- `Create View Template solution.rvt`

## Step-by-step

1. Open Create View Template.rvt. Duplicate the Floor 2 plan view and rename it Floor 2 Furniture Layout, then apply the Main Zone scope box to set its crop region.

   > `Project Browser ▸ Floor 2 ▸ Duplicate View · Properties ▸ Scope Box = Main Zone`

2. Open Visibility/Graphic Overrides (VG). Override the Walls Cut pattern to Solid Fill light grey with light-grey lines, and the Furniture projection lines/pattern to red Diagonal Down-Small.

   > `View ▸ Graphics ▸ Visibility/Graphics (VG)`

3. On the Annotation Categories tab switch off Sections and set Grids to Halftone, then close VG and review the styled view.

   > `VG ▸ Annotation Categories`

4. Save the styling as a template: right-click the view ▸ Create View Template From View, and apply it to another duplicate to prove the styling is reusable.

   > `Right-click view ▸ Create View Template From View`

5. Create a door schedule: Schedule/Quantities, category Doors, add fields (Mark, Level, Width, Height, Count), and sort by Level — the schedule fills itself from the model.

   > `View ▸ Create ▸ Schedules ▸ Schedule/Quantities ▸ Doors`

6. Create a Material Takeoff for Walls with Material: Name and Material: Area, then add a Calculated Value field (e.g. Cost = Area × unit rate) to produce a preliminary cost estimate.

   > `View ▸ Schedules ▸ Material Takeoff ▸ Calculated Value`


## Test it

Applying your view template restyles a fresh duplicate in one click; the door schedule lists every door sorted by level and updates when a door is deleted; and the wall takeoff's calculated column prices the walls from live model quantities — the model is the single quantity and cost database.

---
© 2026 Tertiary Infotech Academy Pte Ltd · UEN: 201200696W