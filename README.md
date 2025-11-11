# MKB Scraper

This project contains a small Python utility that downloads the full list of
MKB-10 (ICD-10) entries from [stetoskop.info](https://www.stetoskop.info/mkb)
and stores them in a CSV file. The script was written for the Institute of
Public Health of Serbia "Dr Milan Jovanović Batut" to facilitate internal use of
the dataset.

> **Note:** Network access is disabled in the execution environment that built
> this repository, so the scraper could not be executed or validated from here.
> The code is ready to run in an environment with Internet access.

## Running locally

1. Ensure you have Python 3.9 or newer installed.
2. Install the dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the scraper:

   ```bash
   python -m mkb_scrape -o mkb10.csv
   ```

   The output CSV contains the columns `code`, `description_serbian`, and
   `description_latin` separated by a pipe (`|`) character and sorted by code.

## Running with Docker

Build the image and run it while mounting a local directory where the CSV should
be written:

```bash
docker build -t mkb-scraper .
docker run --rm -v "$(pwd)":/data mkb-scraper -o /data/mkb10.csv
```

Adjust the output path (`-o`) to match the mounted directory. The optional
`--delay` argument controls the pause in seconds between requests (default
`0.2`).
