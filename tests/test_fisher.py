import math
import unittest

from simphile.fisher import fisher_exact
from tests.fisher_vectors import FISHER_EXACT_VECTORS


class TestFisherExact(unittest.TestCase):

    def test_reference_vectors_generated_by_scipy(self):
        for case in FISHER_EXACT_VECTORS:
            table = case["table"]
            expected_odds = case["odds_ratio"]
            expected_p = case["p_value"]

            odds, p_value = fisher_exact(table)

            if math.isnan(expected_odds):
                self.assertTrue(math.isnan(odds), msg=f"table={table}")
            elif math.isinf(expected_odds):
                self.assertTrue(math.isinf(odds), msg=f"table={table}")
            else:
                self.assertAlmostEqual(odds, expected_odds, msg=f"table={table}")

            self.assertAlmostEqual(p_value, expected_p, msg=f"table={table}")
            self.assertGreaterEqual(p_value, 0.0, msg=f"table={table}")
            self.assertLessEqual(p_value, 1.0, msg=f"table={table}")

    def test_extreme_counts(self):
        odds, p_value = fisher_exact([[10, 0], [0, 10]])
        self.assertTrue(math.isinf(odds))
        self.assertAlmostEqual(p_value, 1.082508822446903e-05)

        odds, _ = fisher_exact([[0, 5], [0, 0]])
        self.assertTrue(math.isnan(odds))

    def test_symmetry_invariance_of_p_value(self):
        table = [[4, 1], [2, 6]]

        def swap_rows(t):
            return [t[1], t[0]]

        def swap_cols(t):
            return [[t[0][1], t[0][0]], [t[1][1], t[1][0]]]

        def transpose(t):
            return [[t[0][0], t[1][0]], [t[0][1], t[1][1]]]

        base_p = fisher_exact(table)[1]
        self.assertAlmostEqual(base_p, fisher_exact(swap_rows(table))[1])
        self.assertAlmostEqual(base_p, fisher_exact(swap_cols(table))[1])
        self.assertAlmostEqual(base_p, fisher_exact(transpose(table))[1])

    def test_odds_ratio_transforms_under_swaps(self):
        table = [[4, 1], [2, 6]]
        base_odds = fisher_exact(table)[0]
        self.assertAlmostEqual(fisher_exact([table[1], table[0]])[0], 1.0 / base_odds)
        self.assertAlmostEqual(
            fisher_exact([[table[0][1], table[0][0]], [table[1][1], table[1][0]]])[0],
            1.0 / base_odds,
        )
        self.assertAlmostEqual(
            fisher_exact([[table[1][1], table[1][0]], [table[0][1], table[0][0]]])[0],
            base_odds,
        )

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            fisher_exact([[1, 2, 3], [4, 5, 6]])

        with self.assertRaises(ValueError):
            fisher_exact([[1, -1], [2, 3]])

        with self.assertRaises(ValueError):
            fisher_exact([[0, 0], [0, 0]])

        with self.assertRaises(TypeError):
            fisher_exact([[1.0, 2], [3, 4]])
