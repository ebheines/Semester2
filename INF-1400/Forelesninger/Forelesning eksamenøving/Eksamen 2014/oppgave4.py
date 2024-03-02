class A:
    def __init__(self):
        pass

    def foo(self, val):
        print("A", val)


class B(A):
    def __init__(self):
        super().__init__()


class C(B):
    def __init__(self):
        super().__init__()

    def foo(self, val):
        print("B", val)



a = A()
b = B()
c = C()

a.foo(1)
b.foo(2)
c.foo(3)

        