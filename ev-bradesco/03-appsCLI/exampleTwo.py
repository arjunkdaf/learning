import math

class Esfera:
    # __init__ é chamado sempre que um novo objeto é instanciado
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio
    def volume(self):
        vol = (4 / 3) * math.pi * (self.raio ** 3)
        return vol
    def area(self):
        ar = 4 * math.pi * (self.raio ** 2)
        return ar

bola1 = Esfera("vermelha", 4)
bola2 = Esfera("azul", 7)

print(f"O volume da bola 1 é {bola1.volume()}cm3")
print(f"A área superficial da bola 1 é {bola1.area()}cm2")

# duas expressões/formas de ter o mesmo retorno
print(bola1.volume())
print(Esfera.volume(bola1))
