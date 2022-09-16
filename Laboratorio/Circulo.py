import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def diametro(self):
        dia = self.radio * 2
        return dia

    def perimetro(self):
        per = math.pi * self.diametro()
        return per

    def superficie(self):
        sup = math.pi * (self.radio**2)
        return sup
nuevoCirculo = Circulo(5)

print(f"El diametro del circulo es {nuevoCirculo.diametro()}")
print(f"El perimetro del circlo es {nuevoCirculo.perimetro()}")
print(f"La superficie del circulo es {nuevoCirculo.superficie()}")

