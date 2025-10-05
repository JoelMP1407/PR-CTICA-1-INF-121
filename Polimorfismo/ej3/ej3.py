class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[0] * columnas for i in range (filas)]

        for i in range(self.filas):
            for j in range(self.columnas):
                if i == j:
                    self.matriz[i][j] = 1
                else:
                    self.matriz[i][j] = 0

    def __str__(self):
        Matriz = ""
        for i in range (self.filas):
            for j in range (self.columnas):
                Matriz = Matriz + str(self.matriz[i][j]) + " "
            Matriz = Matriz + "\n"
        return Matriz


matriz = Matriz(10, 10)
print(matriz)