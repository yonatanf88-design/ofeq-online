import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from update_feed import safe_text, parse_date, SOURCES

class TestFeed(unittest.TestCase):
    def test_html(self):
        self.assertEqual(safe_text("<b>שלום</b> &amp; טוב"), "שלום & טוב")

    def test_date(self):
        self.assertEqual(parse_date("Mon, 16 Nov 2026 04:00:00 GMT").isoformat(), "2026-11-16T04:00:00+00:00")

    def test_sources(self):
        self.assertGreaterEqual(len(SOURCES), 5)

if __name__ == "__main__":
    unittest.main()
