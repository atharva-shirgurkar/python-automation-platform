import pytest

@pytest.fixture(scope="session")
def sample_fixture(test_config):
    return test_config["test_data"]["sample"].copy()
