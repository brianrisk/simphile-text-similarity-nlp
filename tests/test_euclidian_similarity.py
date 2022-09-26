from unittest import TestCase

from simphile.euclidian_similarity import euclidian_similarity


class TestEuclidianSimilarity(TestCase):

    def test_euclidian_similarity(self):
        many_cats = "cat cat cat dog"
        many_dogs = "dog dog dog cat"
        only_cats = "cat cat cat"
        only_dogs = "dog dog dog"

        # no similarity should be 0
        self.assertEqual(euclidian_similarity(only_dogs, only_cats), 0)

        # equality should be 1
        self.assertEqual(euclidian_similarity(only_cats, only_cats), 1)

        # empty strings
        self.assertEqual(euclidian_similarity(only_dogs, ""), 0)
        self.assertEqual(euclidian_similarity("", ""), 0)

        # should equal if token proportions are the same
        self.assertEqual(
            euclidian_similarity(only_dogs, many_dogs),
            euclidian_similarity(only_cats, many_cats)
        )
