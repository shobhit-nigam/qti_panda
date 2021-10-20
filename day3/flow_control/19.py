lista = ['ww', 'yy', 'uu', 'ww', 'rr', 'qq', 'ww', 'dd', 'kk', 'rr', 'ww']

# for with range

ww_index = []

for x in range(len(lista)):
    if lista[x] == 'ww':
        ww_index.append(x)

print(ww_index)
