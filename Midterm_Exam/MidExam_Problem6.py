def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    maks = max(L)
    if (L.count(maks) % 2) == 0:
        return None
    else:
        return maks


print(largest_odd_times([3,9,9,9,5,5,3,5,3]))