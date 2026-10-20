"""Builds the Success stories pages (success-stories/ and one folder per story) from the STORIES list below.

Run from the repo root:  python tools/build_stories.py
To add images to a story, put them in assets/stories/<slug>/ and list them under "figures" as
(file name, caption, number of paragraphs to place the image after).
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://bombridgegroup.com"
PUBLISHED = "2026-10-20"

STORIES = [
    {
        "slug": "genicalc",
        "client": "GeniCalc",
        "menu": "GeniCalc, AI calculator",
        "client_url": "https://www.genicalc.com/",
        "product": "AI scientific calculator",
        "where": "China",
        "title": "From a troubled prototype to the right manufacturing partner",
        "sub": "A European founder, a failed first supplier, and a product that is now better and cheaper than its rivals.",
        "description": "How BOM Bridge Group helped GeniCalc repair a faulty prototype of its AI scientific calculator, "
                       "find a partner to redevelop and manufacture it in China, and cut the unit cost from €70 to €40.",
        "services": "Prototype assessment · Manufacturer sourcing · Factory visits in China · Negotiation",
        "body": [
            "GeniCalc, a Cyprus-based startup building an AI scientific calculator for students, came to us with what "
            "looked like a simple brief, find a factory in China able to reproduce a prototype they had already "
            "developed with other suppliers. The prototype did not work properly though, so before recommending anyone "
            "we had it sent over and spent almost a week with technicians diagnosing and repairing it.",
            "Fixing it showed the real problem, the design itself was too expensive and not suited to production at "
            "scale, as the overseas design work they had paid for left it buggy and hard to manufacture. Together with "
            "Amaury we changed the brief, from copying the prototype to finding a partner able to redevelop and "
            "manufacture a commercially viable version, and as the product was quite new we looked at several types of "
            "electronics manufacturers, got quotes from more than ten factories, visited eight and shortlisted four for "
            "him to meet in China.",
            "We organised the factory visits and supported the negotiations on the ground in Mandarin, and after three "
            "rounds GeniCalc chose a partner for both redevelopment and manufacturing. The new professional design cost "
            "around €12k, barely more than the failed one, and brought the unit cost down from €70 to €40, 43% less, "
            "for a calculator that is now better and cheaper than the AI education devices already on the market.",
        ],
        "stats": [
            ("−43% unit cost", "From €70 to €40 per unit"),
            ("10", "Facilities benchmarked for optimal price-to-tolerance ratios"),
            ("4", "Credible factories vetted in person, the rest filtered out"),
            ("~€12k", "Professional design cost, barely more than the failed cheap design, and it worked"),
            ("Better &amp; cheaper", "Than competing AI educational products already on the market"),
        ],
        "person": {
            "name": "Amaury Clerens",
            "role": "Co-founder, GeniCalc",
            "photo": "assets/people/amaury-clerens.jpg",
            "linkedin": "https://www.linkedin.com/in/amaury-clerens-979ba7146/",
        },
        "quote": ("This would not have happened without him.", "Amaury Clerens, European co-founder"),
        "footnote": "Figures from the founder’s engagement records.",
        "card_figure": ("−43%", "Unit cost, from €70 to €40"),
        "figures": [],
    },
    {
        "slug": "sleke",
        "client": "SLEKE",
        "menu": "SLEKE, smartphone",
        "client_url": "https://sleke.io/",
        "product": "Compact premium smartphone",
        "where": "Shenzhen, Guangdong",
        "title": "Helping a smartphone startup secure better manufacturing terms",
        "sub": "Five factories in four days gave the founders behind SLEKE a real comparison, better terms and a signed "
               "manufacturing agreement.",
        "description": "How BOM Bridge Group built the hardware supply chain for a smartphone project by the founders of "
                       "SLEKE: five factories in Guangdong in four days, better terms, a revised contract and a "
                       "financial model.",
        "services": "Manufacturer sourcing · Factory visits in Guangdong · Negotiation · Contract review · Financial model",
        "body": [
            "The founders of SLEKE, who sell a distraction-free phone built on refurbished Google Pixels, asked us to "
            "help build the hardware supply chain for a side company of theirs, a compact and premium smartphone with a "
            "minimalist user experience. They came to us shortly before signing with a manufacturer they had met at an "
            "industry event, without having compared any other factory, so we recommended comparing options in person "
            "first, and over the following month we found four more suitable manufacturers and got them interested, "
            "which was not easy as an early-stage startup cannot promise the steady volumes factories prefer.",
            "When the two founders arrived in Shenzhen we took them to five factories across Guangdong in four days, "
            "and the factories differed on development fees, minimum order quantities, product experience, technical "
            "capability and timelines, we also helped them refine the specifications and weigh up the chipset and "
            "connectivity options. Two factories stood out, and having a credible alternative gave the founders a "
            "stronger position with their original contact, who improved the terms and was chosen in the end.",
            "In the week after the visits our legal team helped rework the payment milestones and the one-sided clauses "
            "in the contract, and our financial model showed the project would need more capital than expected, which "
            "helped the founders plan how to fund development and launch. The manufacturing "
            "agreement is now signed, development is underway and they have a first sample as they prepare their "
            "Kickstarter campaign.",
        ],
        "stats": [
            ("5", "Factories visited across Guangdong in four days"),
            ("4", "New manufacturers found and interested within a month"),
            ("2", "Finalists compared on terms and capability"),
            ("Signed", "Manufacturing agreement, with a first sample made"),
        ],
        "person": None,
        "quote": None,
        "footnote": None,
        "card_figure": ("5", "Factories visited in four days"),
        "figures": [],
    },
]

E = html.escape


def head(title, description, canonical, depth, extra_ld):
    root = "../" * depth
    ld = "\n".join(f'<script type="application/ld+json">\n{json.dumps(x, ensure_ascii=False)}\n</script>' for x in extra_ld)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(description)}">
<meta name="theme-color" content="#003763">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="{root}assets/logo/favicon.svg" type="image/svg+xml">

<meta property="og:type" content="article">
<meta property="og:site_name" content="BOM Bridge Group">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">

{ld}

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@400;500;600;700&family=Carlito:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}css/tokens.css">
<link rel="stylesheet" href="{root}css/main.css">
</head>
<body>

<a class="skip" href="#top">Skip to content</a>
"""


MARK = """<svg viewBox="-13 -4 90 61.5" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="BOM Bridge Group compass mark"{style}>
        <path d="M54 28 H59.5 M10 28 H4.5 M32 3.5 V-2 M32 50 V55.5" stroke="{tick}" stroke-width="1.4" fill="none"/>
        <path d="M51.05 17 L55.82 14.25 M43 8.95 L45.75 4.18 M21 8.95 L18.25 4.18 M12.95 17 L8.18 14.25 M51.05 39 L55.82 41.75 M43 47.05 L45.75 51.82 M21 47.05 L18.25 51.82 M12.95 39 L8.18 41.75" stroke="{tick}" stroke-width="1.4" fill="none"/>
        <text x="-9.5" y="33" font-family="Bahnschrift,'Barlow Semi Condensed',sans-serif" font-size="14.3" font-weight="700" fill="#71B7E4">W</text>
        <text x="62" y="33" font-family="Bahnschrift,'Barlow Semi Condensed',sans-serif" font-size="14.3" font-weight="700" fill="#71B7E4">E</text>
        <path d="M9 28 H55" stroke="{bridge}" stroke-width="3.4" fill="none"/>
        <path d="M32 6 V43.1" stroke="{bridge}" stroke-width="3"/>
        <path d="M32 12 L13 28" stroke="{bridge}" stroke-width="1.8" fill="none"/>
        <path d="M32 12 L51 28" stroke="{bridge}" stroke-width="1.8" fill="none"/>
      </svg>"""


def header(depth):
    root = "../" * depth
    items = "\n".join(f'          <a href="{root}success-stories/{s["slug"]}/">{E(s["menu"])}</a>' for s in STORIES)
    return f"""
<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="{root}" aria-label="BOM Bridge Group, home">
      {MARK.format(style="", tick="#B8DBF1", bridge="#0067B1")}
      <span class="brand-text">
        <span class="brand-name">BOM Bridge</span>
        <span class="brand-sub">Group</span>
      </span>
    </a>
    <button class="btn btn--secondary nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <a href="{root}#problem">Problem</a>
      <a href="{root}#how">How we work</a>
      <a href="{root}#team">Team</a>
      <a href="{root}#network">Network</a>
      <a href="{root}#clients">Clients</a>
      <div class="nav-dd">
        <button class="nav-dd-toggle" type="button" aria-expanded="false" aria-controls="nav-stories">Success stories
          <svg width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4.5 L6 8.5 L10 4.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>
        </button>
        <div class="nav-dd-panel" id="nav-stories" hidden>
{items}
          <a href="{root}success-stories/">All success stories</a>
        </div>
      </div>
      <a class="btn" href="{root}#connect">Connect with us</a>
    </nav>
  </div>
</header>
"""


def footer(depth):
    root = "../" * depth
    return f"""
<footer class="footer">
  <div class="wrap">
    <div class="footer-inner">
      <div class="brand" aria-label="BOM Bridge Group">
        {MARK.format(style=' style="height:40px;width:auto"', tick="rgba(184,219,241,0.45)", bridge="#FFFFFF")}
        <span class="brand-text">
          <span class="brand-name">BOM Bridge</span>
          <span class="brand-sub">Group</span>
        </span>
      </div>
      <div class="footer-labels">
        <span>© 2026 BOM Bridge Group</span>
        <span>Benchmark · Negotiate · Verify, On the ground in China</span>
      </div>
    </div>
  </div>
</footer>

<script src="{root}js/site.js"></script>
</body>
</html>
"""


def cta(depth):
    root = "../" * depth
    return f"""    <div class="callout story-cta">
      <div>
        <h3>Planning a hardware project in China?</h3>
        <p>Talk to us about finding and evaluating the right manufacturing partner.</p>
      </div>
      <a class="btn btn--on-dark" href="{root}#connect">Get your 48-hour benchmark</a>
    </div>
"""


def story_card(s, root):
    fig, label = s["card_figure"]
    return f"""      <a class="card story-card" href="{root}success-stories/{s['slug']}/">
        <p class="case-label">{E(s['client'])} · {E(s['product'])}</p>
        <h3>{E(s['title'])}</h3>
        <p class="figure">{fig}<span class="figure-label" style="display:block">{E(label)}</span></p>
        <span class="story-read">Read the story</span>
      </a>"""


def org():
    return {"@type": "Organization", "name": "BOM Bridge Group", "url": f"{SITE}/",
            "logo": f"{SITE}/assets/logo/compass-blue.png"}


def build_story(s):
    depth = 2
    root = "../" * depth
    url = f"{SITE}/success-stories/{s['slug']}/"
    article = {
        "@context": "https://schema.org", "@type": "Article", "headline": s["title"], "description": s["description"],
        "datePublished": PUBLISHED, "dateModified": PUBLISHED, "author": org(), "publisher": org(),
        "mainEntityOfPage": url, "image": f"{SITE}/assets/og/og-image.png",
        "about": {"@type": "Organization", "name": s["client"], "url": s["client_url"]},
    }
    if s["person"]:
        p = s["person"]
        article["mentions"] = {"@type": "Person", "name": p["name"], "jobTitle": p["role"], "sameAs": p["linkedin"],
                               "image": f"{SITE}/{p['photo']}"}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "Success stories", "item": f"{SITE}/success-stories/"},
        {"@type": "ListItem", "position": 3, "name": s["client"], "item": url}]}

    paras = []
    figs = {after: (f, cap) for f, cap, after in s["figures"]}
    for i, text in enumerate(s["body"], 1):
        paras.append(f"        <p>{E(text)}</p>")
        if i in figs:
            f, cap = figs[i]
            paras.append(f'        <figure class="story-figure"><img src="{root}assets/stories/{s["slug"]}/{f}" alt="{E(cap)}" loading="lazy">'
                         f"<figcaption>{E(cap)}</figcaption></figure>")
    stats = "\n".join(f'        <div class="stat"><p class="figure">{fig}<span class="figure-label" style="display:block">{E(label)}</span></p></div>'
                      for fig, label in s["stats"])

    person = ""
    if s["person"]:
        p = s["person"]
        person = f"""
    <div class="person" style="padding-bottom:0">
      <div class="portrait"><img src="{root}{p['photo']}" alt="Portrait of {E(p['name'])}" width="240" height="240"></div>
      <div>
        <h3>{E(p['name'])}</h3>
        <p class="role">{E(p['role'])}</p>
        <p class="cv"><a href="{p['linkedin']}" rel="noopener" target="_blank">LinkedIn</a> · <a href="{s['client_url']}" rel="noopener" target="_blank">{E(s['client_url'].split('//')[1].strip('/'))}</a></p>
      </div>
    </div>"""
    quote = ""
    if s["quote"]:
        q, attr = s["quote"]
        p = s["person"]
        quote = f"""
    <hr class="rule">
    <div class="story-quote">
      <div class="portrait"><img src="{root}{p['photo']}" alt="" width="240" height="240" loading="lazy"></div>
      <blockquote class="quote quote--closer" style="margin:0">“{E(q)}”
        <span class="quote-attr"><a href="{p['linkedin']}" rel="noopener" target="_blank">{E(attr)}</a></span>
      </blockquote>
    </div>"""
    footnote = f'\n    <p class="footnote">{E(s["footnote"])}</p>' if s["footnote"] else ""
    client_link = f'<a href="{s["client_url"]}" rel="noopener" target="_blank">{E(s["client"])}</a>'

    page = head(f"{s['title']} | {s['client']} | BOM Bridge Group", s["description"], url, depth, [article, crumbs])
    page += header(depth)
    page += f"""
<main id="top">
<article class="section">
  <div class="wrap">
    <p class="eyebrow crumbs"><a href="{root}success-stories/">Success stories</a> / {E(s['client'])}</p>
    <h1>{E(s['title'])}</h1>
    <p class="section-sub">{E(s['sub'])}</p>
    <ul class="story-meta">
      <li><b>Client</b>{client_link}</li>
      <li><b>Product</b>{E(s['product'])}</li>
      <li><b>Where</b>{E(s['where'])}</li>
      <li><b>What we did</b>{E(s['services'])}</li>
    </ul>{person}
    <hr class="rule">
    <div class="story-grid">
      <div class="story-body">
{chr(10).join(paras)}
      </div>
      <aside class="story-aside" aria-label="Key figures">
{stats}
      </aside>
    </div>{quote}{footnote}
    <hr class="rule">
{cta(depth)}  </div>
</article>
</main>
"""
    page += footer(depth)
    out = ROOT / "success-stories" / s["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out


def build_index():
    depth = 1
    root = "../" * depth
    url = f"{SITE}/success-stories/"
    title = "Success stories | BOM Bridge Group"
    description = "Hardware projects BOM Bridge Group has helped make in China, from a troubled prototype to a smartphone sourced across Guangdong."
    coll = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Success stories", "url": url,
            "description": description, "publisher": org(),
            "mainEntity": {"@type": "ItemList", "itemListElement": [
                {"@type": "ListItem", "position": i, "url": f"{SITE}/success-stories/{s['slug']}/", "name": s["title"]}
                for i, s in enumerate(STORIES, 1)]}}
    cards = "\n".join(story_card(s, root) for s in STORIES)
    page = head(title, description, url, depth, [coll])
    page += header(depth)
    page += f"""
<main id="top">
<section class="section">
  <div class="wrap">
    <p class="eyebrow">Success Stories</p>
    <h1>Hardware we have helped make in China</h1>
    <p class="section-sub">An AI calculator rebuilt from a troubled prototype, and a smartphone sourced across Guangdong in four days.</p>
    <hr class="rule">
    <div class="story-cards">
{cards}
    </div>
    <hr class="rule">
{cta(depth)}  </div>
</section>
</main>
"""
    page += footer(depth)
    out = ROOT / "success-stories" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out


def build_sitemap():
    urls = [f"{SITE}/", f"{SITE}/success-stories/"] + [f"{SITE}/success-stories/{s['slug']}/" for s in STORIES]
    body = "\n".join(f"  <url><loc>{u}</loc><lastmod>{PUBLISHED}</lastmod></url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n',
        encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    for s in STORIES:
        print("wrote", build_story(s).relative_to(ROOT))
    print("wrote", build_index().relative_to(ROOT))
    build_sitemap()
    print("wrote sitemap.xml, robots.txt")
