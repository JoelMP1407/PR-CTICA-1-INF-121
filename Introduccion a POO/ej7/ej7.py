#Ejercicio 7. Dada la clase Mascota
class Mascota:
    def __init__(self, nombre, tipo, energia):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__energia = energia

    def getNombre(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo 
    
    def getEnergia(self):
        return self.__energia
    
    def setEnergia(self, energia):
        self.__energia = energia
        if self.__energia <= 0:
            self.__energia = 0
        elif self.__energia >= 100:
            self.__energia = 100
        return self.__energia

#a) Agrega un método para alimentar (+20 de energía, máximo 100).
    def alimentar(self):
        if self.getEnergia() < 100:
            self.setEnergia(self.getEnergia() + 20)
        else:
            self.setEnergia(100)
        print(f"{self.getNombre} fue alimentado. Su energia es de {self.getEnergia}.")

#b) Agrega un método para jugar (-15 de energía, mínimo 0).
    def jugar(self):
        if self.getEnergia() >= 15:
            self.setEnergia(self.getEnergia() - 15)
        else:
            self.setEnergia(0)
        print(f"{self.getNombre} se divirtió jugando. Su energia es de {self.getEnergia}.")

#c) Crea dos mascotas, aliméntalas y hazlas jugar, mostrando su energía en cada paso.
print("Crea una mascota:")
nombre = input("Ingrese el nombre de la mascota: ")
tipo = input("Ingrese el tipo de mascota: ")
energia = int(input("Ingrese la energia inicial de la mascota (0-100): "))
while energia < 0 or energia > 100:
    energia = int(input("Energia invalida. Ingrese la energia inicial de la mascota (0-100): "))
mascota1 = Mascota(nombre, tipo, energia)

print("------------------------------------------------")

print("Crea otra mascota:")
nombre = input("Ingrese el nombre de la mascota: ")
tipo = input("Ingrese el tipo de mascota: ")
energia = int(input("Ingrese la energia inicial de la mascota (0-100): "))
while energia < 0 or energia > 100:
    energia = int(input("Energia invalida. Ingrese la energia inicial de la mascota (0-100): "))
mascota2 = Mascota(nombre, tipo, energia)

mascota1.alimentar()
mascota1.jugar()

mascota2.alimentar()
mascota2.jugar()