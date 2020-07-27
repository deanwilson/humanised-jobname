#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))

from humanised_jobname import HumanisedJobname

job_name = HumanisedJobname("capital-cities.yaml")

print(job_name)
