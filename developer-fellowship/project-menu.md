# Project Menu - Developer Fellowship

Codebases where Code Orange contributors are **already active**. That matters more than it sounds: it means when you get stuck, someone in Discord has been stuck on the same thing.

You are not limited to this list. If you want to work on something else, make the case in your application - the only real requirement is that the project is open source, Bitcoin-related, and actually accepts outside contributions.

**Difficulty** is about how hard it is to land your first PR, not how hard the code is.

---

## 🦀 Rust - best entry point for most fellows

The Rust Bitcoin ecosystem has the friendliest review culture in Bitcoin open-source, good first issues that are genuinely first issues, and maintainers who respond in days rather than months. If you are unsure, start here.

| Project | What it is | Difficulty | Good if you like |
|---|---|---|---|
| **[rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin)** | The foundational Bitcoin library in Rust | 🟢 Approachable | Types, correctness, API design |
| **[rust-silentpayments](https://github.com/cygnet3/rust-silentpayments)** | Silent Payments (BIP352) library | 🟡 Moderate | ECDH, scanning performance, the privacy sweet spot |
| **[rust-payjoin](https://github.com/payjoin/rust-payjoin)** | Payjoin (BIP77/78) implementation | 🟡 Moderate | Privacy protocols, real-world wallet integration |
| **[Coinswap](https://github.com/citadel-tech/coinswap)** | CoinSwap protocol implementation | 🔴 Hard | Atomic swaps, protocol design, maker/taker markets |
| **[BDK](https://github.com/bitcoindevkit/bdk)** | Bitcoin Dev Kit - wallet library | 🟡 Moderate | Wallets, descriptors, coin selection |
| **[LDK](https://github.com/lightningdevkit/rust-lightning)** | Lightning Dev Kit | 🔴 Hard | Lightning internals, state machines |
| **[ldk-node](https://github.com/lightningdevkit/ldk-node)** | Batteries-included Lightning node | 🟡 Moderate | Making hard things usable |
| **[rust-miniscript](https://github.com/rust-bitcoin/rust-miniscript)** | Miniscript implementation | 🔴 Hard | Script analysis, formal reasoning |
| **[hex-conservative](https://github.com/rust-bitcoin/hex-conservative)** | Hex encoding, small and focused | 🟢 Approachable | A genuinely small first PR |
| **[Floresta](https://github.com/vinteumorg/Floresta)** | Utreexo-based full node | 🟡 Moderate | Novel node architecture, [Vinteum](https://vinteum.org/) |
| **[Kyoto](https://github.com/rustaceanrob/kyoto)** | Compact block filter light client (BIP157/158) | 🟡 Moderate | Light client privacy |

---

## ⚙️ C++ - Bitcoin Core and around it

Highest prestige, slowest feedback loop. A Core PR can sit for months. Real, but a hard place to build early momentum - most fellows do better landing a few Rust PRs first and coming to Core in month 3 or 4.

| Project | What it is | Difficulty | Good if you like |
|---|---|---|---|
| **[Bitcoin Core](https://github.com/bitcoin/bitcoin)** | The reference implementation | 🔴 Hard | The deep end. Review, test, consensus |
| **[kernel-node](https://github.com/TheCharlatan/kernel-node)** | Node built on the libbitcoinkernel library | 🟡 Moderate | Core internals, smaller surface |
| **[peer-observer](https://github.com/0xB10C/peer-observer)** | P2P network monitoring | 🟡 Moderate | Networking, observability |

**Realistic on-ramp to Core:** review other people's PRs first. Testing and reviewing an open PR is a genuine contribution, gets you known by maintainers, and teaches you the codebase faster than reading it. Several of our contributors got their first Core interaction this way.

---

## ⚡ Lightning and eCash

| Project | What it is | Difficulty | Good if you like |
|---|---|---|---|
| **[Core Lightning](https://github.com/ElementsProject/lightning)** | C implementation of Lightning | 🔴 Hard | Plugins are a soft entry - write one |
| **[Fedimint](https://github.com/fedimint/fedimint)** | Federated eCash | 🟡 Moderate | Federations, community custody |
| **[Cashu](https://github.com/cashubtc)** | Chaumian eCash protocol | 🟢 Approachable | Blind signatures, small codebases |
| **[BTCPay Server](https://github.com/btcpayserver/btcpayserver)** | Self-hosted payment processor | 🟢 Approachable | C#, merchant tooling, product work |

Fedimint and Cashu matter regionally: Bitcoin Indonesia's Fedimint federation is [estimated at 10,000-20,000 members](https://www.fedi.xyz/blog/community-spotlight-bitcoin-indonesia). Work here has users nearby.

---

## 🛠️ Tooling and education infrastructure

Lower barrier, immediately useful, and genuinely counts. Do not let anyone tell you tooling is a lesser contribution.

| Project | What it is | Difficulty | Good if you like |
|---|---|---|---|
| **[rawBit](https://github.com/rawBit-io/rawbit)** | Visual transaction builder and Script debugger | 🟢 Approachable | Frontend, teaching tools. Partner project |
| **[OpenTollGate](https://github.com/OpenTollGate)** | Bitcoin-paid internet access | 🟡 Moderate | Networking, Lightning payments, hardware |
| **[Code Orange curriculum](https://github.com/code-orange-dev/curriculum)** | Our own CC0 curriculum | 🟢 Approachable | Teaching, writing, translation |
| **[Bitcoin Dev Project](https://github.com/bitcoin-dev-project)** | Educational tooling and resources | 🟢 Approachable | Developer experience |

---

## Choosing well

**Pick the project whose *problem* you find interesting, not the one with the best reputation.** Six months is long enough that prestige stops carrying you and curiosity has to take over.

**Match the language you actually know.** The fellowship is for learning Bitcoin, not for learning your first systems language. If you know Rust, start in Rust.

**Check the pulse before you commit.** Open the repo and look at: how long recent PRs took to get a first review, whether good-first-issues are actually unclaimed, and whether maintainers reply kindly. A responsive small project beats a prestigious silent one for a first fellowship.

**Ask in Discord first.** Someone has probably already tried the project you are considering and can tell you what the first PR was like.

---

## A note on Bitcoin Core specifically

Contributing to Bitcoin Core is a legitimate ambition and one of our contributors has an [open PR there](https://github.com/bitcoin/bitcoin/pull/34885). It is also the single most common place fellowships stall, because the feedback loop is measured in months and the review bar is unforgiving.

If Core is your goal, the path that actually works:

1. Land 2-3 PRs in rust-bitcoin or BDK first - learn Bitcoin's semantics with fast feedback
2. Start reviewing and testing Core PRs - contribution without waiting on your own PR
3. Fix something small and real that you found yourself
4. Then attempt something substantive

Going straight to step 4 in month 1 is how people burn six months and leave with nothing merged.
