#coding=utf8
def var():
    a = int(42)
    print("{0} has a type {1}".format(a, a.__class__))
    b = "42"
    print("{0} has a type {1}".format(b, b.__class__))
    c = "quarante-deux"
    print("{0} has a type {1}".format(c, c.__class__))
    d = float(42.0)
    print("{0} has a type {1}".format(d, d.__class__))
    e = True
    print("{0} has a type {1}".format(e, e.__class__))
    f = [42]
    print("{0} has a type {1}".format(f, f.__class__))
    g = {42: 42}
    print("{0} has a type {1}".format(g, g.__class__))
    q = (42,)
    print("{0} has a type {1}".format(q, q.__class__))
    i = set()
    print("{0} has a type {1}".format(i, i.__class__))

if __name__ == '__main__':
    var()