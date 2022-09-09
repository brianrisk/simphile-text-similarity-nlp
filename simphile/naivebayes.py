from scipy import stats


class NaiveBayes:

    def __init__(self, prior_total, prior_positives):
        assert prior_positives < prior_total, "must have prior_positives < prior_total"
        assert prior_positives > 0, "must have prior_positives > 0"
        assert prior_total > 0, "must have prior_total > 0"

        self.prior_positives = prior_positives
        self.prior_total = prior_total
        self.prior_negatives = prior_total - prior_positives
        self.alpha = 1
        self.observation_significance_threshold = 0.05
        self.observations = []

    def set_observation_significance_threshold(self, threshold):
        assert threshold is None or threshold > 0
        assert threshold is None or threshold < 0.5
        self.observation_significance_threshold = threshold

    def set_alpha(self, alpha):
        assert alpha >= 0
        self.alpha = alpha

    def add_observation(self, total, positives):
        """
        An observation is the total population and number of positives for a given category.  For example,
        the total number of emails that contain "money" and the number of those emails that are spam.

        :param total: the total population count in the observation.
        For example the number of emails that contain "money"
        :param positives: the number of positives in the population.
        For example the number of spam emails that contain "money"
        :return: True or False based on if the observation was significantly different from the prior likelihood
        """
        assert positives <= total, "must have positives <= total"
        expectation = [self.prior_total, self.prior_positives]
        observation = [total, positives]
        table = [observation, expectation]
        p_value = stats.fisher_exact(table)[1]
        if self.observation_significance_threshold is None or p_value <= self.observation_significance_threshold:
            self.observations.append(observation)
            return True   # observation added
        else:
            return False  # observation not added

    def calculate_probability(self):
        prior_probability = self.prior_positives / self.prior_total
        alpha_denominator = self.alpha / prior_probability
        positive_score = prior_probability
        negative_score = 1.0 - prior_probability
        for observation in self.observations:
            observation_positives = self.alpha + observation[1]
            observation_total = alpha_denominator + observation[0]
            observation_negatives = observation_total - observation_positives
            positive_score *= observation_positives / (self.prior_positives + alpha_denominator)
            negative_score *= observation_negatives / (self.prior_negatives + alpha_denominator)
        return positive_score / (positive_score + negative_score)
