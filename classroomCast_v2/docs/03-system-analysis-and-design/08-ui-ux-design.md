# UI and UX design

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Screen inventory proposal

| Role / screen | Primary actions | Required visible states | Flows |
|---|---|---|---|
| Teacher class page | Create/start/end; show URL/code/QR; select assigned profile | Created/open/ending/ended, actual restriction status | F04/F01/F13 |
| Teacher broadcast panel | Capture, supported audio/quality, pause/resume/stop | Requested versus confirmed publishing state, capture limitation | F06/F07 |
| Teacher roster | Approve/reject/remove/block | Pending/admitted/blocked/removed, connection and unresolved cleanup | F05/F08 |
| Student join | Network instructions, code, optional agreed ID | Invalid/full/pending/rejected/closed | F05 |
| Student viewer | Playback, volume, fullscreen | Admitted waiting, viewing, media unavailable, revoked/ended | F06/F07/F12 |
| Scoped policy dashboard | Profiles, approved scope, apply/restore | Saved/applying/verified/degraded/restoration unresolved; scope/time | F09/F10/F14 |
| Authorized diagnostics | Component health and recovery evidence | Component fault, action pending, verified or unresolved result | F15 |
| SYS administration | Accounts/roles/settings within agreed scope | Permission denied, validated changes, audit outcome | D01/D14 proposals |

## 2. Interaction rules

Starting class and starting screen capture are distinct. Stop sharing must not look like End class. A saved profile must not display a verified badge. Provide actionable error text without exposing credentials or another class's data. Teacher approval is not the same as media becoming available. Show pending restoration after verified class closure.

## 3. Accessibility and review

Use readable labels, keyboard-operable controls and text/icons alongside color. The board's MoSCoW palette denotes priority only; operational success/failure needs a separate labeled legend. Accessibility specifics and supported browser/layout matrix require usability review rather than an unsupported conformance claim.

## 4. Prototype evaluation

Give pilot teacher tasks: create class, share joining information, start screen/audio, admit/remove student, stop sharing, end class and interpret restoration failure. Students join, adjust playback, recover connection and recognize denied access. Record completion, assistance, error interpretation and improvement; do not invent trial results.
