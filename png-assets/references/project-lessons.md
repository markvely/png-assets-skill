# Project Lessons

These lessons came from two validated workflows: an app function-icon set and a mobile H5 campaign page.

## App Function Icon Set

- Anchor generation to the approved brand icon or current visual baseline. Do not use archived or rejected icon directions as the source of truth.
- A sprite sheet is acceptable only for highly standardized icon systems when it is a strict grid, has wide key-color gutters, and each cell contains exactly one icon with the same live-area and shape rules.
- Prompt exact count, grid, reading order, style, colors, and icon meanings. Ambiguity creates inconsistent icons.
- Crop each cell into an independent transparent PNG, then normalize via alpha bbox to a stable live area.
- Use optical offsets for icons that look visually off-center despite mathematically centered bboxes.
- Produce a contact sheet and inspect small-size readability. Green-screen removal can pass mechanically while the icons still fail as a system.
- For a brand mascot or character glyph, prefer extracting from the approved icon layer when available instead of asking the model to redraw it from memory.

## H5 Campaign Asset Page

- A campaign page must be assembled from controllable assets, not one generated poster.
- Generate hero characters, selectable objects, reward icons, CTA ornaments, title signs, and badges as separate files.
- Generate H5/page assets one by one by default. Do not combine multiple rewards, props, characters, or title elements into a shared canvas.
- Key gameplay objects should themselves be clickable or sit directly above their button. Avoid "big illustration plus separate list" when the object is the choice.
- If a generated source contains several important objects in one image, regenerate each object separately. Do not use the whole sheet as the page visual.
- Keep operational text, prices, odds, values, buttons, and rules code-native so they remain editable and responsive.
- Use project-local versioned filenames such as `reward-box-basic-v1.png` and `event-character-v2.png`.
- After placing assets in HTML, inspect real screenshots for occlusion, z-index mistakes, mobile overflow, blurry scaling, and weak click affordance.

## Chroma-Key Lessons

- Direct transparent PNG output is the preferred first attempt when the image model supports alpha. It removes a processing step and avoids key-color contamination.
- Chroma-key remains the fallback for opaque mattes, dirty alpha, bad semi-transparent edges, or tools that cannot produce true alpha.
- Default green key works for warm, dark, gold, orange, black, cream, and many blue assets.
- Use magenta key when the subject contains green, moss, jade, leaf, neon-green, or green-tinted highlights.
- `--despill` handles normal edge tint; `--edge-contract 1` is useful when a visible halo remains.
- Transparent PNG verification must include both script checks and visual checks on the actual target background.

## Asset Quality Lessons

- Reject assets that look assembled from basic geometry, CSS/SVG primitives, icon fonts, emoji, or generic pictograms. They usually feel cheap in apps, websites, and campaign pages.
- For finished PNG material, require coherent lighting, material, depth, silhouette, and edge polish.
- Simple geometry is acceptable only for deliberate wireframes, placeholders, or strict flat icon systems that the user explicitly requested.
