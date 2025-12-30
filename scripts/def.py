def min_number(list):
    minimanl = list[0]

    for el in list:
        if (el < minimanl):
            minimanl = el

    return minimanl

print(min_number([5, 2, 6, 9, 1, 7]))
print(min_number([6, 7, 4, 2, 7, 5, 8, 4.2, 1.1]))

mult = lambda x, y: x * y
print(mult(9, 4.1))