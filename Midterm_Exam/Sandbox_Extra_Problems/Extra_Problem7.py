def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    dict_intersect = {}
    dict_difference = {}
    for key in d1.keys():
        if key in d2.keys():
            dict_intersect[key] = f(d1[key], d2[key])
        else:
            dict_difference[key] = d1[key]
    for key in d2.keys():
        if key not in d1.keys():
            dict_difference[key] = d2[key]
    return (dict_intersect, dict_difference)

def f(a, b):
    return a + b

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
print(dict_interdiff(d1, d2))

def f(a, b):
    return a > b

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print(dict_interdiff(d1, d2))