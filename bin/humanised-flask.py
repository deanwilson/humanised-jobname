from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))

from humanised_jobname import HumanisedJobname  # noqa: E402

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info(
    "humanised_jobnames", "humanised_flask", version="0.0.3"
)  # TODO: Dynamic version


@app.route("/")
def default():
    separator = request.args.get("separator")
    adjectives = request.args.get("adjectives")
    right_hand = request.args.get("right")

    job_name = HumanisedJobname()

    if separator:
        job_name.set_separator(separator)

    if adjectives:
        job_name.adjective_file(adjectives)

    if right_hand:
        job_name.right_hand_file(right_hand)

    return str(job_name)


metrics.register_default(
    metrics.counter(
        "by_path_counter",
        "Request count by request paths",
        labels={"path": lambda: request.path},
    )
)
