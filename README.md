<div align="center">

# Simphile
**Python Text Similarity NLP Libray**

[![License](https://img.shields.io/github/license/brianrisk/simphile)](https://opensource.org/licenses/MIT)
![master passing](https://github.com/brianrisk/simphile/actions/workflows/tests.yml/badge.svg?branch=master)
![master passing](https://github.com/brianrisk/simphile/actions/workflows/publish_package.yml/badge.svg?branch=master)
![master passing](https://github.com/brianrisk/simphile/actions/workflows/publish_docs.yml/badge.svg?branch=master)

</div>

## Install
```bash
pip install simphile
```

## Usage
Just use comparison functions to get started quickly:
```python
from simphile import jaccard_similarity, euclidian_similarity, compression_similarity

text_a = "I love dogs"
text_b = "I love cats"

print(f"Jaccard: {jaccard_similarity(text_a, text_b)}")
print(f"Euclidian: {euclidian_similarity(text_a, text_b)}")
print(f"Compression: {compression_similarity(text_a, text_b)}")
```
Output:
```
Jaccard: 0.5
Euclidian: 0.5917517095361369
Compression: 0.6842105263157894
```

When you need to compare one reference text to many, it's more effecient to
set up a comparison object with that text

```python
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
    print(f"{comparison}: {comparator.score(comparison)}")
```
Output:
```
I love dogs: 0.09090909090909091
A fox. And a dog. Could never... be friends: 0.058823529411764705
The LAZY DOG was annoyed by the QUICK FOX, 0.38461538461538464
the quick dogs ran over the 23 brown carpets: 0.5454545454545454
```


## About
Sim•phile = "the love of similarities"

The aim is to proved easy access to text similarity methods that are language-agnostic and (ideally) much 
faster in execution time than methods that employ text embeddings.

* **Compression Similairty** – leverages the pattern recognition of compression algorithms
* **Euclidian Similarity** – Treats text like points in multi-dimensional space and calculates their closeness
* **Jaccard Similairy** – Texts are more similar the more their words overlap

### Use Cases:
* When speed is required
  * fast pre-filters:  Reduce a set of 10,000,000 text to the top 1000 then score those with CPU-intensive methods
* when language is unknown
* non-language comparisons (e.g. URL clustering)
* language detection (e.g. compare a text to Spanish, English, French, etc. lexicons and return match with highest score)

## Work with me!
My group is hiring two data scientists.  [Contact me on LinkedIn](https://www.linkedin.com/in/brianrisk/) about the positions

## Documentation
[Simphile text similarity documentation](https://brianrisk.github.io/simphile/index.html)

The /examples directory contains working code examples.

## E-Z ways to help
This is a world where the more popular something is, the more quickly it improves.  Help get the word out:
* Give this repo a ⭐️
* Vote up these answers on Stack Overflow 👍:
  * [How to compute the similarity between two text documents?](https://stackoverflow.com/a/73908280/2595659)
  * [How can I calculate the Jaccard Similarity of two lists containing strings in Python?](https://stackoverflow.com/a/73873869/2595659)
* Vote up the [Reddit post](https://www.reddit.com/r/LanguageTechnology/comments/xs11mx/new_python_text_similarity_package/)

## Brief Explanations

### Compression Similarity
Compression algorithms find patterns in files in order to shrink them.
This method uses that pattern detection to measure similarity. If a compressor can use
the patterns that it found in text_a to also decently compress text_b, then that means
there are similar patterns in both files.  The crux of the similarity score is computed
akin to this pseudocode example:

```
numerator = length(compress(concatenate(text_a, text_b)))
denominator = length(compress(text_a)) + length(compress(text_b))
score = numerator / denominator
```

Further Reading:
* ["The Similarity Metric"](https://ieeexplore.ieee.org/abstract/document/1362909) - the origin of this method
* [a nice writeup](https://maxhalford.github.io/blog/text-classification-by-compression/)

### Jaccard Similarity
![Jaccard Formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/eaef5aa86949f49e7dc6b9c8c3dd8b233332c9e7)

All of the write-ups I have seen for Jaccard get it wrong in the implementation.  They all use set() data structures.
At a quick glance this makes because the method uses set arithmetic (e.g. union, intersection).  However, sets don't allow duplicate elements,
so this is unsatisfactory for text analysis.  For example "dog cat cat cat" and "dog dog dog cat" are two very different
types of pet owners, but using sets would see that as {"dog", "cat"} and another {"dog", "cat"} and 100% similar.

This imeplementation of Jaccard uses set arithmetic on lists.

Further Reading:
* [Jaccard Index on Wikipedia](https://en.wikipedia.org/wiki/Jaccard_index)


### Euclidian Similarity
![Euclidian Distance](https://www.gstatic.com/education/formulas2/472522532/en/euclidean_distance.svg)

Treats tokenized words like dimensions and strings as normalized
points in this multi-dimensional space and uses the above formula
to calculate the distance between the two points being compared.


