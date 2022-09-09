from unittest import TestCase

from simphile.textsimilarity.jaccard import jaccard


class TestJaccard(TestCase):
    def test_jaccard(self):
        many_cats = "cat cat cat dog".split(" ")
        many_dogs = "dog dog dog cat".split(" ")
        some_cats = "cat cat dog".split(" ")
        some_dogs = "dog dog cat".split(" ")
        only_cats = "cat cat cat".split(" ")
        only_dogs = "dog dog dog".split(" ")
        no_pets = []
        # worked examples
        self.assertEqual(
            jaccard(many_cats, many_dogs),
            2 / 6
        )
        self.assertEqual(
            jaccard(some_cats, many_dogs),
            2 / 5
        )
        self.assertEqual(
            jaccard(some_cats, many_cats),
            3 / 4
        )
        # non intersecting is 0
        self.assertEqual(
            jaccard(only_cats, only_dogs),
            0
        )
        # test that multiple instances of same token affect outcome
        self.assertGreater(
            jaccard(some_cats, some_dogs),
            jaccard(many_cats, many_dogs)
        )
        # test symmetry
        self.assertEqual(
            jaccard(many_cats, many_dogs),
            jaccard(many_dogs, many_cats)
        )
        # score zero when compared to empty
        self.assertEqual(
            jaccard(many_cats, no_pets),
            0
        )


