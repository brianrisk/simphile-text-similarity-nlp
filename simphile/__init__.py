"""
## Install
```pip install simphile```
## About
Sim•phile = "the love of similarities"

The aim is to proved easy access to text similairty metods that are language-agnostic and (ideally) much
faster in execution time than methods that employ text embeddings.

* **Compression Similarity** – leverages the pattern recognition of compression algorithms
* **Euclidian Similarity** – Treating text like points in multi-dimensional space and calculating their closeness
* **Jaccard Similarity** – Texts are more similar the more their words overlap

"""
from . import sets
from . import text_utils
from .text_processor import TextProcessor
from .naive_bayes import NaiveBayes
from .compression_similarity import compression_similarity, CompressionSimilarity
from .euclidian_similarity import euclidian_similarity, EuclidianSimilarity
from .jaccard_similarity import jaccard_similarity, jaccard_list_similarity, JaccardSimilarity

__all__ = [
    "sets",
    "text_utils",
    "TextProcessor",
    "NaiveBayes",
    "compression_similarity",
    "CompressionSimilarity",
    "euclidian_similarity",
    "EuclidianSimilarity",
    "jaccard_similarity",
    "jaccard_list_similarity",
    "JaccardSimilarity"
]