def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    sum_of_digits = 0
    sum_of_not_digits = 0
    for sign in s:
        try:
            sum_of_digits += int(sign)
        except:
            sum_of_not_digits += 1
    if len(s) != sum_of_not_digits:
        return sum_of_digits
    else:
        return ValueError("There are no digits in this string.")
        #raise ValueError

print(sum_digits("a;35d4"))
print(sum_digits("!@#$%%"))
