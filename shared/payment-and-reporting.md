# Payment and Reporting

How stipends are calculated and paid, and what happens when a month falls short.

> Two items below are marked ⚠️ and are not yet settled: the Apprentice and Lead Educator rates, and the BTC conversion reference. Everything else is final.

---

## Stipends

| Track | Monthly | Basis |
|---|---|---|
| **Educator Fellow** | **$256** | 8 session credits/month, averaged quarterly |
| Apprentice Educator | ⚠️ *to be set* | 4 credits/month |
| Lead Educator | ⚠️ *to be set* | 8 credits + track ownership + mentoring |
| **Developer Fellow** | **$512** | ~15-20 hours/week |

Amounts are denominated in **USD and paid in Bitcoin**. The USD figure is the fixed obligation; the sat amount varies with the rate.

---

## How payment works

**Schedule:** paid by the **10th** of the following month, after the report lands on the 5th.

**Conversion:** ⚠️ *Needs your decision.* Standard practice is spot rate at the moment of payment, using a named reference. Recommended wording once decided:

> Converted at the spot BTC/USD rate at time of payment, per `<reference source>`.

Pick one reference and never change it mid-term. Ambiguity here is how goodwill gets destroyed.

**Rails: your choice.** Pick whichever suits you, and change it whenever you like - just tell us before the 5th so it applies to that month's payment.

| Rail | Good for | Worth knowing |
|---|---|---|
| **Lightning** | Fast, cheap, no waiting | Needs enough inbound liquidity to receive $256-512 in one payment. Check before your first invoice. |
| **On-chain** | Reliable at any size, nothing to configure | Mining fee, and you wait for confirmations |
| **eCash (Fedimint / Cashu)** | Practical regionally - Bitcoin Indonesia's federation is [10,000-20,000 members](https://www.fedi.xyz/blog/community-spotlight-bitcoin-indonesia) | You are trusting the federation's guardians. Sweep to self-custody if you are holding. |

No rail is treated as more legitimate than another. If you are unsure, on-chain is the boring reliable default and nobody will think less of you for it.

**Fellows provide the address.** Confirm it in each monthly report. Address changes must be confirmed over a second channel before payment - a compromised Discord account should never redirect a stipend.

**No invoicing.** The monthly report is the invoice.

**Fellows are responsible for their own tax.** Code Orange is not an employer and this is not employment. If your jurisdiction taxes this, that is between you and it.

---

## Reporting deadlines

| What | When | Where |
|---|---|---|
| Session logs (Educator) | Within 48h of each session | `fellowships/logs/<handle>/YYYY-MM.md` |
| Weekly standup (Developer) | Every Monday | `#fellowships` on Discord |
| Monthly report | **5th** of following month | PR to `fellowships/reports/<handle>/YYYY-MM.md` |
| Month-3 checkpoint | End of month 3 | 45-min call |
| Month-6 review | End of month 6 | 1-hour call |

**Late reports:** the 5th is a real deadline because payment depends on it, but life happens. Tell us before the 5th and it is a non-event. Silence past the 10th delays payment, simply because we have nothing to pay against.

---

## When a month falls short

The honest version, because vagueness here is worse than strictness.

### Educator credits

Credits average **quarterly** - 24 per quarter, not 8 every month. This is deliberate: travel, illness, Ramadan, exam season and family emergencies are normal.

| Situation | Outcome |
|---|---|
| Short month, flagged in advance, quarter still on track | **Full stipend.** No conversation needed. |
| Short month, not flagged, quarter still on track | **Full stipend**, plus a note to flag earlier next time |
| Quarter ends below 24 credits, cause known and discussed | **Full stipend**, and we fix the underlying problem together |
| Quarter ends below 24, no communication throughout | Conversation about whether the fellowship is working. Payment for work delivered is not withheld. |
| Sustained under-delivery with no engagement across two quarters | Conclusion conversation |

**We do not pro-rata a short month.** Docking pay for a 6-credit month punishes honesty and teaches fellows to pad their logs, which destroys the only thing that makes the public record worth anything.

### Developer output

Not measured in units, because open-source does not work that way. A month spent fighting a build system, or waiting on a review that never came, is a normal month.

What we need is **communication**. Standups posted, report submitted, honest about the state of things. A fellow who reports "I got nothing merged, here is what I was stuck on and what I am trying next" is in good standing.

A fellow who goes quiet for three weeks is not - not because of the output, but because we cannot help someone who is invisible.

---

## Pausing

Life happens. Fellowships can pause for up to **2 months** and resume where they left off.

- Tell us before the pause where possible
- No payment during a pause
- Term extends by the pause length - a 6-month fellowship paused for 1 month runs 7 months
- No penalty, no explanation required

Pausing is always better than quietly disappearing. Every fellow who has vanished mid-term would have been welcome back if they had said "I need two months."

---

## Ending early

**Fellow-initiated:** tell us, we pay for the month worked, no hard feelings. You keep everything you built. A reference is still available if the work was good.

**Code Orange-initiated:** only after the escalation sequence in the [rubric](./evaluation-rubric.md) - concern named, conversation had, adjustment tried. Final month paid in full regardless.

**Immediate termination:** only for a Code of Conduct breach. Handled separately.

---

## Public record

All reports and logs are **public in this repo**. Applying means accepting that.

**Why:** it is the credential. When we recommend you to OpenSats, Brink, HRF or a company hiring, we point at a verifiable public record rather than making claims. That record is worth more than the stipend.

**Adjustments available on request:**

- Attendee names can be handles, initials or omitted - counts are what matter
- No photograph of any person without their explicit consent, every time
- If your location or Bitcoin involvement creates real personal risk, tell us. We will find a private arrangement. This is a legitimate concern in several jurisdictions our community spans and asking for it counts against you in no way whatsoever.

---

## Questions

`#fellowships` on [Discord](https://discord.gg/xd6dmPF9bA), or open an issue.

**If anything about money is ever unclear, ask immediately.** Unclear payment terms are the fastest way to poison an otherwise good program, and we would much rather over-explain.
