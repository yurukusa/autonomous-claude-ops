# Autonomous Claude Ops

**Your AI agent isn't lazy. It's busy at the floor — and that's worse.**

This is the free companion to the short book *[Autonomous Claude Ops](#get-the-book)*. It contains a tool you can run today, a free sample chapter, and the core idea, so you can check the claim against your own machine before reading another word.

---

## The 60-second version

I ran Claude Code autonomously for a month and built every safeguard against the obvious fear — that it would sit idle. It worked: the machine almost never went idle. Then I counted my own session logs:

- **295 sessions**, a **median of 488 assistant responses each**
- **85%** of sessions did **100+** responses — the machine was a firehose
- only **2%** did nothing

…and in the same month it produced **47 product folders, 36 finished-but-unpublished drafts, and almost nothing that reached a single reader.**

The failure mode of autonomous AI operation is **not idleness**. It's **motion that never reaches anyone**, and a tireless agent generates that comforting motion *faster* than a lazy one. This repo and the book are about catching it.

## Run the audit on your own logs

`verify.py` reads your local Claude Code session logs (read-only — it writes nothing) and shows the shape of your own activity:

```bash
python3 verify.py
```

It reports your session count, the median responses per session, and how many ran past 100. If the median is in the hundreds and your *outward* output (things published, shipped, sold) is near zero, you are where I was. (For a richer version that also breaks down where your tokens actually go, see [`cc-ops-audit`](https://gist.github.com/yurukusa/94f847ee8096ae5d821a2213989760e4).)

## Free sample chapter

[**Chapter 1 — The Busy-Machine Trap**](SAMPLE-chapter-1.md) is included here in full. It's the diagnosis; the book is the fix.

## What the book covers

Six short chapters, one idea aimed at six surfaces, every claim checkable against your own logs — deliberately *not* another 500-page "build powerful agents" manual:

1. **The Busy-Machine Trap** — why activity isn't progress *(free, in this repo)*
2. **The Outcome Ledger** — redefine progress so busywork can't count as a win
3. **The Gate Before the Action** — two questions that kill floor-pointed work before it starts
4. **The Silent Failure** — when a tool reports success but changed nothing (a confirmed `ENOSPC` case), and how to make the silence loud
5. **The Drain You Can't See** — where your tokens really go (it isn't the size of the edit)
6. **Surviving the Session Boundary** — the one handoff rule that stops every restart from re-deriving what the last session settled

## Get the book

***Autonomous Claude Ops* is now live on [Gumroad (~$6, instant download)](https://yurukusa.gumroad.com/l/iglmx)** — all 7 chapters, including Ch.7 *The Reset You Didn't Type* (the `git reset --hard` you never ran). The free `verify.py` above runs the same audit the book is built on. A Kindle / Leanpub edition is in progress.

## License

The tools in this repo (`verify.py`) are MIT licensed — use them however you like. The sample chapter is shared free; the full book text is not under the MIT license.
