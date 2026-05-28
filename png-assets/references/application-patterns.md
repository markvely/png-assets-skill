# Application Patterns

Use these patterns after final PNG assets exist or when planning how they will be used.

## File Layout

Prefer a local, versioned asset folder:

```text
assets/generated/<feature-or-page>/
  raw/
    hero-character-source-v1.png
    reward-icon-source-v1.png
  hero-character-v1.png
  reward-icon-v1.png
  background-main-v1.png
```

Rules:

- Final code references only final project-local PNGs.
- Keep raw sources when later reprocessing is likely.
- Use lowercase ASCII names when the surrounding project allows it.
- Use version suffixes. Do not overwrite stable assets unless the user asks.

## Apps

- Follow the repo's existing asset catalog or static-image folder.
- Use platform-native image sets when the project already uses them.
- Keep text, localization, accessibility labels, state, and business values native to the app.
- Create state variants deliberately: normal, selected, disabled, pressed, empty, loading, reward/result.
- Verify at real target sizes. Icons that look good at 512px can fail at 24pt.
- For launcher or app icons, follow platform mask/safe-zone rules and do not rely on alpha if the platform disallows it.

## Websites And H5

- Use PNGs as layered `<img>` elements or CSS backgrounds with explicit width, aspect ratio, `object-fit`, and z-index.
- Keep page title, CTA labels, countdowns, prices, odds, reward names, and rules in HTML/CSS/JS.
- Make primary objects clickable when they are the visible choice. Avoid a large illustration plus a separate unrelated list.
- Set `pointer-events: none` on decorative images so they do not block controls.
- Use stable dimensions for repeated visual components; selection should not change row or card height.
- Check local references:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/png-assets/scripts/check_html_asset_refs.py" <page.html>
```

## Standalone Mobile H5 Shell

Use a constrained phone canvas when the deliverable is a standalone mobile HTML page:

```css
:root {
  --page-max: 430px;
  --safe-x: 16px;
}

body {
  margin: 0;
  min-height: 100svh;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.phone-page {
  position: relative;
  width: min(100vw, var(--page-max));
  min-height: 100svh;
  margin: 0 auto;
  overflow: hidden;
}

.asset {
  display: block;
  width: 100%;
  height: auto;
  object-fit: contain;
  user-select: none;
  -webkit-user-drag: none;
}
```

Use `100svh` for mobile browser chrome. Add `padding-bottom: env(safe-area-inset-bottom)` when CTAs are near the bottom.

## Design, Deck, And Social Output

- Use transparent PNGs as composable elements, not flattened one-off screenshots.
- Build a contact sheet when delivering multiple assets so style consistency and edge quality are visible at once.
- Preview assets on the actual background color or image, especially dark, warm, and textured backgrounds.
- Keep editable text in the design tool or document whenever future copy changes are likely.
- Export final canvases only after checking that subject scale, crop, shadow, and edge color work together.

## Layering

For pages and app-like surfaces, define layers deliberately:

```css
.bg { z-index: 0; }
.ambient { z-index: 1; pointer-events: none; }
.hero-art { z-index: 2; pointer-events: none; }
.content { z-index: 3; }
.sticky-cta { z-index: 5; }
.overlay { z-index: 20; }
```

## Interaction And Motion

- Use lightweight transforms, opacity, glow, and short bursts rather than heavy canvas effects unless the project already uses them.
- Respect reduced motion in web output.
- For prototypes, make every visible primary control do something or show disabled feedback.
- For reward/result flows, keep icon boxes fixed and let text wrap in a controlled area.

## Text And Raster Boundaries

Keep these native unless the user explicitly wants a flat graphic:

- Page title and subtitle.
- CTA labels.
- Countdown and status text.
- Values, prices, and reward ratios.
- Reward names and durations.
- Rules and legal text.
- Error, toast, and disabled-state messages.

Raster text is acceptable only when it is intrinsic to an illustration, product label, decorative logo, sign, or poster whose copy is already final.
