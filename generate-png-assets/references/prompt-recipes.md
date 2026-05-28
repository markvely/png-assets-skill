# Prompt Recipes

Use these templates with the available image generation tool. Replace bracketed fields and keep the constraints intact.

## Universal Chroma-Key Cutout

```text
Create a single isolated PNG asset.
Subject: [one specific object].
Target use: [app / website / H5 campaign page / design comp / deck / social visual].
Style: [polished 3D game UI / flat vector-like app icon / premium illustration / cute sticker / realistic product render].
Composition: one object only, centered, full object visible, generous empty padding, clear silhouette.
Background: perfectly flat solid #00ff00 chroma-key background, one uniform color only.
Constraints: single isolated asset, one object only, no collage, no sheet, no multiple separate items, no text, no watermark, no floor, no ground shadow, no cast shadow, no background gradient, no texture, no reflection, do not use #00ff00 anywhere in the object.
```

Use `#ff00ff` instead of `#00ff00` if the subject contains green.

## App Function Icon

```text
Create a single production-ready mobile app function icon.
Function: [feature meaning].
Style anchor: [approved brand icon / current product style / visual reference].
Style: crisp vector-like filled pictogram, simple silhouette, readable at 24px, consistent optical weight.
Colors: [allowed subject colors].
Composition: one icon glyph only, centered, generous safe area, no badge unless requested.
Background: perfectly flat solid #00ff00 chroma-key background.
Constraints: no text, no numbers, no UI card, no border box, no shadow, no gradient background, no extra decoration, do not use #00ff00 in the icon.
```

## Function Icon Sprite Sheet

```text
Generate one production-ready sprite sheet of [count] professional mobile app function icons.
Canvas: [columns] columns by [rows] rows, pure chroma-key green background #00FF00 only.
Grid: each icon centered in its own invisible square safe area, wide green gutters between icons, consistent optical weight.
Style: [approved brand style], one coherent filled pictogram per icon, crisp vector-like edges, readable at 24px.
Colors: [allowed subject colors only].
Do not add labels, borders, grid lines, UI cards, mockups, shadows, gradients, texture, words, numbers, or extra decoration.
Icon meanings in exact order: [ordered list].
```

After generation, cut the sheet into independent PNGs, normalize each icon by alpha bbox, and inspect a contact sheet.

## H5 Or Website Campaign Prop

```text
Create a single isolated selectable campaign prop for a mobile H5 or website activity page.
Object: [material and type, e.g. bronze reward box / silver reward box / crystal reward box].
Tier feeling: [basic / mid / premium] expressed through material, silhouette, and details, not text.
Style: polished 3D mobile game event asset, readable at small phone size, appealing material texture.
Composition: one object only, front three-quarter view, centered, full object visible, generous padding, suitable as a large tappable button.
Background: perfectly flat solid #00ff00 chroma-key background.
Constraints: no labels, no numbers, no text, no watermark, no collage, no sheet, no multiple items, no floor, no cast shadow, do not use #00ff00 in the object.
```

## Character Or Mascot

```text
Create a single isolated character asset.
Character: [role, outfit, expression, pose].
Target use: [app onboarding / H5 campaign / website hero / design comp / sticker].
Style: polished colorful 3D mobile game event mascot, friendly, strong silhouette, premium marketing art.
Composition: one character only, full body or half body as requested, centered, generous padding.
Background: perfectly flat solid #00ff00 chroma-key background.
Constraints: no text, no watermark, no extra characters, no separated props, no collage, no sheet, no floor, no cast shadow, do not use #00ff00 in the character.
```

If the character holds a prop, make it attached to the character, not a separate floating object.

## Reward Or Result Icon

```text
Create a single isolated reward icon.
Reward: [gift pack / ticket / key / avatar frame / entry effect / coin pack / badge].
Target use: [app list / H5 result row / website card / design comp].
Style: compact polished 3D app icon, clear silhouette, high contrast, readable at 48px.
Composition: one icon only, centered, full icon visible, generous padding.
Background: perfectly flat solid #00ff00 chroma-key background.
Constraints: no text, no watermark, no collage, no sheet, no multiple icons, no floor, no cast shadow, do not use #00ff00 in the icon.
```

## Title Plaque Or UI Ornament

```text
Create a single isolated UI ornament asset.
Subject: [blank title plaque / gold festival banner / neon label frame / button medallion / compass token].
Design: decorative edges, strong silhouette, blank center or simple shape for native text/control overlay.
Target use: [website section title / H5 event title / app onboarding / deck visual].
Composition: one object only, centered, full object visible, generous padding.
Background: perfectly flat solid #00ff00 chroma-key background.
Constraints: no text, no watermark, one object only, no collage, no sheet, no ground, no cast shadow, do not use #00ff00 in the object.
```

## Full Background

```text
Create a [vertical 9:16 / horizontal 16:9 / square 1:1] background scene.
Target use: [mobile H5 first screen / website hero / app onboarding / deck cover].
Theme: [theme].
Scene: [environment].
Mood: [festive / mysterious / premium / playful / warm].
Composition: strong atmosphere, clear depth, quieter readable zones at [top/middle/bottom] for native UI, no central object that would block controls.
Style: [3D rendered / painterly / game event art / polished app campaign / product marketing].
Constraints: no UI, no buttons, no labels, no prices, no readable text, no watermark, no pasted poster layout.
```

Backgrounds do not need alpha. They must not include operational UI.

## Small Decoration Sprite Sheet Exception

```text
Create a [3x3 / 4x4] sprite sheet of [small same-type decoration] assets on a perfectly flat solid #00ff00 chroma-key background.
Each cell contains exactly one object, centered, with wide empty padding.
Use a clean grid layout with no overlap, no shadows connecting cells, no text, no watermark, no collage outside the grid.
Do not use #00ff00 anywhere in the objects.
```

Use this only for low-risk same-type decorations such as sparkles, bubbles, confetti, tiny coins, or small badges.

## Repair Prompts

Multiple objects:

```text
Regenerate as exactly one isolated [object]. One object only. No extra props, no separate pieces, no collage, no sheet.
```

Bad key background:

```text
The background must be a perfectly flat, uniform solid #00ff00 chroma-key color with no gradients, no shadows, no floor, no vignette, and no texture.
```

Subject includes key color:

```text
Use a perfectly flat solid #ff00ff chroma-key background. The subject must not contain #ff00ff in highlights, reflections, rim light, shadows, or transparent materials.
```

Subject too small:

```text
Make the object fill about 75% of the canvas while keeping the full silhouette visible and leaving clean padding around all edges.
```

Edge contamination:

```text
Do not use the chroma-key color in highlights, reflections, rim light, shadows, transparent materials, or anti-aliased edge pixels.
```
