Module simphile
===============
## Install
```pip install simphile```
## About
Sim•phile = "the love of similarities"

The aim is to proved easy access to text similairty metods that are language-agnostic and (ideally) much
faster in execution time than methods that employ text embeddings.

* **Compression Similairty** – leverages the pattern recognition of compression algorithms
* **Euclidian Similarity** – Treating text like points in multi-dimensional space and calculating their closeness
* **Jaccard Similairy** – Texts are more similar the more their words overlap

Sub-modules
-----------
* simphile.naive_bayes
* simphile.sets
* simphile.text_processor
* simphile.text_utils

Functions
---------

    
`compression_similarity(string_a, string_b)`
:   

    
`euclidian_similarity(string_a, string_b)`
:   

    
`jaccard_similarity(string_a, string_b)`
:   

Classes
-------

`CompressionSimilarity(reference, text_processor=None)`
:   Compression exploits patterns in data in order to compress the data.
    This method produces a text similarity score by using compression to find similar patterns
    in the compared documents
    
    Note, not symmetric.  Scoring A against B is not always the same as B against A
    
    Initializes this scorer with the reference string.  Allows for efficient processing when
    comparing one string to many other strings
    
    :param reference: the string to which all other strings will be compared

    ### Methods

    `score(self, comparison)`
    :   Producing a similarity score of the comparison string to the reference string supplied
        in the initialization
        
        :param comparison:
        
        :return: decimal between 0 and 1 from lowest to highest

`EuclidianSimilarity(reference, text_processor=None)`
:   Initializes this scorer with the reference string.  Allows for efficient processing when
    comparing one string to many other strings
    
    :param reference: the string to which all other strings will be compared

    ### Methods

    `score(self, comparison)`
    :   Producing a similarity score of the comparison string to the reference string supplied
        in the initialization
        
        :param comparison:
        
        :return: decimal between 0 and 1 from lowest to highest

`JaccardSimilarity(reference, text_processor=None)`
:   Initializes this scorer with the reference string.  Allows for efficient processing when
    comparing one string to many other strings
    
    :param reference: the string to which all other strings will be compared

    ### Methods

    `score(self, comparison)`
    :   Using the Jaccard Index, produces a similarity score of the comparison string
        to the reference string supplied in the initialization
        
        :param comparison:
        
        :return: decimal between 0 and 1 from lowest to highest

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

`TextProcessor(lowercase=False, only_alpha_numeric=False, adjacent_pairs=False)`
:   A TextProcessor has common cleaning and tokenization methods to ensure
    that strings are processed in a consistent way
    
    Constructor for TextProcessor
    :param lowercase:
    :param only_alpha_numeric:
    :param adjacent_pairs:

    ### Methods

    `frequencies(self, string)`
    :   First processes and tokenizes string into words.  Then returns a map of the occurrences count of tokens.
        e.g. "a b b" yields {'a': 1, 'b', 2}
        :param string:
        :return: Dictionary containing token frequencies

    `normalized_frequencies(self, string)`
    :   Finds word frequencies in string, then treats all words as an axis and
        divides all the counts by the magnitude of the resulting vector.
        e.g. "a b b" yields {'a': 0.4472135954999579, 'b': 0.8944271909999159}
        
        :param string:
        :return: Dictionary containing normalized token frequencies

    `process(self, string)`
    :   If processor has only_alphabetic as True, then replaces all non-alphabetic characters with a whitespace.
        if processor has lowercase as True, it lowercases the string.
        
        :param string:
        :return: processed string

    `tokenize(self, string)`
    :   First processes string then splits string into tokens by word
        :param string:
        :return: list containing tokens