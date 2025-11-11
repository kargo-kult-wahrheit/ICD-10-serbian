"""Command line entry point for scraping MKB-10 data."""

from __future__ import annotations

import argparse
import sys

from .scraper import scrape_to_csv


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scrape MKB-10 data into CSV")
    parser.add_argument(
        "-o",
        "--output",
        default="mkb10.csv",
        help="Path where the CSV file will be written (default: mkb10.csv)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.2,
        help="Delay in seconds between requests to avoid overwhelming the site",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        count = scrape_to_csv(args.output, delay=args.delay)
    except Exception as exc:  # pragma: no cover - convenience message
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Successfully wrote {count} entries to {args.output}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
