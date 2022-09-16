class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombre_completo(self):
        return (f"{self.apellido}, {self.nombre}")
    
    def es_mayor(self):
        if self.edad >= 18:
            return True
        else:
            return False
    
persona1 = Persona("Miguel", "Lescano", 27)
print(persona1.nombre_completo())
print(persona1.es_mayor())