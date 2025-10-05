package ej13;

public class Fruta {
    private String nombre;
    private String tipo;
    private int nroVitaminas;
    private String[] v = new String[30];

    public Fruta(String nombre, String tipo, String[] vitaminas) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.nroVitaminas = vitaminas.length;
        for (int i = 0; i < vitaminas.length && i < 30; i++) {
            v[i] = vitaminas[i];
        }
    }

    public String getNombre() {
        return nombre;
    }

    public int getNroVitaminas() {
        return nroVitaminas;
    }

    public String[] getVitaminas() {
        return v;
    }

    public String mostrarVitaminas() {
        String resultado = "Vitaminas de " + nombre + ": ";
        for (int i=0; i < nroVitaminas; i++) {
            resultado = resultado + v[i];
            if (i < nroVitaminas - 1) {
                resultado = resultado + ", ";
            }
        }
        return resultado;
    }

    public int contarVitaminasCitricas() {
        int contador = 0;
        for (int i=0; i < nroVitaminas; i++) {
            if (v[i] != null && (v[i].equalsIgnoreCase("C") || v[i].equalsIgnoreCase("A"))){
                contador++;
            }
        }return contador;
    }

    public static Fruta masVitaminas(Fruta f1, Fruta f2, Fruta f3) {
        Fruta mayor = f1;
        if (f2.getNroVitaminas() > mayor.getNroVitaminas()) mayor = f2;
        if (f3.getNroVitaminas() > mayor.getNroVitaminas()) mayor = f3;
        return mayor;
    }

    public void ordenarVitaminas() {
        for (int i = 0; i < nroVitaminas - 1; i++) {
            for (int j = i + 1; j < nroVitaminas; j++) {
                if (v[i].compareToIgnoreCase(v[j]) > 0) {
                    String temp = v[i];
                    v[i] = v[j];
                    v[j] = temp;
                }
            }
        }
    }
}
