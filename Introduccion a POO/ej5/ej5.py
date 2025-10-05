#Ejercicio 5. Define la clase Persona (nombre, paterno, materno, edad, ci)
class Persona:
    def __init__(self, nombre, paterno, materno, edad, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci
#b) Implementar método mostrarDatos()
    def mostrarDatos(self):
        print(f"Nombre: {self.nombre} {self.paterno} {self.materno}")
        print(f"Edad: {self.edad}")
        print(f"C.I.: {self.ci}")

#c) Implementar el metodo mayorDeEdad() que determina si la persona es mayor de edad o no
    def mayorDeEdad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} no es mayor de edad.")

#d) Implementar método modificarEdad(nuevo) que modifica la edad de la persona.
    def modificarEdad(self, nuevo):
        self.edad = nuevo
        print(f"La nueva edad de {self.nombre} es {self.edad}.")

#e) Verificar si las dos personas tienen el mismo apellido paterno.
    def verificarPaterno(self, otraPersona):
        if self.paterno == otraPersona.paterno:
            print(f"{self.nombre} y {otraPersona.nombre} tienen el mismo apellido paterno: {self.paterno}.")
        else:
            print(f"{self.nombre} y {otraPersona.nombre} no tienen el mismo apellido paterno.")

#a) Instanciar a dos personas.
persona1 = Persona("Pepe", "Cabrera", "Gutierrez", 16, 1764508)
persona2 = Persona("Lupita", "Perez", "Sanchez", 54, 1273409)

persona1.mostrarDatos()
persona1.mayorDeEdad()
nuevaEdad = int(input(f"Ingrese la nueva edad de {persona1.nombre}: "))
persona1.modificarEdad(nuevaEdad)
persona1.mayorDeEdad()

persona2.mostrarDatos()
persona2.mayorDeEdad()

persona1.verificarPaterno(persona2)

print("Ahora ingresa los datos de una nueva persona.")
nombre = input("Ingrese el nombre: ")
paterno = input("Ingrese el apellido paterno: ")
materno = input("Ingrese el apellido materno: ")
edad = int(input("Ingrese la edad: "))
ci = input("Ingrese la C.I.: ")
persona3 = Persona(nombre, paterno, materno, edad, ci)
persona3.mostrarDatos()