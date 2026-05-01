# SMS Bomber

> **Authorized Penetration Testing Tool Only** — Unauthorized use is illegal.

SMS Bomber is a lightweight security testing tool that sends SMS messages using real API endpoints from 20+ Turkish platforms including Trendyol, Hepsiburada, N11, Turkcell, Instagram, Twitter, Telegram, Discord, WhatsApp, and more. Designed for authorized pentesters to test SMS rate limiting, account enumeration, and authentication resilience.

## Features

- **20 real SMS providers** — actual working APIs, not fake
- **Turkish phone support** — 5XX format, 10 digits
- **2 modes**: Sequential (sıralı) and Turbo (eşzamanlı threading)
- **Auto TC Kimlik generation** for IDO and similar APIs
- **Auto email generation** for registration endpoints
- **Windows & Linux compatible** — pure Python, zero config
- **Color-coded real-time feedback** — green for success, red for failure

## Quick Start

```bash
pip install requests colorama
python sms_bomber.py
