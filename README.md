# The Curb Guy — Landing Page

Single-page Google Ads landing page for **The Curb Guy LLC** (Marcus Reimer), custom concrete
landscape curbing, Dardanelle AR + Central Arkansas / River Valley.

**Read this before editing.**

## Files
- `index.html` — the whole page (self-contained; all CSS/JS inline).
- `images/` — optimized JPEGs (from Facebook photos in `../assets/`) + `logo.png`.

## The quote button (external — do NOT build a form)
Every CTA opens Marcus's **Jobber** request form in a new tab:
`https://clienthub.getjobber.com/hubs/f4e088fd-10e7-4f54-9a27-cfb65f989ff5/public/requests/2758953/new`
Jobber blocks embedding (iframe), so a button-to-new-tab is the correct approach.
If the Jobber link ever changes, find/replace it everywhere in `index.html`.

## Contact info (keep consistent — Google call tracking expects the format)
- Call AND text: **(479) 237-9888** → `tel:+14792379888` / `sms:+14792379888`
  (unified 2026-07-24 — this is Marcus's Jobber dedicated number, so texts land in his
  Jobber inbox. Jobber numbers are text-first: voice calls only reach Marcus if a
  forwarding number is saved in Jobber → Settings → Company Settings. VERIFY with Marcus
  before launch. His direct line (479) 317-1554 is no longer shown on the page.)
- Email: marcus@mrcurber.com
- Address: 1606 North 3rd Street, Dardanelle, AR

## Conversion tracking — LIVE (Google Ads AW-18345842541)
Google tag is installed in `<head>` of `index.html` and `thank-you.html`. Three conversions:

| Conversion | How it fires | Where | Label |
|---|---|---|---|
| **Call** | "Calls from a website" — Google forwarding number swaps in for ad visitors on the call buttons, counts real calls past the min length | `index.html` phone snippet, scoped by CSS class `call-swap` | `KunVCMuj3tccEO2u_atE` |
| **Text** | tap on a Text button (`sms:`) fires `gtag('event','conversion')` | `index.html` JS, `.track-text` handler | `NXxWCKTy49ccEO2u_atE` |
| **Booking** | thank-you page load after a real Jobber submit (`fireBooking()`) | `thank-you.html` | `2l4mCIGW39ccEO2u_atE` |

- **`call-swap` class is on CALL buttons ONLY** — never add it to an `sms:`/Text element, or texts would route to the call-tracking number. Call and Text share (479) 237-9888, so this scoping is what keeps them separate.
- Google Ads only *counts* these when the visitor came from a Google Ads click (GCLID). Total lead volume (all sources) lives in Jobber.
- **Requires in Jobber:** the request form's confirmation must **redirect to `https://the-curb-guy.vercel.app/thank-you`** — that's what drives visitors to the booking-conversion page. If that redirect isn't set, the Booking conversion never fires.
- `request_quote_click` / `call_click` / `messenger_click` still fire as plain (non-conversion) dataLayer events — harmless signals, not Ads conversions.

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
