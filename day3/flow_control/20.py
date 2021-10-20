lista = ['ww', 'yy', 'uu', 'ww', 'rr', 'qq', 'ww', 'dd', 'kk', 'rr', 'ww']

for x in range(len(lista)):
    if lista[x] == 'rr':
        print("found")
        break
else:
    print("not found")

print("---")

for x in range(len(lista)):
    if lista[x] == 'bb':
        print("found")
        break
else:
    print("not found")

####
