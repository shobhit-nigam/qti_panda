fa = open("books.txt", "r")

stra = fa.read(7)
print("stra =", stra)

fa.close()

print(type(fa))
