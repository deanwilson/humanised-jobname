import os
import pytest
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import humanisedflask  # noqa: E402


@pytest.fixture
def client():
    humanisedflask.app.config['TESTING'] = True

    with humanisedflask.app.test_client() as client:
        yield client


def test_default_page(client):
    """Test the default page contains our default separator."""

    rv = client.get('/')
    assert "-" in str(rv.data)


def test_metrics_page(client):
    """Test the /metrics page contains a default metric."""

    rv = client.get('/metrics')
    assert "flask_exporter_info{" in str(rv.data)


def test_setting_separator(client):
    rv = client.get('/?separator=AAA')
    assert "AAA" in str(rv.data)

    rv = client.get('/?separator=BBB')
    assert "BBB" in str(rv.data)


def test_setting_files(client, shared_datadir):
    adjectives = (shared_datadir / "adjectives.yaml")
    right_hand = (shared_datadir / "fedora-names.yaml")

    rv = client.get(f"/?separator=^^^&adjectives={adjectives}&right={right_hand}")

    assert "perfect^^^beefy_miracle" in str(rv.data)
