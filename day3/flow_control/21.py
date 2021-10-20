lista = ['ww', 'yy', 'uu', 'ww', 'rr', 'qq', 'ww', 'dd', 'kk', 'rr', 'ww']

dictc = {}
dictc.clear()

for x in lista:
    if x in dictc:
        dictc[x] = dictc[x] + 1
    else:
        dictc[x] = 1
#    print(dictc)



print(dictc)
