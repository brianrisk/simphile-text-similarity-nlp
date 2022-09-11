import zlib


class CompressionSimilarity:
    """
    Compression exploits patterns in data in order to compress the data.
    This method produces a text similarity score by using compression to find similar patterns
    in the compared documents
    """

    def __init__(self, reference):
        """
        Initializes this scorer with the reference string.  Allows for effecient processing when
        comparing one string to many other strings

        :param reference: the string to which all other strings will be compared
        """
        # zlib docs: https://docs.python.org/3/library/zlib.html
        # note: consider using https://pypi.org/project/compress/ if it can save in-progress compression
        # using the highest compression to produce the best result
        compress = zlib.compressobj(level=9)
        partially_compressed_reference = compress.compress(bytes(reference, 'utf-8'))
        # Saving compression object with reference to avoid repeatedly compressing the same data
        self.in_progress_compression = compress
        self.partially_compressed_reference_len = len(partially_compressed_reference)
        self.compressed_reference_len = len(partially_compressed_reference + compress.copy().flush())

    def score(self, comparison):
        """
        Producing a similarity score of the comparison string to the reference string supplied
        in the initialization

        :param comparison:

        :return: decimal between 0 and 1 from lowest to highest
        """
        compression_copy = self.in_progress_compression.copy()
        compressed_concat_len = len(compression_copy.compress(bytes(comparison, 'utf-8'))) \
                            + len(compression_copy.flush()) \
                            + self.partially_compressed_reference_len
        compressed_comparison_len = len(zlib.compress(bytes(comparison, 'utf-8')))
        ratio = compressed_concat_len / (compressed_comparison_len + self.compressed_reference_len)
        # ratio is low when high similarity, so subtracting from 1 so that a number close to 1 is better
        # TODO is lowest ratio 0.5?  should we normalize?
        return 1.0 - ratio


