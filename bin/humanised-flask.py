from flask import Flask, request

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))

from humanised_jobname import HumanisedJobname  # noqa: E402

app = Flask(__name__)


@app.route("/")
def default():
    separator = request.args.get("separator")

    job_name = HumanisedJobname("capital-cities.yaml")

    if separator:
        job_name.separator = separator

    return str(job_name)
