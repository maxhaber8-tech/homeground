# CardScout

AI-powered sports card deal finder. CardScout monitors newly listed eBay cards, identifies the
exact card from the listing image *and* text, estimates market value from recent comparable
sales, and alerts you when a listing looks significantly underpriced.

**CardScout never buys anything.** It surfaces opportunities; you review and purchase manually
through eBay.

## Scope (v1)

eBay only · sports trading cards only · baseball and basketball · PSA-graded only ·
Buy It Now only · newly listed only · United States marketplace.

## Why image analysis matters

Sellers mislist cards constantly — a missing card number, a misspelled player, the wrong year,
or a valuable parallel never mentioned in the title. CardScout reads the card and the PSA label
from the listing photos and compares that against what the seller claimed. The gap between the
two is often where the profit is.

## Quick start (mock mode, no credentials needed)

```bash
cp .env.example .env
docker compose up --build
```

- API: http://localhost:8000 (docs at `/docs`)
- Frontend: http://localhost:3000

Mock mode is the default, so the full pipeline runs against realistic generated listings
before any eBay credentials exist.

### Backend without Docker

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest            # run the test suite
```

## Configuration

All settings live in `.env` (see `.env.example`). Key thresholds:

| Setting | Default | Meaning |
|---|---|---|
| `MIN_IDENTIFICATION_CONFIDENCE` | 0.90 | Skip listings the AI isn't sure it identified |
| `MIN_VALUATION_CONFIDENCE` | 0.80 | Skip listings without solid comparable sales |
| `MIN_NET_PROFIT` | 50 | Dollars of expected profit required to alert |
| `MIN_ROI` | 0.20 | Return on total purchase cost required to alert |
| `RESALE_FEE_PCT` | 0.1325 | Assumed marketplace fees on resale |
| `TAX_PCT` | 0.07 | Assumed sales tax on purchase |

## Build status

- [x] **Phase 1** — project setup, config, structured logging, health/config API, Docker, mock mode
- [ ] Phase 2 — database schema and migrations
- [ ] Phase 3 — mock listing pipeline
- [ ] Phase 4 — card identification (image + text)
- [ ] Phase 5 — comparable-sales engine
- [ ] Phase 6 — profitability calculation
- [ ] Phase 7 — opportunity scoring
- [ ] Phase 8 — dashboard
- [ ] Phase 9 — Discord alerts
- [ ] Phase 10 — live eBay Browse API

## Notes and limitations

- Valuations are estimates from historical comps, not guarantees. Card markets move.
- CardScout uses the official eBay Browse API and does not scrape eBay web pages.
- Grading, authenticity, and condition risk remain yours to assess before buying.
