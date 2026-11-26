"""Builds assets/hero-dark.svg and assets/hero-light.svg. Run: python3 assets/build.py"""
from pathlib import Path

OUT = Path(__file__).parent
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

THEMES = {
    "dark": dict(text="#e6edf3", muted="#9198a1", border="#3d444d", surface="#151b23", accent="#b27aff", ok="#3fb950"),
    "light": dict(text="#1f2328", muted="#59636e", border="#d1d9e0", surface="#f6f8fa", accent="#8405ff", ok="#1a7f37"),
}

TASKS = [
    ("design", "Figma", '<rect x="9" y="9" width="12" height="12" rx="2"/><circle cx="23" cy="23" r="6"/>'),
    ("build", "Vue", '<path d="M8 15l-4 3 4 3M28 15l4 3-4 3M21 10l-6 16"/>'),
    ("review", "PullRequest", '<circle cx="11" cy="10" r="3"/><circle cx="11" cy="26" r="3"/><circle cx="25" cy="26" r="3"/><path d="M11 13v10M25 23v-8a4 4 0 0 0-4-4h-4"/>'),
    ("ship", "Release", '<path d="M18 7v18M11 14l7-7 7 7M9 29h18"/>'),
]

STYLE = f"""
.mono {{ font-family: {MONO}; }}
.sans {{ font-family: {SANS}; }}
.in {{ animation: in .5s cubic-bezier(.2,.8,.2,1) var(--t) both; }}
.flow {{ stroke-dasharray: 4 5; animation: in .3s var(--t) both, flow 1s linear var(--t) infinite; }}
.pulse {{ animation: in .3s var(--t) both, pulse 1.4s ease-in-out var(--t) infinite; transform-box: fill-box; transform-origin: center; }}
@keyframes in {{ from {{ opacity: 0; transform: translateY(4px); }} to {{ opacity: 1; transform: none; }} }}
@keyframes flow {{ to {{ stroke-dashoffset: -9; }} }}
@keyframes pulse {{ 50% {{ opacity: .35; transform: scale(1.6); }} }}
@media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
"""


def hero(t):
    w, h = 960, 252
    nw, nh, gap, top = 200, 64, 48, 140
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
        f'aria-label="Piyush Bhaskar, frontend engineer at Kestra">',
        f"<style>{STYLE}</style>",
        f'<text x="8" y="56" class="sans in" font-size="40" font-weight="600" fill="{t["text"]}" style="--t:0s">Piyush Bhaskar</text>',
        f'<text x="10" y="88" class="mono in" font-size="14" xml:space="preserve" fill="{t["muted"]}" style="--t:.1s">frontend engineer at '
        f'<tspan fill="{t["accent"]}">kestra-io</tspan>  ·  vue, typescript, design systems</text>',
    ]
    for i, (task, kind, icon) in enumerate(TASKS):
        x = 8 + i * (nw + gap)
        appear = 0.3 + i * 0.15
        done = 0.9 + i * 0.45
        out.append(f'<g class="in" style="--t:{appear:.2f}s">')
        out.append(f'<rect x="{x}" y="{top}" width="{nw}" height="{nh}" rx="8" fill="{t["surface"]}" stroke="{t["border"]}"/>')
        out.append(f'<g transform="translate({x + 14} {top + 14})"><rect width="36" height="36" rx="6" fill="{t["accent"]}" fill-opacity=".12"/>'
                   f'<g fill="none" stroke="{t["accent"]}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{icon}</g></g>')
        out.append(f'<text x="{x + 62}" y="{top + 29}" class="mono" font-size="14" font-weight="600" fill="{t["text"]}">{task}</text>')
        out.append(f'<text x="{x + 62}" y="{top + 48}" class="mono" font-size="11.5" fill="{t["muted"]}">{kind}</text>')
        out.append("</g>")
        if i < len(TASKS) - 1:
            out.append(f'<circle cx="{x + nw - 16}" cy="{top + 16}" r="4" fill="{t["ok"]}" class="in" style="--t:{done:.2f}s"/>')
            ex, ey = x + nw, top + nh / 2
            out.append(f'<path d="M{ex + 4} {ey}h{gap - 14}" stroke="{t["muted"]}" stroke-width="1.5" class="flow" style="--t:{appear:.2f}s"/>')
            out.append(f'<path d="M{ex + gap - 12} {ey - 4}l5 4-5 4" fill="none" stroke="{t["muted"]}" stroke-width="1.5" '
                       f'stroke-linecap="round" stroke-linejoin="round" class="in" style="--t:{appear:.2f}s"/>')
        else:
            out.append(f'<circle cx="{x + nw - 16}" cy="{top + 16}" r="4" fill="{t["accent"]}" class="pulse" style="--t:{done:.2f}s"/>')
    out.append(f'<text x="10" y="{top + nh + 28}" class="mono in" font-size="12" xml:space="preserve" fill="{t["muted"]}" style="--t:{0.9 + 3 * 0.45:.2f}s">'
               f'<tspan fill="{t["ok"]}">3 SUCCESS</tspan>  ·  <tspan fill="{t["accent"]}">1 RUNNING</tspan></text>')
    out.append("</svg>")
    return "\n".join(out)



# Shapes from Simple Icons (CC0), drawn on a 24x24 grid.
ICONS = {
    "Vue 3": ("#4FC08D", "M24,1.61H14.06L12,5.16,9.94,1.61H0L12,22.39ZM12,14.08,5.16,2.23H9.59L12,6.41l2.41-4.18h4.43Z"),
    "TypeScript": ("#3178C6", "M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z"),
    "Pinia": ("#E6B400", "M13.277.002c-.079-.01-.193.024-.31.09a2.346 2.346 0 0 0-.415.311c-.301.274-.65.68-.985 1.176-.672.99-1.31 2.356-1.485 3.785-.12.977-.154 1.849-.074 2.578a5.878 5.878 0 0 1 1.956-.338c.922 0 1.804.218 2.618.613.197-.637.34-1.395.445-2.246.175-1.429-.1-2.907-.499-4.028a6.695 6.695 0 0 0-.653-1.378 2.296 2.296 0 0 0-.321-.401c-.097-.092-.199-.153-.277-.162zm-6.81 2.965a.603.603 0 0 0-.288.117l-.013.011a.863.863 0 0 0-.177.327c-.051.15-.094.344-.126.565a8.205 8.205 0 0 0-.044 1.637c.08 1.222.397 2.665 1.079 3.769.093.15.193.296.294.442.726-.776 1.567-1.385 2.488-1.768-.1-.79-.06-1.714.066-2.744.038-.31.1-.616.176-.916a6.45 6.45 0 0 0-1.692-1.08 4.575 4.575 0 0 0-1.29-.366 1.805 1.805 0 0 0-.474.006zm11.751 1.789c-.21.003-.442.022-.687.06a5.974 5.974 0 0 0-2.132.76c-.009.146-.019.291-.036.437-.11.888-.258 1.684-.475 2.364.848.468 1.614 1.13 2.267 1.94.823-.85 1.43-2.05 1.787-3.13.187-.57.304-1.1.35-1.514.022-.207.027-.38.017-.51-.01-.133-.042-.206-.04-.202a.35.35 0 0 0-.114-.072 1.516 1.516 0 0 0-.375-.1 3.42 3.42 0 0 0-.562-.033zm-6.254 3.139c-2.014 0-3.83 1.087-5.147 2.834-1.316 1.748-2.131 4.16-2.131 6.807 0 2.65.806 4.258 2.131 5.218C8.132 23.707 9.96 24 11.964 24c2.004 0 3.831-.293 5.147-1.246 1.326-.96 2.133-2.568 2.133-5.218 0-2.647-.816-5.059-2.133-6.806-1.317-1.748-3.134-2.835-5.147-2.835Zm-3.297 5.209a1.282 1.282 0 0 1 .292 2.518c.115.094.177.201.164.307-.032.265-.521.424-1.09.354-.571-.07-1.007-.342-.974-.607.024-.198.302-.336.678-.364a1.282 1.282 0 0 1 .93-2.208zm6.284.22a1.282 1.282 0 0 1 .726 2.303c.437.058.757.244.757.466 0 .267-.466.483-1.04.483-.574 0-1.04-.216-1.04-.483 0-.098.063-.189.17-.265a1.282 1.282 0 0 1 .427-2.505zm-6.318.215a.822.822 0 1 0 .028 1.645.822.822 0 0 0-.028-1.645zm6.284.22a.822.822 0 1 0 .027 1.644.822.822 0 0 0-.027-1.644zm-6.543.109a.338.338 0 1 1-.023.677.338.338 0 0 1 .023-.677zm6.284.22a.339.339 0 1 1-.018 0h.018zm-3.91 1.179c.17.252.432.404.808.447.372.043.694-.05.976-.28a.145.145 0 1 1 .183.226c-.344.28-.745.394-1.192.343-.445-.051-.79-.24-1.016-.574a.145.145 0 1 1 .24-.162z"),
    "Vite": ("#9135FF", "M13.056 23.238a.57.57 0 0 1-1.02-.355v-5.202c0-.63-.512-1.143-1.144-1.143H5.148a.57.57 0 0 1-.464-.903l3.777-5.29c.54-.753 0-1.804-.93-1.804H.57a.574.574 0 0 1-.543-.746.6.6 0 0 1 .08-.157L5.008.78a.57.57 0 0 1 .467-.24h14.589a.57.57 0 0 1 .466.903l-3.778 5.29c-.54.755 0 1.806.93 1.806h5.745c.238 0 .424.138.513.322a.56.56 0 0 1-.063.603z"),
    "Vitest": ("#6E9F18", "M11.545 23.3a.613.613 0 0 1-.895.197L.252 15.936A.61.61 0 0 1 0 15.439V6.325c0-.502.569-.792.975-.497l6.358 4.624c.594.433 1.432.25 1.793-.39L14.393.7a.62.62 0 0 1 .535-.314h8.455a.613.613 0 0 1 .537.916z"),
    "Storybook": ("#FF4785", "M16.71.243l-.12 2.71a.18.18 0 00.29.15l1.06-.8.9.7a.18.18 0 00.28-.14l-.1-2.76 1.33-.1a1.2 1.2 0 011.279 1.2v21.596a1.2 1.2 0 01-1.26 1.2l-16.096-.72a1.2 1.2 0 01-1.15-1.16l-.75-19.797a1.2 1.2 0 011.13-1.27L16.7.222zM13.64 9.3c0 .47 3.16.24 3.59-.08 0-3.2-1.72-4.89-4.859-4.89-3.15 0-4.899 1.72-4.899 4.29 0 4.45 5.999 4.53 5.999 6.959 0 .7-.32 1.1-1.05 1.1-.96 0-1.35-.49-1.3-2.16 0-.36-3.649-.48-3.769 0-.27 4.03 2.23 5.2 5.099 5.2 2.79 0 4.969-1.49 4.969-4.18 0-4.77-6.099-4.64-6.099-6.999 0-.97.72-1.1 1.13-1.1.45 0 1.25.07 1.19 1.87z"),
    "Playwright": ("#2EAD33", "M23.996 7.462c-.056.837-.257 2.135-.716 3.85-.995 3.715-4.27 10.874-10.42 9.227-6.15-1.65-5.407-9.487-4.412-13.201.46-1.716.934-2.94 1.305-3.694.42-.853.846-.289 1.815.523.684.573 2.41 1.791 5.011 2.488 2.601.697 4.706.506 5.583.352 1.245-.219 1.897-.494 1.834.455Zm-9.807 3.863s-.127-1.819-1.773-2.286c-1.644-.467-2.613 1.04-2.613 1.04Zm4.058 4.539-7.769-2.172s.446 2.306 3.338 3.153c2.862.836 4.43-.98 4.43-.981Zm2.701-2.51s-.13-1.818-1.773-2.286c-1.644-.469-2.612 1.038-2.612 1.038ZM8.57 18.23c-4.749 1.279-7.261-4.224-8.021-7.08C.197 9.831.044 8.832.003 8.188c-.047-.73.455-.52 1.415-.354.677.118 2.3.261 4.308-.28a11.28 11.28 0 0 0 2.41-.956c-.058.197-.114.4-.17.61-.433 1.618-.827 4.055-.632 6.426-1.976.732-2.267 2.423-2.267 2.423l2.524-.715c.227 1.002.6 1.987 1.15 2.838a5.914 5.914 0 0 1-.171.049Zm-4.188-6.298c1.265-.333 1.363-1.631 1.363-1.631l-3.374.888s.745 1.076 2.01.743Z"),
    "Figma": ("#F24E1E", "M15.852 8.981h-4.588V0h4.588c2.476 0 4.49 2.014 4.49 4.49s-2.014 4.491-4.49 4.491zM12.735 7.51h3.117c1.665 0 3.019-1.355 3.019-3.019s-1.355-3.019-3.019-3.019h-3.117V7.51zm0 1.471H8.148c-2.476 0-4.49-2.014-4.49-4.49S5.672 0 8.148 0h4.588v8.981zm-4.587-7.51c-1.665 0-3.019 1.355-3.019 3.019s1.354 3.02 3.019 3.02h3.117V1.471H8.148zm4.587 15.019H8.148c-2.476 0-4.49-2.014-4.49-4.49s2.014-4.49 4.49-4.49h4.588v8.98zM8.148 8.981c-1.665 0-3.019 1.355-3.019 3.019s1.355 3.019 3.019 3.019h3.117V8.981H8.148zM8.172 24c-2.489 0-4.515-2.014-4.515-4.49s2.014-4.49 4.49-4.49h4.588v4.441c0 2.503-2.047 4.539-4.563 4.539zm-.024-7.51a3.023 3.023 0 0 0-3.019 3.019c0 1.665 1.365 3.019 3.044 3.019 1.705 0 3.093-1.376 3.093-3.068v-2.97H8.148zm7.704 0h-.098c-2.476 0-4.49-2.014-4.49-4.49s2.014-4.49 4.49-4.49h.098c2.476 0 4.49 2.014 4.49 4.49s-2.014 4.49-4.49 4.49zm-.097-7.509c-1.665 0-3.019 1.355-3.019 3.019s1.355 3.019 3.019 3.019h.098c1.665 0 3.019-1.355 3.019-3.019s-1.355-3.019-3.019-3.019h-.098z"),
}

TOOLS = [
    ("build", ["Vue 3", "TypeScript", "Pinia", "Element Plus", "Vite"]),
    ("test", ["Vitest", "Storybook", "Playwright"]),
    ("design", ["Figma", "Design tokens", "Light and dark themes"]),
]


def mark(t, name, x, y):
    if name not in ICONS:
        return f'<circle cx="{x + 7:.1f}" cy="{y + 7}" r="3.5" fill="{t["accent"]}"/>'
    color, d = ICONS[name]
    return f'<path transform="translate({x:.1f} {y}) scale({14 / 24:.4f})" fill="{color}" d="{d}"/>'


def tools(t):
    w, row, label = 960, 46, 96
    h = row * len(TOOLS) + 2
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
        f'aria-label="Tools: {", ".join(name for _, names in TOOLS for name in names)}">',
        f"<style>{STYLE}</style>",
    ]
    step = 0
    for r, (group, names) in enumerate(TOOLS):
        y = 1 + r * row
        out.append(f'<text x="10" y="{y + 23}" class="mono in" font-size="13" fill="{t["muted"]}" style="--t:{r * 0.12:.2f}s">{group}</text>')
        x = label
        for name in names:
            cw = len(name) * 13 * 0.602 + 46
            out.append(f'<g class="in" style="--t:{0.1 + step * 0.05:.2f}s">'
                       f'<rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="34" rx="8" fill="{t["surface"]}" stroke="{t["border"]}"/>'
                       f'{mark(t, name, x + 10, y + 10)}'
                       f'<text x="{x + 32:.1f}" y="{y + 21.5}" class="mono" font-size="13" fill="{t["text"]}">{name}</text></g>')
            x += cw + 10
            step += 1
    out.append("</svg>")
    return "\n".join(out)


for scheme, theme in THEMES.items():
    (OUT / f"hero-{scheme}.svg").write_text(hero(theme))
    (OUT / f"tools-{scheme}.svg").write_text(tools(theme))
