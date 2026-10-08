# The Curb Guy — Landing Page

Single-page Google Ads landing page for **The Curb Guy LLC** (Marcus Reimer), custom concrete
landscape curbing, Dardanelle AR + Central Arkansas / River Valley.

**Read this before editing.**

## Files
- `index.html` — the whole page (self-contained; all CSS/JS inline).
- `images/` — WebP (converted 2026-08-03 from the Facebook photos in `../assets/`; heroes 1600px q78, gallery 1200px, `logo.webp`). Below-fold images use `loading="lazy"`. Above-fold heroes re-compressed 2026-09-10 (splashpad 900px, farmhouse 1100px, tree-ring 800px, q74). Originals still in git history.
- CTA wording (2026-09-08, Kennedy): every scroll-to-form button says **"Submit Form"** and the form button says **"Submit"** — "for now". The form heading keeps "Free Consultation" so the ad promise is still on the page.

## The quote form (native, added 2026-09-08 — replaces the Jobber button)
The page now has its own form (`#quote`, top of the "What We Do" section, pill-style fields:
Full Name · Phone · City · "Tell Us About Your Project"). Every "Book … Consultation" button
scrolls to it. It posts to **Web3Forms** by AJAX, then redirects to `/thank-you`, which fires
the Google Ads conversion **"Quote Form Submit (landing page)"** (`AW-18345842541/EbxSCITKvfMcEO2u_atE`,
action id 7758374148, created 2026-09-10). The old "Booked appointment on Landing Page" action
(`2l4mCIGW39ccEO2u_atE`) is left in place, unused, in case the Jobber form ever comes back.
- **Web3Forms access key `acfa2cee-950a-46fb-b2c4-a7f8dd9a3bb6` — LIVE 2026-09-08** (Kennedy supplied it).
  Test submits must be done in a real browser (Web3Forms blocks curl/headless).
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

## Section anchors (for Google Ads sitelinks — don't rename)
`#quote` form · `#why` benefits · `#work` gallery · `#how` steps · `#reviews` · `#area` service area. The campaign's sitelinks point at #work, #reviews, #how, #area.

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
| **Form submit** | thank-you page load after a real on-page form submit (`fireBooking()`) | `thank-you.html` | `EbxSCITKvfMcEO2u_atE` |

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

---

## Lighting landing page — `lighting.html` + `lighting-thank-you.html` (built 2026-10-06, NOT yet deployed)
Second Google Ads landing page on the same repo/project for the new **permanent exterior / holiday lighting**
service (roofline only). Clean URLs: `/lighting`, `/lighting-thank-you`. Also the landing page for the Facebook
lighting campaign (FB traffic lands with no `?ag=` and sees the default hero).

- **Ad-group message match via `?ag=`:** `/lighting` = Permanent Lighting (default) · `/lighting?ag=install` =
  Christmas Light Installers · `/lighting?ag=house` = Lights On a House. Swaps eyebrow + H1 + subhead only.
  `?loc=<geotarget id>` still swaps the eyebrow to the searcher's town (same map as index.html; runs after `ag`).
  Google Ads final URL suffix for this campaign: `loc={loc_physical_ms}` (ag is baked into each ad group's final URL).
- **Photos (`images/lighting/`) are the SUPPLIER'S library** (Trimlight, Utah homes — see
  `../holiday-lighting/photo-library.md`). Captions deliberately say "what the system looks like installed", never
  "our work". Kennedy (2026-10-06): supplier photos are fine as-is; no need to swap in Marcus's own.
  The 4-photo "same house, four nights" row + the day/night slider are all one Riverton UT house.
- **Form:** same Web3Forms key, subject "New LIGHTING consultation request", hidden `service=Permanent exterior
  lighting` + `source` fields. Redirects to `/lighting-thank-you`, which fires the **"Lighting Quote Form"**
  conversion (action 7830500870, label `VcjCCIbs75UdEO2u_atE`, created 2026-10-08) — separate from curbing's form action.
- Text taps on this page fire **"Lighting Text Click"** (action 7830611037, label `coK0CN3I9pUdEO2u_atE`), not curbing's
  "Text From Website". Call tracking (`call-swap`) + Meta pixel: identical wiring to index.html.
- **Google Ads campaign BUILT 2026-10-08, PAUSED** (24333481814) — see `../google-ads/reports/2026-10-08-changes.md`. GA4 events carry
  `service:'lighting'`; pixel events carry `content_name:'lighting'`.
- **Claims used (Kennedy confirmed 2026-10-06):** licensed & insured · lifetime warranty on the lights ·
  5-year LABOR warranty on the install (confirmed 2026-10-06) · app-controlled colors + schedules (confirmed) ·
  owner-operated · 13 years in the trades · 5-star rated. **Deliberately NOT claimed (Kennedy, 2026-10-06):** one-day install.
  Trim-matched track CONFIRMED 2026-10-08 (the "in a color that matches your trim" line stays). Photos section is titled just "Photos" — supplier photos are fine to use as-is;
  no need to wait for Marcus's own installs.
- No prices on the page (Kennedy: the $4–6k figure was for the report only). FAQ answers "how much" with the
  free on-site written quote.
- Curbing page (`index.html`) is untouched; the curbing campaign stays live.

### Design (v2, 2026-10-06 — Kennedy's direction)
- NOT the Curb Guy brand. No logo, no business name in the header: a small roofline-with-lights SVG mark + "Exterior Lighting"
  wordmark. The only "The Curb Guy LLC" mention is the footer copyright line (business identity for Google's policy + the
  privacy policy) — Kennedy knows, hasn't asked to remove it.
- Palette = "Midnight": near-black blue `#0D1320` / `#080D18`, matte navy button `#2C4A78`, steel-blue accent `#9BB3D4`,
  cool gray light sections `#EEF1F5`. Picked from three matte options (Evergreen / Midnight / Graphite); the other two are
  in git history of this README's session notes if he wants them back. Gold (v1 of the redesign) was rejected.
- Fonts: Instrument Serif (display, italic accents) + Figtree (body). Buttons are pill-shaped, matte, no glow.
- Token names in the CSS are the shared ones (`--navy`, `--red`, `--cream`…) so the sections stay interchangeable; values changed.
- **REVIEW LABEL (remove before launch):** a yellow strip under the header (`#hdPage`) names the page version
  ("For Permanent Lighting and Facebook" / "For Christmas Lights" / "For Lights on a House") so Kennedy can tell
  tabs apart while reviewing. REMOVED 2026-10-08 before deploy (the `?ag=` H1/media swap stays).
- Hero: Kennedy plans a VIDEO hero, possibly a different video (and color pattern) per page version — he is choosing
  the clips himself; don't add any yet.
- 2026-10-06 (later): Kennedy wants these pages SIMPLE. Hero = title + two buttons + three trust pills only (eyebrow
  and subhead removed on all three versions). The `?loc=` town-name swap was removed with the eyebrow — the Google Ads
  final URL suffix no longer needs `loc={loc_physical_ms}` for this campaign.
- 2026-10-07: **Color demo** section (`#colors-demo`, right under the trust bar): "Click/Tap to Change the Color" — ten scenes of
  the SAME house (Springdale Dr, the angled-from-the-left view = Kennedy's "other angle"; files `260617 … UT-1…44`), cropped
  4:3 into `images/lighting/colors/`: off (daytime), warm, white, blue (blue+white), purple, razorbacks (red/white/teal — the
  closest the set has), christmas, halloween (orange), july, party. No solid blue/green exists in that angle. Two stacked
  images crossfade; scenes preload near the viewport; taps log a `color_demo_tap` GA4 event. A comment marks the slot above
  it for Kennedy's generated "person holding the phone app" photo (not received yet).
- `?review=1` on any page URL collapses the full-screen hero (screenshot helper only; harmless for visitors).
- 2026-10-07 (later): **Page cut down to the sections Kennedy kept** — hero · trust bar · phone photo + 6 stats + color demo ·
  NEW product section (`#product`, six fact cards sourced from trimlight.com: patented channel under the soffit, Edge app +
  Google Home/Alexa, 50,000-hr bulbs / 20–30 yrs normal use / lifetime product warranty on core components, no lens so no
  fading, 0.9 W per bulb on 12 V, authorized-dealer install + 5-yr labor warranty) · day/night slider · estimate form ·
  Marcus · service area · final CTA. REMOVED: four-nights row, why-permanent cards, photo gallery, warranty band, reviews, FAQ.
  Stats shown: Millions of colors · Lifetime warranty · 50,000 hrs · 0.9 W · 5 Years labor · Since 2010 (Trimlight).
  **The page now names Trimlight** (stats + product cards) — CONFIRMED 2026-10-08 (Kennedy): Marcus IS an authorized Trimlight dealer, brand name stays.
- 2026-10-07: **Hero media per version** (inline script right after the hero): default + `?ag=house` = Ariat Cove 42.jpg
  (desktop) / Ariat Cove 6.mov (phone); `?ag=install` = Indian Wells UT-95.jpg (desktop, red/green) / Copper Gulch 8.mov
  (phone — came pillar-boxed inside a 1920×1080 frame, black bars cropped off). All clips: first 12 s, muted, loop, crf 24.
