#!/usr/bin/env python3
"""sessionStart: inject file-SoT reminder. Fire-and-forget (Cursor docs)."""
from __future__ import annotations

import json
import sys

from _handoff_signal import read_pending


def main() -> int:
    pending = read_pending()
    parts = [
        "Handoff SoT: read active_context.md then progress.md before acting. Chat recall is not SoT.",
        "Pins: SPFx 1.20 gulp, React 17, Fluent v8. Reject Heft/v9, classic master, secrets, Codegraph Cursor hooks.",
        "If context thin or Status/NEXT stale: handoff only — no code.",
        "Mode B: ..chain → y → y; one STEP per y.",
    ]
    if pending and pending.get("pending"):
        parts.insert(
            1,
            "Compaction signal is pending on disk — this turn is handoff only (no new code). "
            "Refresh DONE/PARTIAL/NEXT + paste, then delete the Compaction signal block "
            "and .cursor/compaction-pending.json.",
        )
    json.dump({"additional_context": " ".join(parts)}, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
