import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))

from humanised_jobname import HumanisedJobname  # noqa: E402

class TestClass:
    def test_simple_object(self):
        """ check the default seperate is in the object string representation """
        job_name = HumanisedJobname()
        assert "-" in str(job_name)
