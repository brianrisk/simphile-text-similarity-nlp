import re

# regex to remove all non-alphabetic
regex = re.compile('[^a-zA-Z ]')


# a common method to apply to both web and the training data
def clean(text):
    text = regex.sub(' ', text).lower()
    # removing multiple spaces
    text = re.sub(' +', ' ', text)
    return text


# example:
# input: ["one", "two", "three"]
# output: ["onetwo", "twothree"]
def adjacent_pairs(list):
    out = []
    for i, element in enumerate(list):
        if i > 0:
            out.append(list[i - 1] + list[i])
    return out