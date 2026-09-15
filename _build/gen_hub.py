#!/usr/bin/env python3
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPS = json.load(open(os.path.join(ROOT, "_build", "operators.json")))
order = ["spinjo","rooster-bet","kingdom","fortune-play","smash","lucky7even","spino","lucky-circus",
         "rivo","lucky-vibe","ivibet","roby","hellspin","slotsgem","bet-and-play","madcasino"]

def clip(s, n=92):
    """Trim to a word boundary without splitting an HTML entity."""
    if len(s) <= n:
        return s
    cut = s[:n]
    amp = cut.rfind("&")
    if amp != -1 and ";" not in cut[amp:]:
        cut = cut[:amp]
    return cut.rsplit(" ", 1)[0].rstrip(" ,;&") + "\u2026"


def stars(r):
    f = int(r); h = 1 if r - f >= 0.25 else 0
    return "&#9733;"*f + ("&#189;" if h else "") + "&#9734;"*(5-f-h)

rows, cards = [], []
for i, slug in enumerate(order, 1):
    op = OPS[slug]
    initials = "".join(w[0] for w in op["name"].split()[:2]).upper()
    rows.append(f"""<tr><th scope="row"><a href="/casino-reviews/{slug}/">{op['name']}</a></th>
<td>{op['welcome']}</td><td>{op['wagering']}</td><td>{op['games']}</td>
<td class="{'yes' if op['sports'] else 'no'}">{'Yes' if op['sports'] else 'No'}</td>
<td>{op['licence'].split('(')[0].strip()}</td><td><strong>{op['rating']}</strong></td></tr>""")
    linked = bool(op["casinoLink"] or op["sportsLink"])
    kind = "affs" if (op["sports"] and not op["casinoLink"]) else "aff"
    btn = (f'<a class="btn btn-gold btn-block btn-sm" href="{{{{{kind}:{slug}}}}}" target="_blank" rel="nofollow sponsored noopener">Visit {op["name"]}</a>'
           if linked else '<span class="fine">Unranked &mdash; not recommended</span>')
    cards.append(f"""<article class="op-card{' is-top' if i==1 else ''}">
<div class="op-rank">{i}</div>
<div class="op-id"><span class="op-logo" aria-hidden="true">{initials}</span><span class="op-name"><a href="/casino-reviews/{slug}/">{op['name']}</a></span><p class="op-meta">{clip(op['usp'])}</p></div>
<div class="op-offer"><p class="o-main">{op['welcome'][:72]}</p><p class="o-sub">{op['licence'].split('(')[0].strip()} &middot; {op['games']}</p></div>
<div class="op-score"><span class="num">{op['rating']}</span><div class="stars">{stars(op['rating'])}</div><div class="lbl">Our score</div></div>
<div class="op-act">{btn}<span class="terms">18+ &middot; <a href="/casino-reviews/{slug}/">Full review</a></span></div>
</article>""")

fm = {
 "url": "/casino-reviews/",
 "title": "Casino Reviews NZ 2026 | 16 Sites Tested by Kiwis",
 "description": "Every online casino we have tested for New Zealand players, with scores, bonus terms, payout speeds and licensing verified — including the ones we cannot recommend.",
 "h1": "Casino Reviews",
 "author": "rawiri",
 "published": "2026-01-12",
 "priority": "0.8",
 "crumbs": [["Casino Reviews", "/casino-reviews/"]],
 "itemlistName": "Online Casino Reviews NZ",
 "itemlist": order[:12],
 "lbHeading": "Every Casino We Have Tested, Ranked",
 "lbIntro": "Every operator here went through the same test: I opened an account, deposited my own money, played to a withdrawable balance and timed the cashout. That includes the two near the bottom I cannot recommend — we publish those rather than quietly leaving them out.",
}

body = f"""<section class="hero"><div class="wrap">
<p class="eyebrow">Reviews index &middot; Updated 1 September 2026</p>
<h1>Casino Reviews NZ 2026: Every Site We Have Tested</h1>
<p class="hero-lede">Sixteen operators, each opened with a real New Zealand account, funded with real money, and put through the same withdrawal test. Including the two we could not verify and will not recommend.</p>
<div class="hero-ctas"><a class="btn btn-gold" href="#all">Browse all reviews &rarr;</a><a class="btn btn-ghost" href="/how-we-review/">How we score</a></div>
</div></section>

<section class="section"><div class="wrap">
<div class="answer"><span class="label">Start here</span>
<p>Our highest-scoring casino for New Zealand players is <strong><a href="/casino-reviews/spinjo/">Spinjo</a></strong> at 4.6/5, followed by <strong><a href="/casino-reviews/rooster-bet/">Rooster Bet</a></strong> and <strong><a href="/casino-reviews/kingdom/">Kingdom</a></strong> at 4.5. Two operators sit lower than their product alone would justify, for the same reason: <a href="/casino-reviews/roby/">Roby</a> and <a href="/casino-reviews/madcasino/">MadCasino</a> do not publish a gaming licence we can verify. Roby has the largest catalogue we counted and MadCasino the largest bonus on this site — and both are capped anyway, because a licence you cannot check gives you no recourse if a withdrawal is refused.</p></div>

<h2 id="all">All casino reviews, ranked</h2>
<div class="toplist">
{"".join(cards)}
</div>

<h2>Every site compared</h2>
<div class="table-scroll"><table class="data">
<caption>All operators reviewed, verified 1 September 2026. All amounts in NZD unless stated.</caption>
<thead><tr><th scope="col">Casino</th><th scope="col">Welcome offer</th><th scope="col">Wagering</th><th scope="col">Games</th><th scope="col">Sports</th><th scope="col">Licence</th><th scope="col">Score</th></tr></thead>
<tbody>
{"".join(rows)}
</tbody></table></div>

<h2>How to read our scores</h2>
<p>Every score is built from five weighted categories: payouts and banking (30%), bonus fairness (25%), games and software (20%), trust and safety (15%) and experience (10%). The full model, including the exact withdrawal test script, is published on our <a href="/how-we-review/">review methodology page</a>.</p>
<p>A few things our scores deliberately punish. An unverifiable licence caps a site regardless of how good the product is, which is why Roby's 13,500-game catalogue does not lift it above 4.0. A large bonus with hostile terms scores below a small clean one. And any operator that stops paying players is removed the same week, not at the next review cycle.</p>

<h2 id="how-to-read">How to read a casino review</h2>
<p>Reviews are easy to write and hard to trust. These are the four things I look for in anyone else's, including ours.</p>
<h3>Did they actually deposit?</h3>
<p>A review written from a screenshot tour cannot tell you what happens at the cashier, which is the only part that matters when you win. Look for timestamps, method names and specific figures rather than adjectives.</p>
<h3>Is the licence verified or just repeated?</h3>
<p>A licence number copied off the operator's own footer proves nothing. It has to be checked against the regulator's register — which is why two operators on this page are capped despite good products.</p>
<h3>Do they publish anything negative?</h3>
<p>A list where every site scores 4.5+ is a directory, not a review set. Ours ranges from 3.8 to 4.6 and explains every deduction.</p>
<h3>Are the bonus terms priced, or just quoted?</h3>
<p>"600% up to NZ$19,500" is a number. "600% at 10x, so NZ$7,000 of turnover on a NZ$100 deposit" is information. If a review does not do that arithmetic, it has not read the terms.</p>

<h2 id="scores">What our scores mean</h2>
<div class="table-scroll"><table class="data">
<thead><tr><th scope="col">Score</th><th scope="col">What it means</th><th scope="col">On this page</th></tr></thead>
<tbody>
<tr><th scope="row">4.5 – 5.0</th><td>Recommended without qualification. Fast, verifiable, honest terms.</td><td>Spinjo, Rooster Bet, Kingdom</td></tr>
<tr><th scope="row">4.2 – 4.4</th><td>Strong, with a specific caveat we name in the review.</td><td>Fortune Play, Smash, Lucky7even, Spino, Lucky Circus, Rivo</td></tr>
<tr><th scope="row">3.9 – 4.1</th><td>Usable, but something material is missing — depth, transparency or speed.</td><td>Lucky Vibe, IviBet, Roby, HellSpin, SlotsGem</td></tr>
<tr><th scope="row">Below 3.9</th><td>Listed for completeness. We do not recommend depositing.</td><td>MadCasino</td></tr>
</tbody></table></div>
<p>No operator can move between those bands by paying us. The scores come from the weights published on our <a href="/how-we-review/">methodology page</a>, and they change when the test results change.</p>

<h2 id="faq">Casino reviews: FAQ</h2>
<div class="faq">
<details open><summary>How often are these reviews updated?</summary><div class="a"><p>Every operator is re-tested quarterly, and re-scored immediately whenever a licence, owner or headline term changes. Any site that stops paying players is removed the same week rather than at the next review cycle. Each page shows its last-updated date.</p></div></details>
<details><summary>Why do you list casinos you do not recommend?</summary><div class="a"><p>Because readers search for the brand and deserve an answer. Quietly omitting an operator tells you nothing; publishing it with the reason it is capped tells you exactly what to weigh up. MadCasino and Roby are both listed with their licensing gaps stated plainly.</p></div></details>
<details><summary>Do operators pay for a higher position?</summary><div class="a"><p>No. We earn commission when readers open accounts through links here, and that funds the testing programme — but the order comes from the scoring model published on our methodology page. Sites we cannot recommend are excluded regardless of commercial terms, and we decline placements that would require suppressing a negative finding.</p></div></details>
<details><summary>What makes a casino score badly with you?</summary><div class="a"><p>An unverifiable licence caps a site regardless of product quality. Beyond that: wagering above 45x, terms that contradict the advertised offer, withdrawal delays without explanation, KYC demanded only after a win, and responsible gambling tools that are missing or buried more than three clicks deep.</p></div></details>
<details><summary>Which casino should I pick if I only read one review?</summary><div class="a"><p>Spinjo, at 4.6 out of 5 — the largest verified library, a competitive four-deposit package and crypto payouts within hours. If payout speed matters more than game count, read Kingdom instead. If you have been defeated by wagering requirements before, read Smash.</p></div></details>
</div>

<div class="grid grid-3">
<a class="card link-card" href="/"><h3>Best Online Casinos NZ</h3><p>The main ranking, with full written reviews of the top ten.</p><span class="go">See rankings &rarr;</span></a>
<a class="card link-card" href="/how-we-review/"><h3>How We Review</h3><p>Scoring weights, the withdrawal test, and what gets a site removed.</p><span class="go">Read method &rarr;</span></a>
<a class="card link-card" href="/authors/"><h3>Our Authors</h3><p>Who tests these sites, and what they did before this.</p><span class="go">Meet the team &rarr;</span></a>
</div>
</div></section>
"""
open(os.path.join(ROOT, "_build", "pages", "290-reviews-hub.html"), "w", encoding="utf-8").write(
    "<!--@\n" + json.dumps(fm, indent=1, ensure_ascii=False) + "\n@-->\n" + body)
print("hub written")
