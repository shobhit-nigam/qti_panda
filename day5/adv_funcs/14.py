lista = [2, 6, 7, 9, 8, 3]
listb = [20, 10, 5, 4, 6, 8]

def calc(a, b):
    return 3*a + 4*b - 3

listx = list(map(calc, lista, listb))

print(listx)
