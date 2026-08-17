# Developer Fellowship - Detailed Spec

> The short version is in the [track README](./README.md). This is the full rulebook: the six-month arc, what good looks like, and renewal.

**Six months of runway to become a real Bitcoin open-source contributor. You pick the project. We fund the learning curve.**

The hardest part of contributing to Bitcoin open-source is not the code. It is the first six months, when you are slow, your PRs get torn apart in review, and you have no idea whether any of it is going anywhere. Almost everyone who quits, quits there.

This fellowship exists to pay for exactly that period.

---

## The deal in one table

| | |
|---|---|
| **Stipend** | **$512/month** in Bitcoin |
| **Term** | 6 months, renewable |
| **Commitment** | ~15-20 hours/week |
| **You choose** | Which open-source project you contribute to |
| **Reporting** | Weekly standup + monthly report due the 5th |
| **Exit outcome** | Grant-ready: a public contribution record strong enough to apply to OpenSats, Brink, HRF or Spiral |

Paid in Bitcoin, monthly. You choose the rail - Lightning, on-chain, or eCash. See [payment and reporting](../shared/payment-and-reporting.md).

---

## How it works

### You pick a project

Not us. Fellows who are assigned a project drift; fellows who chose one stay. See the **[project menu](./project-menu.md)** for the codebases where Code Orange contributors are already active - meaning there is someone nearby who can unstick you.

You can also propose something not on the list. Make the case in your application.

### You get a mentor

Someone who has merged code in that project or one close to it - from our contributor community, or from the wider network we can reach through [Chaincode Labs](https://chaincode.com/), [Btrust](https://www.btrust.tech/) and the [Bitcoin Dev Project](https://bitcoindevs.xyz/). Expect one 45-minute call a fortnight, plus async help.

### You work in public

Every PR, every review, every question in the project's IRC or Discord. Your record lands in the [PR tracking dashboard](https://github.com/code-orange-dev/PR-tracking-dashboard) alongside the 110+ PRs our community has already opened.

### You write

One technical writeup per quarter - a walkthrough, a deep-dive on the subsystem you have been living in, a post-mortem of a PR that got rejected. Published publicly. This is not busywork: technical writing is how reviewers and grant committees decide whether you actually understand what you touched.

---

## The six-month arc

The months are a guide, not a contract. People arrive at different levels and move at different speeds.

### Month 1 - Orientation
- Development environment building and tests passing locally
- Read the project's contributing guide, review process and coding standards properly
- Lurk: read 20 merged PRs and 5 rejected ones. Learn what the maintainers care about.
- **Deliverable:** one scoping document - what the project does, its architecture, and three areas you might work in

### Month 2 - First contribution
- Open your first PR. Small. Docs, a test, a tidy-up, a good first issue.
- Expect it to take longer than you think and get more comments than feels fair
- **Deliverable:** 1+ PR opened

### Month 3 - Review muscle
- Start reviewing other people's PRs. This is the single most undervalued contribution in Bitcoin open-source and the fastest way to earn maintainer trust.
- Second PR, slightly more substantial
- **Deliverable:** 2+ PRs opened, 3+ reviews given, quarterly technical writeup published
- **Checkpoint:** month-3 review against the [rubric](../shared/evaluation-rubric.md)

### Month 4 - Depth
- Pick one subsystem and go deep enough to have opinions about it
- Engage on the mailing list, IRC or the project's dev channel
- **Deliverable:** 1+ substantive PR, 3+ reviews

### Month 5 - Sustained contribution
- Work that a maintainer asked for, or that you proposed and got buy-in on
- **Deliverable:** sustained PR and review activity

### Month 6 - Grant-ready
- Draft a funding application to [OpenSats](https://opensats.org/), [Brink](https://brink.dev/), [HRF](https://hrf.org/program/financial-freedom/bitcoin-development-fund/) or [Spiral](https://spiral.xyz/) - we review the draft with you before you send it
- **Deliverable:** second technical writeup, funding application submitted, exit review

---

## What "good" looks like at month 6

Not a fixed quota - different projects move at very different speeds, and one merged Bitcoin Core PR can represent more work than ten elsewhere. As a rough shape:

| Signal | Weak | Solid | Strong |
|---|---|---|---|
| PRs opened | 1-2 | 4-6 | 8+ |
| PRs merged | 0 | 2-3 | 5+ |
| Reviews given | 0-2 | 8-12 | 20+ |
| Technical writeups | 0 | 2 | 2 with real readership |
| Maintainer relationship | Unknown to them | They recognise your handle | They tag you on relevant issues |

**Reviews are weighted heavily on purpose.** Review capacity is the scarcest resource in Bitcoin open-source. A fellow with 3 merged PRs and 25 thoughtful reviews is more valuable to the ecosystem, and more fundable, than one with 8 merged PRs and no reviews.

---

## What we expect

**Weekly standup.** Written, in `#fellowships` on [Discord](https://discord.gg/xd6dmPF9bA), by Monday. Three lines: what you did, what is next, what is blocking you. Two minutes to write.

**Monthly report by the 5th.** Use the [template](./monthly-report-template.md). PR it to `fellowships/reports/<your-handle>/YYYY-MM.md`.

**Ask for help before you are stuck for a week.** The single biggest failure mode in this fellowship is silent struggling. Getting stuck is expected. Staying stuck quietly is the problem.

**Blocked weeks are fine, hidden ones are not.** A month where you got nothing merged because you were fighting a build system is a normal month in Bitcoin open-source. Report it honestly.

---

## What this is not

**Not a job.** No tickets, no manager, no deadlines from us. The project's maintainers set the pace and you answer to review, not to us.

**Not a guarantee of merged code.** Some PRs die. Bitcoin Core PRs can sit for a year. We assess your contribution behaviour, not merge counts alone.

**Not a course.** There is no syllabus. If you want structured teaching first, do a cohort - [Bitcoin Dojo](https://github.com/code-orange-dev/curriculum/tree/main/bitcoin-dojo), [rawBit](https://github.com/code-orange-dev/curriculum/tree/main/rawbit) or [Decoding Bitcoin](https://github.com/code-orange-dev/curriculum/tree/main/decoding-bitcoin) - and apply after.

---

## Who this is for

**Good fit:**
- Completed a Code Orange cohort, or equivalent self-study, and hit the "what now?" wall
- Can read code in the project's language without a tutorial open
- At least one merged PR somewhere, in any project, any language
- Can commit 15-20 hours a week for six months without your life falling apart

**Not yet:**
- Never opened a pull request → do a cohort first
- Looking for a full-time salary → this is part-time runway, not employment
- Want to build your own product → excellent, but that is a grant application, not this

---

## Renewal and exit

At month 6, against the [rubric](../shared/evaluation-rubric.md):

- **Renew** - six more months, usually with a larger scope
- **Graduate to direct funding** - you have the record to get funded by [OpenSats](https://opensats.org/), [Brink](https://brink.dev/) or [HRF](https://hrf.org/program/financial-freedom/bitcoin-development-fund/) directly. We write the reference and help with the application. **This is the intended outcome.**
- **Move to Educator** - some people discover they would rather teach. That is a promotion, not a consolation prize.
- **Conclude** - it did not work. You keep your contribution record, which is yours regardless.

---

## Apply

Fill in the [application template](./application.md) and open a PR at `fellowships/applications/<your-github-handle>.md`.

Include a link to code you have written. It does not need to be Bitcoin-related or good. It needs to be yours.

We respond within 14 days.
