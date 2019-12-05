def closest_power(base, num):
    if base == num:
        return 1
    elif base > num:
        return 0
    else:
        exponent = 2
        while base**exponent <= num:
            exponent += 1
        if abs(base**exponent - num) < abs(base**(exponent - 1) - num):
            return exponent
        else:
            exponent -= 1
        return exponent

print(closest_power(3,3))
print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))