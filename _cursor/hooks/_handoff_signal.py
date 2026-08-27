#!/usr/bin/env python3
"""Shared compaction-pending signal. No secrets. Fail open at callers."""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PENDING = ROOT / ".cursor" / "compaction-pending.json"
ACTIVE = ROOT / "active_context.md"

MARKER_START = "<!-- compaction-signal:start -->"
MARKER_END = "<!-- compaction-signal:end -->"


def now_local() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def meta_line(data: dict) -> str:
    bits = [f"trigger={data.get('trigger') or 'unknown'}"]
    pct = data.get("context_usage_percent")
    tokens = data.get("context_tokens")
    window = data.get("context_window_size")
    if pct is not None:
        bits.append(f"~{pct}%")
    if tokens is not None and window is not None:
        bits.append(f"{tokens}/{window} tok")
    if data.get("is_first_compaction") is True:
        bits.append("first compact")
    return " · ".join(bits)


def pending_payload(data: dict) -> dict:
    return {
        "pending": True,
        "written_at": now_local(),
        "trigger": data.get("trigger") or "unknown",
        "context_usage_percent": data.get("context_usage_percent"),
        "context_tokens": data.get("context_tokens"),
        "context_window_size": data.get("context_window_size"),
        "is_first_compaction": data.get("is_first_compaction"),
        "nudged": False,
    }


def write_pending(data: dict) -> None:
    PENDING.parent.mkdir(parents=True, exist_ok=True)
    PENDING.write_text(
        json.dumps(pending_payload(data), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def read_pending() -> dict | None:
    if not PENDING.is_file():
        return None
    try:
        raw = json.loads(PENDING.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return raw if isinstance(raw, dict) else None


def mark_nudged(pending: dict) -> None:
    out = dict(pending)
    out["nudged"] = True
    PENDING.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def stamp_active_context(data: dict) -> None:
    if not ACTIVE.is_file():
        return
    text = ACTIVE.read_text(encoding="utf-8")
    rel = PENDING.relative_to(ROOT).as_posix()
    block = (
        f"{MARKER_START}\n"
        f"## Compaction signal (machine)\n\n"
        f"- **At:** {now_local()} · {meta_line(data)}\n"
        f"- Treat as thin this turn (handoff only — no new code).\n"
        f"- After handoff refresh: delete this block and `{rel}`.\n"
        f"{MARKER_END}\n"
    )
    if MARKER_START in text and MARKER_END in text:
        text = re.sub(
            re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END) + r"\n?",
            block,
            text,
            count=1,
            flags=re.S,
        )
    else:
        m = re.search(r"(\*\*Updated:\*\*[^\n]*\n)", text)
        if m:
            insert_at = m.end()
            text = text[:insert_at] + "\n" + block + "\n" + text[insert_at:]
        else:
            text = text.rstrip() + "\n\n" + block + "\n"
    ACTIVE.write_text(text, encoding="utf-8")
