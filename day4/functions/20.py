ga = 10

def funcx():
    global ga
    la = 20
    ga = 33
    print("ga =", ga)
    print("la =", la)

print("outside ga =", ga)
print("---")
funcx()
print("---")
print("outside ga =", ga)
