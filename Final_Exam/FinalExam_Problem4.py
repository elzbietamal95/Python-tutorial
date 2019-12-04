def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    item = 0
    maksimum = 0

    for element in t:
        if type(element) == tuple or type(element) == list:
            recursively_maksimum = max_val(t[item])
            if recursively_maksimum > maksimum:
                maksimum = recursively_maksimum
        elif type(element) == int:
            if element > maksimum:
                maksimum = element
        item += 1
    return maksimum

print(max_val(([5], 12, (1,2, [67, [[4,[100]]]]), [[1],[9]])))
