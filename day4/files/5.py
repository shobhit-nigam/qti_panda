
with open("books.txt", "r") as fa:
    stra = fa.readlines()

print("stra =", stra)

for x in stra:
    print(x)
