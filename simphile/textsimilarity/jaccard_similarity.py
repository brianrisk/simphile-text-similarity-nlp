from simphile.sets import intersect, minus
from simphile.textsimilarity.text_processor import TextProcessor


class JaccardSimilarity:

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
        self.reference = self.text_processor.tokenize(reference)

    def score(self, comparison):
        """
        Producing a similarity score of the comparison string to the reference string supplied
        in the initialization

        :param comparison:

        :return: decimal between 0 and 1 from lowest to highest
        """
        return jaccard_similarity(self.reference, self.text_processor.tokenize(comparison))


def jaccard_similarity(list_a, list_b):
    assert len(list_a) > 0 or len(list_b > 0), "at least one list needs to have elements"
    intersected = intersect(list_a, list_b)
    combined = list_a + list_b
    # did not use the union function for efficiency in sets.  Union also calculates intersection,
    # so we don't want to duplicate that processing
    unioned = minus(combined, intersected)
    return len(intersected) / len(unioned)
