import os
import pytest
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import humanisedflask

@pytest.fixture
def client():
    humanisedflask.app.config['TESTING'] = True

    with humanisedflask.app.test_client() as client:
        yield client


def test_default_page(client):
    """Test the default page contains our default separator."""

    rv = client.get('/')
    assert "-" in str(rv.data)
