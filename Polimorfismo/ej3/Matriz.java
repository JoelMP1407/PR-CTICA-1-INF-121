package Polimorfismo.ej3;

public class Matriz {
    public int[][] datos;
    public int filas;
    public int columnas;

    public Matriz(){
        this.filas = 10;
        this.columnas = 10;
        this.datos = new int[filas][columnas];

        for (int i = 0; i < filas; i++){
            for (int j = 0; j < columnas; j++){
                if (i == j){
                    datos[i][j] = 1;
                }else{
                    datos[i][j] = 0;
                }
            }
        }
    }

    public Matriz(int datos){
        this.filas = 10;
        this.columnas = 10;
        this.datos = new int[filas][columnas];

        for (int i = 0; i < filas; i++){
            for (int j = 0; j < columnas; j++){
                datos[i][j] = datos;
            }
        }
    }

    @Override
    public String toString(){
        String matriz = "";
        for (int i = 0; i < filas; i++){
            for (int j = 0; j < columnas; j++){
                matriz = matriz + datos[i][j] + " ";
            }matriz = matriz + "\n";
        }return matriz;
    }
}
