Module simphile.text_processor
==============================

Classes
-------

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