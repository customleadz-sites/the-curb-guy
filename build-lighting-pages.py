#!/usr/bin/env python3
"""lighting.html is the ONE source. This writes the two ad-group versions as real static pages
(own <title>, meta description, H1, hero media) so Google's AdsBot sees the matching headline
without running JavaScript. Run after ANY edit to lighting.html, then commit all three files:
    python3 build-lighting-pages.py
"""
import os, re
here = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(here, "lighting.html")).read()

VERSIONS = {
  "christmas-light-installation.html": {
    "ad_group": "Christmas Light Installers",
    "title": "Christmas Light Installation in the River Valley | Permanent Lights, Installed Once",
    "description": "Christmas light installation done once. Permanent LED lights along your roofline, any color from your phone, lifetime warranty on the lights. Licensed & insured. Serving Russellville, Fort Smith & the River Valley. Call (479) 237-9888.",
    "h1": "Christmas Light Installation. <em>Hang Them Once. Never Again.</em>",
    "service": "Christmas light installation",
    "media": {"images/lighting/hero-permanent-desktop.webp": "images/lighting/hero-christmas-desktop.webp",
              "videos/hero-permanent-poster.webp": "videos/hero-christmas-poster.webp",
              "videos/hero-permanent.mp4": "videos/hero-christmas.mp4"},
  },
  "christmas-lights-on-house.html": {
    "ad_group": "Lights On a House",
    "title": "Christmas Lights on Your House, Without the Ladder | River Valley & Fort Smith",
    "description": "Permanent Christmas lights installed on your house once. Red, green, warm white, any color from your phone. Licensed & insured, lifetime warranty on the lights. Serving Russellville, Fort Smith & the River Valley. Call (479) 237-9888.",
    "h1": "Christmas Lights on Your House, <em>Without the Ladder.</em>",
    "service": "Christmas lights on house",
    "media": {},
  },
}

def sub1(s, old, new):
    assert s.count(old) >= 1, old[:60]
    return s.replace(old, new)

for fname, v in VERSIONS.items():
    s = base
    s = sub1(s, re.search(r"<title>.*?</title>", s).group(0), f"<title>{v['title'].replace('&','&amp;')}</title>")
    s = sub1(s, re.search(r'<meta name="description" content="[^"]*">', s).group(0), f'<meta name="description" content="{v["description"]}">')
    s = sub1(s, re.search(r'<h1 class="hero-anim d1" id="heroH1">.*?</h1>', s, re.S).group(0), f'<h1 class="hero-anim d1" id="heroH1">{v["h1"]}</h1>')
    s = sub1(s, '<input type="hidden" name="service" value="Permanent exterior lighting">', f'<input type="hidden" name="service" value="{v["service"]}">')
    for old, new in v["media"].items(): s = sub1(s, old, new)
    s = s.replace("<!DOCTYPE html>", f"<!DOCTYPE html>\n<!-- GENERATED from lighting.html by build-lighting-pages.py — ad group: {v['ad_group']}. Edit lighting.html, then re-run the script. -->", 1)
    open(os.path.join(here, fname), "w").write(s)
    print("wrote", fname, len(s))
