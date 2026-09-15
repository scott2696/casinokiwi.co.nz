#!/usr/bin/env python3
"""Insert new sections and FAQ entries into an existing page fragment."""
import sys, re, os

def insert_before_faq(path, html_block):
    s = open(path).read()
    m = re.search(r'<h2 id="faq">', s)
    assert m, f"{path}: no FAQ anchor"
    # walk back to the start of the section that contains the FAQ
    cut = s.rfind('<section class="section', 0, m.start())
    cut = m.start() if cut == -1 else cut
    s = s[:cut] + html_block + s[cut:]
    open(path, 'w').write(s)

def add_faqs(path, pairs):
    s = open(path).read()
    m = re.search(r'(<div class="faq">)(.*?)(</div>\s*\n)', s, re.S)
    assert m, f"{path}: no .faq block"
    extra = "".join(
        f'<details><summary>{q}</summary><div class="a"><p>{a}</p></div></details>\n'
        for q, a in pairs)
    s = s[:m.end(2)] + extra + s[m.end(2):]
    open(path, 'w').write(s)
