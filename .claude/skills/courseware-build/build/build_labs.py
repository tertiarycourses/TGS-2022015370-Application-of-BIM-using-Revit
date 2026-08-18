#!/usr/bin/env python3
"""Generate labs/ from the single source: one folder per lab (README.md + its
Revit dataset files) plus a labs/README.md index. Dataset files are copied from
reference/datasets/ when present (they are also on the LMS)."""
import os, re, shutil, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3; from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
ACT=DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4+DOMAIN5
def _find_repo(start):
    env=os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d=start
    for _ in range(8):
        d=os.path.dirname(d)
        if os.path.isdir(os.path.join(d,"courseware")) and os.path.isdir(os.path.join(d,"labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO=_find_repo(HERE)
LABS=os.path.join(REPO,"labs"); DS=os.path.join(REPO,"reference","datasets")

# lab number -> dataset files copied into the lab folder
DATASETS={
 2:["Planning Site.pdf","Site Image.png","Planning Site solution.rvt"],
 3:["Embed Walls.rvt","Embed Walls solution.rvt"],
 4:["Create Ceilings.rvt","Create Ceilings Solution.rvt"],
 5:["Studio Block.rvt","Studio Block Structure.rvt","Studio Block Finished.rvt"],
 7:["Create View Template.rvt","Create View Template solution.rvt"],
 9:["CA-L15-01-Use PDF and Images.rvt"],
}

def slug(t):
    s=re.sub(r"[^a-z0-9]+","-",t.lower()).strip("-")
    return s[:60].rstrip("-")

TOPICS={t["num"]:t for t in C.TOPICS}
index=[f"# {C.TITLE} — Hands-On Labs","",
 f"Ten hands-on Autodesk Revit labs for the WSQ course **{C.TITLE}** ({C.COURSE_CODE}), "
 f"aligned to the Skills Framework TSC {C.TSC_TITLE} ({C.TSC_CODE}). "
 "Each lab has its own folder with a README and the Revit dataset files it uses "
 "(also downloadable from the LMS at https://lms-tms.tertiaryinfotech.com).","",
 "| Lab | Title | Topic | Datasets |","|---|---|---|---|"]

for a in ACT:
    d=os.path.join(LABS,f"lab-{a['num']:02d}-{slug(a['title'])}")
    os.makedirs(d,exist_ok=True)
    files=DATASETS.get(a["num"],[])
    for f in files:
        srcp=os.path.join(DS,f)
        if os.path.exists(srcp): shutil.copy2(srcp,os.path.join(d,f))
    t=TOPICS[a["topic"]]
    md=[f"# Lab {a['num']} — {a['title']}","",
        f"**Course:** {C.TITLE} ({C.COURSE_CODE})  ·  **Topic {t['code']}:** {t['title']}  ·  **Alignment:** {a['objective']}","",
        f"{a['desc']}","",
        "## What you'll build","",a["build"],"",
        f"**Tools:** {a['services']}",""]
    if files:
        md+=["## Dataset files in this folder",""]+[f"- `{f}`" for f in files]+[""]
    md+=["## Step-by-step",""]
    for i,(instr,cmd) in enumerate(a["steps"],1):
        md.append(f"{i}. {instr}")
        if cmd: md+=["",f"   > `{cmd}`",""]
    md+=["","## Test it","",a["test"],"","---",
         f"© 2026 {C.ORG} · {C.UEN}"]
    open(os.path.join(d,"README.md"),"w").write("\n".join(md))
    index.append(f"| {a['num']:02d} | [{a['title']}](lab-{a['num']:02d}-{slug(a['title'])}/) | Topic {t['code']}: {t['title']} | {', '.join(files) if files else '—'} |")

index+=["", "Lab 1 uses the Autodesk sample project installed with Revit (`rac_basic_sample_project.rvt`); "
 "Lab 6 uses `GSG_03_Terrain_Pad.rvt` from the Revit Getting Started files (or any small project model); "
 "Labs 8 and 10 continue on your own course model.","",
 f"© 2026 {C.ORG} · {C.UEN}"]
open(os.path.join(LABS,"README.md"),"w").write("\n".join(index))
print("labs/ generated:",len(ACT),"lab folders")
