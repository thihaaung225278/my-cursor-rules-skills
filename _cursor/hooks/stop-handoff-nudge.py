#!/usr/bin/env python3
"""stop: one auto follow-up after compaction signal. loop_limit=1 in hooks.json."""
from __future__ import annotations

import json
import sys

from _handoff_signal import mark_nudged, read_pending

FOLLOWUP = (
    "handoff only — no code. Compaction just ran (lossy summary). "
    "Read active_context.md + progress.md. Refresh DONE / PARTIAL / NEXT + paste block. "
    "Reply with short status + paste only. Then delete the Compaction signal block in "
    "active_context.md and delete .cursor/compaction-pending.json."
)


def main() -> int:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        data = {}
    if not isinstance(data, dict):
        data = {}

    pending = read_pending()
    should = (
        data.get("status") == "completed"
        and int(data.get("loop_count") or 0) == 0
        and pending is not None
        and pending.get("pending") is True
        and pending.get("nudged") is not True
    )
    if not should:
        json.dump({}, sys.stdout)
        sys.stdout.write("\n")
        return 0

    try:
        mark_nudged(pending)
    except OSError:
        pass

    json.dump({"followup_message": FOLLOWUP}, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
