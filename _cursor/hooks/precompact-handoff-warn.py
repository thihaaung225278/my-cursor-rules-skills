#!/usr/bin/env python3
"""preCompact: warn + persist signal. Cannot block compaction (Cursor docs)."""
from __future__ import annotations

import json
import sys

from _handoff_signal import ROOT, meta_line, stamp_active_context, write_pending


def main() -> int:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        data = {}
    if not isinstance(data, dict):
        data = {}

    try:
        write_pending(data)
        stamp_active_context(data)
    except OSError:
        pass

    msg = (
        f"[{ROOT.name}] Compaction စနေပြီ ({meta_line(data)}) — summary lossy ဖြစ်နိုင်။ "
        "Agent: code/STEP 3 ရပ် · active_context.md မှာ DONE/PARTIAL/NEXT + paste ရေး · "
        "Compaction signal block + .cursor/compaction-pending.json ရှင်း။ "
        "reply = handoff သာ။ User: chat အသစ်ဖွင့် · active_context paste (သို့ `handoff only` ပြော)။ "
        "ဒီ hook က compact မပိတ်နိုင် — signal + warn သာ။"
    )
    json.dump({"user_message": msg}, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
