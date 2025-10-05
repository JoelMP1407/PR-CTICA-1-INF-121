package ej15;

public class Buzon {
    private int nro;
    private int nroC;
    private String[][] c;
    
    public Buzon(int nro, int nroC) {
        this.nro = nro;
        this.nroC = nroC;
        this.c = new String[50][3];
    }

    public int getNro() {
        return nro;
    }

    public int getNroC() {
        return nroC;
    }

    public String[][] getC() {
        return c;
    }

    public void setNro(int nro) {
        this.nro = nro;
    }

    public void setNroC(int nroC) {
        this.nroC = nroC;
    }

    public int contarCartasDeDestinatario(String destinatario) {
        int contador = 0;
        for (int i = 0; i < nroC; i++) {
            if (c[i][1] != null && c[i][1].equalsIgnoreCase(destinatario)) {
                contador++;
            }
        }
        return contador;
    }

    public boolean eliminarCartaPorCodigo(String codigo) {
        for (int i = 0; i < nroC; i++) {
            if (c[i][0] != null && c[i][0].equalsIgnoreCase(codigo)) {

                for (int j = i; j < nroC - 1; j++) {
                    c[j][0] = c[j + 1][0];
                    c[j][1] = c[j + 1][1];
                    c[j][2] = c[j + 1][2];
                }

                c[nroC - 1][0] = null;
                c[nroC - 1][1] = null;
                c[nroC - 1][2] = null;

                nroC--; 
                return true; 
            }
        }return false;
    }
}
