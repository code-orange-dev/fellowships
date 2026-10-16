# Developer Fellowship: Guidelines & Expectations

> $512 a month, paid in bitcoin, for 6 months, to build Bitcoin or Nostr open source with a mentor.
> Read online at **[codeorange.dev/fellowships/guidelines](https://codeorange.dev/fellowships/guidelines)** · Apply at **[codeorange.dev/fellowships/apply](https://codeorange.dev/fellowships/apply)**

This page is the short, practical version of everything in this folder: the bar to apply, what you build, the weekly rhythm, how pay works, and what happens when a month goes sideways. The deal in one line:

**You show up every week and tell us honestly how it's going; we pay you, unblock you, and help you get to your next step.**

---

## At a glance

| | |
|---|---|
| **Stipend** | $512 a month, paid in bitcoin |
| **Length** | 6 months, extendable after the month-6 review |
| **Time** | 15–20 hours a week (part-time is fine) |
| **Scope** | Any Bitcoin or Nostr open-source project. Privacy projects are a big plus. |
| **Support** | A mentor, a peer group of fellows, a fellow dashboard and a public proof-of-work page |

---

## 1. The bar to apply

We pick people who have already started. We judge where you're heading, not just where you are.

**Must have**

- **You've done the learning.** A Code Orange cohort (like [Decoding Bitcoin](https://codeorange.dev/decoding-bitcoin)), Chaincode, Summer of Bitcoin, Btrust, or serious self-study.
- **At least one PR or real review** on the project you want to work on. Small is fine.
- **A working setup:** you can build the project and run its tests.
- **Time:** 15–20 hours a week for 6 months.
- **A 6-month plan** with one goal per month.
- **Okay with working in public:** your monthly highlights and GitHub work go on your proof-of-work page. Payments stay private.

**Makes you stand out**

- A maintainer or contributor of the project who will vouch for your plan.
- Work on a [Privacy Track](https://codeorange.dev/privacy-track) project: Payjoin, Silent Payments, Floresta, JoinMarket, OpenSwap, Fedimint, ecash.
- Reviews of other people's PRs, not just your own code.
- Showing up: Code Review Club, BitDevs, project calls, Discord.
- Helping others learn.
- Builders from Southeast Asia and from regions with few Bitcoin developers get priority.

The [readiness check](https://codeorange.dev/fellowships/apply) tells you what's missing before you apply.

---

## 2. What you can build

Anything Bitcoin or Nostr, as long as it's open source. See the difficulty-rated [project menu](project-menu.md).

- **Privacy (a big plus):** rust-payjoin, rust-silentpayments, Floresta, JoinMarket, OpenSwap, Fedimint, Cashu / ecash, Kyoto
- **Wallets, Lightning, protocol:** BDK, LDK, BTCPay Server, rust-bitcoin, Bitcoin Core, Core Lightning, LND
- **Nostr:** rust-nostr, NDK, nostr-tools, NIPs, Nostr Wallet Connect, relays and clients

**What counts as work:** PRs, code review, tests, benchmarks, bug reports with a reproduction, docs and design discussion. A careful review is worth as much as a small PR. We never judge a month by merge count alone, and we never want low-value PRs opened to look busy.

---

## 3. The 6-month arc

You agree one milestone per month with your mentor in month 1. Defaults:

1. **Get set up:** build and tests pass, introduce yourself, read recent PRs, first small PR, refine your plan.
2. **Find your groove:** 2+ PRs, at least one with real functionality; review others' work weekly.
3. **Check in honestly:** keep shipping; month-3 review with your mentor.
4. **Go deep:** a feature, refactor or hard bug.
5. **Finish the big piece:** land it or get it close; start your handoff.
6. **Land it and show it:** wrap up PRs, document, demo to the community, line up your next step.

---

## 4. Your weekly rhythm

| When | What | Where |
|---|---|---|
| Every Monday | 2-minute standup: did, next, blocked. Tick "I'd like help" to get a call. | Fellow dashboard |
| Every week | 30–60 minute mentor call | Call |
| Every Friday | Review at least one PR by someone else | GitHub |
| Every 2 weeks | Fellows sync: short demo or update | Discord |
| By the 5th | Monthly report: shipped, PRs, reviews, next. It's your invoice. | Fellow dashboard |
| Month 3 & 6 | 45-minute check / 1-hour review | Call |

No timesheets. If it helps the project and you can link to it, it counts.

---

## 5. Getting paid

- **$512 a month, paid in bitcoin.** The dollar amount is fixed; the sats depend on the price.
- **Price reference:** the **Coinbase BTC-USD spot price at the moment the payment is sent**. It never changes mid-fellowship.
- **Timing:** report by the 5th; once approved, paid by the 10th.
- **Rail:** Lightning, on-chain or ecash, your choice, switchable any month.
- **Safety:** a changed payout address is confirmed with you on a second channel before we pay.
- **Private:** payments, amounts and addresses are never published. Only you and the organisers see them, on your dashboard.
- **Taxes:** this is a fellowship, not employment. Tax where you live is yours to handle.

Full detail: [payment and reporting](../shared/payment-and-reporting.md).

---

## 6. Accountability with support

A fellow who reports "nothing merged, here's what I was stuck on and what I'm trying next" is in good standing. A fellow who goes quiet for three weeks isn't, because we can't help someone we can't see.

| Status | Means | What happens |
|---|---|---|
| 🟢 Green | Standups and reports coming in | Carry on |
| 🟡 Yellow | Missed standups or a stuck project | A call and a written 30-day recovery plan |
| 🔴 Red | No contact or no progress after the plan | Pause or end, with a respectful handoff |

Step by step: a missed Monday gets a friendly ping; two silent weeks get a call; a month off track gets a named concern and a 30-day plan; still off track means pause or end. The last month worked is always paid.

**Pausing:** up to 2 months, no explanation needed, no pay during it, and the term extends by the same amount. Pausing is always better than disappearing.

Being honest about a bad month never counts against you; hiding one is the only thing that does. Full detail: [evaluation rubric](../shared/evaluation-rubric.md).

---

## 7. Public proof of work

Every fellow gets a public page at `codeorange.dev/fellowships/f/<github>` that fills itself as they work.

| Public | Private (fellow + organisers only) |
|---|---|
| Name or nym and GitHub, project, the 6 milestones, PRs opened and reviewed on GitHub, monthly highlights (summary, PRs, reviews, what's next), number of weekly standups | Application, standups, blockers and help requests, **payments, amounts and addresses**, email |

If being public about Bitcoin work puts you at real risk where you live, tell us and your page stays private. It won't count against you.

---

## 8. How we work

- **Respect maintainers' time:** read the contributing guide, keep PRs small, write good descriptions, answer review comments.
- **Review before you ask for review.**
- **AI tools are fine; AI slop is not.** Understand and be able to explain every line you submit. Never open a PR you haven't tested and read yourself.
- **Learn in public:** share one thing a month (a thread, a Nostr note, a write-up or a session).
- **Pay it forward:** help one newer learner during your fellowship.
- **Be kind.** The [code of conduct](../CODE_OF_CONDUCT.md) applies everywhere.

---

## 9. What you get

- $512 a month in bitcoin for 6 months.
- A mentor from your project or a close one, matched before you start, with a weekly call.
- A fellow dashboard for standups, reports, milestones and payment history.
- A public proof-of-work page.
- A peer group of fellows, Code Review Club, the Privacy Track and the Code Orange community.
- Help with your next step: intros to maintainers and Bitcoin companies, references for good work, and help applying for long-term open-source support.

---

## 10. How to apply

1. Take the **readiness check** at [codeorange.dev/fellowships/apply](https://codeorange.dev/fellowships/apply).
2. Fill in the **application**: proof of work, project, and a 6-month plan with a goal per month.
3. **A human replies within 2 weeks.** Shortlisted applicants get a short Discord call.
4. **Offer and mentor match.** A fellowship only starts once its mentor is confirmed.
5. **Start on the 1st** with your fellow dashboard, milestones and first standup.

Questions: `#fellowships` on [Discord](https://discord.gg/ZtvA79paWa).

---

*[Code Orange Dev School](https://codeorange.dev) | CC0 1.0 Universal*
