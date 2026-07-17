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
- Call: **(479) 317-1554** → `tel:+14793171554`
- Text: **(479) 237-9888** → `sms:+14792379888`
- Email: marcus@mrcurber.com
- Address: 1606 North 3rd Street, Dardanelle, AR

## Conversion tracking — NOT live yet
The page fires `request_quote_click` and `call_click` events **if** a `gtag` is present.
To activate: paste Kennedy's Google Ads / GA4 gtag snippet into `<head>` and map those
event names to conversions. (Jobber hosts its own confirmation page on their domain, so the
quote-button click is the trackable signal on our side, not a thank-you-page load.)

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
