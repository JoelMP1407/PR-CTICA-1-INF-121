#Ejercicio 3. Diseña una clase Producto que tenga atributos nombre, precio y stock. Agrega métodos para vender productos y reabastecer el stock.
class Producto:
#a) Define la clase y los atributos
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

#b) Agrega un método vender(cantidad: Int) que reste del stock
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock = self.stock - cantidad
            ganancia = cantidad * self.precio
            print(f"Se vendieron {cantidad} unidades de {self.nombre}. Ganancia: Bs. {ganancia}")
        else:
            print(f"No hay suficiente stock de {self.nombre}. Stock actual: {self.stock}")
#c) Agrega un método reabastecer(cantidad: Int) que sume al stock.
    def reabastecer(self, cantidad):
        self.stock = self.stock + cantidad
        print(f"Se reabastecieron {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

    def mostrarProducto(self):
        print(f"Producto: {self.nombre}, Precio: Bs. {self.precio}, Stock: {self.stock}")

producto = input("Ingrese el producto que va a vender:")
cantidad = int(input("Ingrese la cantidad de productos que va a vender:"))
precio = float(input("Ingrese el precio del producto:"))
miTienda = Producto(producto, precio, cantidad)
miTienda.mostrarProducto()

opcion = int(input("Para comprar presione 1, para reabastecer presione 2, para salir presione 3: "))
while opcion != 3:
    if opcion == 1:
        cantidadParaVender = int(input("Ingrese la cantidad de productos que desea vender: "))
        miTienda.vender(cantidadParaVender)
        miTienda.mostrarProducto()
    elif opcion == 2:
        cantidadParaReabastecer = int(input("Ingrese la cantidad de productos que desea reabastecer: "))
        miTienda.reabastecer(cantidadParaReabastecer)
        miTienda.mostrarProducto()
    opcion = int(input("Para comprar mas presione 1, para reabastecer presione 2, para salir presione 3: "))