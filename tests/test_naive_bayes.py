import unittest

from simphile.naive_bayes import NaiveBayes


class TestNaiveBayes(unittest.TestCase):

    def test_calculate_probability(self):
        nb = NaiveBayes(1000, 600)
        nb.set_alpha(0)
        nb.set_observation_significance_threshold(None)
        nb.add_observation(400, 300)
        nb.add_observation(100, 90)
        # worked example is within a small fraction of what was calculated
        # (avoiding test being false due to floating-point inaccuracy)
        self.assertLess(
            nb.calculate_probability() - 0.94736,
            0.00001
        )

        # no alpha and an observation with 0 positives returns 0 prediction
        nb = NaiveBayes(1000, 600)
        nb.set_alpha(0)
        nb.add_observation(400, 0)
        self.assertEqual(
            nb.calculate_probability(),
            0
        )

        # using alpha keeps prediction from being 0
        nb = NaiveBayes(1000, 600)
        nb.set_alpha(1)
        nb.add_observation(400, 0)
        self.assertGreater(
            nb.calculate_probability(),
            0
        )

    def test_add_observation(self):
        nb = NaiveBayes(1000, 600)
        nb.set_observation_significance_threshold(.01)
        # Does not add an observation with a probability that is not
        # significantly different from the priors
        self.assertFalse(
            nb.add_observation(100, 60)
        )
        # Does add when significant difference
        self.assertTrue(
            nb.add_observation(100, 10)
        )


