def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    inverse_dict = {}
    for key in d.keys():
        if d[key] in inverse_dict:
            inverse_dict[d[key]].append(key)
        else:
            inverse_dict[d[key]] = [key]
    for value in inverse_dict.values():
        value.sort()
    return inverse_dict

d = {4:True, 2:True, 0:True}
#d = {1:10, 2:20, 3:30, 4:30}
#d = {1:10, 2:20, 3:30}
print(dict_invert(d))
