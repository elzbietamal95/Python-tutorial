import math

def polysum(n, s):
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    perimeter = n * s
    sum = area + perimeter ** 2
    return round(sum, 4)

# print(polysum(23, 30))