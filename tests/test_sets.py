import unittest

from simphile import sets


class TestSets(unittest.TestCase):

    def test_intersect(self):
        # INTS
        # single element
        self.assertCountEqual(sets.intersect([1, 2], [2, 3]), [2])
        # multiple elements
        self.assertCountEqual(sets.intersect([1, 2, 3], [2, 3, 4]), [2, 3])
        # full subset
        self.assertCountEqual(sets.intersect([1, 2, 3, 4], [2, 3]), [2, 3])
        # symmetry
        self.assertCountEqual(sets.intersect([2, 3], [1, 2, 3, 4]), [2, 3])
        # no intersection
        self.assertCountEqual(sets.intersect([1, 2], [3, 4]), [])
        # repeated elements
        self.assertCountEqual(sets.intersect([1, 2, 2], [2, 3, 2]), [2, 2])
        # with empty
        self.assertCountEqual(sets.intersect([1, 2], []), [])
        # empty and empty
        self.assertCountEqual(sets.intersect([], []), [])

        # STRINGS
        # single element
        self.assertCountEqual(sets.intersect(['1', '2'], ['2', '3']), ['2'])
        # multiple elements
        self.assertCountEqual(sets.intersect(['1', '2', '3'], ['2', '3', '4']), ['2', '3'])
        # full subset
        self.assertCountEqual(sets.intersect(['1', '2', '3', '4'], ['2', '3']), ['2', '3'])
        # symmetry
        self.assertCountEqual(sets.intersect(['2', '3'], ['1', '2', '3', '4']), ['2', '3'])
        # no intersection
        self.assertCountEqual(sets.intersect(['1', '2'], ['3', '4']), [])
        # repeated elements
        self.assertCountEqual(sets.intersect(['1', '2', '2'], ['2', '3', '2']), ['2', '2'])
        # with empty
        self.assertCountEqual(sets.intersect(['1', '2'], []), [])

    def test_union(self):
        # single element
        self.assertCountEqual(sets.union([1, 2], [2, 3]), [1, 2, 3])
        # multiple element
        self.assertCountEqual(sets.union([1, 2, 3], [2, 3, 4]), [1, 2, 3, 4])
        # full subset
        self.assertCountEqual(sets.union([1, 2, 3, 4], [2, 3]), [1, 2, 3, 4])
        # symmetry
        self.assertCountEqual(sets.union([2, 3], [1, 2, 3, 4]), [1, 2, 3, 4])
        # no overlap
        self.assertCountEqual(sets.union([1, 2], [3, 4]), [1, 2, 3, 4])
        # repeated elements
        self.assertCountEqual(sets.union([1, 2, 2], [2, 3, 2]), [1, 2, 2, 3])
        # with empty
        self.assertCountEqual(sets.union([1, 2], []), [1, 2])
        # empty and empty
        self.assertCountEqual(sets.union([], []), [])

    def test_minus(self):
        # single element
        self.assertCountEqual(sets.minus([1, 2], [2, 3]), [1])
        # multiple element
        self.assertCountEqual(sets.minus([1, 2, 3], [2, 3, 4]), [1])
        # full subset
        self.assertCountEqual(sets.minus([1, 2, 3, 4], [2, 3]), [1, 4])
        # symmetry, order flipped
        self.assertCountEqual(sets.minus([2, 3], [1, 2, 3, 4]), [])
        # with no overlap
        self.assertCountEqual(sets.minus([1, 2], [3, 4]), [1, 2])
        # repeated elements
        self.assertCountEqual(sets.minus([1, 2, 2], [2, 3, 2]), [1])
        # with empty
        self.assertCountEqual(sets.minus([1, 2], []), [1, 2])
        # empty and empty
        self.assertCountEqual(sets.minus([], []), [])


if __name__ == '__main__':
    unittest.main()