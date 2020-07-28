import random
import yaml

from pathlib import Path
from sys import exit


class HumanisedJobname:
    def __init__(self, right_hand="data/capital-cities.yaml", adjective_file="data/adjectives.yaml", separator="-"):
        self.separator = separator

        self.right_hand_word = self._random_word(right_hand)
        self.adjective = self._random_word(adjective_file)

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

    def _random_word(self, filename):
        return(random.choice(self._load_yaml(filename)))


    def separator(self, new_separator):
        self.separator = new_separator


    def right_hand_file(self, right_hand):
        self.right_hand_word = self._random_word(right_hand)


    def adjective_file(self, adjective):
        self.adjective = self._random_word(adjective)


    def __str__(self):
        return f"{self.adjective}{self.separator}{self.right_hand_word}"
