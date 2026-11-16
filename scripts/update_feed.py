#!/usr/bin/env python3
"""Publish real sourced RSS headlines for Ofeq. Never fabricates articles."""
import datetime as dt
import hashlib
import html
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from email.utils import parsedate_to_datetime
from pathlib import Path

SOURCES = [
  ("תעשייה", "ייצור מזון OR מפעלי מזון OR תעשיית החלב"),
  ("מצוינות תפעולית", "מצוינות תפעולית OR שיפור פריון OR תעשייה 4.0"),
  ("כספים", "FP&A OR מנהלי כספים OR תקציב חברות תעשייה"),
  ("חדשנות ו-AI", "בינה מלאכותית מפעלים OR AI תעשייה"),
  ("מנהיגות", "ניהול עובדים OR מנהיגות ארגונית OR ניהול שינוי"),
  ("קריירה", "משרות פיננסים ניהול תעשייה OR שוק התעסוקה מנהלים"),
]
SITE = Path(__file__).resolve().parents[1] / "site"
FEED = SITE / "feed.json"

def safe_text(raw):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]*>", " ", raw or ""))).strip()[:280]

def parse_date(raw):
    try:
        return parsedate_to_datetime(raw).astimezone(dt.timezone.utc)
    except (TypeError, ValueError, OverflowError):
        return None

def fetch_category(category, query):
    params = urllib.parse.urlencode({"q": query, "hl": "he", "gl": "IL", "ceid": "IL:he"})
    url = "https://news.google.com/rss/search?" + params
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 OfeqDaily/2.0"})
    with urllib.request.urlopen(req, timeout=12) as response:
        raw = response.read(500000)
    xml = ET.fromstring(raw)
    items = []
    now = dt.datetime.now(dt.timezone.utc)
    for node in xml.findall(".//channel/item")[:12]:
        title = safe_text(node.findtext("title"))
        link = (node.findtext("link") or "").strip()
        when = parse_date(node.findtext("pubDate"))
        if not (title and link.startswith("https://") and when):
            continue
        age = now - when
        if age < dt.timedelta(hours=-2) or age > dt.timedelta(days=14):
            continue
        source = node.find("source")
        publisher = safe_text(source.text) if source is not None else "Google News"
        ident = hashlib.sha256((category + "|" + title + "|" + link).encode()).hexdigest()[:24]
        items.append({"id": ident, "title": title, "url": link, "category": category,
                      "source": publisher or "Google News", "published_at": when.isoformat(),
                      "type": "external_article", "language": "he"})
    return items

def main():
    collected, errors = [], []
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(fetch_category, cat, query): cat for cat, query in SOURCES}
        for future in as_completed(futures):
            try:
                collected.extend(future.result())
            except Exception as err:
                errors.append(f"{futures[future]}: {type(err).__name__}")
    unique = {x["id"]: x for x in collected}
    articles = sorted(unique.values(), key=lambda x: x["published_at"], reverse=True)[:40]
    if not articles:
        raise RuntimeError("No verified recent RSS headlines. Keeping last published feed. " + "; ".join(errors))
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
    payload = {"items": articles, "updated_at": timestamp, "attempted_at": timestamp,
               "errors": errors, "live": True, "refresh_interval_hours": 24}
    FEED.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Ofeq feed: {len(articles)} real sourced headlines, {len(errors)} feed errors")

if __name__ == "__main__":
    main()
