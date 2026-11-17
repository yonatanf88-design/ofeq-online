import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from generate_insights import clean, parse_date, SCHEMA, load_existing, SOURCES

class InsightTests(unittest.TestCase):
    def test_html_clean(self):
        self.assertEqual(clean("<p>Value&nbsp; stream &amp; flow</p>"), "Value stream & flow")
    def test_rfc_date(self):
        self.assertEqual(parse_date("Mon, 16 Nov 2026 04:00:00 GMT").isoformat(), "2026-11-16T04:00:00+00:00")
    def test_schema(self):
        self.assertEqual(len(SCHEMA["required"]), 5)
        self.assertTrue(SCHEMA["additionalProperties"] is False)
    def test_sources(self):
        self.assertGreaterEqual(len(SOURCES), 3)
        self.assertTrue(all(src[2].startswith("https://") for src in SOURCES))
    def test_missing_current_cards_file(self):
        self.assertIsInstance(load_existing(), list)

if __name__ == "__main__":
    unittest.main()
