import gzip


class CompressionScore:
    """
    Compression (in this case GZIP) finds patterns data in order to compress the data.
    This method produces a text similarity score by using GZIP to find similar patterns
    in the compared documents
    """

    def __init__(self, reference):
        self.reference = reference
        compressed_reference = gzip.compress(bytes(reference, 'utf-8'))
        self.compressed_reference_len = len(compressed_reference)

    def score(self, comparison):
        concat = comparison + " " + self.reference
        compressed_comparison = gzip.compress(bytes(comparison, 'utf-8'))
        compressed_concat = gzip.compress(bytes(concat, 'utf-8'))
        ratio = len(compressed_concat) / (len(compressed_comparison) + self.compressed_reference_len)
        # a low ratio is good, so subtracting from 1
        return 1.0 - ratio

