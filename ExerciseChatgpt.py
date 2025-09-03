class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

personas = [Persona("Ana"), Persona("Luis"), Persona("Marta")]

nombres = [p.nombre for p in personas if "a" in p.nombre.lower()]
print(nombres)