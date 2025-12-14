import math
import unittest

from simphile.fisher import fisher_exact


class TestFisherExact(unittest.TestCase):

    def test_known_reference_tables(self):
        odds, p_value = fisher_exact([[8, 2], [1, 5]])
        self.assertAlmostEqual(odds, 20.0)
        self.assertAlmostEqual(p_value, 0.034965034965034975)

        odds, p_value = fisher_exact([[1, 9], [11, 3]])
        self.assertAlmostEqual(odds, 0.030303030303030304)
        self.assertAlmostEqual(p_value, 0.0027594561852200836)

    def test_extreme_counts(self):
        odds, p_value = fisher_exact([[10, 0], [0, 10]])
        self.assertTrue(math.isinf(odds))
        self.assertAlmostEqual(p_value, 1.082508822446903e-05)

        odds, _ = fisher_exact([[0, 5], [0, 0]])
        self.assertTrue(math.isnan(odds))

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            fisher_exact([[1, 2, 3], [4, 5, 6]])

        with self.assertRaises(ValueError):
            fisher_exact([[1, -1], [2, 3]])

