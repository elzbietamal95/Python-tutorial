def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    while len(L) != 0:
        maks = max(L)
        counter_maks = L.count(maks)
        if (counter_maks % 2) != 0:
            return maks
        else:
            for i in range(counter_maks):
                L.remove(maks)
            largest_odd_times(L)
    return None


print(largest_odd_times([3,9,9,9,5,5,3,5,3]))