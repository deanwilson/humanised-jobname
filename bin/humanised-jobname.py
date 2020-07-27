#!/usr/bin/env python3

import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))

from humanised_jobname import HumanisedJobname

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Query GitHub repo pull requests")

    parser.add_argument(
        "-s",
        "--separator",
        dest="separator",
        help="Specify a separator between the adjective and the right hand phrase",
    )

    args = parser.parse_args()

    job_name = HumanisedJobname("capital-cities.yaml")

    if args.separator:
        job_name.separator = args.separator

    print(job_name)
