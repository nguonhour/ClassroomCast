"""Build local SVG/Markdown/CSV feature cards from the requirements catalogue."""

from pathlib import Path
import csv
import html
import re
import textwrap
import xml.etree.ElementTree as ET


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "REQUIREMENTS-AND-ACTIVITIES.md"
PALETTE = {
    "Must": ("#DCFCE7", "#15803D", "MUST"),
    "Should": ("#FEF3C7", "#B45309", "SHOULD"),
    "Could": ("#E5E7EB", "#6B7280", "COULD"),
    "Deployment": ("#DCFCE7", "#15803D", "MUST* / proposed classification"),
    "Required": ("#DCFCE7", "#15803D", "REQUIRED / source obligation"),
    "Proposed": ("#FFFFFF", "#64748B", "PROPOSED / no source priority"),
}
SHORT_NAMES = [
    "Classroom broadcasting",
    "Classroom management\nand participation",
    "Network access control",
    "Deployment and\ninfrastructure",
    "Diagnostics, verification\nand recovery",
    "Application administration\nand security",
]


def wrap(value, width=46):
    return textwrap.wrap(value, width=width, break_long_words=False,
                         break_on_hyphens=False) or [""]


def text(x, y, lines, size=15, weight=400, fill="#0F172A", leading=20):
    if isinstance(lines, str):
        lines = [lines]
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else leading}">{html.escape(line)}</tspan>'
        for i, line in enumerate(lines)
    )
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}">{spans}</text>')


def rect(x, y, w, h, fill, stroke="none", radius=12):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
            f'fill="{fill}" stroke="{stroke}"/>')


def read_areas():
    source = SOURCE.read_text()
    catalogue = source.split("## Product areas, features and functions", 1)[1]
    catalogue = catalogue.split("## Four user roles and account model", 1)[0]
    groups = re.findall(
        r"^### (Area (\d{2})[^\n]*)\n(.*?)(?=^### Area \d{2}|^### Source priority|\Z)",
        catalogue, re.M | re.S,
    )
    result = []
    for heading, number, body in groups:
        cards = []
        for line in body.splitlines():
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if not cells or cells[0] == "Feature" or re.fullmatch(r":?-+:?", cells[0]):
                continue
            if number == "04":
                name, functions, actor, basis, flows = cells
                priority = "Deployment"
            else:
                name, functions, actor, basis, source_priority, flows = cells
                if source_priority in ("Must", "Should", "Could"):
                    priority = source_priority
                elif source_priority.startswith("Required by source"):
                    priority = "Required"
                else:
                    priority = "Proposed"
            primary = re.fullmatch(r"(?:NAC|CN|OR|T|S)\d{2}", basis)
            if primary:
                refs = [basis]
                tests = ["TC-" + basis]
                display_basis = basis
            else:
                refs = []
                display_basis = "Unnumbered source obligation" if priority == "Required" else "Proposed supporting capability"
                tests = ["TC-RECOVERY", "TC-LOCAL"] if name == "Basic health and operations" else ["TC-AUTH"]
            cards.append({
                "card_id": f"BF-{number}-{len(cards) + 1:02}",
                "area": heading,
                "area_number": number,
                "feature": name,
                "functions": functions,
                "actor": actor,
                "basis": basis,
                "display_basis": display_basis,
                "source_ids": " ".join(refs),
                "priority": priority,
                "priority_label": PALETTE[priority][2],
                "flows": flows,
                "tests": ", ".join(tests),
                "approval": "Pending confirmation",
                "test_status": "Not run",
            })
        result.append((heading, number, cards))
    assert [len(a[2]) for a in result] == [7, 11, 13, 22, 7, 8]
    ids = [c["source_ids"] for _, _, cards in result for c in cards if c["source_ids"]]
    assert len(ids) == len(set(ids)) == 63
    return result


def render_card(card, x, y):
    fill, border, badge = PALETTE[card["priority"]]
    content = []
    cursor = y + 26
    content.append(text(x + 18, cursor, badge.upper(), 10, 700, border))
    cursor += 27
    title = wrap(card["feature"], 31)
    content.append(text(x + 18, cursor, title, 18, 700, leading=23))
    cursor += (len(title) - 1) * 23 + 26
    content.append(text(x + 18, cursor, card["display_basis"] + "  |  " + card["card_id"], 12, 600))
    cursor += 27
    content.append(text(x + 18, cursor, "FUNCTIONS", 10, 700, border))
    cursor += 20
    functions = wrap(card["functions"])
    content.append(text(x + 18, cursor, functions, 14, leading=19))
    cursor += (len(functions) - 1) * 19 + 26
    actors = wrap("Actor / service: " + card["actor"], 48)
    content.append(text(x + 18, cursor, actors, 12, leading=17))
    cursor += (len(actors) - 1) * 17 + 22
    flow_lines = wrap("Workflows / references: " + card["flows"], 49)
    content.append(text(x + 18, cursor, flow_lines, 12, leading=17))
    cursor += (len(flow_lines) - 1) * 17 + 22
    content.append(text(x + 18, cursor, "Test refs: " + card["tests"], 12))
    cursor += 25
    content.append(text(x + 18, cursor, "Approval pending  /  Tests not run", 11, 600, "#475569"))
    height = cursor - y + 20
    return rect(x, y, 416, height, fill, border) + "".join(content), height


def svg_document(width, height, content, description):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img">'
            '<title>ClassroomCast — Row 2 feature catalogue</title>'
            f'<desc>{html.escape(description)}</desc>'
            '<g font-family="Helvetica Neue, Arial, sans-serif">' + content + '</g></svg>')


def render_area(heading, number, cards, x, y):
    content = rect(x, y, 440, 104, "#18263B")
    content += text(x + 18, y + 24, "AREA " + number + "  /  " + str(len(cards)) + " FEATURES", 11, 700, "#CBD5E1")
    content += text(x + 18, y + 52, SHORT_NAMES[int(number) - 1].split("\n"), 20, 700, "#FFFFFF", 25)
    cursor = y + 122
    for card in cards:
        fragment, height = render_card(card, x + 12, cursor)
        content += fragment
        cursor += height + 16
    return content, cursor


def main():
    areas = read_areas()
    cards = [c for _, _, group in areas for c in group]
    content = rect(0, 0, 2832, 250, "#18263B", radius=0)
    content += text(36, 49, "ROW 2 — WHO AND WHICH CAPABILITIES", 15, 700, "#CBD5E1")
    content += text(36, 95, "Six Product Areas → Features → Functions", 34, 700, "#FFFFFF")
    content += text(36, 132, "ClassroomCast  /  68 catalogue entries  /  63 original IDs  /  Draft for client review  /  6 November 2026", 17, 400, "#E2E8F0")
    content += text(36, 163, "Columns group scope. Vertical order is not a workflow. Colors show priority, not completion or approval.", 16, 400, "#E2E8F0")
    legends = [("MUST", "#DCFCE7"), ("SHOULD", "#FEF3C7"), ("COULD", "#E5E7EB"), ("WON'T — proposed exclusion", "#FEE2E2"), ("WHITE — proposed / unclassified", "#FFFFFF")]
    x = 36
    for title, fill in legends:
        width = max(130, len(title) * 8 + 30)
        content += rect(x, 190, width, 34, fill, radius=7)
        content += text(x + 12, 212, title, 12, 700)
        x += width + 12
    bottom = 0
    for i, (heading, number, group) in enumerate(areas):
        fragment, end = render_area(heading, number, group, 36 + i * 456, 278)
        content += fragment
        bottom = max(bottom, end)
        single, single_end = render_area(heading, number, group, 18, 24)
        single = rect(0, 0, 476, single_end + 32, "#F8FAFC", radius=0) + single
        path = HERE / f"AREA-{number}-FEATURE-CARDS.svg"
        path.write_text(svg_document(476, single_end + 32, single, heading + ": individual feature cards with source priorities."))
    foot = bottom + 18
    content += rect(36, foot, 2720, 156, "#FFFFFF", "#CBD5E1")
    notes = [
        "MUST* on CN/OR is a proposed classification: all 22 source deployment obligations are individually unlabeled.",
        "Two unnumbered required source obligations are green; three proposed administration entries remain white. No new original requirement IDs are invented.",
        "Red is reserved for proposed Won't scope: no feature card here is excluded. Existing exclusion proposals stay in the requirements companion.",
        "Function text is grouped, not an atomic-function count. TC references are specifications, not executed tests. See the report for exact acceptance and permissions.",
        "Source: REQUIREMENTS-AND-ACTIVITIES.md, revision 0.5. Each original requirement has one primary card; cross-cutting work can involve several areas.",
    ]
    content += text(54, foot + 29, notes, 14, leading=26)
    height = foot + 198
    content = rect(0, 250, 2832, height - 250, "#F8FAFC", radius=0) + content
    main_path = HERE / "ROW-2-FEATURE-CATALOGUE.svg"
    main_path.write_text(svg_document(2832, height, content, "Six columns containing 68 feature cards. MoSCoW colors preserve the requirement catalogue's scope and proposal status."))
    md = ["# Row 2 — Six-area feature catalogue\n\nPrepared 6 November 2026 from REQUIREMENTS-AND-ACTIVITIES.md revision 0.5. Draft for client review.\n\n"]
    md.append("**Board placement:** beside Roles & Permissions, before Use Cases. Import the full SVG or the six individual area SVGs. Markdown is the editable content source for copying native text/sticky cards; SVG import is a visual artifact and may not create individually editable FigJam cards.\n\n")
    md.append("Green = Must; yellow = Should; gray = Could; red = proposed Won't; white = unclassified/proposed. CN/OR green Must* is proposed, not source-labeled. No red feature card is included because this catalogue contains capabilities, not excluded proposals.\n\n")
    md.append("**Counts:** 68 entries = 63 original IDs + 2 unnumbered required obligations + 3 proposed administration entries. This is not 68 approved client requirements or an atomic-function count.\n\n")
    for heading, number, group in areas:
        md.append(f"## {heading} — {len(group)} entries\n\n")
        for card in group:
            md.append(f"### {card['card_id']} — {card['feature']}\n\n")
            md.append(f"- **Priority:** {card['priority_label']}\n- **Requirement / basis:** {card['basis']}\n- **Actor / service:** {card['actor']}\n- **Functions:** {card['functions']}\n- **Workflows / references:** {card['flows']}\n- **Test references:** {card['tests']}\n- **Approval:** Pending confirmation\n- **Test result:** Not run\n\n")
    (HERE / "ROW-2-FEATURE-CARDS.md").write_text("".join(md))
    with (HERE / "ROW-2-FEATURE-CARDS.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(cards[0]))
        writer.writeheader()
        writer.writerows(cards)
    for path in HERE.glob("*.svg"):
        ET.parse(path)
    print("Created main SVG, six area SVGs, 68-card Markdown and CSV.")
    print("Board dimensions:", 2832, "x", height)
    print("Counts:", {key: sum(c["priority"] == key for c in cards) for key in PALETTE})


if __name__ == "__main__":
    main()
