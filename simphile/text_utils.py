import re

# regex to remove all non-alphabetic
regex = re.compile('[^a-zA-Z ]')

# https://en.wikipedia.org/wiki/Most_common_words_in_English
common_english_words = [
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i'
]


# a common method to apply to both web and the training data
def only_alpha_numeric(text):
    text = regex.sub(' ', text)
    # removing multiple spaces
    text = re.sub(' +', ' ', text)
    return text


# example:
# input: ["one", "two", "three"]
# output: ["onetwo", "twothree"]
def create_adjacent_pairs(list):
    out = []
    for i, element in enumerate(list):
        if i > 0:
            out.append(list[i - 1] + list[i])
    return out

# TODO: add remove_words where a list can be specified,
#  if no list, then the top 10 most common English words are removed.
