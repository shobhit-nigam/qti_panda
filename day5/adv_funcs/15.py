lista = [2, 6, 7, 9, 8, 3]
listb = [20, 10, 5, 4, 6, 8]

def calc(a):
    if a%4 == 0:
        return True
    else:
        return False

listx = list(filter(calc, listb))

print(listx)
