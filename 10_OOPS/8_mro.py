class A:
    label = "A: Base Class"

class B(A):
    label = "B: Cold Coffee"

class C(A):
    label = "C: Hot Latte"

class D(B, C):
    pass

cup =D()
print(cup.label)
print(D.__mro__)
