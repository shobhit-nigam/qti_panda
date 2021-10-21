def boil(x):
    print("boiled", x)

def dipped(x):
    print(x, "with milk")

def cook(x):
    print("had", x)

# dipped("corn flakes")
# boil("sweet potato")

def eat(gen, y):
    gen(y)

eat(cook, "poha")

eat(dipped, "toast")

# higher order functions
