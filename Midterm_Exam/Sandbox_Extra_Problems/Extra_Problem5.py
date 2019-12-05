def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    skalar_product = 0
    for i in range(len(listA)):
        skalar_product += listA[i] * listB[i]
    return skalar_product

print(dotProduct([-2, -5, 28, -100, 20, 75, 17], [11, -3, -67, 86, 55, -24, -77]))