# Row 2 — Six-area feature board

Prepared 6 November 2026. This is a local board artifact; the live FigJam board has not been edited.

## Place it on your board

1. Open `ROW-2-FEATURE-CATALOGUE.png` and place/import it to the right of Roles & Permissions in Row 2. It is the full-resolution image, not the smaller preview.
2. Keep Use Cases to its right. Columns group capabilities; vertical ordering does not indicate a process sequence.
3. For vector workflows, use `ROW-2-FEATURE-CATALOGUE.svg`, or import the six separate `AREA-xx-FEATURE-CARDS.svg` files if your application supports SVG.
4. To create editable native FigJam sticky/text cards, copy each feature's content from `ROW-2-FEATURE-CARDS.md`. Image/vector import may remain one object rather than becoming individually editable native cards.

## Files

| File | Purpose |
|---|---|
| `ROW-2-FEATURE-CATALOGUE.png` | Full-resolution six-column board image |
| `ROW-2-FEATURE-CATALOGUE.svg` | Scalable six-column vector board |
| `AREA-01-FEATURE-CARDS.svg` through `AREA-06-FEATURE-CARDS.svg` | Individual area columns |
| `ROW-2-FEATURE-CARDS.md` | Copy-ready text for all 68 cards |
| `ROW-2-FEATURE-CARDS.csv` | Structured card data |
| `ROW-2-FEATURE-CATALOGUE-preview.png` | Smaller overview preview |
| `generate_feature_board.py` | Regenerate from the current requirements catalogue using Python standard library |

Every card includes feature name, functions, actor/service, requirement/basis, priority, workflow/reference, test reference and pending/not-run status. BF identifiers are board-card labels, not new client requirement IDs.

## Scope and colors

- 31 original Must cards: green.
- 7 original Should cards: yellow.
- 3 original Could cards: gray.
- 22 CN/OR deployment cards: green **Must***, explicitly a proposed classification of individually unlabeled source obligations.
- 2 unnumbered required architectural/classroom-administration cards: green, labeled Required rather than assigning a new source ID.
- 3 proposed administration entries: white, with no source MoSCoW priority.
- Red means proposed Won't scope. No catalogue capability is colored red or excluded by this artifact.

Total: **68 entries**, covering **63 original IDs** once as primary cards plus five supporting/proposed entries. Functions remain grouped descriptions, not a numbered count of atomic actions. Approval is pending; tests have not been run.

## Regenerate

From the workspace root:

```sh
python3 IT-project-management/project/classroomcast/board/generate_feature_board.py
rsvg-convert -o IT-project-management/project/classroomcast/board/ROW-2-FEATURE-CATALOGUE.png IT-project-management/project/classroomcast/board/ROW-2-FEATURE-CATALOGUE.svg
rsvg-convert -w 1400 -o IT-project-management/project/classroomcast/board/ROW-2-FEATURE-CATALOGUE-preview.png IT-project-management/project/classroomcast/board/ROW-2-FEATURE-CATALOGUE.svg
```

SVG/Markdown/CSV generation requires only Python. PNG rendering uses the separately installed `rsvg-convert` command.
