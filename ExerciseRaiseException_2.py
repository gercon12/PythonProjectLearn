class AdultError(Exception):
    def __init__(self, age, name, message="Person is an adult"):
        super().__init__(f"{message} (age={age} name={name})")
        self.age = age
        self.name = name


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def is_minor(self) -> bool:
        if self.age >= 18:
            bandera = True
        else:
            bandera = False
        return bandera

    def get_minor_age(self) -> int:
        if self.is_minor():
            raise AdultError(self.name, self.age)
        return self.age

    def display_person(self) -> None:
        try:
            edad = self.get_minor_age()

        except AdultError as e:
            # 3) Manejo aquí porque sé qué mostrar
            print("AdultError capturada:", e)
        else:
            # 4) Solo si no hubo excepción
            print(f"Edad -> {edad}")
        finally:
            # 5) Siempre se ejecuta (limpieza o info final)
            print(f"Nombre -> {self.name}")

# Demostración
Person("Bhavin", 17).display_person()   # menor
Person("Dhaval", 23).display_person()   # adulto (lanza y se atrapa)