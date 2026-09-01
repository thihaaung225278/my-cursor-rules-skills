# Cursor Rules Flow Diagram

`_cursor/rules/` စည်းမျဉ်းများ **Mode A / Mode B** နဲ့ **Always-on / Glob-gated** rule set ဘယ်လို အလုပ်လုပ်သလဲ — diagram အတွက်။

## ဖိုင်များ

| ဖိုင် | အသုံးပြုပုံ |
|---|---|
| **cursor-rules-flow.png** | PNG ပုံ — Preview / Slack / slide မှာ တိုက်ရိုက်သုံး |
| **cursor-rules-flow.svg** | Vector — zoom လုပ်လို့ ရ၊ print အတွက် ကောင်းသည် |
| **cursor-rules-flow.html** | Browser ဖွင့်ကြည့် — Mermaid interactive + legend |
| **cursor-rules-flow.mmd** | Mermaid source — diagram ပြင်ချင်ရင် |

## ဖွင့်နည်း

```bash
# PNG (Preview.app)
open docs/rules-diagram/cursor-rules-flow.png

# HTML (Chrome/Safari — interactive)
open docs/rules-diagram/cursor-rules-flow.html
```

## Diagram အကျဉ်း

```
User Message
    │
    ├─ ..chain ──► Mode B (STEP 1→2→3)
    │                 ├─ 08-chain-steps
    │                 └─ 11-active-rules-report
    │
    └─ Normal ──► Mode A (Scout→Plan→Build တိုက်ရိုက်)

Always-on (chat တိုင်း): 00 · 13 · 14 · 19
Glob-gated (ဖိုင်ပေါ်): 01/04 · 06/07 · 15–18
```

## PNG ပြန်ထုတ်ချင်ရင်

SVG မှ PNG:

```bash
qlmanage -t -s 1400 -o docs/rules-diagram docs/rules-diagram/cursor-rules-flow.svg
mv docs/rules-diagram/cursor-rules-flow.svg.png docs/rules-diagram/cursor-rules-flow.png
```

Mermaid CLI (network + Node 18+):

```bash
npx @mermaid-js/mermaid-cli -i docs/rules-diagram/cursor-rules-flow.mmd -o docs/rules-diagram/cursor-rules-flow.png
```
