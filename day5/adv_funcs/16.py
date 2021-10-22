lista = ["xd22", "ed34", "xd34", "ed44", "ex34"]

def only_34(val):
    return val[-2:] == "34"

listx = list(filter(only_34, lista))

print(listx)
