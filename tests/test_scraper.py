import unittest

from bs4 import BeautifulSoup

from mkb_scrape.scraper import MKBScraper, _strip_labels


class ParseHelpersTests(unittest.TestCase):
    def setUp(self) -> None:
        self.scraper = MKBScraper()

    def _soup(self, html: str) -> BeautifulSoup:
        return BeautifulSoup(html, "html.parser")

    def test_parse_structured_blocks_with_labels(self) -> None:
        html = """
        <div class="mkb-item">
            <span class="sifra">Šifra: A00</span>
            <span class="naziv">Opis: Kolera</span>
            <span class="latin">Latinski: Cholera</span>
        </div>
        """
        soup = self._soup(html)

        entries = self.scraper._parse_from_structured_blocks(soup)

        self.assertEqual(1, len(entries))
        entry = entries[0]
        self.assertEqual("A00", entry.code)
        self.assertEqual("Kolera", entry.serbian)
        self.assertEqual("Cholera", entry.latin)

    def test_parse_tables_strips_labels(self) -> None:
        html = """
        <table>
            <tr>
                <td>Šifra: B00</td>
                <td>Naziv: Herpes simpleks</td>
                <td>Latinski: Herpes simplex</td>
            </tr>
        </table>
        """
        soup = self._soup(html)

        entries = self.scraper._parse_from_tables(soup)

        self.assertEqual(1, len(entries))
        entry = entries[0]
        self.assertEqual("B00", entry.code)
        self.assertEqual("Herpes simpleks", entry.serbian)
        self.assertEqual("Herpes simplex", entry.latin)

    def test_strip_labels_handles_empty_strings(self) -> None:
        self.assertEqual("", _strip_labels(""))
        self.assertEqual("tekst", _strip_labels("Naziv: tekst"))
        self.assertEqual("tekst", _strip_labels("latinski - tekst"))


if __name__ == "__main__":
    unittest.main()
