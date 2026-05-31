# PNG 素材 Skill

这是一个可复用的 Codex skill，用于生成、抠图、验证并应用透明 PNG 素材，覆盖 App、网站、H5 活动页、设计稿、演示文稿、社媒图、icon 系统、角色、道具、奖励素材等场景。

核心思路：

- 先拆素材清单，再生成图片。
- 重要元素默认一物一图，避免把多张素材合到同一画布后再切。
- 只有高度相似、严格贴合同一设计规范和形状规范的 icon / 状态组，才允许合并到同一画布生成。
- 优先直接生成透明背景 PNG；如果模型输出白底、脏边或不支持 alpha，再回退到绿幕/洋红幕抠图。
- 拒绝用几何图形、CSS/SVG 形状、emoji、icon font 或通用 pictogram 拼凑出来的假素材。
- 文案、价格、按钮、规则、状态和交互保留在 App/Web/设计工具中。
- 最终用脚本和实际渲染结果一起检查。

## 安装

把 `png-assets` 目录复制到你的 Codex skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R png-assets "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重新打开 Codex 或刷新 skill 列表后，可使用显示名：

```text
PNG 素材
```

## 目录

```text
png-assets/
  SKILL.md
  agents/openai.yaml
  references/
    application-patterns.md
    project-lessons.md
    prompt-recipes.md
    verification.md
  scripts/
    batch_remove_chroma_key.py
    check_html_asset_refs.py
    verify_png_assets.py
```

## 常用命令

验证 PNG 透明度和主体裁切：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/png-assets/scripts/verify_png_assets.py" <asset-dir-or-files>
```

批量绿幕/洋红幕抠图：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/png-assets/scripts/batch_remove_chroma_key.py" <raw-png-dir> --out-dir <output-dir>
```

检查 HTML 中的本地资源引用：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/png-assets/scripts/check_html_asset_refs.py" <page.html>
```

## 适用场景

- App 功能图标、空状态、引导页、奖励图标、贴纸、素材包。
- 网站 hero、营销页、活动页、产品展示素材。
- H5 活动页、互动页、小游戏式营销页面。
- 设计稿、PPT、社媒图中的可复用透明 PNG 元素。
- 需要从 AI 生成图中切出可控素材，而不是只拿一张成品图的场景。
