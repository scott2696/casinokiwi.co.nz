#!/usr/bin/env python3
import glob, re, html, os, sys
CHROME = re.compile(r'<(script|style|nav|header|footer)[^>]*>.*?</\1>', re.S)
WORD = re.compile(r"[A-Za-z][A-Za-z'’-]+")
rows = []
for f in sorted(glob.glob("**/index.html", recursive=True)):
    h = open(f).read()
    body = CHROME.sub('', h).split('<footer', 1)[0]
    txt = html.unescape(re.sub(r'<[^>]+>', ' ', body))
    rows.append(dict(page="/" + f.replace("index.html", ""),
                     w=len(WORD.findall(txt)),
                     h2=len(re.findall(r'<h2[ >]', h)),
                     h3=len(re.findall(r'<h3[ >]', h)),
                     faq=len(re.findall(r'<details class="faq"', h)),
                     tables=len(re.findall(r'<table class="t"', h))))
only = sys.argv[1:] 
rows.sort(key=lambda r: r["w"])
print(f"{'words':>6} {'h2':>3} {'h3':>3} {'faq':>4} {'tbl':>4}  page")
for r in rows:
    if only and not any(o in r["page"] for o in only): continue
    print(f"{r['w']:>6} {r['h2']:>3} {r['h3']:>3} {r['faq']:>4} {r['tables']:>4}  {r['page']}")
tot = sum(r["w"] for r in rows)
med = rows[len(rows)//2]["w"]
print(f"\ntotal {tot:,} words · median page {med:,}")
