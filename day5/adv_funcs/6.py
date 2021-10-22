listx = ["joey", "does'nt", "share", "food"]

print(list(enumerate(listx)))

print(list(enumerate(listx, start=6)))

enum = (enumerate(listx))

print(type(enum))
print(enum)
