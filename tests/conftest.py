import pytest

@pytest.fixture()
def test_runner():
    print("TEST STARTED")
    yield
    print("TEST FINISHED")