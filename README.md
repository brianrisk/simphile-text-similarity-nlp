<div align="center">

# Simphile
**Python Text Similarity NLP Libray**

[![License](https://img.shields.io/github/license/brianrisk/simphile)](https://opensource.org/licenses/MIT)
![master passing](https://github.com/brianrisk/simphile/actions/workflows/test.yml/badge.svg?branch=master)

</div>

## Intro
Sim•phile = "the love of similarities"

The aim is to proved easy access to text similairty metods that are language-agnostic and (ideally) much 
faster in execution time than methods that employ text embeddings.

* **Compression Similairty** – leverages the pattern recognition of compression algorithms
* **Euclidian Similarity** – Treating text like points in multi-dimensional space and calculating their closeness
* **Jaccard Similairy** – Texts are more similar the more their words overlap

### Use Cases:
* When speed is required
  * as fast pre-filters of results to reduce the set then fed to more CPU-intensive methods (e.g. embeddings)
* when language is unknown
* non-language comparisons (e.g. URL clustering)
* language detection (e.g. compare a text to Spanish, English, French, etc. lexicons and return match with highest score)

### Usage:

```pip install simphile```

## Documentation
[Simphile text similarity documentation](https://brianrisk.github.io/simphile/textsimilarity/index.html)

## E-Z ways to help
* Give this repo a ⭐️
* [Vote up this answer](https://stackoverflow.com/questions/46975929/how-can-i-calculate-the-jaccard-similarity-of-two-lists-containing-strings-in-py) on Stack Overflow!

## Brief Explanations

### Compression Similarity
Compression algorithms find patterns in files in order to shrink them.
This method uses that pattern detection to measure similarity. If a compressor can use
the patterns that it found in text_a to also decently compress text_b, then that means
there are similar patterns in both files.  The crux of the similarity score is computed
akin to this pseudocode example:

```length(compress(concatenate(text_a, text_b))) / (length(compress(text_a)) + length(compress(text_b)))```

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
* [Vote up this answer](https://stackoverflow.com/questions/46975929/how-can-i-calculate-the-jaccard-similarity-of-two-lists-containing-strings-in-py) on Stack Overflow!
* [Jaccard Index on Wikipedia](https://en.wikipedia.org/wiki/Jaccard_index)


### Euclidian Similarity



