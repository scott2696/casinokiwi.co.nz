#!/usr/bin/env python3
"""Export every built page as clean Markdown into a deliverable folder."""
import os, re, html, json, shutil, glob

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(os.path.dirname(SITE), "content 1")

def unescape(t):
    t = html.unescape(t)
    return t.replace(" ", " ").replace("‑", "-")

def inline(s):
    """Inline HTML -> Markdown."""
    s = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', s, flags=re.S)
    s = re.sub(r'</?(strong|b)>', '**', s)
    s = re.sub(r'</?(em|i)>', '*', s)
    s = re.sub(r'<br\s*/?>', '  \n', s)
    s = re.sub(r'<span class="eng-ic".*?</span>', '', s, flags=re.S)
    s = re.sub(r'<svg.*?</svg>', '', s, flags=re.S)
    s = re.sub(r'<[^>]+>', '', s)
    return unescape(re.sub(r'[ \t]+', ' ', s)).strip()

def table_md(block):
    rows = []
    for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', block, re.S):
        cells = [inline(c) for c in re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', tr, re.S)]
        if cells: rows.append(cells)
    if not rows: return ""
    w = max(len(r) for r in rows)
    rows = [r + [""] * (w - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * w]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    cap = re.search(r'<caption>(.*?)</caption>', block, re.S)
    if cap: out.append(f"\n*{inline(cap.group(1))}*")
    return "\n".join(out)

def to_markdown(path):
    h = open(path).read()
    title = inline(re.search(r'<title>(.*?)</title>', h, re.S).group(1))
    desc  = re.search(r'<meta name="description" content="([^"]*)"', h).group(1)
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', h).group(1)
    h1m   = re.search(r'<h1>(.*?)</h1>', h, re.S)
    h1    = inline(h1m.group(1)) if h1m else ""
    by    = re.search(r'By <a class="by-link"[^>]*><b>(.*?)</b></a>, ([^<]+)', h, re.S)
    byline = f"{inline(by.group(1))}, {unescape(by.group(2))}" if by else "The CasinoKiwi Team"

    body = h.split('</header>', 1)[1].split('<footer', 1)[0]
    body = re.sub(r'<section class="hero">.*?</section>', '', body, flags=re.S)

    out = []
    # leaderboard first, if present
    for li in re.findall(r'<li class="lb-row.*?</li>', body, re.S):
        name = re.search(r'class="lb-name">(.*?)<span', li, re.S)
        sub  = re.search(r'class="lb-sub">(.*?)</span>', li, re.S)
        rate = re.search(r'<b>([\d.]+)/10</b>', li)
        off  = re.search(r'class="lb-bonus-v">(.*?)</span>', li, re.S)
        terms= re.search(r'class="lb-min">(.*?)</span>', li, re.S)
        href = re.search(r'class="eng-btn" href="([^"]+)"', li)
        if name:
            out.append(f"- **{inline(name.group(1))}** — {inline(sub.group(1)) if sub else ''}  \n"
                       f"  Rating: {rate.group(1) if rate else '—'}/10 · Offer: {inline(off.group(1)) if off else '—'}  \n"
                       f"  {inline(terms.group(1)) if terms else ''} · Link: {html.unescape(href.group(1)) if href else '—'}")
    if out:
        out = ["## Ranked operators\n"] + out + [""]

    body = re.sub(r'<ol class="lb-rows">.*?</ol>', '', body, flags=re.S)

    TOKEN = re.compile(
        r'<h([234])[^>]*>(.*?)</h\1>'
        r'|<p[^>]*>(.*?)</p>'
        r'|<(ul|ol)[^>]*>(.*?)</\4>'
        r'|<table[^>]*>(.*?)</table>'
        r'|<div class="cal cal--(\w+)">(.*?)</div>\s*</div>'
        r'|<details class="faq"[^>]*>\s*<summary>(.*?)</summary>\s*<div class="faq-a">(.*?)</div>',
        re.S)
    for m in TOKEN.finditer(body):
        if m.group(1):
            out.append("\n" + "#" * int(m.group(1)) + " " + inline(m.group(2)) + "\n")
        elif m.group(3) is not None:
            t = inline(m.group(3))
            if t: out.append(t + "\n")
        elif m.group(4):
            items = re.findall(r'<li[^>]*>(.*?)</li>', m.group(5), re.S)
            mark = "- " if m.group(4) == "ul" else None
            for i, it in enumerate(items, 1):
                t = inline(it)
                if t: out.append((mark or f"{i}. ") + t)
            out.append("")
        elif m.group(6):
            md = table_md("<table>" + m.group(6) + "</table>")
            if md: out.append(md + "\n")
        elif m.group(7):
            label = {"warn": "⚠️", "info": "ℹ️", "good": "✅", "gold": "★"}.get(m.group(7), "")
            out.append(f"> {label} {inline(m.group(8))}\n")
        elif m.group(9):
            out.append(f"**Q: {inline(m.group(9))}**\n\n{inline(m.group(10))}\n")

    md = "\n".join(out)
    md = re.sub(r'\n{3,}', '\n\n', md).strip()
    words = len(re.findall(r"[A-Za-z][A-Za-z'-]+", md))
    fm = (f"---\nurl: {canon}\ntitle: \"{title}\"\nmeta_description: \"{unescape(desc)}\"\n"
          f"h1: \"{h1}\"\nauthor: \"{byline}\"\nwords: {words}\n---\n\n# {h1 or title}\n\n")
    return fm + md + "\n", words

# ---------------------------------------------------------------- build folder
if os.path.exists(OUT): shutil.rmtree(OUT)
for d in ("pages", "site", "research", "data"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)

index = []
for f in sorted(glob.glob(os.path.join(SITE, "**", "index.html"), recursive=True)):
    url = "/" + os.path.relpath(f, SITE).replace("index.html", "")
    slug = url.strip("/").replace("/", "--") or "home"
    md, words = to_markdown(f)
    open(os.path.join(OUT, "pages", f"{slug}.md"), "w").write(md)
    index.append((url, slug, words))

# full built site, research and data
for item in os.listdir(SITE):
    if item.startswith("_") or item in ("research",): continue
    src = os.path.join(SITE, item); dst = os.path.join(OUT, "site", item)
    shutil.copytree(src, dst) if os.path.isdir(src) else shutil.copy2(src, dst)
for f in glob.glob(os.path.join(SITE, "research", "*")):
    shutil.copy2(f, os.path.join(OUT, "research", os.path.basename(f)))
shutil.copy2(os.path.join(SITE, "_build", "operators.json"), os.path.join(OUT, "data", "operators.json"))

index.sort(key=lambda r: -r[2])
total = sum(r[2] for r in index)
readme = [
 "# CasinoKiwi — content pack 1",
 "",
 f"Full written content for **casinokiwi.co.nz**. {len(index)} pages · **{total:,} words** · exported 1 September 2026.",
 "",
 "## What is in here",
 "",
 "| Folder | Contents |",
 "|---|---|",
 "| `pages/` | Every page as Markdown with front matter (URL, title, meta description, H1, author, word count). Portable into any CMS. |",
 "| `site/` | The built static site exactly as it deploys — clean URLs, schema, sitemap, robots.txt, favicons, logos. |",
 "| `research/` | SERP gap analysis: competitor heading outlines from the NZ and AU SERPs, uncontested opportunities, keyword variations. |",
 "| `data/` | `operators.json` — the single source of truth for all 16 operators: affiliate links, bonuses, licences, logos, ratings. |",
 "",
 "## Pages by size",
 "",
 "| Words | URL | File |",
 "|---:|---|---|",
]
for url, slug, w in index:
    readme.append(f"| {w:,} | `{url}` | `pages/{slug}.md` |")
readme += [
 "",
 "## Rebuilding",
 "",
 "The site is generated, not hand-edited. From the `casinokiwi.co.nz` working directory:",
 "",
 "```",
 "python3 _build/gen_reviews.py   # regenerate the 16 operator reviews",
 "python3 _build/gen_hub.py       # regenerate the reviews hub",
 "python3 _build/build.py         # build all pages + sitemap.xml + robots.txt",
 "```",
 "",
 "Changing an operator's affiliate link, bonus or logo is one edit in `data/operators.json` plus a rebuild — it propagates to every page.",
 "",
 "## Before you publish",
 "",
 "Section 10 of the Online Casino Gambling Act prohibits advertising unlicensed online casino gambling to New Zealanders, and from 1 December 2026 unlicensed provision carries penalties up to NZ$5m. Every operator in `operators.json` is licensed offshore (Curaçao, Anjouan, Tobique), not by the DIA. Get a New Zealand gambling lawyer to review this before pointing a live domain at it.",
]
open(os.path.join(OUT, "README.md"), "w").write("\n".join(readme) + "\n")
print(f"exported {len(index)} pages · {total:,} words -> {OUT}")
