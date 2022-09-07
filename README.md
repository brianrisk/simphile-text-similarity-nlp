# Simphile
**Python Text Similarity Libray**

Sim•phile = "the love of similarities"

## GZIP Score - "The Similarity Metric"
An interesting fact is that many pattern recognition algorithms can be used as compression algorithms. As Simphile proves, the converse of that statement is also true. Simphile uses the common compression algorithm gzip as its pattern detection engine. Let us say that we are comparing file A and file B. We compress file A to determine how small it can get. We then compress file B to see the amount it will shrink. Finally, we compress file A+B. If gzip(A+B) is significantly less than gzip(A) + gzip(B), then that means files A and B share patterns! (This method was inspired by Ming Li et al. in [The Similarity Metric](https://ieeexplore.ieee.org/abstract/document/1362909))

[a nice writeup](https://maxhalford.github.io/blog/text-classification-by-compression/)

## Jaccard ##

vote up this on Stack Overflow:
https://stackoverflow.com/questions/46975929/how-can-i-calculate-the-jaccard-similarity-of-two-lists-containing-strings-in-py



## List-based set operations ##

## Naive Bayes
![Naive Bayes](media/naive-bayes.png?raw=true)
