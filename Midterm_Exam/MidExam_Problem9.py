def permutation(L1, L2):
    result = False
    if len(L1) == len(L2):
        for element in L1:
            if L1.count(element) == L2.count(element):
                result = True
            else:
                return False
    else:
        return False

def is_list_permutation(L1, L2):
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    elif (permutation(L1, L2) == False):
        return False
    else:
        most_occur_elem = max(L1, key=L1.count)
        how_many_times_occur = L1.count(most_occur_elem)
        type_most_occur_elem = type(most_occur_elem)
        return (most_occur_elem, how_many_times_occur, type_most_occur_elem)

L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']

#L1 = ['a', 'a', 'b']
#L2 = ['a', 'b']

#L1 = []
#L2 = []
print(is_list_permutation(L1, L2))
print(is_list_permutation([0, 4, 8, 3, 0, 2, 2, 1, 4, 7, 8, 3, 7, 0, 0], [3, 4, 0, 3, 8, 0, 2, 0, 7, 2, 0, 3, 7, 2, 1]))