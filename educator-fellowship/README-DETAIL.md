# Educator Fellowship - Detailed Spec

> The short version is in the [track README](./README.md). This is the full rulebook: credits, caps, tiers and renewal.

**$256/month in Bitcoin to teach Bitcoin. 8 session credits per month. 6-month renewable term.**

You run study cohorts, workshops and meetups. We pay you for it, give you a curriculum you do not have to write from scratch, and back you as you build a local Bitcoin developer community that outlasts the fellowship.

---

## The deal in one table

| | |
|---|---|
| **Stipend** | **$256/month**, paid in Bitcoin |
| **Expected output** | **8 session credits per month**, averaged across the quarter |
| **Effective rate** | ~$32 per session credit |
| **Term** | 6 months, renewable indefinitely on performance |
| **Reporting** | One monthly report, due the 5th |
| **Time commitment** | Realistically 8-12 hours/week including prep |
| **Where** | Anywhere. In-person, online, or both |
| **Language** | Any. We actively want non-English cohorts |

---

## What counts as a session credit

Not every session is the same size, so we count credits rather than raw sessions. **Eight credits is the monthly target.**

| Session type | Minimum length | Minimum attendees | Credits |
|---|---|---|---|
| **Study cohort session** - one week of a structured multi-week track | 90 min | 3 | **1.0** |
| **Hands-on workshop** - participants leave with something deployed or built | 120 min | 5 | **1.5** |
| **Community meetup / reading club** - discussion-led, less structured | 60 min | 4 | **0.75** |
| **Train-the-trainer session** - you teaching another facilitator to run a session | 90 min | 2 | **1.5** |
| **1:1 mentoring** - scheduled, with an agenda | 45 min | 1 | **0.25** |
| **Conference or event talk** - technical content, public audience | 30 min | 20 | **1.0** |

**Caps and floors, so the number means something:**

- **1:1 mentoring is capped at 2.0 credits/month.** It is valuable but it does not build community, and it is the easiest category to inflate.
- **At least 3.0 credits/month must come from structured cohort sessions.** A fellowship that is only casual meetups does not move anyone toward contribution.
- **Credits are averaged over the quarter, not enforced monthly.** Target 24 credits per quarter. A 5-credit month followed by an 11-credit month is completely fine. Travel, illness and Ramadan exist.

### Why credits instead of "8 meetups"

Because "8 meetups" is trivially gameable and quietly punishes the good version of the job. Under a raw count, an hour-long coffee chat with three people scores the same as a four-hour BitAxe workshop that sends five people home with working miners. Credits make the second one worth more, which is the behaviour we actually want.

---

## The outcome target

Activity is necessary but not sufficient. **Each quarter, at least two participants from your sessions must reach one of these milestones:**

- Opened their first pull request to any Bitcoin open-source project
- Completed a full multi-week cohort track
- Deployed and kept running a full node, BTCPay server, or similar infrastructure
- Started facilitating sessions themselves
- Applied to a fellowship, grant, or program (Code Orange's, [Btrust](https://www.btrust.tech/), [Summer of Bitcoin](https://www.summerofbitcoin.org/), [OpenSats](https://opensats.org/), or anywhere else)

Two per quarter is a deliberately achievable bar. It exists to keep the fellowship pointed at the pipeline rather than at attendance figures. If you are running eight credits a month and *nobody* is progressing in three months, something is wrong with the format and we should fix it together - that is a conversation, not a penalty.

---

## What you get beyond the money

**A curriculum you do not have to write.** Everything in the [curriculum repo](https://github.com/code-orange-dev/curriculum) is CC0 and yours to run, fork, translate or butcher:

| Track | Length | What it does |
|---|---|---|
| [Bitcoin Dojo](https://github.com/code-orange-dev/curriculum/tree/main/bitcoin-dojo) | 7 weeks | Cryptographic primitives from scratch, via Programming Bitcoin |
| [rawBit](https://github.com/code-orange-dev/curriculum/tree/main/rawbit) | 10 weeks | Raw transaction construction with a visual builder |
| [Decoding Bitcoin](https://github.com/code-orange-dev/curriculum/tree/main/decoding-bitcoin) | 8 weeks | Transactions, Script, Taproot, PSBTs, Core contribution workflow |
| [Sovereign Bitcoiner](https://github.com/code-orange-dev/curriculum/tree/main/sovereign-bitcoiner) | 5-10 weeks | Nodes, mining, multisig, inheritance, BTCPay, privacy tools |
| [Privacy Track](https://github.com/code-orange-dev/curriculum/tree/main/privacy-track) | 24 sessions, drop-in | Chain analysis defence, Silent Payments, Payjoin, contribution-first |
| [Nostr Workshops](https://github.com/code-orange-dev/curriculum/tree/main/nostr-workshops) | Monthly | Nostr, Lightning integrations, FOSS tooling |

**The [facilitation playbook](./facilitation-playbook.md).** How to run a session that works when you are not the smartest person in the room - and what to do when you are asked something you cannot answer.

**Monthly train-the-trainer calls.** All Educator Fellows, one hour, once a month. Curriculum updates, what is landing and what is not, and a place to complain about things that are broken.

**Guest speakers.** We have brought in people from Fedi, Nunchuk, rawBit and the Bitcoin privacy community. Ask and we will try to get someone into your cohort.

**A reference that means something.** After six months you have a public, verifiable record: sessions run, people taught, outcomes produced. That record is what we point at when recommending you to [Btrust](https://www.btrust.tech/), [OpenSats](https://opensats.org/), [HRF](https://hrf.org/program/financial-freedom/bitcoin-development-fund/) or a Bitcoin company hiring educators.

---

## What we expect

**Every session logged.** Use the [session log template](./session-log-template.md). Log it within 48 hours while you still remember what happened - retroactive logging at month end is where accuracy goes to die.

**One monthly report, due the 5th.** Use the [monthly report template](./monthly-report-template.md). It is short by design. Submit as a PR to `fellowships/reports/<your-handle>/YYYY-MM.md`.

**Materials pushed upstream.** If you build a slide deck, a worksheet, a translation or a new exercise, it goes into the [curriculum repo](https://github.com/code-orange-dev/curriculum) under CC0. If you improve an existing session, PR the improvement rather than keeping a private fork.

**Show up to the monthly train-the-trainer call.** Missing one is fine. Missing three in a row means we should talk about whether this is working.

**Tell us early when a month is going to be short.** Nobody gets penalised for a bad month that was flagged in advance. See [payment and reporting](../shared/payment-and-reporting.md).

---

## Tiers

Most fellows start and stay at Fellow. The tiers exist so there is somewhere to go.

| Tier | Credits/month | Stipend | Additional expectation |
|---|---|---|---|
| **Apprentice Educator** | 4 | *(to be set)* | Co-facilitates alongside an existing fellow. For people who can teach but have not yet. |
| **Educator Fellow** | 8 | **$256/month** | The standard track. Everything on this page. |
| **Lead Educator** | 8 | *(to be set)* | Owns a curriculum track, mentors 2 apprentices, runs the train-the-trainer call |

> Apprentice and Lead rates are not yet fixed. If either tier is right for you, apply anyway and we will agree a number before you start.

---

## Renewal and exit

At month 6 we review against the [evaluation rubric](../shared/evaluation-rubric.md) and one of four things happens:

- **Renew** - another 6 months, same or higher tier
- **Promote** - move to Lead Educator, take ownership of a track
- **Graduate** - you are running something self-sustaining and no longer need us. We help you apply for direct funding from [OpenSats](https://opensats.org/), [HRF](https://hrf.org/program/financial-freedom/bitcoin-development-fund/) or [Btrust](https://www.btrust.tech/) so your hub stands on its own.
- **Conclude** - it is not working. We say so directly, you keep everything you built, and there is no bad blood.

The third outcome is the one we are actually optimising for. The goal is 10 Bitcoin Houses across Southeast Asia, and that does not happen if every hub is on Code Orange's payroll forever.

---

## Apply

Read the [application template](./application.md), fill it in, and open a PR at `fellowships/applications/<your-github-handle>.md`. Or send it in `#fellowships` on [Discord](https://discord.gg/xd6dmPF9bA) if you would rather not apply in public.

We respond within 14 days.

---

*Questions that are not answered here belong in the [FAQ](../shared/faq.md) - open an issue and we will add them.*
