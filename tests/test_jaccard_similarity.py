from unittest import TestCase

from simphile.jaccard_similarity import jaccard_similarity


class TestJaccardSimilarity(TestCase):

    def test_jaccard(self):
        many_cats = "cat cat cat dog"
        many_dogs = "dog dog dog cat"
        some_cats = "cat cat dog"
        some_dogs = "dog dog cat"
        only_cats = "cat cat cat"
        only_dogs = "dog dog dog"
        no_pets = ""
        # worked examples
        self.assertEqual(
            jaccard_similarity(many_cats, many_dogs),
            2 / 6
        )
        self.assertEqual(
            jaccard_similarity(some_cats, many_dogs),
            2 / 5
        )
        self.assertEqual(
            jaccard_similarity(some_cats, many_cats),
            3 / 4
        )
        # a set with itself is 1
        self.assertEqual(
            jaccard_similarity(some_cats, some_cats),
            1
        )
        # non intersecting is 0
        self.assertEqual(
            jaccard_similarity(only_cats, only_dogs),
            0
        )
        # test that multiple instances of same token affect outcome
        self.assertGreater(
            jaccard_similarity(some_cats, some_dogs),
            jaccard_similarity(many_cats, many_dogs)
        )
        # test symmetry
        self.assertEqual(
            jaccard_similarity(many_cats, many_dogs),
            jaccard_similarity(many_dogs, many_cats)
        )
        # score zero when compared to empty
        self.assertEqual(
            jaccard_similarity(many_cats, no_pets),
            0
        )


