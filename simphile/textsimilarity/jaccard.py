from sets import intersect, minus


def jaccard(list_a, list_b):
    intersected = intersect(list_a, list_b)
    combined = list_a + list_b
    # did not use the union function for effeciency.  Union also calculates intersection,
    # so we don't want to duplicate that processing
    unioned = minus(combined, intersected)
    return len(intersected) / len(unioned)



a = "hey you people over there".split(" ")
b = "you people over what".split(" ")
jaccard(a, b)