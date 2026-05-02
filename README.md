# Code Orange Fellowship

> Ship code. Grow builders. Make Bitcoin more private — from Southeast Asia.

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-orange.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

---

## The Short Version

Code Orange runs workshops, cohorts, and meetups that turn curious Bitcoiners into technical contributors. The fellowship is what happens next: you pick a project, we give you a stipend and a mentor, and you ship real open-source code for 6 months.

We have two tracks because Bitcoin needs both builders and teachers:

| | Developer Track | Educator Track |
|---|---|---|
| **You are** | A dev who wants to contribute to Bitcoin FOSS full-time or part-time | Someone who wants to teach Bitcoin development in your community |
| **You do** | Write code, open PRs, review code, work with a mentor | Run cohorts, host workshops, create materials, grow the local scene |
| **You get** | $500/month + mentorship + Bali hub access | $250/month + curriculum + event support + Bali hub access |
| **Duration** | 6 months (extendable) | 6 months (extendable) |
| **Details** | [Developer Track →](developer-fellowship/) | [Educator Track →](education-fellowship/) |

---

## Why We Built This

Southeast Asia has 700 million people, growing Bitcoin adoption, and almost zero Bitcoin open-source developers. India has Bitshala. Africa has Btrust. Latin America has Libreria de Satoshi. This region has been invisible.

Code Orange has spent 15 months proving the demand exists. We've run 60+ workshops across Bali and Chiang Mai, graduated 33+ developers through technical cohorts, and shepherded 15 PRs into Bitcoin FOSS projects. People here want to build. They just need a path.

The fellowship is that path:

```
 Workshops & Meetups        Cohorts              Fellowship             Independent
 ──────────────────    ──────────────────    ──────────────────    ──────────────────
 Sovereign Bitcoiner   Bitcoin Dojo (7wk)    6 months focused      OpenSats grant
 Self-Custody          Decoding BTC (8wk)    contribution with     HRF grant
 Mining                Privacy Track (12s)   mentor + stipend      Spiral grant
 Privacy               rawBit (10wk)                               Full-time FOSS
 Meetups & Talks                                                   career

 "I'm interested"     "I understand it"     "I'm contributing"    "I'm independent"
```

The fellowship bridges the gap between "I finished a cohort" and "I have a track record that gets me a grant."

---

## What Makes This Different

**We're not an online-only program.** Fellows can work from our Bali hub — a physical space where Bitcoin developers show up, build together, and learn from each other in person. Remote participation works too, but the IRL component is what accelerates learning.

**We're privacy-focused.** Our curriculum emphasizes Silent Payments, Payjoin, compact block filters, and wallet privacy. This aligns with where the protocol is headed and where the funding is going (OpenSats explicitly prioritizes base-layer privacy work).

**We grow our own.** Most fellowship applicants come through our cohorts. By the time someone applies, they've already spent 7-12 weeks building technical Bitcoin skills with us. We know their work. They know our culture. The fellowship isn't a cold start — it's the next step.

**Education is not an afterthought.** We fund educators with the same seriousness as developers. The developer pipeline only works if someone is running the workshops and cohorts at the front of it. Educators make everything else possible.

---

## Projects We Contribute To

Fellows choose a project based on their skills and interests. Our sweet spot is privacy and wallet infrastructure, but we support any Bitcoin FOSS work.

| Project | Language | Area |
|---------|----------|------|
| [rust-silentpayments](https://github.com/cygnet3/rust-silentpayments) | Rust | Silent Payments (BIP352) |
| [payjoin-rust](https://github.com/payjoin/rust-payjoin) | Rust | Payjoin Dev Kit (BIP77) |
| [BDK](https://github.com/bitcoindevkit/bdk) | Rust | Wallet development |
| [Kyoto](https://github.com/rustaceanrob/kyoto) | Rust | Compact block filters (BIP157/158) |
| [Coinswap](https://github.com/citadel-tech/coinswap) | Rust | CoinSwap protocol |
| [Floresta](https://github.com/Davidson-Souza/Floresta) | Rust | Utreexo full node |
| [Bitcoin Core](https://github.com/bitcoin/bitcoin) | C++ | Protocol, wallet, P2P |
| [BTCPay Server](https://github.com/btcpayserver/btcpayserver) | C# | Merchant payments |
| [Fedimint](https://github.com/fedimint/fedimint) | Rust | Federated eCash |
| [LDK](https://github.com/lightningdevkit/rust-lightning) | Rust | Lightning |

Working on something else? Propose it. If it's Bitcoin FOSS, we'll consider it.

---

## How It Works

### 1. Apply

No forms. Send us your proposal — what you want to work on and why. Templates are in [`templates/`](templates/).

**Developer Track:** Start contributing to your chosen project first (even a small PR), then send your 6-month work plan with a maintainer endorsement.

**Educator Track:** Tell us what you want to teach, where, and to whom. Show us you understand the material well enough to teach it.

Email: **fellowship@codeorange.dev**

### 2. Get Accepted

We review applications on a rolling basis. We look at your prior work, your proposal quality, and whether you're a good fit for the community. Expect a response within 2 weeks.

### 3. Onboard (Month 1)

Meet your mentor. Finalize your work plan. Set up your dev environment. Get your first PR in. Join the cohort sync.

### 4. Build (Months 2-5)

Ship code or run events every week. Meet with your mentor weekly. Submit a monthly work report. Participate in bi-weekly cohort syncs with the other fellows. Show up at Code Orange sessions when you can.

### 5. Graduate (Month 6)

Present your work to the community. Document everything. Apply for grants to keep going. Join the alumni network. Help select the next cohort.

---

## The Numbers

### For Fellows

| | Developer | Educator |
|---|---|---|
| Monthly stipend | $500 USD | $250 USD |
| Payment method | BTC or fiat (your choice) | BTC or fiat (your choice) |
| Duration | 6 months | 6 months |
| Time commitment | 15-20 hrs/wk (part-time) or 35+ (full-time) | 10-15 hrs/wk |
| Extension | Possible based on performance | Possible based on performance |

### For Funders

| Metric | Per Developer Fellow (6mo) | Per Educator Fellow (6mo) |
|--------|---------------------------|--------------------------|
| Total cost | $3,000 | $1,500 |
| Expected PRs merged | 6+ | — |
| Expected events hosted | — | 24+ |
| Expected participants reached | — | 30+ |
| Cost per merged PR | ~$500 | — |

Compare: a single full-time Bitcoin Core developer costs $150K-250K/year. We produce emerging contributors at a fraction of that, from a region with none.

---

## Cohort Schedule

Two cohorts per year:

| Cohort | Applications Open | Starts | Ends |
|--------|-------------------|--------|------|
| H1 | November 1 | January 15 | July 15 |
| H2 | May 1 | July 15 | January 15 |

---

## What a Fellowship Actually Looks Like

Vague proposals don't get accepted. Here's what real fellowship work plans look like:

### Example Developer Fellow: Silent Payments Focus

**Project:** rust-silentpayments + Bitcoin Core SP support
**6-month targets:**
- Month 1: Add 15+ test cases covering BIP352 edge cases (mixed input types, label collision, multiple recipients)
- Month 2: Implement label management module in rust-silentpayments
- Month 3: Optimize scanning performance — benchmark and improve tweak cache
- Month 4-5: Submit 2+ PRs to Bitcoin Core #28122 (testing, review, or code)
- Month 6: Write integration guide for wallet developers adopting Silent Payments
- **Total expected: 8+ PRs merged, 1 published guide**

### Example Developer Fellow: Payjoin Focus

**Project:** rust-payjoin / Payjoin Dev Kit
**6-month targets:**
- Month 1: Add BIP77 (async Payjoin) integration tests for relay failure scenarios
- Month 2-3: Implement Payjoin sender support in a wallet that doesn't have it (BDK-based)
- Month 4: Submit 2+ PRs to rust-payjoin improving error handling and documentation
- Month 5: Write "Adding Payjoin to Your Wallet" tutorial for PDK
- Month 6: Help onboard the next Privacy Track cohort to Payjoin concepts
- **Total expected: 6+ PRs merged, 1 wallet integration, 1 published tutorial**

### Example Developer Fellow: Light Client Privacy

**Project:** Floresta / Kyoto
**6-month targets:**
- Month 1: Fix 3+ open issues in Floresta labeled "good first issue"
- Month 2-3: Implement compact block filter caching optimization in Kyoto
- Month 4: Add Silent Payments scanning support to Kyoto using CBF
- Month 5-6: Benchmark privacy properties of Floresta vs Kyoto vs full node, publish results
- **Total expected: 8+ PRs merged, 1 published benchmark**

### Example Educator Fellow: Privacy Track Facilitator — Chiang Mai

**Initiative:** Run the 24-session Privacy Track in Chiang Mai, Thailand
**6-month targets:**
- Month 1: Recruit 15+ participants. Host sessions 1-2 (Foundations)
- Month 2: Host sessions 3-4. Ensure every participant has filed their first GitHub issue
- Month 3: Host sessions 5-6 (Silent Payments). Track participant PRs
- Month 4: Host sessions 7-8. Mid-term review — at least 5 participants have submitted PRs
- Month 5: Host sessions 9-10 (Payjoin). Begin training successor facilitator
- Month 6: Host sessions 11-12. Hand off to trained successor. Present cohort results
- **Total expected: 12 sessions hosted, 15+ participants, 20+ PRs from participants, 1 trained successor**

---

## Expected Output Per Fellow

| Fellow Type | Duration | PRs Merged | Cost | Cost per PR |
|-------------|----------|-----------|------|-------------|
| Developer (full-time) | 6 months | 8+ | $3,000 | ~$375 |
| Developer (part-time) | 6 months | 6+ | $3,000 | ~$500 |
| Educator | 6 months | 20+ (from participants) | $1,500 | ~$75 |

Compare: a single full-time Bitcoin Core developer costs $150K-250K/year. We produce emerging contributors at a fraction of that, from a region with none.

---

## Alumni

*(First cohort launching H2 2026. This section will be filled with real people and real PRs.)*

---

## License

Everything here is [CC0](LICENSE). Take it. Adapt it. Build your own fellowship in your own community.

---

*[Code Orange Dev School](https://codeorange.dev) | Bali, Indonesia | [github.com/code-orange-dev](https://github.com/code-orange-dev)*
