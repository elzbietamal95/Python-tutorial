def flatten(aList):
    '''
    aList: a list
    Returns: a copy of aList, which is a flattened version of aList
    '''
    if aList == []:
        return []
    for item in aList:
        if type(item) == list:
            aList.remove(item)
            return flatten(item) + flatten(aList)
        else:
            aList.remove(item)
            return [item] + flatten(aList)


aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(aList))