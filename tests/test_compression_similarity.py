from unittest import TestCase

from simphile.compression_similarity import CompressionSimilarity


class TestCompressionSimilarity(TestCase):

    def test_score(self):
        a = "the quick brown fox jumped over the lazy dogs "
        cs = CompressionSimilarity(a)
        first = cs.score(a)
        second = cs.score("sldfjldkjfd")
        third = cs.score(a)
        # scoring should be same regardless of intermediate, unrelated score.
        # this tests that the intermediate compression state of the reference
        # is maintained
        self.assertEqual(first, third)

