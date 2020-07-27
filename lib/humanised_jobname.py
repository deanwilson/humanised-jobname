import random
import yaml

from pathlib import Path


class HumanisedJobname:
    def __init__(self, right_hand, adjective_file="adjectives.yaml", separator="-"):
        self.adjective_file = adjective_file
        self.separator = separator
        self.right_hand = right_hand

        self.adjective = random.choice(self._load_yaml(self.adjective_file))
        self.right_hand_word = random.choice(self._load_yaml(self.right_hand))

    def _load_yaml(self, filename):
        words = []

        expanded_filename = Path("data", filename)

        # TODO: filename existence checks
        with open(expanded_filename) as f:
            # TODO: Exception handling
            yaml_content = yaml.load(f.read(), Loader=yaml.SafeLoader)
            words = yaml_content["words"]["words"]

        return words

    def separator(self, new_separator):
        self.separator = new_separator

    def __str__(self):
        return f"{self.adjective}{self.separator}{self.right_hand_word}"
