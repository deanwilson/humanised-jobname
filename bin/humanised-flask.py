from flask import Flask

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))

from humanised_jobname import HumanisedJobname  # noqa: E402

app = Flask(__name__)


@app.route("/")
def default():
    job_name = HumanisedJobname("capital-cities.yaml")

    return str(job_name)
