import random
import yaml

from pathlib import Path
from sys import exit


class HumanisedJobname:
    def __init__(self, right_hand, adjective_file="data/adjectives.yaml", separator="-"):
        self.adjective_file = adjective_file
        self.separator = separator
        self.right_hand = right_hand

        self.adjective = random.choice(self._load_yaml(self.adjective_file))
        self.right_hand_word = random.choice(self._load_yaml(self.right_hand))

    def _load_yaml(self, filename):
        words = []

        filename = Path(filename)

        if not filename.exists():
            print(f"Unable to find [{filename}]. Please check the data directory")
            exit(1)

        with open(filename) as f:
            # TODO: Exception handling
            yaml_content = yaml.load(f.read(), Loader=yaml.SafeLoader)
            words = yaml_content["words"]["words"]

        return words

    def separator(self, new_separator):
        self.separator = new_separator

    def __str__(self):
        return f"{self.adjective}{self.separator}{self.right_hand_word}"
