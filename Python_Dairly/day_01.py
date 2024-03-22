def foo(x, y=[]):
    y.append(x)
    return y
print(foo(1))
print(foo(2))