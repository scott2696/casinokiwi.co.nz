#!/usr/bin/env python3
"""CasinoKiwi NZ builder — emits the Better Choice template structure.

Reads _build/pages/*.html fragments (JSON front matter in <!--@ ... @-->) and
writes clean-URL pages at {url}index.html using the template's exact markup:
.nav / .hero + .hero-by / #leaderboard .lb / .sec > .wrap > .prose / .foot.
"""
import json, os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_build", "pages")
DOMAIN = "https://casinokiwi.co.nz"
SITE = "CasinoKiwi"
BRAND_WORD = "CASINO&nbsp;KIWI"
TAGLINE = "NZ Casino &amp; Pokies Guide"
UPDATED = "2026-09-01"
UPDATED_HUMAN = "01/09/2026"

OPS = json.load(open(os.path.join(ROOT, "_build", "operators.json")))

AUTHORS = {
 "rawiri": dict(name="Rawiri Kingi", slug="rawiri-kingi", initials="RK",
   role="Lead Casino Reviewer",
   photo="/images/authors/rawiri-kingi.jpg",
   knows=["online casinos","pokies","NZD payments","withdrawal testing","cryptocurrency gambling","sports betting"],
   bio="Rawiri spent five years as a payments analyst for a licensed operator before moving to the other side of the cashier. He opens every account on this site himself, deposits his own New Zealand dollars, and times each withdrawal from an Auckland connection."),
 "maia": dict(name="Maia Williams", slug="maia-williams", initials="MW",
   role="Editor, Bonuses &amp; Regulation",
   photo="/images/authors/maia-williams.jpg",
   knows=["gambling law","New Zealand regulation","Online Casino Gambling Act","bonus terms and conditions","gambling taxation","responsible gambling"],
   bio="Maia read law at Victoria University of Wellington and reported on regulation before joining us. She reads the full terms on every offer we publish, tracks the Department of Internal Affairs licensing programme week by week, and fact-checks every legal and tax claim on this site."),
 "team": dict(name="The CasinoKiwi Team", slug="editorial-team", initials="CK",
   role="Editorial Team",
   photo="/images/authors/rawiri-kingi.jpg",
   knows=["online casinos","New Zealand gambling"],
   bio="Our editorial team is based in New Zealand and tests every site we write about with real money in New Zealand dollars."),
}

NAV = [
 ("Home", "/", None),
 ("Online Casinos", "/", [
   ("Online Pokies", "/online-pokies/"),
   ("High Payout Casinos", "/high-payout-casinos/"),
   ("Fast Payout Casinos", "/fast-payout-casinos/"),
   ("Live Dealer Casinos", "/live-casinos/"),
   ("Crypto Casinos", "/best-crypto-casinos/"),
   ("Casino Bonuses", "/online-casinos/bonuses/"),
   ("No Deposit Bonuses", "/no-deposit-casinos/"),
   ("Casino Reviews", "/casino-reviews/"),
 ]),
 ("Sports Betting", "/best-sports-betting-sites/", [
   ("Best Sports Betting Sites", "/best-sports-betting-sites/"),
   ("Online Betting NZ", "/online-betting/"),
 ]),
 ("Guides", None, [
   ("NZ Online Casino Law", "/nz-online-casino-law/"),
   ("Tax on Gambling Winnings", "/gambling-winnings-tax-nz/"),
   ("NZ Payment Methods", "/payment-methods/"),
   ("How We Review", "/how-we-review/"),
 ]),
 ("About", "/about/", None),
 ("Contact", "/contact/", None),
]

FOOTER = [
 ("Casinos", [("Online Pokies","/online-pokies/"),("High Payout Casinos","/high-payout-casinos/"),
   ("Fast Payout Casinos","/fast-payout-casinos/"),("Live Dealer Casinos","/live-casinos/"),
   ("Crypto Casinos","/best-crypto-casinos/"),("Casino Bonuses","/online-casinos/bonuses/"),
   ("No Deposit Casinos","/no-deposit-casinos/"),("Casino Reviews","/casino-reviews/")]),
 ("Betting &amp; Guides", [("Best Sports Betting Sites","/best-sports-betting-sites/"),
   ("Online Betting NZ","/online-betting/"),("NZ Online Casino Law","/nz-online-casino-law/"),
   ("Tax on Gambling Winnings","/gambling-winnings-tax-nz/"),("NZ Payment Methods","/payment-methods/")]),
 ("Company", [("About &amp; Methodology","/about/"),("Contact","/contact/"),("Our Authors","/authors/"),
   ("How We Review","/how-we-review/"),("Terms","/terms/"),("Privacy","/privacy/"),
   ("Cookie Policy","/cookie-policy/"),("Responsible Gambling","/responsible-gambling/")]),
]

# ---------------------------------------------------------------- icons
IC = {
 "star": '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9 6.8 19.2l1-5.8L3.5 9.2l5.9-.9z"/>',
 "bolt": '<path d="M13 2 3 14h7l-1 8 10-12h-7z"/>',
 "warn": '<path d="M10.3 3.6 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.6a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
 "info": '<circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v4h1"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
}
def ic(k):
    return ('<span class="eng-ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{IC[k]}</svg></span>')

MISSING = set()
def aff(slug, kind="casino"):
    op = OPS[slug]
    url = op["sportsLink"] if kind == "sports" else op["casinoLink"]
    url = url or op["casinoLink"] or op["sportsLink"]
    if not url:
        MISSING.add(op["name"]); return "/casino-reviews/"
    return url

def resolve_tokens(s):
    s = re.sub(r"\{\{(aff|affs):([a-z0-9\-]+)\}\}",
               lambda m: html.escape(aff(m.group(2), "sports" if m.group(1)=="affs" else "casino"), quote=True), s)
    s = re.sub(r"\{\{op:([a-z0-9\-]+):([A-Za-z]+)\}\}", lambda m: html.escape(str(OPS[m.group(1)].get(m.group(2),""))), s)
    return s

# ---------------------------------------------------------------- chrome
def nav_html():
    out = ['<header class="nav"><div class="wrap">',
      f'<a class="eng-logo" href="/" aria-label="{SITE} — {TAGLINE}"><span class="eng-lockup">'
      f'<span class="eng-word">{BRAND_WORD}</span>'
      '<svg class="eng-mark" viewBox="0 0 70 40" aria-hidden="true">'
      '<path d="M5 7 L21 20 L5 33" fill="none" stroke="var(--gold)" stroke-width="7.5" stroke-linecap="round" stroke-linejoin="round"></path>'
      '<path d="M22 7 L38 20 L22 33" fill="none" stroke="var(--gold)" stroke-width="7.5" stroke-linecap="round" stroke-linejoin="round"></path>'
      '<path d="M40 5 L66 20 L40 35 Z" fill="var(--slate)"></path></svg></span>'
      f'<span class="eng-tag">{TAGLINE}</span></a>',
      '<nav class="nav-links">']
    caret = ('<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
             '<path d="M3 4.5l3 3 3-3"></path></svg>')
    for label, href, kids in NAV:
        if not kids:
            out.append(f'<a href="{href}">{label}</a>')
        else:
            trig = (f'<a class="nav-trigger" href="{href}">{label} {caret}</a>' if href
                    else f'<span class="nav-trigger" tabindex="0">{label} {caret}</span>')
            links = "".join(f'<a href="{h}">{l}</a>' for l, h in kids)
            out.append(f'<div class="nav-item">{trig}<div class="nav-dd"><div class="nav-dd-inner">{links}</div></div></div>')
    out.append('</nav>')
    out.append('<details class="menu"><summary aria-label="Open menu"><svg viewBox="0 0 24 24" width="22" height="22" '
      'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"></path>'
      '</svg></summary><div class="menu-panel">')
    for label, href, kids in NAV:
        if kids:
            out.append(f'<b>{label}</b>')
            out += [f'<a href="{h}">{l}</a>' for l, h in kids]
        else:
            out.append(f'<a href="{href}">{label}</a>')
    out.append('<b>Company</b><a href="/about/">About</a><a href="/contact/">Contact</a>'
               '<a href="/responsible-gambling/">Responsible Gambling</a>')
    out.append('</div></details></div></header>')
    return "".join(out)


def hero_html(fm, lede):
    a = AUTHORS[fm.get("author", "team")]
    crumbs = ""
    if fm.get("crumbs"):
        parts = ['<a href="/">Home</a>']
        for i, (n, h) in enumerate(fm["crumbs"]):
            parts.append('<span>&rsaquo;</span>')
            parts.append(n if i == len(fm["crumbs"]) - 1 else f'<a href="{h}">{n}</a>')
        crumbs = f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'
    facts = ""
    if fm.get("facts"):
        facts = '<div class="hero-facts">' + "".join(
            f'<span class="hero-fact">{f}</span>' for f in fm["facts"]) + '</div>'
    return f'''<section class="hero"><div class="wrap">
{crumbs}<h1>{fm["h1"]}</h1>
<div class="hero-by">
<a href="/authors/" aria-label="{a['name']}, author"><img src="{a['photo']}" srcset="{a['photo']} 1x, {a['photo'].replace('.jpg','@2x.jpg')} 2x" alt="{a['name']}" width="42" height="42" loading="eager"></a>
<div class="hero-by-txt">
<span>By <a class="by-link" href="/authors/"><b>{a['name']}</b></a>, {a['role']}</span>
<span class="eng-mono hero-by-date">{ic("clock")} Updated {UPDATED_HUMAN}</span>
</div></div>
<p class="lede">{lede}</p>{facts}
</div></section>'''


def foot_html():
    cols = ""
    for title, links in FOOTER:
        items = "".join(f'<a href="{h}">{l}</a>' for l, h in links)
        cols += f'<div class="foot-col"><b>{title}</b>{items}</div>'
    return f'''<footer class="foot"><div class="wrap">
<div class="foot-top">
<div><a class="eng-logo" href="/" aria-label="{SITE}"><span class="eng-lockup"><span class="eng-word">{BRAND_WORD}</span>
<svg class="eng-mark" viewBox="0 0 70 40" aria-hidden="true">
<path d="M5 7 L21 20 L5 33" fill="none" stroke="var(--gold)" stroke-width="7.5" stroke-linecap="round" stroke-linejoin="round"></path>
<path d="M22 7 L38 20 L22 33" fill="none" stroke="var(--gold)" stroke-width="7.5" stroke-linecap="round" stroke-linejoin="round"></path>
<path d="M40 5 L66 20 L40 35 Z" fill="#fff"></path></svg></span>
<span class="eng-tag">{TAGLINE}</span></a>
<p style="margin:.7em 0 0;max-width:44ch;color:#9FB0D4">New Zealand's independent guide to online casinos, pokies and betting sites. We test with real NZD deposits and timed withdrawals so you don't have to.</p></div>
<div class="foot-cols">{cols}</div>
</div>
<div class="foot-rg"><strong>18+. Gamble responsibly.</strong> Online casinos serving New Zealanders are licensed offshore (Cura&ccedil;ao, Anjouan, Tobique and the like). The Department of Internal Affairs is issuing up to 15 New Zealand online casino licences, and a prohibition on advertising unlicensed online casino gambling has commenced under section 10 of the Online Casino Gambling Act. Sports and racing betting is separate: TAB NZ and Betcha hold the only legal right to take New Zealand bets. Gambling carries real risk. Free, confidential help: <strong>Gambling Helpline NZ 0800 654 655</strong> (free text 8006), 24/7, the <strong>Problem Gambling Foundation on 0800 664 262</strong>, or <strong>Need to Talk 1737</strong>. Affiliate links never affect our tested rankings.</div>
</div></footer>'''


# ---------------------------------------------------------------- transformer
def slug_from(url):
    return url.strip("/").split("/")[-1]

def stars_row(rating):
    return f'{ic("star")}<b>{rating}/10</b>'

def op_logo(slug, sports=False):
    """Logo path for an operator. README: dark artwork on a white tile;
    IviBet has a separate sportsbook mark for betting pages."""
    op = OPS.get(slug) or {}
    if sports and op.get("logoSports"):
        return op["logoSports"]
    return op.get("logo") or f"/images/casino-logos/{slug}.png"


def build_leaderboard(toplist_html, heading, sports=False, intro=""):
    """Convert an authored .toplist block into the template's .lb leaderboard."""
    rows = re.findall(r'<article class="op-card([^"]*)">(.*?)</article>', toplist_html, re.S)
    if not rows:
        return "", ""
    lis = []
    for i, (cls, inner) in enumerate(rows, 1):
        feat = " lb-row--feat" if "is-top" in cls else ""
        badge = re.search(r'<span class="op-badge">(.*?)</span>', inner, re.S)
        name_m = re.search(r'<span class="op-name"><a href="([^"]+)">(.*?)</a></span>', inner, re.S)
        meta_m = re.search(r'<p class="op-meta">(.*?)</p>', inner, re.S)
        main_m = re.search(r'<p class="o-main">(.*?)</p>', inner, re.S)
        sub_m  = re.search(r'<p class="o-sub">(.*?)</p>', inner, re.S)
        num_m  = re.search(r'<span class="num">([\d.]+)</span>', inner, re.S)
        cta_m  = re.search(r'<a class="btn[^"]*" href="([^"]+)"[^>]*>(.*?)</a>', inner, re.S)
        if not (name_m and cta_m):
            continue
        rev_url, name = name_m.group(1), name_m.group(2)
        sub = meta_m.group(1) if meta_m else ""
        offer = main_m.group(1) if main_m else ""
        terms = sub_m.group(1) if sub_m else "18+ &middot; T&amp;Cs apply"
        rating10 = round(float(num_m.group(1)) * 2, 1) if num_m else 8.0
        href = cta_m.group(1)
        logo = op_logo(slug_from(rev_url), sports)
        fast = f'<span class="lb-fast">{ic("bolt")}{badge.group(1)}</span>' if badge else ""
        lis.append(f'''<li class="lb-row{feat}">
<a class="lb-cover" href="{href}" rel="nofollow sponsored noopener" target="_blank" aria-label="Visit {re.sub(r'<[^>]+>','',name)}"></a>
<span class="lb-rank">{i}</span>
<div class="lb-brand"><img class="lb-logo" src="{logo}" alt="{re.sub(r'<[^>]+>','',name)} logo" loading="lazy" width="96" height="48"><div class="lb-name">{name}<span class="lb-sub">{sub}</span></div></div>
<div class="lb-speed"><div class="lb-payout">{stars_row(rating10)}{fast}</div><div class="lb-bar"><span class="lb-bar-fill" style="width:{min(99,int(rating10*10))}%"></span></div></div>
<div class="lb-bonus"><span class="lb-bonus-l">Welcome offer</span><span class="lb-bonus-v">{offer}</span></div>
<div class="lb-cta"><a class="eng-btn" href="{href}" rel="nofollow sponsored noopener" target="_blank">Get bonus</a><span class="lb-min">{terms}</span></div>
</li>''')
    if not lis:
        return "", ""
    intro_html = f'<p class="lb-intro">{intro}</p>' if intro else ""
    sec = f'''<section id="leaderboard" class="sec sec--white"><div class="wrap">
<div class="sec-head sec--lead"><h2>{heading}</h2>{intro_html}</div>
<div class="lb">
<div class="lb-head" aria-hidden="true"><span>#</span><span>Casino</span><span>Our rating</span><span>Welcome offer</span><span></span></div>
<ol class="lb-rows">{"".join(lis)}</ol>
</div>
<div style="max-width:820px;margin:22px auto 0">
<p>The leaderboard sorts our verdict &mdash; number one scored highest across payout speed, game range, bonus value and cashier reliability, and the scores step down from there. The full scoring weights are on our <a href="/how-we-review/">review methodology</a> page.</p>
</div></div></section>'''

    # The licensing disclaimer is returned separately so the page can close on it.
    notice = f'''<section class="sec sec--alt" id="licensing-notice"><div class="wrap"><div class="prose">
<div class="cal cal--warn">{ic("warn")}<div><b>One thing to know up front</b>No operator on this list holds a New Zealand licence yet. The Department of Internal Affairs is issuing up to 15 online casino licences and a prohibition on advertising unlicensed online casino gambling has already commenced under section 10 of the Online Casino Gambling Act. Playing at an offshore casino has never been an offence for a New Zealand resident &mdash; but your recourse runs through a foreign regulator, which is why our tested payout data matters.</div></div>
</div></div></section>'''
    return sec, notice


def transform(body, review_slug=None):
    """Map authored content markup onto the template's classes."""
    # answer box -> cal--info
    body = re.sub(r'<div class="answer">\s*<span class="label">(.*?)</span>\s*(.*?)</div>',
        lambda m: f'<div class="cal cal--info">{ic("info")}<div><b>{m.group(1)}</b>{m.group(2)}</div></div>',
        body, flags=re.S)
    # callouts -> cal
    CAL = {"tip":"good","warn":"warn","note":"gold","law":"info"}
    ICO = {"tip":"check","warn":"warn","note":"info","law":"info"}
    body = re.sub(r'<div class="callout (tip|warn|note|law)"[^>]*>\s*<span class="t">(.*?)</span>\s*(.*?)</div>',
        lambda m: f'<div class="cal cal--{CAL[m.group(1)]}">{ic(ICO[m.group(1)])}<div><b>{m.group(2)}</b>{m.group(3)}</div></div>',
        body, flags=re.S)
    # tables -> fig / t-scroll / table.t
    def tbl(m):
        inner = m.group(1)
        cap = re.search(r'<caption>(.*?)</caption>', inner, re.S)
        capd = f'<figcaption>{cap.group(1)}</figcaption>' if cap else ""
        inner = re.sub(r'<caption>.*?</caption>', '', inner, flags=re.S)
        inner = inner.replace('<table class="data">', '<table class="t">')
        return f'<figure class="fig">{capd}<div class="t-scroll">{inner}</div></figure>'
    body = re.sub(r'<div class="table-scroll">(.*?)</div>', tbl, body, flags=re.S)
    # FAQ -> faqs / details.faq / faq-a
    body = body.replace('<div class="faq">', '<div class="faqs">')
    body = re.sub(r'<details( open)?><summary>', lambda m: f'<details class="faq"{m.group(1) or ""}><summary>', body)
    body = body.replace('<div class="a">', '<div class="faq-a">')
    # reviews -> rev
    def rev(m):
        rid, inner = m.group(1), m.group(2)
        h = re.search(r'<div class="review-head">\s*<span class="op-logo"[^>]*>(.*?)</span>\s*'
                      r'<div><h3>(.*?)</h3><p class="rk">(.*?)</p></div>\s*'
                      r'<span class="score-pill">([\d.]+)</span>\s*</div>', inner, re.S)
        rest = re.sub(r'<div class="review-head">.*?</div>\s*<span class="score-pill">[\d.]+</span>\s*</div>', '', inner, flags=re.S)
        if h:
            rest = inner[h.end():]
            title, meta, score = h.group(2), h.group(3), round(float(h.group(4))*2, 1)
            rank = re.match(r'\s*(\d+)\.', title)
            rankb = f'<span class="rev-rank">#{rank.group(1)}</span>' if rank else ""
            title = re.sub(r'^\s*\d+\.\s*', '', title)
            logo = (f'<img class="lb-logo" src="{op_logo(rid)}" alt="{re.sub(chr(60)+"[^"+chr(62)+"]*"+chr(62),"",title)} logo" '
                    f'loading="lazy" width="96" height="48">') if rid in OPS else ""
            cta = re.search(r'<a class="btn btn-gold" href="([^"]+)"[^>]*>(.*?)</a>', rest, re.S)
            ctab = (f'<a class="eng-btn rev-cta-btn" href="{cta.group(1)}" rel="nofollow sponsored noopener" target="_blank">Get bonus</a>'
                    if cta else "")
            head = (f'<div class="rev-head">{rankb}{logo}<div class="rev-h"><h3>{title}</h3>'
                    f'<span class="rev-meta">{meta} &middot; {ic("star")} {score}/10</span></div>{ctab}</div>')
            return f'<article class="rev" id="{rid}">{head}<div class="rev-body">{rest}</div></article>'
        return f'<article class="rev" id="{rid}"><div class="rev-body">{inner}</div></article>'
    body = re.sub(r'<article class="review" id="([^"]+)">(.*?)</article>', rev, body, flags=re.S)
    body = re.sub(r'<article class="review">(.*?)</article>',
                  lambda m: f'<article class="rev"><div class="rev-body">{m.group(1)}</div></article>', body, flags=re.S)
    # standalone review-head -> rev-head
    def head_std(m):
        ini, title, rk, score = m.group(1), m.group(2), m.group(3), float(m.group(4))
        mark = (f'<img class="lb-logo" src="{op_logo(review_slug)}" alt="{review_slug} logo" '
                f'loading="lazy" width="96" height="48">') if review_slug in OPS else f'<span class="rev-logo">{ini}</span>'
        return (f'<div class="rev-head">{mark}'
                f'<div class="rev-h"><h2 style="margin:0;font-size:1.3rem">{title}</h2>'
                f'<span class="rev-meta">{rk}</span></div>'
                f'<span class="rev-score">{ic("star")} {round(score*2,1)}/10</span></div>')
    body = re.sub(r'<div class="review-head"[^>]*>\s*<span class="op-logo"[^>]*>(.*?)</span>\s*'
                  r'<div><h[23][^>]*>(.*?)</h[23]><p class="rk">(.*?)</p></div>\s*'
                  r'<span class="score-pill">([\d.]+)</span>\s*</div>', head_std, body, flags=re.S)
    body = re.sub(r'<div class="review-head"[^>]*>\s*<span class="op-logo"[^>]*>(.*?)</span>\s*'
                  r'<div><h([23])[^>]*>(.*?)</h[23]><p class="rk">(.*?)</p></div>\s*</div>',
                  lambda m: (f'<div class="rev-head"><span class="rev-logo">{m.group(1)}</span>'
                             f'<div class="rev-h"><h{m.group(2)} style="margin:0;font-size:1.25rem">{m.group(3)}</h{m.group(2)}>'
                             f'<span class="rev-meta">{m.group(4)}</span></div></div>'), body, flags=re.S)
    # pros/cons -> rev-pc
    body = body.replace('<div class="pros-cons">', '<div class="rev-pc">')
    body = body.replace('<div class="pros">', '<div class="rev-pros">')
    body = body.replace('<div class="cons">', '<div class="rev-cons">')
    # spec grid
    body = body.replace('<div class="spec-grid">', '<div class="specs">')
    # verdict paragraph
    body = body.replace('<p><strong>Verdict:</strong>', '<p class="rev-for"><b>Verdict:</b>')
    # card grids -> linkrow
    def linkrow(m):
        links = re.findall(r'<a class="card link-card" href="([^"]+)"><h3>(.*?)</h3>', m.group(1), re.S)
        if links:
            return '<div class="linkrow">' + "".join(f'<a href="{h}">{t}</a>' for h, t in links) + '</div>'
        return m.group(0)
    body = re.sub(r'<div class="grid grid-\d">(.*?)</div>\s*(?=<|$)', linkrow, body, flags=re.S)
    # feature cards -> checklist
    def cards(m):
        items = re.findall(r'<div class="card"><div class="ico">(?:.*?)</div><h3>(.*?)</h3>(.*?)</div>', m.group(0), re.S)
        if not items:
            return m.group(0)
        lis = "".join(f'<li>{ic("check")}<div><strong>{t}</strong>{b}</div></li>' for t, b in items)
        return f'<ul class="checklist">{lis}</ul>'
    body = re.sub(r'<div class="grid grid-2"[^>]*>(?:\s*<div class="card">.*?</div>\s*)+</div>', cards, body, flags=re.S)
    # cta band -> brief
    body = re.sub(r'<div class="cta-band">\s*<div><h3>(.*?)</h3><p>(.*?)</p></div>\s*<a class="btn btn-gold" href="([^"]+)"([^>]*)>(.*?)</a>\s*</div>',
        lambda m: (f'<div class="method"><div class="method-ic">{ic("star")}</div><div><span class="lab">{m.group(1)}</span>'
                   f'<p>{m.group(2)}</p><p style="margin-top:12px"><a class="eng-btn" href="{m.group(3)}"{m.group(4)}>{m.group(5)}</a></p></div></div>'),
        body, flags=re.S)
    # remaining buttons
    body = re.sub(r'class="btn btn-ghost[^"]*"', 'class="eng-btn eng-btn--ghost"', body)
    body = re.sub(r'class="btn btn-[a-z]+(?: btn-[a-z]+)*"', 'class="eng-btn"', body)
    # ordered "how to" lists inside sections stay as-is; fine text
    body = body.replace('<p class="fine">', '<p style="font-size:13px;color:var(--mut)">')
    body = body.replace('<span class="fine">', '<span style="font-size:12.5px;color:var(--mut)">')
    body = body.replace('<p class="lede">', '<p>')
    return body


SEC_OPEN  = '<section class="section"><div class="wrap">'
SECA_OPEN = '<section class="section section-alt"><div class="wrap">'
SEC_CLOSE = '</div></section>'

def split_fragment(raw):
    """Strip authored hero/trust-bar, capture h1 + lede, and unwrap section shells."""
    lede = h1 = ""
    m = re.search(r'<p class="hero-lede">(.*?)</p>', raw, re.S)
    if m:
        lede = m.group(1).strip()
    m = re.search(r'<section class="hero">.*?<h1>(.*?)</h1>', raw, re.S)
    if m:
        h1 = m.group(1).strip()
    raw = re.sub(r'<section class="hero">.*?</section>\s*', '', raw, flags=re.S)
    raw = re.sub(r'<div class="trust-bar">.*?</ul></div></div>\s*', '', raw, flags=re.S)
    raw = raw.replace(SECA_OPEN, "\x00ALT\x00").replace(SEC_OPEN, "\x00SEC\x00")
    raw = raw.replace(SEC_CLOSE, "\x00END\x00")
    n_open = raw.count("\x00ALT\x00") + raw.count("\x00SEC\x00")
    n_close = raw.count("\x00END\x00")
    assert n_open == n_close, f"section open/close mismatch: {n_open} vs {n_close}"
    raw = raw.replace("\x00ALT\x00", '<section class="sec sec--alt"><div class="wrap"><div class="prose">')
    raw = raw.replace("\x00SEC\x00", '<section class="sec"><div class="wrap"><div class="prose">')
    raw = raw.replace("\x00END\x00", '</div></div></section>')
    return h1, lede, raw


# ---------------------------------------------------------------- schema
def strip_tags(s):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s))).strip()

def extract_faq(body):
    out = []
    for m in re.finditer(r'<details class="faq"[^>]*>\s*<summary>(.*?)</summary>\s*<div class="faq-a">(.*?)</div>\s*</details>',
                         body, re.S):
        q, a = strip_tags(m.group(1)), strip_tags(m.group(2))
        if q and a:
            out.append({"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}})
    return out

def schema_blocks(fm, body, url):
    a = AUTHORS[fm.get("author","team")]
    org_site = {"@context":"https://schema.org","@graph":[
      {"@type":"Organization","@id":f"{DOMAIN}/#organization","name":SITE,"url":DOMAIN,
       "logo":{"@type":"ImageObject","url":f"{DOMAIN}/images/logo.png","width":400,"height":120},
       "areaServed":{"@type":"Country","name":"New Zealand"},"email":"editor@casinokiwi.co.nz","sameAs":[]},
      {"@type":"WebSite","@id":f"{DOMAIN}/#website","name":SITE,"url":DOMAIN,
       "publisher":{"@id":f"{DOMAIN}/#organization"},"inLanguage":"en-NZ",
       "potentialAction":{"@type":"SearchAction","target":f"{DOMAIN}/?s={{search_term_string}}",
                          "query-input":"required name=search_term_string"}}]}
    g = [{"@type":"Person","@id":f"{DOMAIN}/#author-{a['slug']}","name":a["name"],
          "url":f"{DOMAIN}/authors/","jobTitle":html.unescape(a["role"]),
          "worksFor":{"@id":f"{DOMAIN}/#organization"},"knowsAbout":a["knows"]},
         {"@type":["WebPage","CollectionPage"] if fm.get("itemlist") else "WebPage",
          "@id":url+"#webpage","url":url,"name":fm["title"],"description":fm["description"],
          "inLanguage":"en-NZ","isPartOf":{"@id":f"{DOMAIN}/#website"},
          "author":{"@id":f"{DOMAIN}/#author-{a['slug']}"},"publisher":{"@id":f"{DOMAIN}/#organization"},
          "datePublished":fm.get("published","2026-01-15"),"dateModified":fm.get("modified",UPDATED),
          "breadcrumb":{"@id":url+"#breadcrumb"}}]
    if fm.get("itemlist"):
        g[1]["mainEntity"] = {"@id": url + "#ranking"}
    items = [{"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"}]
    for i,(n,h) in enumerate(fm.get("crumbs",[]), start=2):
        items.append({"@type":"ListItem","position":i,"name":n,"item":DOMAIN+h})
    g.append({"@type":"BreadcrumbList","@id":url+"#breadcrumb","itemListElement":items})
    if fm.get("itemlist"):
        g.append({"@type":"ItemList","@id":url+"#ranking","numberOfItems":len(fm["itemlist"]),
          "itemListOrder":"https://schema.org/ItemListOrderDescending",
          "itemListElement":[{"@type":"ListItem","position":i,
            "item":{"@type":"Organization","name":OPS[s]["name"],
                    "url":f"{DOMAIN}/casino-reviews/{s}/"}} for i,s in enumerate(fm["itemlist"],1)]})
    faqs = extract_faq(body)
    if faqs:
        g.append({"@type":"FAQPage","@id":url+"#faq","mainEntity":faqs})
    if fm.get("reviewOf"):
        op = OPS[fm["reviewOf"]]
        g.append({"@type":"Review","@id":url+"#review",
          "itemReviewed":{"@type":"Organization","name":op["name"],"description":op["usp"]},
          "author":{"@id":f"{DOMAIN}/#author-{a['slug']}"},"publisher":{"@id":f"{DOMAIN}/#organization"},
          "datePublished":fm.get("published","2026-01-15"),
          "reviewRating":{"@type":"Rating","ratingValue":round(op["rating"]*2,1),"bestRating":10,"worstRating":1}})
    for extra in fm.get("extraSchema", []):
        g.append(extra)
    page = {"@context":"https://schema.org","@graph":g}
    j = lambda d: json.dumps(d, ensure_ascii=False, separators=(",",":"))
    return (f'<script type="application/ld+json">\n{j(org_site)}\n</script>'
            f'<script type="application/ld+json">\n{j(page)}\n</script>')


# ---------------------------------------------------------------- page
def article(lic):
    """'the Anjouan Gaming Authority' but 'Curacao eGaming' — only bodies take an article."""
    name = lic.split("(")[0].strip()
    return f"the {name}" if name.rsplit(" ", 1)[-1] in ("Board", "Authority", "Commission") else name


def review_notice(slug):
    """The same licensing disclaimer, worded for a single-operator page."""
    op = OPS.get(slug)
    if not op:
        return ""
    lic = op["licence"]
    unverified = ("not" in lic.lower() and "publish" in lic.lower()) or "verify" in lic.lower()
    recourse = ("runs through whichever regulator licences it &mdash; and "
                f"{op['name']} does not publish one we can check"
                if unverified else
                f"runs through {article(lic)} rather than a New Zealand regulator")
    return f'''<section class="sec sec--alt" id="licensing-notice"><div class="wrap"><div class="prose">
<div class="cal cal--warn">{ic("warn")}<div><b>One thing to know up front</b>{op["name"]} does not hold a New Zealand licence. The Department of Internal Affairs is issuing up to 15 online casino licences and a prohibition on advertising unlicensed online casino gambling has already commenced under section 10 of the Online Casino Gambling Act. Playing at an offshore casino has never been an offence for a New Zealand resident &mdash; but your recourse {recourse}, which is why our tested payout data matters.</div></div>
</div></div></section>'''


def render(fm, lede, body):
    url = DOMAIN + fm["url"]
    t, d = html.escape(fm["title"]), html.escape(fm["description"])
    robots = fm.get("robots","index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1")
    return f'''<!DOCTYPE html><html lang="en-NZ"> <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{t}</title><link rel="canonical" href="{url}"><meta name="description" content="{d}"><meta name="robots" content="{robots}"><link rel="alternate" hreflang="en-nz" href="{url}"><link rel="alternate" hreflang="x-default" href="{url}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png"><link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png"><link rel="icon" type="image/png" sizes="144x144" href="/favicon-144x144.png"><link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png"><link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png"><link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png"><link rel="shortcut icon" href="/favicon.ico">{schema_blocks(fm, body, url)}<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:type" content="{fm.get('ogType','article')}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{SITE}">
<meta property="og:locale" content="en_NZ">
<meta property="og:image" content="{DOMAIN}/images/og-casinokiwi.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{DOMAIN}/images/og-casinokiwi.jpg"><link rel="stylesheet" href="/assets/css/site.css"></head> <body> {nav_html()} {hero_html(fm, lede)}
{body}
 {foot_html()} </body></html>
'''


FM_RE = re.compile(r"^\s*<!--@(.*?)@-->\s*", re.S)

def main():
    pages = []
    for fn in sorted(os.listdir(SRC)):
        if not fn.endswith(".html"):
            continue
        raw = open(os.path.join(SRC, fn), encoding="utf-8").read()
        m = FM_RE.match(raw)
        if not m:
            raise SystemExit(f"{fn}: missing front matter")
        pages.append((fn, json.loads(m.group(1)), raw[m.end():]))

    for fn, fm, frag in pages:
        try:
            full_h1, lede, unwrapped = split_fragment(frag)
        except AssertionError as e:
            raise SystemExit(f"{fn}: {e}")
        if full_h1:
            fm = dict(fm, h1=full_h1)
        lb_html = lb_notice = ""
        tl = re.search(r'<div class="toplist">(.*?</article>)\s*</div>', unwrapped, re.S)
        if tl:
            base = re.split(r'\s*[:\u00b7|]\s*', fm["h1"])[0]
            heading = fm.get("lbHeading") or (f'The {base}' if base.lower().startswith("best")
                                              else f'The Best {base}')
            sports = fm["url"] in ("/online-betting/", "/best-sports-betting-sites/")
            lb_html, lb_notice = build_leaderboard(tl.group(1), heading, sports, fm.get("lbIntro", ""))
            if lb_html:
                unwrapped = unwrapped[:tl.start()] + unwrapped[tl.end():]
        body = transform(unwrapped, fm.get("reviewOf"))
        if not lb_notice and fm.get("reviewOf"):
            lb_notice = review_notice(fm["reviewOf"])
        body = lb_html + body + lb_notice
        doc = resolve_tokens(render(fm, resolve_tokens(lede) or html.escape(fm["description"]), body))
        out_dir = os.path.join(ROOT, fm["url"].strip("/"))
        os.makedirs(out_dir, exist_ok=True)
        open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(doc)

    urls = [(fm["url"], fm.get("modified",UPDATED), fm.get("changefreq","weekly"), fm.get("priority","0.7"))
            for _, fm, _ in pages if "noindex" not in fm.get("robots","")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, lm, cf, pr in urls:
        sm.append(f"  <url>\n    <loc>{DOMAIN}{u}</loc>\n    <lastmod>{lm}</lastmod>\n"
                  f"    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>\n  </url>")
    sm.append("</urlset>")
    open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write("\n".join(sm)+"\n")

    open(os.path.join(ROOT,"robots.txt"),"w",encoding="utf-8").write(f"""# robots.txt for {DOMAIN}
User-agent: *
Allow: /
Disallow: /go/
Disallow: /*?

Sitemap: {DOMAIN}/sitemap.xml

# SEO crawlers — blocked to keep our link graph and content out of third-party indexes.
User-agent: AhrefsBot
Disallow: /

User-agent: SemrushBot
Disallow: /

User-agent: MJ12bot
Disallow: /

User-agent: DotBot
Disallow: /

User-agent: Rogerbot
Disallow: /

User-agent: serpstatbot
Disallow: /

User-agent: SistrixBot
Disallow: /
""")
    print(f"built {len(pages)} pages · sitemap {len(urls)} urls")
    if MISSING:
        print("WARNING no affiliate link for: " + ", ".join(sorted(MISSING)))

if __name__ == "__main__":
    main()
