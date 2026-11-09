# Row 3 — corrected F01

Updated 8 November 2026. These files are local planning artifacts; the live FigJam board has not been changed.

1. Open [F01-MASTER-PROMPT.md](F01-MASTER-PROMPT.md). Copy everything below its separator into ChatGPT. It includes the full corrected Mermaid source and instructions for readable responsibility lanes/panels.
2. Use [F01-CLASSROOM-LIFECYCLE.mmd](F01-CLASSROOM-LIFECYCLE.mmd) directly if you only need the Mermaid code.
3. Export the rendered diagram/panels as SVG or PNG, then place them in Row 3 above the detailed F05/F06/F10/F13 diagrams. A combined source may still need panel layout refinement by the renderer.

The source is synchronized with F01 in both requirements documents. It separates aborted startup from normal class end, handles failed/pending subprocess outcomes, allows publication before viewers join, checks end authority through F13 before changes, and records distinct restoration outcomes before terminal nodes. Incomplete media/access closure stays **Class ending**, rather than falsely claiming the class ended.

Checks cover diagram-source structure and lifecycle reachability. Product tests remain Not run; no visual Mermaid render has been performed in this update.
