# syntax error
def funca(la=22, lb, lc=33):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)

funca(100, 200, 300)
print("----")
funca(100, 200)
print("----")
funca(100)
print("----")
# error
funca()
