from logging import getLogger
import pytest

log = getLogger(__name__)

class TestBasicAPI:
    def test_basic_api(self, api_client):
        response = api_client.get("posts/1")
        log.info(f"Response text: {response.text}")
        assert response.status_code == 200