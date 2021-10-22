lista = [2, 6, 7, 9, 8, 3]
listb = [20, 10, 5, 4, 6, 8]

listx = list(map(lambda x, y: x if x>y else y, lista, listb))

print(listx)
