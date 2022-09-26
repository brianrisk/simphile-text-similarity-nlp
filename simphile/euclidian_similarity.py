import math

from simphile.text_processor import TextProcessor


class EuclidianSimilarity:

    def __init__(self, reference, text_processor=None):
        """
        Initializes this scorer with the reference string.  Allows for efficient processing when
        comparing one string to many other strings

        :param reference: the string to which all other strings will be compared
        """
        if text_processor is None:
            self.text_processor = TextProcessor()
        else:
            self.text_processor = text_processor

        self.reference_frequencies = self.text_processor.normalized_frequencies(reference)

    def score(self, comparison):
        """
        Producing a similarity score of the comparison string to the reference string supplied
        in the initialization

        :param comparison:

        :return: decimal between 0 and 1 from lowest to highest
        """
        if len(comparison) == 0:
            return 0
        comparison_frequencies = self.text_processor.normalized_frequencies(comparison)
        keys = set(list(comparison_frequencies.keys()) + list(self.reference_frequencies.keys()))
        sum = 0
        for key in keys:
            a = self.reference_frequencies.get(key, 0.0)
            b = comparison_frequencies.get(key, 0.0)
            diff = a - b
            square = diff * diff
            sum += square
        distance = math.sqrt(sum)
        # the max distance may be sqrt(the number of unique tokens), normalizing
        return 1 - (distance / math.sqrt(len(keys)))


def euclidian_similarity(string_a, string_b):
    obj = EuclidianSimilarity(string_a)
    return obj.score(string_b)

