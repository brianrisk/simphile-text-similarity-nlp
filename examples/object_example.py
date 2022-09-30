from simphile import JaccardSimilarity, TextProcessor

reference = "the quick brown fox jumped over the lazy dogs"
comparisons = [
    "I love dogs",
    "A fox. And a dog. Could never... be friends",
    "The LAZY DOG was annoyed by the QUICK FOX",
    "the quick dogs ran over the 23 brown carpets"
]
# TextProcessor applies the same cleaning logic to all text
processor = TextProcessor(lowercase=True, only_alphabetic=True)
# using JaccardSimilarity, but code is exactly the same with
# CompressionSimilarity and EuclidianSimilarity
comparator = JaccardSimilarity(reference, processor)
# scoring the reference to each string in the `comparisons` list
for comparison in comparisons:
    print(comparator.score(comparison))
