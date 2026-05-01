# SMS Bomber - Authorized Penetration Testing Tool

> **⚠️ WARNING: This tool is for AUTHORIZED PENETRATION TESTING ONLY**
> You must have explicit written permission before using this tool.
> Unauthorized use is illegal and unethical.

A high-performance SMS bombing tool built for authorized security assessments.
Extracts real, working SMS API endpoints from popular Turkish and international
platforms to test SMS rate limiting, account enumeration vulnerabilities,
and SMS-based authentication resilience.

## Features

- **20+ Real SMS Providers** — Actual working APIs from major platforms
- **Turkish Phone Support** — Optimized for +90 numbers (5XX XXX XX XX)
- **Dual Operation Modes**:
  - **Sequential Mode** — Sends one SMS at a time with configurable delay
  - **Turbo Mode** — Multithreaded parallel SMS sending for stress testing
- **Auto TC Kimlik Generation** — For APIs requiring Turkish ID numbers
- **Auto Mail Generation** — Random email addresses for registration endpoints
- **Color-Coded Output** — Real-time success/failure feedback
- **Zero Config** — Install dependencies and run

## Supported Providers

| # | Provider | Category | # | Provider | Category |
|---|----------|----------|---|----------|----------|
| 1 | KahveDunyasi | E-commerce | 11 | Getir | Delivery |
| 2 | Money.com.tr | Finance | 12 | Migros | Retail |
| 3 | Alixavien | E-commerce | 13 | A101 | Retail |
| 4 | Jimmykey | E-commerce | 14 | Bim | Retail |
| 5 | IDO | Transport | 15 | Istanbulkart | Transport |
| 6 | Trendyol | E-commerce | 16 | Instagram | Social |
| 7 | Hepsiburada | E-commerce | 17 | Twitter/X | Social |
| 8 | N11 | E-commerce | 18 | Telegram | Messaging |
| 9 | Turkcell | Telecom | 19 | Discord | Social |
| 10 | Sahibinden | Classifieds | 20 | WhatsApp | Messaging |

## Installation

```bash
# Clone the repository
git clone https://github.com/salihpython/sms-bomber.git
cd sms-bomber

# Install dependencies
pip install requests colorama

# Run
python sms_bomber.py
