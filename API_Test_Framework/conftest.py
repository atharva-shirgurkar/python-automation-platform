import pytest
import httpx
import json
from pathlib import Path



@pytest.fixture(scope="session")
def test_config():
    """Load shared configuration once, regardless of the working directory."""
    config_path = Path(__file__).parent/"config"/"test_config.json"
    with config_path.open(encoding="utf-8") as config_file:
        return json.load(config_file)


@pytest.fixture(scope="session")
def base_url(test_config):
    return test_config["base_url"]



@pytest.fixture(scope="session")
def api_client(test_config, base_url):
    """Create an HTTP client with the shared URL, timeout, and headers."""
    with httpx.Client(
        base_url=base_url,
        timeout=test_config["timeout_seconds"],
        headers=test_config["headers"],
    ) as client:
        yield client
