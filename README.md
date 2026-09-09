# The Curb Guy — Landing Page

Single-page Google Ads landing page for **The Curb Guy LLC** (Marcus Reimer), custom concrete
landscape curbing, Dardanelle AR + Central Arkansas / River Valley.

**Read this before editing.**

## Files
- `index.html` — the whole page (self-contained; all CSS/JS inline).
- `images/` — WebP (converted 2026-08-03 from the Facebook photos in `../assets/`; heroes 1600px q78, gallery 1200px, `logo.webp`). Below-fold images use `loading="lazy"`. Originals still in git history.
- CTA wording is **"Book Your Free Consultation"** (Marcus prefers "consultation" over "quote"; "Free" is required for ad message match — keep both words).

## The quote form (native, added 2026-09-08 — replaces the Jobber button)
The page now has its own form (`#quote`, top of the "What We Do" section, pill-style fields:
Full Name · Phone · City · "Tell Us About Your Project"). Every "Book … Consultation" button
scrolls to it. It posts to **Web3Forms** by AJAX, then redirects to `/thank-you`, which fires
the Google Ads form conversion (`AW-18345842541/2l4mCIGW39ccEO2u_atE` — the old "Booked
appointment on Landing Page" action, now repurposed; rename it "Quote form submit" in Ads).
- **ACCESS KEY IS A PLACEHOLDER (`WEB3FORMS_KEY_HERE`) until Kennedy drops in a real one.**
  Get it at web3forms.com with the email that should receive leads (marcus@mrcurber.com, or
  Kennedy's to forward). A placeholder renders fine and silently loses every lead — test one
  live submit in a real browser after the key is in (Web3Forms blocks curl/headless).
- Hidden `source` field tags each lead "Google Ads" / "Facebook" / "Direct / other" from the
  click params, plus the full URL, so Marcus's email says where the lead came from.
- Honeypot `botcheck` checkbox is hidden; leave it.
- The old Jobber request form still exists (`https://clienthub.getjobber.com/hubs/f4e088fd-10e7-4f54-9a27-cfb65f989ff5/public/requests/2758953/new`)
  but is no longer linked from the page.

## Contact info (keep consistent — Google call tracking expects the format)
- Call AND text: **(479) 237-9888** → `tel:+14792379888` / `sms:+14792379888`
  (unified 2026-07-24 — this is Marcus's Jobber dedicated number, so texts land in his
  Jobber inbox. Jobber numbers are text-first: voice calls only reach Marcus if a
  forwarding number is saved in Jobber → Settings → Company Settings. VERIFY with Marcus
  before launch. His direct line (479) 317-1554 is no longer shown on the page.)
- Email: marcus@mrcurber.com
- Address: 1606 North 3rd Street, Dardanelle, AR

## Meta Pixel — LIVE (1363691585178700, added 2026-08-03)
Base code in the `<head>` of all three pages (PageView). Events: `Lead` on quote-button
clicks, `Contact` on call/text taps (via the same handlers as the gtag events), `Schedule`
on thank-you load. Jobber's form can NOT carry the pixel (GA4 only) — Facebook never sees
real submits; real FB lead counts come from Jobber's log (offline upload later).

## Location eyebrow swap (added 2026-08-04)
`?loc=<google-geotarget-id>` swaps the hero eyebrow to "Serving <Town>, <State>".
Map covers 118 towns + all 23 target counties (built from Google's geotargets CSV x Census
place-by-county file). Google Ads campaign needs final URL suffix `loc={loc_physical_ms}` —
Google inserts the searcher's town code automatically. Unknown/missing id -> default eyebrow.
Facebook has no equivalent ValueTrack; FB traffic sees the default line.

## Conversion tracking — LIVE (Google Ads AW-18345842541)
Google tag is installed in `<head>` of `index.html` and `thank-you.html`. Three conversions:

| Conversion | How it fires | Where | Label |
|---|---|---|---|
| **Call** | "Calls from a website" — Google forwarding number swaps in for ad visitors on the call buttons, counts real calls past the min length | `index.html` phone snippet, scoped by CSS class `call-swap` | `KunVCMuj3tccEO2u_atE` |
| **Text** | tap on a Text button (`sms:`) fires `gtag('event','conversion')` | `index.html` JS, `.track-text` handler | `NXxWCKTy49ccEO2u_atE` |
| **Form submit** | thank-you page load after a real on-page form submit (`fireBooking()`) | `thank-you.html` | `2l4mCIGW39ccEO2u_atE` |

- **`call-swap` class is on CALL buttons ONLY** — never add it to an `sms:`/Text element, or texts would route to the call-tracking number. Call and Text share (479) 237-9888, so this scoping is what keeps them separate.
- Google Ads only *counts* these when the visitor came from a Google Ads click (GCLID). Total lead volume (all sources) lives in Jobber.
- The Booking conversion now fires from the native form's redirect to `/thank-you` (the Jobber redirect route is dead).
- `quote_button_click` (scroll-to-form), `call_click`, `text_click`, and `generate_lead` (real form submit) fire as GA4 events. NOTE 2026-09-08: the landing-page GA4 stream (G-25R6YKY6WY) has never received data — needs a fresh web stream (see google-ads/reports/2026-09-08-changes.md item 9).

## Content constraints (important — don't overclaim)
- **No "licensed & insured" claim** — not confirmed by the client. Do not add it.
- **No invented review count / star average number** — we say "5-star rated," which is true
  from his real reviews, but we do NOT state a specific number of reviews (unverified).
- The 6 testimonials are real, pulled from mrcurber.com. Names are as shown there.
- "13 years experience," owner-operated, family (wife + 5 kids), started in trades at 11 —
  all from his About page. True as of build.

## Still to get from Marcus (nice-to-have)
- Hi-res logo (current one is fine but slightly soft) & a real photo of Marcus for the About section
  (currently uses a work photo there).
- True before/after pairs (we have one) for a stronger slider.
- Business hours, Google review count, any license/insurance/guarantee he DOES have.

## Design
- Palette from logo: navy `#1e2a55`, brick red `#b23a2e`, cream `#f5efe3`, gold `#d8a13c`.
- Fonts: Bricolage Grotesque (display) + Instrument Sans (body), via Google Fonts.
- Mobile-first, sticky call/quote bar on phones, no nav menu (1:1 attention ratio for paid traffic).

## Deploy
Static site — deploys to Vercel via Kennedy's usual pipeline (customleadz-sites GitHub org,
set git user.email first). Domain target: mrcurber.com (currently live elsewhere — coordinate cutover).
