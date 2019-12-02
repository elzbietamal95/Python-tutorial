def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not

    wzor na n-ty wyraz ciagu triangulacji: a_0 = 0, a_(n) = a_(n-1) + n
    rozwiazanie rekurencyjne tego ciagu to: a_(n) = [n(n+1)]/2
    """
    i = 0
    triangular_number = 0
    while triangular_number <= k:
        i += 1
        triangular_number = (i*(i+1))/2
        if triangular_number == k:
            return True
    return False

def triangular(k):
    """
    funkcja wypisujaca k pierwszych elementow ciagu triangulacji
    np. dla k =7 funkcja wypisze:
    [1, 3, 6, 10, 15, 21, 28]
    """
    triangular_numbers = []
    number = 0
    for i in range(1, k + 1):
        number += i
        triangular_numbers.append(number)
    print(triangular_numbers)

def trian(k):
    """
    druga wersja funkcji "triangular"
    """

    num = 0
    i = 0
    trian_nums = []
    while i < k:
        i += 1
        num += i
        trian_nums.append(num)
    print(trian_nums)

def is_triangular2(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    i = 1
    triangular_number = 0
    while triangular_number < k:
        triangular_number += i
        i += 1
    if triangular_number == k:
        return True
    return False


triangular(7)
trian(7)
print(is_triangular(10))
print(is_triangular2(21))