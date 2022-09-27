Module simphile.sets
====================

Functions
---------

    
`intersect(list_a, list_b)`
:   Intersection of elements of two lists
    
    Lists allow repeated elements.  For example:
      list_a = ['a', 'b', 'b']
      list_b = ['b', 'b', 'c']
    the intersect of list_a and list_b would be:
      ['b', 'b']
    
    Taken from https://stackoverflow.com/a/64625586/2595659
    Note that most of the other answers on StackOverflow are not suitable as they are not symmetric.
    Symmetry being when  intersect(a, b) == intersect(b, a).
    
    
    :param list_a: list of elements.  Strings, Ints, etc.
    :type list_a: list
    
    :param list_b:  list of elements.  Strings, Ints, etc.
    :type list_a: list
    
    :return: A list of the intersecting elements

    
`minus(list_a, list_b)`
:   https://stackoverflow.com/a/57827145/2595659
    
    :param list_a: list of elements.  Strings, Ints, etc.
    :type list_a: list
    
    :param list_b:  list of elements.  Strings, Ints, etc.
    :type list_a: list
    
    :return: list of elements from list_a with those overlapping with list_b removed

    
`union(list_a, list_b)`
:   Union is not simply A + B.  Thinking of the venn diagram, that would double the intersecting "canoe" shape.
    
    :param list_a: list of elements.  Strings, Ints, etc.
    :type list_a: list
    
    :param list_b:  list of elements.  Strings, Ints, etc.
    :type list_a: list
    
    :return: A list of the intersecting elements