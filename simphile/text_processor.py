import math

from . import text_utils


class TextProcessor:
    """
    A TextProcessor has common cleaning and tokenization methods to ensure
    that strings are processed in a consistent way
    """

    def __init__(self, lowercase=False, only_alphabetic=False, adjacent_pairs=False):
        """
        Constructor for TextProcessor
        :param lowercase:
        :param only_alphabetic:
        :param adjacent_pairs:
        """
        self.lowercase = lowercase
        self.only_alphabetic = only_alphabetic
        self.adjacent_pairs = adjacent_pairs

    def process(self, string):
        """
        If processor has only_alphabetic as True, then replaces all non-alphabetic characters with a whitespace.
        if processor has lowercase as True, it lowercases the string.

        :param string:
        :return: processed string
        """
        result = string
        if self.only_alphabetic:
            result = text_utils.only_alphabetic(result)
        if self.lowercase:
            result = result.lower()
        return result

    def tokenize(self, string):
        """
        First processes string then splits string into tokens by word
        :param string:
        :return: list containing tokens
        """
        result = self.process(string)
        result = result.split()
        if self.adjacent_pairs:
            result = text_utils.create_adjacent_pairs(result)
        return result

    def frequencies(self, string):
        """
        First processes and tokenizes string into words.  Then returns a map of the occurrences count of tokens.
        e.g. "a b b" yields {'a': 1, 'b', 2}
        :param string:
        :return: Dictionary containing token frequencies
        """
        tokens = self.tokenize(string)
        frequencies = {}
        for item in tokens:
            if item in frequencies:
                frequencies[item] += 1
            else:
                frequencies[item] = 1
        return frequencies

    def normalized_frequencies(self, string):
        """
        Finds word frequencies in string, then treats all words as an axis and
        divides all the counts by the magnitude of the resulting vector.
        e.g. "a b b" yields {'a': 0.4472135954999579, 'b': 0.8944271909999159}

        :param string:
        :return: Dictionary containing normalized token frequencies
        """
        frequencies = self.frequencies(string)
        sum = 0
        for value in frequencies.values():
            sum += value * value
        magnitude = math.sqrt(sum)
        normalized = {}
        for key, value in frequencies.items():
            normalized[key] = value / magnitude
        return normalized



