
fa = open("books.txt", "r")

stra = fa.read(7)
print(stra)

stra = fa.read(7)
print(stra)

print(fa.tell())
fa.seek(3)
stra = fa.read(7)
print(stra)

fa.close()
