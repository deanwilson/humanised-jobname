import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))

from humanised_jobname import HumanisedJobname  # noqa: E402

def test_simple_object(datadir):
    """ check the default seperate is in the object string representation """
    job_name = HumanisedJobname()
    assert "-" in str(job_name)


def test_custom_separator_constructor(datadir):
    job_name = HumanisedJobname(separator='===')

    assert "===" in str(job_name)


def test_custom_separator_method(datadir):
    job_name = HumanisedJobname()

    job_name.set_separator("%%%")

    assert "%%%" in str(job_name)


def test_constructor_custom_files(datadir):
    adjectives = (datadir / "adjectives.yaml")
    right_hand = (datadir / "fedora-names.yaml")

    job_name = HumanisedJobname(adjective_file=adjectives, right_hand=right_hand)

    assert "perfect-beefy_miracle" == str(job_name)

