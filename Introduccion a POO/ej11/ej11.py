class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def __del__(self):
        print(f"El producto {self.__nombre} se ha agotado.")
    
    def getNombre(self):
        return self.__nombre
    
    def getPrecio(self):
        return self.__precio
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setPrecio(self, precio):
        self.__precio = precio

    def __str__(self):
        return (f"Producto: {self.__nombre}, Precio: ${self.__precio}")
    
class Pedido:
    def __init__(self, estado):
        self.__productos = []
        self.__estado = estado
    
    def __del__(self):
        print("El pedido ha sido finalizado.")

    def getEstado(self):
        return self.__estado
    
    def setEstado(self, estado):
        self.__estado = estado

    def getProductos(self):
        return self.__productos
    
    def agregarProducto(self, producto):
        self.__productos.append(producto)

    def __str__(self):
        productos_str = ', '.join(str(producto) for producto in self.__productos)
        return f"Pedido ( Estado='{self.__estado}', Productos= [{productos_str}] )"
    
cafe = Producto("Café", 50)
pastel = Producto("Pastel", 150)

pedido1 = Pedido("Registrado")
pedido1.agregarProducto(cafe)
pedido1.agregarProducto(pastel)

print(pedido1)
