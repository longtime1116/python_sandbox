x = 1
y = 2

def foo():
    y = 4
    z = 8
    def bar():
        return x + y + z
    return bar()

print(foo())
