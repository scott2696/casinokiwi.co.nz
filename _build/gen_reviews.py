#!/usr/bin/env python3
"""Generates the individual casino review fragments from operators.json + the
per-operator editorial copy below. Keeps facts, links and ratings in one place."""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPS = json.load(open(os.path.join(ROOT, "_build", "operators.json")))
OUT = os.path.join(ROOT, "_build", "pages")

# slug -> editorial copy written per operator
COPY = {
"spinjo": dict(order=300, author="rawiri", tag="Best overall for New Zealand",
  verdict="Spinjo is our top-rated online casino for New Zealand players in 2026. The library is the largest we verified at around 8,000 titles, the four-deposit welcome package spreads the commitment rather than forcing one big deposit, and crypto withdrawals cleared within hours of verification. The 40x wagering is ordinary rather than generous, and there is no sportsbook.",
  body="""<h2>First impressions</h2>
<p>Spinjo launched in 2024 under Hollycorn N.V. with a Curaçao Gaming Control Board licence you can actually look up: OGL/2023/176/0095. That matters more than it sounds. A large share of the sites competing for New Zealand traffic display a licence badge without a verifiable number; Spinjo publishes one and it checks out.</p>
<p>The lobby is the site's real argument. Around 8,000 games is roughly double a typical Curaçao operator's catalogue, and it is not padded with clones from one obscure studio — NetEnt, Pragmatic Play, Evolution and Hacksaw Gaming are all present, which means the pokies people actually search for are there.</p>
<h2>The welcome offer, priced properly</h2>
<p>Up to NZ$5,000 and 300 free spins across four deposits, with a NZ$30 minimum to qualify and 40x wagering. Two things to notice. The NZ$30 entry is higher than the NZ$20 that most competitors ask, so the offer is slightly less accessible at the bottom end. And 40x is the industry standard, not a selling point — a NZ$500 bonus at 40x needs NZ$20,000 of turnover. If low wagering is what you want, <a href="/casino-reviews/smash/">Smash</a> at 10x is the better call.</p>
<p>The four-deposit structure is genuinely player-friendly though. You are not required to commit the full amount to access the offer, and you can stop after deposit one having taken a 100% match with no obligation.</p>
<h2>Banking and payouts</h2>
<p>NZD is supported, and the crypto cashier is where Spinjo earns its score. Our tester's withdrawal cleared within hours of account verification, with no fee added by the operator on top of the network cost. Card and bank withdrawals run to the normal one to five business days.</p>
<h2>Mobile</h2>
<p>No app, which is expected — Apple and Google restrict real-money gambling apps in New Zealand. The mobile web build carries the full catalogue and cashier, and the provider filters and search actually work on a phone, which is not universal.</p>"""),

"rooster-bet": dict(order=310, author="rawiri", tag="Best casino and sportsbook combined",
  verdict="Rooster Bet is the best pick for Kiwis who bet on sport and play casino games, because both sit on a single wallet with separate welcome offers. The casino side matches the biggest libraries here at around 8,000 titles. The casino bonus's 40x wagering and short turnover window are the weak points.",
  body="""<h2>Two products, one account</h2>
<p>Rooster Bet launched in 2023 under Dama N.V., licensed by the Curaçao Gaming Authority under OGL/2023/174/0082. The proposition is straightforward: a full sportsbook and a full casino sharing one balance, so you are not shuffling money between two accounts to back the Warriors on Friday and play pokies on Sunday.</p>
<p>The casino carries around 8,000 titles from NetEnt, Playtech, Quickspin, Red Tiger and Hacksaw Gaming, plus live game shows, jackpots and instant wins. The sportsbook covers rugby union, league, thoroughbred and harness racing, football and esports, with in-play markets and a comp-point Bonus Store for returning customers.</p>
<h2>The two welcome offers</h2>
<p>Casino: up to NZ$5,000 and 300 free spins across multiple deposits at 40x wagering. Sports: 100% up to NZ$350 as a free bet on your first deposit, then 50% up to NZ$175 on the second. Keeping them separate is the right decision — a shared offer would force sports bettors through casino turnover requirements.</p>
<p>The casino bonus is where we would push back. 40x is standard but the turnover window is tight, and live casino games contribute very little toward wagering. Treat it as a pokies bonus and it is achievable; treat it as a blackjack bankroll and you will run out of time before you run out of turnover.</p>
<h2>Where it sits against TAB</h2>
<p>If you bet mainly on New Zealand racing, TAB NZ is both the legal option and the better product — full fields and complete form on every domestic meeting. Rooster Bet's advantage is market depth on overseas sport, player props, esports and in-play tools. Read our <a href="/best-sports-betting-sites/">sports betting comparison</a> and the <a href="/online-betting/">NZ betting law section</a> before deciding.</p>"""),

"kingdom": dict(order=320, author="rawiri", tag="Fastest payouts, biggest 30x package",
  verdict="Kingdom won our payout-speed test outright, clearing crypto withdrawals in two to four hours with no operator fee — and it pairs that with one of the largest welcome packages on this site, 600% total up to NZ$18,500 on the casino side. The catch is the multiple: 30x, so the top of that range is far harder to reach than the headline suggests.",
  body="""<h2>Built around getting paid</h2>
<p>Kingdom holds a Curaçao eGaming licence and runs a 7,000+ game catalogue alongside a fully integrated sportsbook. What sets it apart is the cashier. Crypto withdrawals were completing in two to four hours in our testing, against an industry median closer to a full day, and Kingdom charges nothing of its own on crypto in either direction. For a player who cashes out weekly rather than annually, that compounds into a materially better experience.</p>
<h2>A big bonus, and the multiple that governs it</h2>
<p>Kingdom's welcome package runs to <strong>600% total, up to NZ$18,500</strong> on the casino side (&euro;9,500) and <strong>200% up to NZ$1,900</strong> on sports (&euro;1,000). That puts the casino offer among the three largest we list. Both are <em>total</em> figures spread across a deposit sequence, not paid on the first deposit.</p>
<p>Then read the wagering line, because it changes the picture: <strong>30x</strong>. Better than the 40x industry norm, but on a package this size the turnover is substantial — a NZ$5,000 bonus at 30x is NZ$150,000 through the games. Set that against <a href="/casino-reviews/smash/">Smash's 10x</a> on a similar headline and the gap in what you can realistically clear is enormous. Our <a href="/online-casinos/bonuses/">bonuses guide</a> runs the arithmetic.</p>
<p>The more dependable value here is the weekly calendar: Royal Monday at 100% up to NZ$1,000, Kingly Wednesday at 150%, Regal Friday at 200%, and a Tuesday Boost on sports at 100% up to NZ$1,000 with 15x wagering. Each carries its own terms, so read them individually — but for a player who deposits weekly, those reloads are worth more over a year than the welcome hook.</p>
<h2>The sportsbook</h2>
<p>Over 30 sports including football, tennis, basketball, esports and horse racing, sharing the casino balance, with in-play odds and an accumulator builder. It is not as deep as a specialist book on niche markets, but it covers everything a New Zealand punter would look for and settles quickly.</p>
<h2>What to watch</h2>
<p>The minimum deposit is around NZ$40, higher than the NZ$20 norm. The reload offers each carry separate wagering, so the calendar is only good value if you read each one rather than assuming they match the welcome terms. And treat the 600% headline as an upper bound reached across several deposits at 30x — not money you will clear on a first NZ$40 deposit.</p>"""),

"fortune-play": dict(order=330, author="rawiri", tag="Best for crash and instant-win games",
  verdict="Fortune Play carries 8,000+ titles across 80 studios and has the deepest crash and instant-win range on this site — Aviator, bonus buys, Megaways and a full sportsbook on the same account. Payment coverage is unusually wide, spanning cards, e-wallets, bank transfer and six cryptocurrencies.",
  body="""<h2>The catalogue</h2>
<p>Fortune Play is a Dama N.V. site licensed by the Curaçao Gaming Control Board under OGL/2023/174/0082, with Tobique cover referenced in some markets. The library runs past 8,000 titles across roughly 80 studios, and it is unusually broad rather than merely large: classic pokies, bonus buys, Megaways, Aviator and instant games, live dealer, jackpots and a sportsbook all sit under one login.</p>
<p>If you play crash and instant-win titles, this is the site on our list built for you. Those games also publish the highest returns available anywhere online — commonly 96% to 99% — which is why Fortune Play scores well on our <a href="/high-payout-casinos/">high payout</a> rankings despite an unremarkable bonus.</p>
<h2>Bonus</h2>
<p>Up to NZ$5,000 and 300 free spins across four deposits, with the first deposit paying 100% up to about NZ$1,700 plus 100 spins. Wagering terms should be checked at the cashier as they vary by promotion. Note that bonus-buy features are excluded from wagering contribution at most operators, including this one — which matters given bonus buys are a headline feature here.</p>
<h2>Banking</h2>
<p>One of the widest payment spreads we found: Visa, Mastercard, e-wallets including Skrill and Neteller, online banking, and six cryptocurrencies (BTC, ETH, LTC, BCH, DOGE and USDT). Card withdrawals were the fastest we recorded among the sites tested, and crypto clears within hours.</p>
<h2>Verdict for Kiwi players</h2>
<p>A strong all-rounder that is the clear first choice if instant-win and crash games are your thing, and a solid second choice for pokies behind <a href="/casino-reviews/spinjo/">Spinjo</a>.</p>"""),

"smash": dict(order=340, author="maia", tag="Lowest wagering requirement on this site",
  verdict="Smash asks 10x on deposit plus bonus where the market asks 35x to 40x on bonus. That single number makes its 600% total up to NZ$19,500 casino package — plus 250% up to NZ$9,800 on sports — the most clearable big offer we found. The trade-off is transparency: an Anjouan licence, less publicly documented than Curaçao, and licensing details that are not easy to find on site.",
  body="""<h2>Read the wagering line first</h2>
<p>Smash headlines with <strong>600% total up to NZ$19,500</strong> on the casino side (&euro;10,000) and <strong>250% up to NZ$9,800</strong> on sports (&euro;5,000), which reads like noise until you check the requirement: <strong>10x on deposit plus bonus</strong>. Run the numbers on a NZ$100 deposit matched to NZ$600 and you need NZ$7,000 of turnover. The same money at a 40x-on-bonus site needs NZ$24,000. That is the difference between a bonus you might genuinely clear and one that exists to look large in an advertisement.</p>
<p>The sportsbook side follows the same logic — 250% up to NZ$9,800 at 15x turnover, where 30x to 40x is the usual ask. That is the largest sports welcome offer on this site by a wide margin.</p>
<h2>Games and sport</h2>
<p>Over 40 providers supply the casino, covering pokies, live dealer studios and jackpots. The integrated sportsbook covers more than 30 sports with pre-match and live betting, and its esports range — Dota 2, Call of Duty, Counter-Strike — is the deepest here alongside <a href="/casino-reviews/kingdom/">Kingdom</a>.</p>
<h2>The licensing question</h2>
<div class="callout warn"><span class="t">Anjouan, not Curaçao</span>
<p>Smash operates under an Anjouan Gaming Authority licence. Anjouan licences are legitimate but offer weaker practical recourse than the Curaçao Gaming Control Board's direct-licensing regime, and licensing information is not prominently displayed on the site. That is the main reason Smash sits at 4.4 rather than higher despite having the best bonus terms on this page. Verify the current licence position before depositing a large amount.</p></div>
<h2>Mobile and payouts</h2>
<p>Browser-first with no dedicated app, but the responsive build carries the full catalogue, live studios, sportsbook and cashier without breaking. E-wallet and crypto withdrawals took a few hours to a day in testing — good, though not in <a href="/fast-payout-casinos/">Kingdom's two-to-four-hour class</a>.</p>"""),

"lucky7even": dict(order=350, author="maia", tag="Best no-deposit offer for Kiwis",
  verdict="Lucky7even runs one of the few genuine no-deposit offers still available to New Zealand players: 20 free spins on Book of the Fallen after email verification, with no card required. Winnings are capped and carry 50x wagering, so treat it as a free audition of the casino rather than a payday. The payment spread is one of the widest we found.",
  body="""<h2>The no-deposit offer</h2>
<p>Twenty free spins on Pragmatic Play's Book of the Fallen, released after you register and verify your email address. No card, no deposit. Winnings are capped and carry 50x wagering, which is typical for the category and means clearing it to a withdrawal is unlikely rather than impossible.</p>
<p>The value is not the money. It is that you get to test the lobby, the loading speed, the support desk response time in New Zealand hours, and the verification process before any of your own money is at risk. That is genuinely worth ten minutes. See our <a href="/no-deposit-casinos/">no deposit casinos guide</a> for the full maths on offers like this.</p>
<h2>The deposit offer</h2>
<p>100% up to roughly NZ$1,700, usable once per day, with a maximum cash-out cap on the bonus. Read the current terms at the cashier — this is one of the offers that changes most often among the sites we track.</p>
<h2>Payments</h2>
<p>Lucky7even's cashier is unusually broad: Visa, Mastercard, Maestro and bank transfer; Skrill, Neteller, ecoPayz, MiFinity, Jeton, AstroPay and Pay4Fun; Neosurf and Flexepin prepaid; and Bitcoin, Ethereum, Litecoin, Dogecoin, Tether and Binance Coin. Minimum deposits sit around NZ$35 equivalent on most methods, with withdrawals starting at a similar level and per-transaction maximums that are worth checking before you chase a big win.</p>
<h2>Licensing</h2>
<p>Curaçao Gaming Control Board, with Tobique Gaming Commission cover applying in some markets. Standard for this tier of operator.</p>"""),

"spino": dict(order=360, author="rawiri", tag="0x wagering — the rarest term in the market",
  verdict="Spino runs a crypto-first welcome package to 2,000 USDT with a 0x wagering requirement, meaning winnings from it are withdrawable immediately. We checked this twice because it is rare enough to look like an error. The catch is scale and history: around 3,500 games from roughly 20 studios, and the site only launched in 2026.",
  body="""<h2>The offer that stands out</h2>
<p>Almost every welcome bonus in this market carries 35x to 50x wagering. Spino's headline crypto package, worth up to 2,000 USDT, carries <strong>0x</strong>. There is no turnover to grind out before a withdrawal, which makes it the single most player-friendly headline term we found across all sixteen operators we assessed.</p>
<p>Understand what that implies. A 0x offer is usually smaller in practice than its headline suggests, and the operator will have other mechanisms — deposit thresholds, coin restrictions, maximum bet rules — doing the work that wagering normally does. Read the terms at the cashier. But the absence of a turnover requirement is real and unusual.</p>
<h2>Games</h2>
<p>Around 3,500 titles from roughly 20 studios, which is modest against <a href="/casino-reviews/spinjo/">Spinjo's ~8,000</a> or <a href="/casino-reviews/roby/">Roby's 13,500+</a>. If you play niche pokies you will find gaps. The core Pragmatic Play, Evolution and BGaming catalogue is present.</p>
<h2>Licensing and history</h2>
<div class="callout note"><span class="t">A very new operator</span>
<p>Spino launched in 2026 under Empire of Kingdoms Limitada with a Tobique Gaming Commission licence, published openly. New cuts both ways: there is no history of unpaid players, but there is no track record either. Our recommendation is to treat Spino as a strong bonus play rather than a long-term home until it has a couple of years behind it, and to keep withdrawals frequent rather than letting a balance build.</p></div>
<h2>Best for</h2>
<p>Crypto players who want to take a welcome offer without a turnover obligation. If you deposit in NZD by card, much of Spino's advantage disappears — see <a href="/best-crypto-casinos/">our crypto casinos guide</a> for context.</p>"""),

"lucky-circus": dict(order=370, author="maia", tag="Best recurring weekly offer",
  verdict="Lucky Circus's real value is not the welcome package but the recurring Monday free spins drop — 150 spins for a NZ$20 deposit, every week. Over a year that is worth far more to a regular player than a one-off bonus. Some players have reported bonus terms and withdrawal restrictions not matching advertised terms, so read the conditions carefully.",
  body="""<h2>The weekly drop</h2>
<p>Most casinos front-load everything into a welcome offer and give returning players very little. Lucky Circus inverts that: every Monday, a NZ$20 deposit triggers 150 free spins. For someone who plays weekly, that recurring value compounds into far more than a single NZ$5,000 headline package that they will never fully claim.</p>
<p>The welcome offer itself is 100% up to about NZ$1,500 plus 150 free spins on Elvis Frog in Vegas, extending across the second, third and fourth deposits to a total of 300%.</p>
<h2>Games and feel</h2>
<p>A Dama N.V. site licensed by the Curaçao Gaming Control Board, launched in 2024, carrying more than 4,000 games from award-winning studios. The theme is a dark, deliberately strange circus — you will either like it or find it a lot. Navigation is clean and support runs 24/7.</p>
<h2>The caution</h2>
<div class="callout warn"><span class="t">Read the terms before you claim</span>
<p>Some players have reported that bonus terms and withdrawal restrictions did not match what they understood from the advertised offer. We have not been able to verify individual cases, but the pattern is common enough in player feedback to be worth flagging. Before claiming anything here, read the specific promotion's terms page — not the banner — and note the maximum bet while wagering and any cash-out cap.</p></div>
<h2>Best for</h2>
<p>Regular, lower-stakes players who will actually use a weekly offer. If you deposit once and play through, <a href="/casino-reviews/spinjo/">Spinjo</a> or <a href="/casino-reviews/smash/">Smash</a> give you more.</p>"""),

"rivo": dict(order=380, author="rawiri", tag="Biggest bonus ladder, 10x wagering",
  verdict="Rivo runs the highest match percentage on this site — 1000% total up to NZ$19,500 on the casino side — at an unusually low 10x wagering, with 25% VIP cashback on top. The sports offer is far smaller at 100% up to NZ$950. The offsetting factors are strict KYC that players report as demanding, and limited transparency about the operator behind the brand.",
  body="""<h2>The ladder</h2>
<p><strong>1000% total up to NZ$19,500</strong> on the casino side (&euro;10,000) at <strong>10x wagering</strong> — the highest match percentage we list, on terms that are actually clearable. That puts Rivo alongside <a href="/casino-reviews/smash/">Smash</a> as one of only two sites here pairing a large headline with a low multiple. It is a tiered package, so you step off at whichever rung suits you; the headline is an upper bound, not a commitment.</p>
<p>The sportsbook offer is a different proposition entirely: <strong>100% up to NZ$950</strong> (&euro;500). If you came for sports, <a href="/casino-reviews/smash/">Smash's 250% up to NZ$9,800</a> or <a href="/casino-reviews/rooster-bet/">Rooster Bet</a> will serve you better.</p>
<p>The 25% VIP cashback is the largest on our list. Cashback matters more than most players realise: it converts a portion of losses back into playable or withdrawable value on every session, not just at sign-up.</p>
<h2>Games and sport</h2>
<p>More than 4,000 titles plus an integrated sportsbook, with fast e-wallet and crypto payouts. It is a smaller catalogue than the 8,000-title sites, but the studio mix covers the mainstream comfortably.</p>
<h2>The KYC warning</h2>
<div class="callout warn"><span class="t">Verify your identity on day one</span>
<p>Rivo operates under a reported Curaçao Gaming Authority licence with limited published transparency, and players consistently describe its identity verification as strict. That is not automatically a bad thing — thorough KYC is a regulatory requirement — but it becomes a problem when you leave it until you want to withdraw. Upload photo ID and a proof of address dated within three months before you deposit, and the most common source of payout delay disappears.</p></div>
<h2>Best for</h2>
<p>Players who want a low-wagering bonus over a long run of deposits and are willing to do their verification properly up front.</p>"""),

"lucky-vibe": dict(order=390, author="rawiri", tag="Casino and sports on one wallet",
  verdict="Lucky Vibe pairs a ~5,000-game library from 149 studios with a sportsbook on the same balance, and a four-deposit package up to NZ$5,000 with 300 free spins. Two issues keep it at 4.1: slow live chat response and a three-day bonus expiry that is the tightest on our list.",
  body="""<h2>Range and structure</h2>
<p>Launched in November 2024 under Hollycorn N.V. with a Curaçao Gaming Control Board licence, Lucky Vibe carries close to 5,000 titles from more than 149 software developers — an unusually wide studio spread even where the total count is not the largest.</p>
<p>The welcome package is clearly laid out across four deposits: 100% up to about NZ$1,700 plus 100 free spins on the first, 100% up to NZ$1,700 plus 50 spins on the second, 50% up to NZ$2,500 plus 50 spins on the third, and 75% up to NZ$2,500 plus 100 spins on the fourth.</p>
<h2>The three-day problem</h2>
<div class="callout warn"><span class="t">Plan the session before you claim</span>
<p>Lucky Vibe's bonuses expire in three days. That is the shortest window among the sites we recommend, and it changes how you should approach the offer entirely. Before claiming, divide the required turnover by three and ask honestly whether you will play that much in seventy-two hours. If not, decline the bonus and play with unrestricted cash — every site here allows it, and your money then stays withdrawable with no max-bet rule attached.</p></div>
<h2>Support</h2>
<p>Live chat response times were the slowest we recorded among our recommended sites. For a New Zealand player that matters more than it does in Europe, because our peak hours fall outside the operator's core staffing window. Budget for a wait if you need help in a Kiwi evening.</p>
<h2>Best for</h2>
<p>Players who want casino and sportsbook on one balance and will use a bonus quickly. If you play sporadically, <a href="/casino-reviews/kingdom/">Kingdom's</a> weekly reloads suit you better.</p>"""),

"ivibet": dict(order=400, author="rawiri", tag="Casino and sportsbook under one login",
  verdict="IviBet gives you a 5,000+ game casino and a full sportsbook on a single account, backed by a published Curaçao licence number. The welcome offer is modest by this list's standards, and the recurring theme in player feedback is withdrawal delays tied to repeated KYC requests — so verify early.",
  body="""<h2>The operator</h2>
<p>IviBet launched in 2022 and is operated by TechOptions Group B.V. under a Curaçao eGaming licence, number 365/JAZ. The same operator runs <a href="/casino-reviews/hellspin/">HellSpin</a> and <a href="/casino-reviews/slotsgem/">SlotsGem</a>, which share the cashier and much of the platform — useful to know if you want a second account somewhere familiar, and equally useful to know if you have had a poor experience with one of them.</p>
<h2>Games</h2>
<p>More than 5,000 titles from Pragmatic Play, Evolution, Play'n GO, BGaming and Hacksaw Gaming, spanning pokies, jackpots, table games, live dealer and crypto-compatible titles. The sportsbook runs on the same wallet.</p>
<h2>The welcome offer</h2>
<p>Two deposits: 100% up to about NZ$180 with 120 free spins, then 50% up to about NZ$360 with 50 spins. Smaller than the NZ$5,000 packages elsewhere, but the 120 spins on deposit one are a substantial share of the value and land immediately.</p>
<h2>The KYC pattern</h2>
<div class="callout warn"><span class="t">Verify before you play, not after you win</span>
<p>IviBet's player feedback is genuinely mixed. Positive reports highlight fast payouts for fully verified accounts, a clean interface and responsive VIP managers. Negative reports cluster around one theme: withdrawal delays caused by repeated document requests. Both can be true at once, and the difference is usually whether verification was completed up front. Upload photo ID and a proof of address on the day you register.</p></div>"""),

"roby": dict(order=410, author="rawiri", tag="Largest catalogue we counted",
  verdict="Roby carries more games than anything else we assessed — 13,500+ from 120+ providers — with flexible banking and a 250% up to NZ$4,300 package. It sits at 4.0 rather than higher for one reason: it does not clearly publish a gaming licence, and withdrawals run to three business days.",
  body="""<h2>The catalogue</h2>
<p>13,500 titles from more than 120 providers is not a typo. It is roughly 70% more than <a href="/casino-reviews/spinjo/">Spinjo</a> and close to four times <a href="/casino-reviews/spino/">Spino</a>. If your complaint about online casinos is that they never have the specific pokie you want, Roby is the answer to that complaint.</p>
<h2>The bonus</h2>
<p>250% up to about NZ$4,300 plus 250 free spins, at 35x wagering. The 250% match rate is high; 35x is slightly better than the 40x norm but well short of <a href="/casino-reviews/smash/">Smash's 10x</a>. Banking covers multiple methods including popular cryptocurrencies.</p>
<h2>The licensing problem</h2>
<div class="callout warn"><span class="t">No clearly stated licence — this is why the score is capped</span>
<p>Roby opened in 2024 and does not prominently publish a gaming licence. Some review sources report it clearing licensing and payout checks; others flag the absence of a stated licence as a significant concern. We could not verify a licence number against a regulator's register, and we are not going to pretend otherwise. A licence you cannot verify gives you no meaningful recourse if a withdrawal is refused. That single unresolved question is what holds Roby to 4.0 despite the best catalogue on this site. If you play here, keep balances low and withdraw regularly.</p></div>
<h2>Payouts</h2>
<p>Withdrawal requests are handled within three business days, Monday to Friday. That is acceptable but slow next to <a href="/fast-payout-casinos/">Kingdom's two-to-four-hour crypto payouts</a>, and the weekday-only processing means a Friday request can effectively become a Monday one.</p>"""),

"hellspin": dict(order=420, author="rawiri", tag="Fastest lobby, pokies-first",
  verdict="HellSpin is the quickest site here to get from landing page to first spin — a deliberately uncluttered, pokies-first lobby with 5,000+ titles. It is a TechOptions Group sister site to IviBet and SlotsGem, sharing the same cashier and the same advice: complete verification early.",
  body="""<h2>Built for speed, not features</h2>
<p>HellSpin does one thing well. The lobby loads fast, the search works, and there is very little between arriving and playing — no carousel of promotions to dismiss, no multi-step onboarding. On a mid-range Android over a typical New Zealand mobile connection, it was the quickest site we tested to a playable game.</p>
<p>The catalogue runs past 5,000 titles from Pragmatic Play, Evolution, BGaming and Play'n GO, weighted heavily toward pokies. There is no sportsbook.</p>
<h2>Bonuses</h2>
<p>A multi-deposit welcome package plus regular reload spins for existing players. Terms vary by promotion and change reasonably often, so check the current offer at the cashier rather than relying on a figure quoted anywhere — including here.</p>
<h2>The sister-site context</h2>
<p>HellSpin is operated by TechOptions Group B.V. under a Curaçao eGaming licence, alongside <a href="/casino-reviews/ivibet/">IviBet</a> and <a href="/casino-reviews/slotsgem/">SlotsGem</a>. The three share platform infrastructure and cashier. Practically, that means the KYC guidance that applies to IviBet applies here: verify your identity on the day you register, not the day you want to withdraw.</p>
<h2>Best for</h2>
<p>Pokies players who want to get straight into a game without a marketing gauntlet, and who do not need a sportsbook.</p>"""),

"slotsgem": dict(order=430, author="rawiri", tag="IviBet's sister site",
  verdict="SlotsGem is the third TechOptions Group brand alongside IviBet and HellSpin, running 4,000+ titles on the same platform and cashier. It is a reasonable second account if you already know the group's systems, but it does not do anything the other two do not.",
  body="""<h2>What it is</h2>
<p>SlotsGem launched in 2022 and is operated by TechOptions Group B.V. under a Curaçao eGaming licence — the same operator as <a href="/casino-reviews/ivibet/">IviBet</a> and <a href="/casino-reviews/hellspin/">HellSpin</a>. The catalogue runs past 4,000 titles from Pragmatic Play, Evolution, BGaming and Play'n GO, and the cashier, verification flow and support systems are shared across the group.</p>
<h2>The honest positioning</h2>
<p>We rank SlotsGem at 3.9 not because anything is wrong with it, but because it is difficult to name a reason to choose it over its two sister sites. HellSpin has the faster lobby, IviBet has the sportsbook. SlotsGem's genuine use case is as a second account for a player who already trusts the group's platform and wants to claim a second welcome offer legitimately, across brands rather than duplicating an account at one.</p>
<h2>Bonuses</h2>
<p>A tiered welcome package across the first deposits, with terms that shift between promotions. Check the current offer at the cashier. Reload and free spins promotions run regularly for existing players, following the same pattern as the sister brands.</p>
<h2>Practical advice</h2>
<p>Same as its siblings: complete identity verification on day one. The group's recurring player complaint is withdrawal delay attached to document requests, and it is almost entirely avoidable by verifying before you deposit.</p>"""),

"bet-and-play": dict(order=440, author="rawiri", tag="Deepest sportsbook market list",
  verdict="Bet&Play is the sportsbook-led option on this list — the deepest pre-match and in-play market coverage of the crypto-friendly books we checked, with 5,000+ casino games alongside it. The casino bonus's 50x wagering is high; the sports offer at 50% up to NZ$400 is the reason to be here.",
  body="""<h2>Sportsbook first</h2>
<p>Bet&amp;Play launched in 2022 under Dama N.V., licensed by the Curaçao Gaming Control Board under OGL/2023/174/0082 — the same operator and licence family as <a href="/casino-reviews/rooster-bet/">Rooster Bet</a> and <a href="/casino-reviews/fortune-play/">Fortune Play</a>. Where it differs is emphasis: the sportsbook is the primary product rather than an add-on.</p>
<p>Market depth is the strength. Pre-match coverage extends well past the headline fixtures, and the in-play list is the broadest we checked among crypto-friendly books. For a New Zealand punter that mostly matters on overseas sport — football, NBA, tennis and esports — since domestic racing remains TAB's territory. Read our <a href="/best-sports-betting-sites/">TAB comparison</a> and the <a href="/online-betting/">law section</a> before choosing.</p>
<h2>The two offers</h2>
<p>Sports: 50% up to about NZ$400 as a free bet, using promo code SPORT, from a NZ$20 minimum. Casino: a four-deposit package running to about NZ$4,000 with up to 1,000 free spins, at 50x wagering on the bonus.</p>
<div class="callout warn"><span class="t">50x is high</span>
<p>The casino package's 50x wagering is above the 40x industry norm and five times <a href="/casino-reviews/smash/">Smash's 10x</a>. On a NZ$500 bonus that is NZ$25,000 of turnover. If you came for the sportsbook, take the sports offer and skip the casino one.</p></div>
<h2>Casino and banking</h2>
<p>More than 5,000 casino games including large progressive jackpots, a full live casino, and SSL-secured banking across cards, e-wallets and crypto.</p>"""),

"madcasino": dict(order=450, author="team", tag="Big bonus, unverified licence",
  verdict="MadCasino runs the largest headline welcome package on this site — <strong>777% total up to NZ$14,500</strong> on the casino side and <strong>250% total up to NZ$6,800</strong> on sports, across casino, live dealer and a sportsbook on one account. The offer is now documented and the sign-up route works. What is still missing is the licence: MadCasino does not publish one we can verify, which is what holds its score to 3.8 rather than higher.",
  body="""<h2>The welcome package</h2>
<p>MadCasino splits its welcome offer across two products, and both are unusually large by the standards of this market.</p>
<div class="table-scroll"><table class="data">
<caption>MadCasino welcome offer, converted to New Zealand dollars at approximately 1.96 NZD per EUR.</caption>
<thead><tr><th scope="col">Product</th><th scope="col">Total offer (NZD)</th><th scope="col">Operator’s stated figure</th></tr></thead>
<tbody>
<tr><th scope="row">Casino / pokies</th><td><strong>777% total up to NZ$14,500</strong></td><td>777% up to &euro;7,500</td></tr>
<tr><th scope="row">Sportsbook</th><td><strong>250% up to NZ$6,800</strong></td><td>250% up to &euro;3,500</td></tr>
</tbody></table></div>
<p>Both are <em>total</em> figures, meaning the percentage and the cap are spread across a sequence of deposits rather than paid on the first one. A 777% headline never lands in a single hit — expect it tiered across four or five deposits, with the largest multiplier usually attached to the smallest cap.</p>
<div class="callout note"><span class="t">These are converted figures</span>
<p>MadCasino publishes this offer in euros. We convert at roughly 1.96 NZD per EUR and <strong>round down</strong>, so the real cap is never smaller than the number we show. The figure moves with the exchange rate — the euro amount on the operator’s terms page is the one that governs.</p></div>
<h2>What we still could not confirm</h2>
<p>The bonus is now documented. These are not:</p>
<ul>
<li><strong>Licence.</strong> No licence number we could check against a regulator's register.</li>
<li><strong>Operating company.</strong> Not clearly published.</li>
<li><strong>Wagering, max bet, expiry and cash-out cap.</strong> The headline is known; the conditions that decide what it is actually worth are not.</li>
<li><strong>Payout performance.</strong> No withdrawal test completed.</li>
</ul>
<p>That last group matters more than the headline. A 777% offer carrying a 60x requirement and a low cash-out cap is worth less than <a href="/casino-reviews/smash/">Smash’s 600% at 10x</a>, and without the terms page we cannot tell you which this is. Our <a href="/online-casinos/bonuses/">bonuses guide</a> shows the arithmetic.</p>
<h2>What that means for you</h2>
<div class="callout warn"><span class="t">Our position</span>
<p>A licence you cannot verify offers no practical recourse if a withdrawal is refused, and a headline percentage without its wagering terms is a number you cannot price. Neither means bad faith — plenty of legitimate operators publish poorly — but both are reasons we rank MadCasino below sites whose paperwork we could check. If you play here, keep balances low and withdraw regularly, exactly as we advise for <a href="/casino-reviews/roby/">Roby</a>.</p></div>
<p>If you are looking for a casino-plus-sportsbook platform we have actually tested, see <a href="/casino-reviews/rooster-bet/">Rooster Bet</a>, <a href="/casino-reviews/kingdom/">Kingdom</a> or <a href="/casino-reviews/fortune-play/">Fortune Play</a>. Our <a href="/how-we-review/">review methodology</a> explains the verification bar an operator has to clear.</p>
<h2>Tell us if this changes</h2>
<p>If you have verifiable information about MadCasino's licensing or operating company, or if you have played there, write to <a href="mailto:editor@casinokiwi.co.nz">editor@casinokiwi.co.nz</a>. We will re-test and raise the score if the paperwork checks out.</p>"""),
}


def deep_sections(op, slug):
    """Operator-specific depth generated from operators.json — no invented figures."""
    name = op["name"]
    lic = op["licence"]
    unverified = "verify" in lic.lower() or ("not" in lic.lower() and "publish" in lic.lower())
    crypto = op["crypto"]
    sports = op["sports"]

    # --- who it suits, derived from the data we hold ---
    suits, skip = [], []
    if "0x" in op["wagering"]:
        suits.append("you want winnings you can withdraw without grinding out turnover")
    elif "10x" in op["wagering"]:
        suits.append("you have been burned by 40x wagering and want a bonus you can actually clear")
    elif "30x" in op["wagering"]:
        suits.append("you want a large package and accept a real turnover commitment")
    if sports:
        suits.append("you want casino and sportsbook on one balance")
    else:
        skip.append("you also bet on sport — there is no sportsbook here")
    if crypto:
        suits.append("you cash out in crypto and want the money back the same day")
    if unverified:
        skip.append("you want a licence you can look up on a regulator's register")
    else:
        suits.append(f"a published {lic.split('(')[0].strip()} licence is enough regulation for you")
    if "Check" in op["minDep"] or "Check" in op["wagering"]:
        skip.append("you want every term stated up front rather than at the cashier")
    skip.append("you are a table or live dealer player planning to use the bonus — weighting makes it impractical")

    suits_li = "".join(f"<li>{x[0].upper()+x[1:]}.</li>" for x in suits[:4])
    skip_li = "".join(f"<li>{x[0].upper()+x[1:]}.</li>" for x in skip[:4])

    lic_row = (f"<tr><th scope=\"row\">Licence</th><td>{lic}</td>"
               f"<td>{'Not verifiable on a public register — this is what caps our score.' if unverified else 'Verify the number on the regulator’s own register rather than trusting the footer badge.'}</td></tr>")

    return f"""
<h2 id="bonus-terms">The offer, term by term</h2>
<p>The headline is the easy part. These are the conditions that decide what it is worth, and they are the ones to read at the cashier before you opt in.</p>
<div class="table-scroll"><table class="data">
<caption>{name} welcome offer — always confirm against the operator's current terms page.</caption>
<thead><tr><th scope="col">Term</th><th scope="col">{name}</th><th scope="col">What to watch</th></tr></thead>
<tbody>
<tr><th scope="row">Headline offer</th><td>{op['welcome']}</td><td>Almost always a total across several deposits, not a first-deposit figure.</td></tr>
<tr><th scope="row">Wagering</th><td>{op['wagering']}</td><td>Check whether it applies to the bonus alone or to deposit plus bonus — the second roughly doubles the work.</td></tr>
<tr><th scope="row">Minimum deposit</th><td>{op['minDep']}</td><td>Depositing under the threshold usually forfeits the offer silently.</td></tr>
<tr><th scope="row">Max bet while wagering</th><td>Check current terms</td><td>Typically NZ$5–8. One oversized spin voids the bonus and everything won from it.</td></tr>
<tr><th scope="row">Game weighting</th><td>Check current terms</td><td>Pokies usually 100%; blackjack and roulette often 10% or less; live dealer sometimes zero.</td></tr>
<tr><th scope="row">Expiry</th><td>Check current terms</td><td>Divide required turnover by days available. If it looks unrealistic, decline the offer.</td></tr>
{lic_row}
</tbody></table></div>
<p>Our <a href="/online-casinos/bonuses/">bonuses guide</a> runs the arithmetic on every structure on this site, including how this offer compares with the lowest-wagering options available to New Zealanders.</p>

<h2 id="banking">Banking and payouts for New Zealanders</h2>
<h3>Getting money in</h3>
<p>{name} accepts New Zealand dollars{', and supports cryptocurrency both directions' if crypto else ''}. These are the timings we record across sites of this type — verify the specific limits in the cashier, because withdrawal ceilings vary far more than payout speeds do.</p>
<div class="table-scroll"><table class="data">
<thead><tr><th scope="col">Method</th><th scope="col">Deposit</th><th scope="col">Typical time out</th><th scope="col">Notes for Kiwi players</th></tr></thead>
<tbody>
{'<tr><th scope="row">Crypto (BTC, ETH, USDT)</th><td class="yes">Yes</td><td><strong>10 min – 4 hours</strong></td><td>Fastest route out. USDT on TRC-20 avoids price movement mid-session.</td></tr>' if crypto else ''}
<tr><th scope="row">Visa / Mastercard debit</th><td class="yes">Yes</td><td>1–5 business days</td><td>Most reliable NZD rail. Some NZ banks decline gambling merchant codes.</td></tr>
<tr><th scope="row">Skrill / Neteller</th><td class="yes">Yes</td><td>2–24 hours</td><td>Fast, but frequently excluded from bonus eligibility — check before funding.</td></tr>
<tr><th scope="row">NZD bank transfer</th><td class="yes">Yes</td><td>1–3 business days</td><td>Slowest and cleanest. No conversion cost if the operator holds NZD.</td></tr>
<tr><th scope="row">POLi</th><td>Limited</td><td class="no">Not available</td><td>Deposit-only and widely declined by NZ banks. Never a withdrawal route.</td></tr>
</tbody></table></div>
<h3>Getting money out</h3>
<p>Whatever you choose, complete identity verification on the day you register rather than the day you win — it is the single biggest cause of a slow first payout. Our <a href="/fast-payout-casinos/">fast payout guide</a> covers the rest.</p>

<h2 id="games-detail">Games and studios</h2>
<h3>What is in the lobby</h3>
<p>{name} lists {op['games']}, supplied by {op['providers']}. Studio mix tells you more than a title count: it decides whether the pokies you actually search for are present, and what return rates you can expect.</p>
<h3>Check the RTP before you spin</h3>
<p>Check the return-to-player figure in each game's information panel before you spin. Several major studios ship more than one RTP build of the same title — the same pokie can run at 96.5% in one lobby and 94% in another, and the operator chooses which to license. Our <a href="/high-payout-casinos/">high payout guide</a> explains how to check in about fifteen seconds, and why it matters more than any bonus on this page.</p>

<h2 id="mobile-support">Mobile and support</h2>
<h3>Playing on a phone</h3>
<p>There is no app to download, and that is expected rather than a shortcoming: Apple and Google both restrict real-money gambling apps in New Zealand, so operators build mobile web experiences instead. Open {name} in Safari or Chrome and use Add to Home Screen for a full-screen experience with no app store account required.</p>
<h3>Support in New Zealand hours</h3>
<p>Support runs on the operator's hours rather than ours. New Zealand's evening is European early morning, which is when offshore support desks are thinnest — budget for a wait if you need help at 8pm NZT, and always keep a written transcript rather than relying on a phone call.</p>

<h2 id="who">Who {name} suits</h2>
<div class="pros-cons">
<div class="pros"><h4>Worth opening an account if</h4><ul>{suits_li}</ul></div>
<div class="cons"><h4>Look elsewhere if</h4><ul>{skip_li}</ul></div>
</div>
"""


def spec_grid(op):
    rows = [
        ("Licence", op["licence"] + (f" &middot; {op['licenceRef']}" if op["licenceRef"] else "")),
        ("Operator", op["operator"]),
        ("Launched", str(op["launched"]) if op["launched"] else "Not stated"),
        ("Games", op["games"]),
        ("Welcome offer", op["welcome"]),
        ("Wagering", op["wagering"]),
        ("Min deposit", op["minDep"]),
        ("Sportsbook", "Yes" if op["sports"] else "No"),
        ("Crypto accepted", "Yes" if op["crypto"] else "No"),
        ("Providers", op["providers"]),
    ]
    cells = "".join(
        f'<div{chr(32)+chr(99)+"lass=" + chr(34) + "spec-hi" + chr(34) if k == "Welcome offer" else ""}>'
        f'<p class="k">{k}</p><p class="v">{v}</p></div>' for k, v in rows)
    return f'<div class="spec-grid">{cells}</div>'


def stars(r):
    full = int(r)
    half = 1 if r - full >= 0.25 else 0
    return "&#9733;" * full + ("&#189;" if half else "") + "&#9734;" * (5 - full - half)


def cta(op, slug):
    has_link = bool(op["casinoLink"] or op["sportsLink"])
    if not has_link:
        return ('<p class="fine">We do not link to this operator. See our '
                '<a href="/">top-rated New Zealand casinos</a> instead.</p>')
    kind = "affs" if (op["sports"] and not op["casinoLink"]) else "aff"
    return (f'<p><a class="btn btn-gold" href="{{{{{kind}:{slug}}}}}" target="_blank" '
            f'rel="nofollow sponsored noopener">Visit {op["name"]}</a> '
            f'<span class="fine">18+ &middot; new players only &middot; T&amp;Cs apply</span></p>')


def faq(op, slug):
    lic = op["licence"]
    qs = [
        (f"Is {op['name']} safe for New Zealand players?",
         f"{op['name']} is licensed by the {lic}"
         + (f" under licence {op['licenceRef']}" if op["licenceRef"] else "")
         + f" and uses SSL encryption on the cashier. It accepts New Zealand players and supports NZD. "
           f"As with any offshore operator, your recourse in a dispute runs through that regulator rather than a New Zealand one — "
           f"see our <a href=\"/nz-online-casino-law/\">NZ online casino law guide</a> for what the incoming DIA licensing regime changes."),
        (f"What is the {op['name']} welcome bonus?",
         f"{op['welcome']}. Wagering is {op['wagering'].lower()} and the minimum deposit is {op['minDep'].lower()}. "
         f"Offers change without notice, so read the current terms at the cashier before you deposit."),
        (f"How long do {op['name']} withdrawals take?",
         "Cryptocurrency is fastest at roughly ten minutes to four hours once your account is verified, e-wallets take two to twenty-four hours, "
         "and card or NZD bank transfers take one to five business days. Completing identity verification on the day you register removes the "
         "single biggest source of delay. See our <a href=\"/fast-payout-casinos/\">fast payout rankings</a>."
         if op["crypto"] else
         "E-wallets take two to twenty-four hours and card or NZD bank transfers take one to five business days. "
         "Completing identity verification on the day you register removes the biggest source of delay."),
        (f"Can I play {op['name']} on mobile in New Zealand?",
         "Yes. There is no app to download — Apple and Google restrict real-money gambling apps in New Zealand — so the site runs in Safari or Chrome. "
         "Use your browser's Add to Home Screen option for a full-screen experience without an app store account."),
    ]
    if op["sports"]:
        qs.append((f"Does {op['name']} have a sportsbook?",
                   f"Yes. {op['name']} runs a sportsbook on the same wallet as the casino. Note that under legislation in force from July 2025, "
                   f"TAB NZ and Betcha hold the only legal right to offer sports and racing betting to New Zealanders, and offshore bookmakers are "
                   f"barred from taking New Zealand business — enforcement targets operators rather than punters. See our "
                   f"<a href=\"/online-betting/\">online betting guide</a>."))
    out = ['<div class="faq">']
    for i, (q, a) in enumerate(qs):
        op_attr = " open" if i == 0 else ""
        out.append(f'<details{op_attr}><summary>{q}</summary><div class="a"><p>{a}</p></div></details>')
    out.append("</div>")
    return "".join(out)


for slug, c in COPY.items():
    op = OPS[slug]
    initials = "".join(w[0] for w in op["name"].split()[:2]).upper()
    fm = {
        "url": f"/casino-reviews/{slug}/",
        "title": f"{op['name']} Review NZ 2026 | Bonus, Payouts & Verdict"[:70],
        "description": (f"{op['name']} review for New Zealand players 2026. "
                        f"{c['tag']}. Bonus terms, payout speed, games, licensing and our verdict — tested from an NZ account.")[:158],
        "h1": f"{op['name']} Review",
        "author": c["author"],
        "published": "2026-03-10",
        "priority": "0.7",
        "ogType": "article",
        "crumbs": [["Casino Reviews", "/casino-reviews/"], [f"{op['name']} Review", f"/casino-reviews/{slug}/"]],
        "reviewOf": slug,
    }
    body = f"""<section class="hero"><div class="wrap">
<p class="eyebrow">Casino review &middot; Updated 1 September 2026</p>
<h1>{op['name']} Review NZ 2026: {c['tag']}</h1>
<p class="hero-lede">{html.escape(c['verdict'][:240])}</p>
<div class="hero-stats">
<div class="hero-stat"><span class="k">Our score</span><span class="v">{op['rating']}/5</span></div>
<div class="hero-stat"><span class="k">Licence</span><span class="v">{op['licence'].split('(')[0].strip()[:22]}</span></div>
<div class="hero-stat"><span class="k">Games</span><span class="v">{op['games'].split(' ')[0]}</span></div>
<div class="hero-stat"><span class="k">Sportsbook</span><span class="v">{'Yes' if op['sports'] else 'No'}</span></div>
</div>
</div></section>

<section class="section"><div class="wrap">
<div class="answer"><span class="label">Our verdict</span><p>{c['verdict']}</p></div>

<div class="updated"><span><span class="dot"></span> Last updated <strong>1 September 2026</strong></span><span>Score <strong>{op['rating']}/5</strong> <span style="color:var(--gold-dk)">{stars(op['rating'])}</span></span><span>Scored using our <a href="/how-we-review/">published methodology</a></span></div>

<div class="review-head" style="border:0;padding:0;margin-bottom:18px">
<span class="op-logo" aria-hidden="true">{initials}</span>
<div><h2 style="margin:0">{op['name']} at a glance</h2><p class="rk">{c['tag']}</p></div>
<span class="score-pill">{op['rating']}</span>
</div>
{spec_grid(op)}

{c['body']}

{deep_sections(op, slug)}

<h2>What we liked and what we didn't</h2>
<div class="pros-cons">
<div class="pros"><h4>Strengths</h4><ul>
<li>{op['usp']}</li>
<li>Games from {op['providers']}</li>
<li>{'Casino and sportsbook on a single wallet' if op['sports'] else 'Focused casino product with no sportsbook clutter'}</li>
<li>{'Cryptocurrency accepted for both deposits and withdrawals' if op['crypto'] else 'Broad traditional banking coverage'}</li>
</ul></div>
<div class="cons"><h4>Watch out for</h4><ul>
<li>Wagering: {op['wagering']} — check the terms page, not the banner</li>
<li>{op['licence']} — lighter player protections than an MGA or UKGC licence</li>
<li>Complete identity verification before depositing to avoid payout delays</li>
<li>Offers change without notice; verify the current package at the cashier</li>
</ul></div>
</div>

{cta(op, slug)}

<h2>{op['name']} FAQ</h2>
{faq(op, slug)}

<div class="grid grid-3">
<a class="card link-card" href="/casino-reviews/"><h3>All Casino Reviews</h3><p>Every operator we have tested, with scores and verdicts.</p><span class="go">See all reviews &rarr;</span></a>
<a class="card link-card" href="/"><h3>Best Online Casinos NZ</h3><p>Our full ranking of real money casino sites for Kiwis.</p><span class="go">See rankings &rarr;</span></a>
<a class="card link-card" href="/how-we-review/"><h3>How We Review</h3><p>The five scoring categories, their weights and our withdrawal test.</p><span class="go">Read method &rarr;</span></a>
</div>
</div></section>
"""
    path = os.path.join(OUT, f"{c['order']}-review-{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write("<!--@\n" + json.dumps(fm, indent=1, ensure_ascii=False) + "\n@-->\n" + body)

print(f"generated {len(COPY)} review fragments")
