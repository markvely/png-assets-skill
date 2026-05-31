---
name: png-assets
description: Generate and apply reusable PNG design assets across apps, websites, H5/HTML campaign pages, presentations, design comps, app icon systems, game-like props, stickers, rewards, characters, and UI decorations. Use when Codex needs to plan PNG asset inventory, create AI-generated transparent-background raster assets, use green/magenta chroma-key fallback, cut sprite sheets, validate alpha quality, place assets into a local project, implement them in app/web/design surfaces, or replace placeholder CSS/SVG/geometric blocks with controllable production-style PNG material.
---

# PNG Assets

Use this as the single skill for PNG asset generation and application. It owns the full path from visual planning to usable files: inventory, prompt strategy, direct transparent PNG generation, chroma-key fallback, alpha verification, and integration into apps, websites, H5 pages, prototypes, decks, or design compositions.

## Core Rule

Do not treat image generation as a final poster unless the user explicitly asks for one. Build with controllable assets: text, values, buttons, rules, routing, and interaction stay native to the target surface; PNGs carry visual material such as backgrounds, characters, props, product objects, rewards, badges, icon glyphs, title frames, stickers, textures, and decorative accents.

Generate one source image per asset by default. Do not combine multiple assets into one generated canvas to save time or calls. A shared canvas is allowed only for highly standardized sets whose members must match the same design system and shape rules, such as app function icons, same-size state variants, or another strict icon-like system.

Do not fake assets by assembling basic geometric shapes, emoji, stock pictograms, CSS/SVG placeholder shapes, or icon-font style symbols. If an asset should be visual material, it must be generated or supplied as a real raster illustration/render with coherent lighting, material, silhouette, and edge quality.

## Workflow

1. Read local project instructions first. Follow existing asset paths, naming, style, build, and design-system conventions.
2. Identify the target surface:
   - **App**: native iOS/macOS/Android/web app assets, app icons, feature icons, onboarding art, empty states, stickers, rewards.
   - **Website or H5**: marketing pages, mobile campaign pages, HTML prototypes, landing sections, interactive activity pages.
   - **Design output**: Figma-like comps, decks, social visuals, documentation graphics, contact sheets, brand explorations.
3. Make an asset inventory before generating images. Separate:
   - native UI: text, prices, buttons, forms, rules, countdowns, tabs, lists, state labels
   - full backgrounds: scene, atmosphere, texture, hero backdrop, no alpha needed
   - transparent cutouts: characters, products, props, rewards, badges, icons, stickers, ornaments
4. Default to one generation request and one source image per important subject. Do not generate a collage of several assets and then depend on cropping.
5. Use a shared canvas only for highly similar, standards-bound assets: app function icon sets, same-shape icon state variants, or another strict grid system where every item has the same design rules, visual weight, live area, and shape constraints. Cut the sheet into independent PNGs before final use.
6. Prefer direct transparent-background PNG output when the image model or API supports alpha. Request true transparent alpha, not white/gray/black matte or checkerboard.
7. Use chroma-key fallback only when direct alpha is unavailable, produces an opaque matte, has dirty edges, or fails visual inspection. For fallback, generate on a flat key background:
   - default `#00ff00`
   - use `#ff00ff` when the subject contains green, jade, leaves, moss, neon-green, or green-tinted highlights
8. Reject or regenerate sources with multiple separated subjects, geometric placeholder construction, emoji-like symbols, stock pictograms, opaque mattes, non-flat fallback key backgrounds, ground shadows, text, watermarks, key-color contamination, cropped silhouettes, or unclear small-size readability.
9. Copy raw generated files into the project before processing. App/web/design files must not reference `$CODEX_HOME/generated_images/...`.
10. Convert raw chroma-key fallback sources to alpha PNGs:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/imagegen/scripts/remove_chroma_key.py" \
  --input <source.png> \
  --out <final.png> \
  --auto-key border \
  --soft-matte \
  --transparent-threshold 12 \
  --opaque-threshold 220 \
  --despill
```

If a visible key-color fringe remains, retry once with `--edge-contract 1`.

11. Verify final PNGs:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/png-assets/scripts/verify_png_assets.py" <asset-dir-or-files>
```

12. Integrate assets into the target surface. Use stable sizing, `object-fit: contain`, fixed icon boxes, asset catalogs, responsive constraints, or design-frame dimensions as appropriate.
13. Inspect the real result: browser screenshot, app preview, contact sheet, exported design, or rendered deck. Mechanical alpha checks are not enough.

## Application Rules

- **Apps**: follow the app's asset catalog/static-resource conventions; create size variants only when the platform or repo expects them; verify icons at target sizes such as 24pt, 32pt, 48pt, and any launcher/app-icon sizes.
- **Websites/H5**: keep operational text and controls in HTML/CSS/JS; use PNGs as layered images, backgrounds, reward icons, hero objects, and decorative materials; verify local asset references with `check_html_asset_refs.py`.
- **Design/deck/social output**: use transparent PNGs as composable visual elements; export contact sheets or final canvases only after checking edges against the actual background color.
- **Icon systems**: use approved brand/current visual references as anchors; sprite sheets are acceptable only when the set is highly standardized, with strict grid, wide gutters, exact count, one glyph per cell, and consistent shape/live-area rules.
- **Full backgrounds**: use for atmosphere and scene depth only. Do not bake UI copy, prices, editable labels, rules, or button states into background art.

## Decision Rules

- Use independent assets by default, especially when an element needs separate placement, animation, z-index, click handling, state, reuse, replacement, or visual judgment.
- Use shared canvases only for standardized icon-like systems that must be generated together for consistency. Do not use shared canvases for characters, rewards, props, title boards, products, H5 choices, stickers, hero art, or decorative one-offs.
- Use direct alpha first. Use chroma-key fallback when transparency is unavailable or visually flawed.
- Use magenta key instead of green for fallback when the subject contains green or greenish transparency.
- Reject geometric-shape assembly. Do not deliver assets built from simple circles, rectangles, gradients, CSS shapes, emoji, icon-font glyphs, or generic pictograms unless the user explicitly asked for primitive vector placeholders.
- Regenerate instead of patching when a source combines unrelated objects or has contaminated edges.
- Keep raw sources when later reprocessing is likely; use versioned final filenames instead of overwriting stable assets.

## Quality Gates

Before handoff, check:

- final files are local to the project or deliverable folder
- transparent PNGs have alpha channels and transparent corners
- subject silhouettes are intact and not eaten by key removal
- assets are not crude geometric/emoji/SVG-placeholder compositions
- edge color is acceptable on the real target background
- important files contain one controllable subject
- icons remain readable at their target sizes
- app/web/design integration does not stretch, blur, crop, hide, or block controls
- interactive pages have loaded assets, working controls, and no broken local references

## References

- Use `references/prompt-recipes.md` for copyable prompts.
- Use `references/application-patterns.md` for app, website/H5, and design integration patterns.
- Use `references/verification.md` for static, visual, browser, app, and design checks.
- Use `references/project-lessons.md` for lessons from prior icon and H5 campaign workflows.

## Bundled Scripts

- `scripts/batch_remove_chroma_key.py`: batch convert raw chroma-key PNGs to alpha PNGs with consistent flags.
- `scripts/verify_png_assets.py`: verify alpha, transparent corners, subject bbox, minimum size, and basic crop risk.
- `scripts/check_html_asset_refs.py`: verify local static references in standalone HTML/CSS before browser QA.
