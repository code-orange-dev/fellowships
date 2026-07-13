# Contributing to Code Orange Dev School

Thanks for your interest in contributing! Code Orange is a Bitcoin-only, open-source developer education program. Everything we publish is **CC0 (public domain)** - free to use, fork, translate, and teach.

There are two ways to contribute, depending on whether you're improving **our materials** or contributing to **upstream Bitcoin projects** through our program.

---

## 1. Improving Code Orange materials (this and our other repos)

Curriculum fixes, typo corrections, translations, new exercises, better explanations, and slide improvements are all welcome.

1. **Fork** the repo and create a branch: `git checkout -b fix/short-description`
2. **Make your change.** Keep it focused - one logical change per pull request.
3. **Open a pull request** with a clear title and a sentence on what changed and why.
4. A maintainer will review. Expect friendly feedback and possibly a request for changes - that's a normal part of contributing.

Good first contributions: fixing a typo, clarifying a confusing instruction, translating a lesson, adding a missing link, or improving a diagram.

---

## 2. Contributing to upstream Bitcoin projects through our program

This is the heart of what we do - guiding developers to real, merged contributions to projects like Bitcoin Core, rust-bitcoin, BDK, rust-payjoin, Floresta, Kyoto, LDK, and Silent Payments tooling.

**The path:**

1. **Join our [Discord](https://discord.gg/xd6dmPF9bA)** and introduce yourself in the dev channels.
2. **Pick a study cohort** that fits your level:
   - [Bitcoin Dojo](https://github.com/code-orange-dev/curriculum/tree/main/bitcoin-dojo) - cryptographic primitives from scratch
   - [rawBit](https://github.com/code-orange-dev/curriculum/tree/main/rawbit) - build raw transactions
   - [Decoding Bitcoin](https://github.com/code-orange-dev/curriculum/tree/main/decoding-bitcoin) - Core contribution workflows
   - [Privacy Track](https://github.com/code-orange-dev/curriculum/tree/main/privacy-track) - base-layer privacy, contribution-first
3. **Pick a good-first-issue** from a real project and open a PR.
4. **Log it** so it shows up on our [PR Tracking Dashboard](https://github.com/code-orange-dev/PR-tracking-dashboard).

### Quality bar before you submit upstream

Maintainers are mostly unpaid and time-starved. A prepared PR gets merged; a sloppy one gets ignored and reflects on the whole program. Before you open an upstream PR:

- [ ] It builds locally (`cargo build` / project equivalent)
- [ ] Tests pass (`cargo test`)
- [ ] Formatter and linter are clean (`cargo fmt`, `cargo clippy`)
- [ ] The PR does one thing and links the issue it closes
- [ ] You followed that project's own `CONTRIBUTING.md`
- [ ] You can explain every line if a reviewer asks

> The one-line standard: **"Would a tired, unpaid maintainer be glad to receive this PR?"** If yes, ship it.

---

## Becoming a tutor

Once you've contributed, you can join our **train-the-trainer** program, run workshops or cohorts, and get paid in sats to teach others. Ask in Discord.

## Code of conduct

By participating you agree to our [Code of Conduct](./CODE_OF_CONDUCT.md). Be kind, be curious, help newcomers.

## Questions?

Open an issue, ask in [Discord](https://discord.gg/xd6dmPF9bA), or reach us at keypleb@blink.sv.
