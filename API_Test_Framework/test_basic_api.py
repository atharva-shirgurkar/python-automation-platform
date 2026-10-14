from logging import getLogger
import json

log = getLogger(__name__)

class TestBasicAPI:
    def test_basic_api(self, api_client):
        response = api_client.get("posts/1")
        data = response.json()
        assert data["id"] == 1
        assert response.status_code == 200

    def test_negative_api(self, api_client):
        response = api_client.get("posts/9999")
        assert response.status_code == 404