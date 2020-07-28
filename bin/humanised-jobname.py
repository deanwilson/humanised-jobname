#!/usr/bin/env python3

import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))

from humanised_jobname import HumanisedJobname  # noqa: E402

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Query GitHub repo pull requests")

    parser.add_argument(
        "-s",
        "--separator",
        dest="separator",
        help="Specify a separator between the adjective and the right hand phrase",
    )

    parser.add_argument(
        "-d",
        "--data-file",
        dest="data_file",
        default="data/capital-cities.yaml",
        help="Specify a data source to use for the right hand phrase",
    )

    parser.add_argument(
        "-a",
        "--adjectives",
        "--adjectives-data-file",
        dest="adjectives",
        default="data/adjectives.yaml",
        help="Specify a data source to use for adjectives",
    )


    args = parser.parse_args()

    job_name = HumanisedJobname(args.data_file, args.adjectives)

    if args.separator:
        job_name.separator = args.separator

    print(job_name)
