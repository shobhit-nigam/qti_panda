
with open("books.txt", "r") as fa:
    stra = fa.read()

print("stra =", stra)

print(stra.count('of'))
