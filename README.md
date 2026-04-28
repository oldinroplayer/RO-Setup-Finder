Not Default Pattern Valid Links |
------|
http://rofull.gnjoy.com/Ragnarok_250806_2.zip
http://rofull.gnjoy.com/KR_RO1_Live_20251001_122947.tar
[![Monthly Update Valid Links](https://img.shields.io/badge/%E2%96%B6%20Monthly%20Update%20Valid%20Links%20Here-e8b84b?style=for-the-badge&labelColor=cc0000)](https://github.com/AoShinRO/RO-Setup-Finder/blob/main/links_validos.md)
---

# RO-Setup-Finder

**RO-Setup-Finder** is an automated tool that scans, identifies, and catalogs valid download links for Ragnarok Online client installers, patches, and setup files hosted on official distribution servers (`rofull.gnjoy.com` and `twcdn.gnjoy.com.tw`).

It generates every possible URL combination across a date range using known file naming patterns, tests each one asynchronously, and outputs a list of all available downloads.

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/AoShinRO/RO-Setup-Finder)

---

## Features

- Asynchronous HTTP scanning with configurable concurrency (semaphore-based)
- Automatic date generation in both `YYMMDD` and `YYYYMMDD` formats
- Covers kRO, Sakray, and Zero client variants (`.exe`, `.zip`, `.bin`)
- Rate-limited requests to avoid server-side blocking
- Graceful error handling with per-URL status reporting
- Results automatically committed via GitHub Actions on a monthly schedule

---

## How It Works

The scanner generates URLs from known patterns such as:

```
http://rofull.gnjoy.com/RAG_SETUP_{YYMMDD}.exe
http://rofull.gnjoy.com/ZERO_SETUP_{YYMMDD}.exe
http://rofull.gnjoy.com/RagnarokZero_{YYMMDD}.zip
http://rofull.gnjoy.com/RAG_SETUP_{YYYYMMDD}.exe
http://twcdn.gnjoy.com.tw/ragnarok/Client/RAGNAROK_{YYYYMMDD}.exe
```

Each URL is tested with an HTTP HEAD/GET request. Links returning `200 OK` are saved to the output file.

---

## Requirements

- Python 3.9+
- [aiohttp](https://docs.aiohttp.org/)

```bash
pip install aiohttp
```

---

## Usage

```bash
python3 rosetupfinder.py
```

Valid links will be written to `links_validos.md` (or `links_validos.txt` if configured).

---

## Automation

A GitHub Actions workflow runs this script automatically on the **1th of every month**, committing any updated results back to the repository. It can also be triggered manually via `workflow_dispatch`.

---

## Disclaimer

This tool **does not download any files** — it only checks URL availability.  
Intended for cataloging, preservation, and research purposes.

---

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
