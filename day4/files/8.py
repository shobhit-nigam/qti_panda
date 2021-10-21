
with open("books.txt", "r") as fa:
    lista = fa.readlines()


fb = open("m_books.txt", "w")

for line in lista:
    if "m" in line:
        fb.write(line)

fb.close()
