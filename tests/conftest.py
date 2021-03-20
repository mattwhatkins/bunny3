import pytest

from bunny3.bunny import create_app
from bunny3.bunny import Bunny3


@pytest.fixture
def test_client():
    bunny = Bunny3()
    app = create_app(bunny)
    with app.test_client() as test_client:
        yield test_client


@pytest.fixture
def test_bunny():
    bunny = Bunny3()
    yield bunny
