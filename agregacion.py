
class A:
    
    def __init__(self):
        self.valor = 10

class B:
    
    def __init__(self, objA):
        self.valor = 20
        self.objA = objA



a = A()
b = B(a)

print(b.objA.valor)