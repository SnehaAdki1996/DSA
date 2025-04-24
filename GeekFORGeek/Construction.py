class A:
    def __init__(self):
        print ("A's init")


class B(A):
    def __init__(self):
        super().__init__()
        print ("B's init")


b1= B()
a1 = A()