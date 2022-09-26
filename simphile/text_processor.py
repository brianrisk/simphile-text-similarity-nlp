import math

from . import text_utils


class TextProcessor:

    def __init__(self):
        self.lowercase = True
        self.only_alpha_numeric = True
        self.adjacent_pairs = False

    def process(self, string):
        result = string
        if self.only_alpha_numeric:
            result = text_utils.only_alpha_numeric(result)
        if self.lowercase:
            result = result.lower()
        return result

    # TODO test:  "a b" vs "a  b" vs "a b "
    def tokenize(self, string):
        result = self.process(string)
        result = result.split(" ")
        if self.adjacent_pairs:
            result = text_utils.create_adjacent_pairs(result)
        return result

    def frequencies(self, string):
        tokens = self.tokenize(string)
        frequencies = {}
        for item in tokens:
            if item in frequencies:
                frequencies[item] += 1
            else:
                frequencies[item] = 1
        return frequencies

    def normalized_frequencies(self, string):
        frequencies = self.frequencies(string)
        sum = 0
        for value in frequencies.values():
            sum += value * value
        magnitude = math.sqrt(sum)
        normalized = {}
        for key, value in frequencies.items():
            normalized[key] = value / magnitude
        return normalized



