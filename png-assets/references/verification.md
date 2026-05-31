# Verification

Use this checklist before handing off generated PNG assets or a surface that uses them.

## Static Checks

Check PNG transparency:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/png-assets/scripts/verify_png_assets.py" <asset-dir-or-files>
```

For transparent cutouts, failures to fix:

- Missing alpha channel.
- Non-transparent corners.
- Opaque white, gray, black, or checkerboard matte where alpha was requested.
- Subject almost fills the canvas and risks cropping.
- Subject bbox is empty or tiny.
- Visible green or magenta fringe.
- Multiple separated subjects in one file.
- Crude geometric assembly: obvious circles, rounded rectangles, triangles, gradients, emoji, icon-font symbols, or simple SVG/CSS-like shapes pretending to be finished assets.

If direct transparent output repeatedly fails, regenerate the source with a flat green or magenta chroma-key background and remove it with the bundled fallback flow.

For standalone HTML or H5 pages, check static asset paths:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/png-assets/scripts/check_html_asset_refs.py" <page.html>
```

Run the repo's build, lint, or preview command when integrating into an existing app or website.

## Visual Checks

Inspect at least one rendered output:

- contact sheet for multiple PNGs
- browser screenshot for website/H5
- simulator/device/app preview for native apps
- exported frame/slide for design, deck, or social output

Check:

- asset style is consistent across the set
- subject is readable at target size
- edges look clean on the real background
- asset reads as designed raster material, not placeholder geometry
- no stretching, blurring, accidental cropping, or shadow mismatch
- important text or controls are not placed over busy image details
- decorative assets do not block clicks or gestures

## Website And H5 Checks

Minimum browser viewports for mobile activity pages:

- Target phone, such as 390x844 or 430x932.
- Small phone, such as 360x740.
- Wider desktop fallback if the file may be opened outside a phone shell.

Click through core paths:

1. Initial selection.
2. Requirement or progress update.
3. Disabled state when requirements are unmet, if applicable.
4. Confirmation or modal.
5. Primary action.
6. Animation or loading state.
7. Result state.
8. Secondary action, rules, record, or share surface if present.

Verify:

- all `<img>` elements have `naturalWidth > 0`
- CSS background images are loaded
- no console 404s for local assets
- no references to temporary generation directories
- no horizontal overflow or unsafe bottom CTA placement

## App Checks

- Confirm assets are in the repo's expected bundle/catalog path.
- Verify names match code references and platform case sensitivity expectations.
- Preview target states, not only the default image.
- Check light/dark backgrounds if the asset appears in both.
- Confirm accessibility labels and localized text remain native, not baked into images.

## Design Checks

- Place transparent assets over the final canvas background before export.
- Inspect at 100% and at the final delivery size.
- For icon systems, inspect 24px, 32px, and 48px equivalents.
- For decks/social images, export one final bitmap/PDF and review the actual output, not only the editor canvas.

## Final Handoff Notes

Report:

- asset directory or deliverable path
- important generated asset categories
- integration path, if any
- verification performed
- any limitation, such as no browser/app preview available
