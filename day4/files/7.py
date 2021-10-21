
with open("books.txt", "r") as fa:
    stra = fa.read()

lista = stra.splitlines()

print(lista)
