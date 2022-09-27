import re

# regex to remove all non-alphabetic
regex = re.compile('[^a-zA-Z ]')

# https://en.wikipedia.org/wiki/Most_common_words_in_English
common_english_words = [
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i'
]


def only_alphabetic(text):
    """
    Removes all non-alphabetic characters and replaces with spaces.
    Multiple adjacent spaces are reduced to one.
    :param text:
    :return:
    """
    text = regex.sub(' ', text)
    # removing multiple spaces
    text = re.sub(' +', ' ', text)
    return text


def create_adjacent_pairs(list):
    """
    example:
        input: ["one", "two", "three"]
        output: ["onetwo", "twothree"]
    :param list:
    :return:
    """
    out = []
    for i, element in enumerate(list):
        if i > 0:
            out.append(list[i - 1] + list[i])
    return out

# TODO: add remove_words where a list can be specified,
#  if no list, then the top 10 most common English words are removed.
