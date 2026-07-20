"""Central configuration, loaded from environment with sane defaults."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Core
    mock_mode: bool = True
    database_url: str = "sqlite:///./cardscout.db"
    log_level: str = "INFO"

    # eBay (Phase 10)
    ebay_client_id: str = ""
    ebay_client_secret: str = ""
    ebay_environment: str = "PRODUCTION"
    ebay_marketplace_id: str = "EBAY_US"

    # AI vision (Phase 4)
    anthropic_api_key: str = ""

    # Alerts (Phase 9)
    discord_webhook_url: str = ""

    # Thresholds / assumptions (Phase 6)
    min_identification_confidence: float = 0.90
    min_valuation_confidence: float = 0.80
    min_net_profit: float = 50.0
    min_roi: float = 0.20
    resale_fee_pct: float = 0.1325
    resale_shipping_cost: float = 4.99
    tax_pct: float = 0.07
    poll_interval_seconds: int = 300

    @property
    def ebay_configured(self) -> bool:
        return bool(self.ebay_client_id and self.ebay_client_secret)


settings = Settings()
