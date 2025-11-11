"""Utilities for scraping MKB-10 codes from stetoskop.info."""

__all__ = ["scrape_to_csv", "MKBScraper", "MKBEntry"]

from .scraper import MKBScraper, MKBEntry, scrape_to_csv
