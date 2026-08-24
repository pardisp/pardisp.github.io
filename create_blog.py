"""Build the blog: _posts/post_N.html -> blog/post_N.html, blog.html, feed.xml, sitemap.xml

Each source post in _posts/ looks like:

    <title>...may contain markup and a trailing date...</title>
    <post> ...body html... </post>

blog_layout.html is the shell; the body is substituted for the placeholder.
Run from the repository root:  python3 create_blog.py
"""

import json
import os
import re
import shutil
from datetime import datetime, timezone
from email.utils import format_datetime
from xml.sax.saxutils import escape

SITE_URL = "https://pardisp.github.io"
SITE_TITLE = "Pardis Pashakhanloo"
FEED_TITLE = f"Random Notes by {SITE_TITLE}"
FEED_DESC = (
    "Notes on program analysis, deep learning for code, AI coding agents, "
    "and software security."
)

PLACEHOLDER = "[THE_PLACEHOLDER_FOR_BLOG_LAYOUT]"
DEFAULT_HEADING = '<h1 class="title">Random Notes</h1>'

BLOG_DESC = (
    "Notes by Pardis Pashakhanloo on program analysis, deep learning for code, "
    "AI coding agents, and software security."
)

with open("blog_layout.html") as f:
    layout = f.read()


def get_title(content):
    return re.findall(r"<title>(.*?)</title>", content, re.DOTALL)[0]


def get_body(content):
    return re.findall(r"<post>(.*?)</post>", content, re.DOTALL)[0]


def strip_tags(html):
    """Plain text from a fragment, for <title> tags and feed metadata."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"&nbsp;?", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def split_title(title_html):
    """Separate the headline from the trailing <small>date</small>, if present."""
    m = re.search(r"<small[^>]*>(.*?)</small>", title_html, re.DOTALL)
    date_text = strip_tags(m.group(1)) if m else ""
    without_date = re.sub(r"<small[^>]*>.*?</small>", "", title_html, flags=re.DOTALL)
    return strip_tags(without_date), date_text


def parse_date(date_text):
    """Posts date themselves as 'April 13, 2020' or 'March, 2024'."""
    for fmt in ("%B %d, %Y", "%B %d %Y", "%B, %Y", "%B %Y", "%b %d, %Y", "%b, %Y"):
        try:
            return datetime.strptime(date_text.strip(), fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def attr(text):
    """Escape a string for use inside a double-quoted HTML attribute."""
    return escape(text, {'"': "&quot;"})


def fill_meta(page, title, desc, url, og_type="website", jsonld=""):
    """Substitute the per-page head placeholders in blog_layout.html."""
    for token, value in (
        ("[PAGE_TITLE]", attr(title)),
        ("[PAGE_DESC]", attr(desc)),
        ("[PAGE_URL]", attr(url)),
        ("[PAGE_OG_TYPE]", og_type),
        ("[PAGE_JSONLD]", jsonld),
    ):
        page = page.replace(token, value)
    return page


def blogposting_jsonld(headline, desc, url, dt):
    """schema.org BlogPosting so search engines can show the post as an article."""
    fields = [
        '"@context": "https://schema.org"',
        '"@type": "BlogPosting"',
        f'"headline": {json.dumps(headline)}',
        f'"description": {json.dumps(desc)}',
        f'"url": {json.dumps(url)}',
        f'"mainEntityOfPage": {json.dumps(url)}',
        '"author": {"@type": "Person", "name": "Pardis Pashakhanloo",'
        ' "url": "https://pardisp.github.io/"}',
        '"publisher": {"@type": "Person", "name": "Pardis Pashakhanloo"}',
        '"inLanguage": "en"',
    ]
    if dt:
        fields.append(f'"datePublished": "{dt.date().isoformat()}"')
    body = ",\n        ".join(fields)
    return (
        '\n  <script type="application/ld+json">\n'
        "     {\n        " + body + "\n     }\n  </script>\n"
    )


def post_sort_key(name):
    """Numeric so post_10 sorts after post_9, not after post_1."""
    m = re.search(r"post_(\d+)", name)
    return int(m.group(1)) if m else -1


shutil.rmtree("blog", ignore_errors=True)
os.makedirs("blog")

posts = sorted(
    (p for p in os.listdir("_posts") if p.startswith("post") and p.endswith(".html")),
    key=post_sort_key,
    reverse=True,
)

titles_list = ""
feed_items = []
sitemap_urls = [(f"{SITE_URL}/", None), (f"{SITE_URL}/blog.html", None)]

for post in posts:
    with open(f"_posts/{post}") as f:
        content = f.read()
    title_html = get_title(content)
    body = get_body(content)
    headline, date_text = split_title(title_html)
    print(f"reading {post}  ({headline})")

    plain = strip_tags(body)
    excerpt = plain[:300].rsplit(" ", 1)[0] + "…"
    # Search engines truncate descriptions around 160 characters.
    meta_desc = plain[:155].rsplit(" ", 1)[0] + "…"
    url = f"{SITE_URL}/blog/{post}"
    dt = parse_date(date_text)

    page = layout.replace(DEFAULT_HEADING, f'<h1 class="title">{title_html}</h1>')
    page = page.replace(PLACEHOLDER, body)
    # Each post gets its own title, description, canonical URL, and article markup.
    page = fill_meta(
        page,
        title=headline,
        desc=meta_desc,
        url=url,
        og_type="article",
        jsonld=blogposting_jsonld(headline, meta_desc, url, dt),
    )
    with open(f"blog/{post}", "w") as f:
        f.write(page)

    titles_list += f'<p><a href="/blog/{post}">{title_html}</a></p>\n\n'
    sitemap_urls.append((url, dt))

    item = [
        "    <item>",
        f"      <title>{escape(headline)}</title>",
        f"      <link>{escape(url)}</link>",
        f'      <guid isPermaLink="true">{escape(url)}</guid>',
        f"      <description>{escape(excerpt)}</description>",
    ]
    if dt:
        item.append(f"      <pubDate>{format_datetime(dt)}</pubDate>")
    item.append("    </item>")
    feed_items.append("\n".join(item))

with open("blog.html", "w") as f:
    index_page = layout.replace(PLACEHOLDER, titles_list)
    f.write(fill_meta(
        index_page,
        title="Random Notes",
        desc=BLOG_DESC,
        url=f"{SITE_URL}/blog.html",
    ))
    f.write("\n")

with open("feed.xml", "w") as f:
    f.write("\n".join([
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
        "  <channel>",
        f"    <title>{escape(FEED_TITLE)}</title>",
        f"    <link>{SITE_URL}/blog.html</link>",
        f'    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>',
        f"    <description>{escape(FEED_DESC)}</description>",
        "    <language>en-us</language>",
        "\n".join(feed_items),
        "  </channel>",
        "</rss>",
        "",
    ]))

with open("sitemap.xml", "w") as f:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, dt in sitemap_urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(url)}</loc>")
        if dt:
            lines.append(f"    <lastmod>{dt.date().isoformat()}</lastmod>")
        lines.append("  </url>")
    lines += ["</urlset>", ""]
    f.write("\n".join(lines))

print(f"\nwrote {len(posts)} posts -> blog/, blog.html, feed.xml, sitemap.xml")
