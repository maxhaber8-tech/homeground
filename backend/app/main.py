"""CardScout API entrypoint."""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.logging_config import configure_logging, get_logger

configure_logging(settings.log_level)
logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(_app: FastAPI):
    logger.info("CardScout starting", extra={"extra_fields": {"mock_mode": settings.mock_mode}})
    yield


app = FastAPI(
    lifespan=lifespan,
    title="CardScout API",
    description="AI-powered sports card deal finder. Surfaces underpriced PSA-graded "
                "baseball and basketball listings for manual review.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["system"])
def health() -> dict:
    """Liveness probe plus a readout of how the app is configured."""
    return {
        "status": "ok",
        "mock_mode": settings.mock_mode,
        "ebay_configured": settings.ebay_configured,
        "vision_configured": bool(settings.anthropic_api_key),
        "alerts_configured": bool(settings.discord_webhook_url),
    }


@app.get("/config", tags=["system"])
def config() -> dict:
    """Non-secret runtime settings, so the dashboard can display thresholds."""
    return {
        "min_identification_confidence": settings.min_identification_confidence,
        "min_valuation_confidence": settings.min_valuation_confidence,
        "min_net_profit": settings.min_net_profit,
        "min_roi": settings.min_roi,
        "resale_fee_pct": settings.resale_fee_pct,
        "resale_shipping_cost": settings.resale_shipping_cost,
        "tax_pct": settings.tax_pct,
        "poll_interval_seconds": settings.poll_interval_seconds,
    }



