
class TestSampleData:
    def test_sample_data(self, sample_fixture):
        assert sample_fixture["message"] == "sample_fixture test"