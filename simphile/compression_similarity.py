import zlib

from simphile.text_processor import TextProcessor


class CompressionSimilarity:
    """
    Compression exploits patterns in data in order to compress the data.
    This method produces a text similarity score by using compression to find similar patterns
    in the compared documents

    Note, not symmetric.  Scoring A against B is not always the same as B against A
    """

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

        # zlib docs: https://docs.python.org/3/library/zlib.html
        # note: consider using https://pypi.org/project/compress/ if it can save in-progress compression
        # using the highest compression to produce the best result
        compress = zlib.compressobj(level=9)
        processed_reference = self.text_processor.process(reference)
        partially_compressed_reference = compress.compress(bytes(processed_reference, 'utf-8'))
        # Saving compression object with reference to avoid repeatedly compressing the same data
        self.in_progress_compression = compress
        self.partially_compressed_reference_len = len(partially_compressed_reference)
        self.compressed_reference_len = self.partially_compressed_reference_len + len(compress.copy().flush())

    def score(self, comparison):
        """
        Producing a similarity score of the comparison string to the reference string supplied
        in the initialization

        :param comparison:

        :return: decimal between 0 and 1 from lowest to highest
        """
        compression_copy = self.in_progress_compression.copy()
        processed_comparison = self.text_processor.process(comparison)
        compressed_concat_len = len(compression_copy.compress(bytes(processed_comparison, 'utf-8'))) \
                            + len(compression_copy.flush()) \
                            + self.partially_compressed_reference_len
        compressed_comparison_len = len(zlib.compress(bytes(processed_comparison, 'utf-8')))
        ratio = compressed_concat_len / (compressed_comparison_len + self.compressed_reference_len)
        # lowest ratio is about 0.5; normalizing
        ratio = (ratio - 0.5) * 2.0
        # ratio is low when high similarity, so subtracting from 1 so that a number close to 1 is better
        score = 1.0 - ratio
        # bounding between 1 and 0
        score = min(max(score, 0), 1)
        return score


def compression_similarity(string_a, string_b):
    obj = CompressionSimilarity(string_a)
    return obj.score(string_b)

