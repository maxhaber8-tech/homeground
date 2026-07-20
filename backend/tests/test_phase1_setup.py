"""Phase 1 acceptance: app boots, endpoints respond, mock mode is the default."""
from fastapi.testclient import TestClient

from app.config import Settings
from app.main import app

client = TestClient(app)


def test_health_endpoint_reports_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_app_defaults_to_mock_mode():
    """The app must run before any eBay credentials exist."""
    assert Settings(_env_file=None).mock_mode is True


def test_missing_credentials_do_not_crash_startup():
    fresh = Settings(_env_file=None)
    assert fresh.ebay_configured is False
    assert client.get("/health").json()["ebay_configured"] in (True, False)


def test_config_endpoint_exposes_thresholds_and_no_secrets():
    body = client.get("/config").json()
    assert body["min_net_profit"] == 50.0
    assert body["min_roi"] == 0.20
    assert body["min_identification_confidence"] == 0.90
    for secret in ("ebay_client_secret", "anthropic_api_key", "discord_webhook_url"):
        assert secret not in body


def test_thresholds_are_configurable_via_env(monkeypatch):
    monkeypatch.setenv("MIN_NET_PROFIT", "125")
    monkeypatch.setenv("MIN_ROI", "0.5")
    custom = Settings(_env_file=None)
    assert custom.min_net_profit == 125
    assert custom.min_roi == 0.5
