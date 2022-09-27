Module simphile.naive_bayes
===========================

Classes
-------

`NaiveBayes(prior_total, prior_positives)`
:   Initializes the Bayesian calculator with priors.
    
    :param prior_total: The total N.  In the spam example, this is the total number of emails
    :param prior_positives: The number of positives.  In the spam example, this is the count of spam emails

    ### Methods

    `add_observation(self, total, positives)`
    :   An observation is the total population and number of positives for a given category.  For example,
        the total number of emails that contain "money" and the number of those emails that are spam.
        
        :param total: the total population count in the observation.
        For example the total number of emails that contain "money"
        
        :param positives: the number of positives in the population.
        For example the number of spam emails that contain "money"
        
        :return: True or False based on if the observation was significantly different from the prior likelihood

    `calculate_probability(self)`
    :   Given all the observations, uses Naive Bayes to calculate the probability
        ( 0 to 1) that a specific instance is true
        
        :return: the probability ( 0 to 1) that a specific instance is true (e.g.
        that a specific email is spam)

    `set_alpha(self, alpha)`
    :   And alpha is a constant added to the positives to avoid zeros and generally smooths
        the results to avoid low-N and noisy samples throwing things off.  Default alpha is 1.0.
        
        :param alpha: a number greater than 0
        
        :return:

    `set_observation_significance_threshold(self, threshold)`
    :   Any observation (aka test) that does not pass the p-value threshold will
        not be incorporated into the final prediction.  P-values are calculated
        with Fischer's Exact.  For example, if priors are 1000 with 300 positives,
        an observation sample of 100 with 30 positives won't be added because
        it does not differ significantly from the priors.  This keeps low value and
        potentially noisy observations out. The default threshold is 0.05
        
        :param threshold: can be a number between 0 and 0.5 or None
        
        :return: