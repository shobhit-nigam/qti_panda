def funca(la, lb, *args, **kwargs):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("kwargs =", kwargs)

funca(100, 200, 300, 400, {4:"hi", 5:"hello"}, india='new delhi', norway='oslo')
