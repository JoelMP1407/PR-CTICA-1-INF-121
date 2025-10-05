#Ejercicio 2. Realiza la abstracción de un Bus.
class Bus:
    def __init__(self, cantidadDePasajeros, asientosTotales):
        self.cantidadDePasajeros = cantidadDePasajeros
        self.asientosTotales = asientosTotales
        self.ganancias = 0

#a) Al bus desean subir X cantidad de pasajeros, actualiza los datos del bus.
    def subirPasajeros(self, personasQueQuierenSubir): 
        asientosDisponibles = self.asientosTotales - self.cantidadDePasajeros
        if personasQueQuierenSubir <= asientosDisponibles:
            self.cantidadDePasajeros = self.cantidadDePasajeros + personasQueQuierenSubir
            print(f"{personasQueQuierenSubir} personas subieron al bus.")
        else:
            print(f"No hay suficientes asientos.")

#b) Crea un método para cobrar pasaje a los pasajeros. (Costo del pasaje: bs. 1.50)
    def cobrarPasaje(self):
        precioPasaje = 1.50
        self.totalCobrado = self.cantidadDePasajeros * precioPasaje
        self.ganancias = self.ganancias + self.totalCobrado
        print(f"Se cobraron Bs. {self.totalCobrado} de pasajes.")

#c) Muestra cuántos asientos quedan disponibles.
    def asientosDisponibles(self):
        asientosDisponibles = self.asientosTotales - self.cantidadDePasajeros
        print(f"Quedan {asientosDisponibles} asientos disponibles.")

#Estado del Bus
    def estadoDelBus(self):
        print(f"Cantidad de pasajeros: {self.cantidadDePasajeros}")
        print(f"Ganancias totales: Bs. {self.ganancias}")

#d) Crea una instancia del bus y utiliza los métodos de los incisos anteriores.
miBus = Bus(0, 40)

#Subir Pasajeros
numeroDePersonas = int(input("Ingrese el numero de personas que quieren subir al bus: "))
miBus.subirPasajeros(numeroDePersonas)
#Cobrar Pasaje
miBus.cobrarPasaje()
#Revisar Bus
miBus.estadoDelBus()

#Subir mas Pasajeros
DeseaSubirMasPersonas = input("¿Desea subir mas personas al bus? (si/no): ").lower()
if DeseaSubirMasPersonas == "si":
    numeroDePersonas = int(input("Ingrese el numero de personas que quieren subir al bus: "))
    miBus.subirPasajeros(numeroDePersonas)
    #Cobrar Pasaje
    miBus.cobrarPasaje()
    #Revisar Bus
    miBus.estadoDelBus()
else:
    print("Gracias por usar mi bus.")