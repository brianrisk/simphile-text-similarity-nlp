from simphile.sets import intersect, minus


def jaccard(list_a, list_b):
    assert len(list_a) > 0 or len(list_b > 0), "at least one list needs to have elements"
    intersected = intersect(list_a, list_b)
    combined = list_a + list_b
    # did not use the union function for efficiency in sets.  Union also calculates intersection,
    # so we don't want to duplicate that processing
    unioned = minus(combined, intersected)
    return len(intersected) / len(unioned)
