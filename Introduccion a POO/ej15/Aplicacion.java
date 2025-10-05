package ej15;
import java.util.Scanner;
public class Aplicacion {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Buzon buzon1 = new Buzon(1, 3);
        buzon1.getC()[0][0] = "000"; buzon1.getC()[0][1] = "Juan Perez"; buzon1.getC()[0][2] = "Hola, aqui te envio el comprobante.";
        buzon1.getC()[1][0] = "001"; buzon1.getC()[1][1] = "Adrian Gutierrez"; buzon1.getC()[1][2] = "Hola, necesitamos hablar.";
        buzon1.getC()[2][0] = "002"; buzon1.getC()[2][1] = "Ana Losa"; buzon1.getC()[2][2] = "Hola, ha pasado un tiempo.";
        
        Buzon buzon2 = new Buzon(2, 3);
        buzon2.getC()[0][0] = "004"; buzon2.getC()[0][1] = "Emilio Marquez"; buzon2.getC()[0][2] = "Hola, gracias por tu donativo.";
        buzon2.getC()[1][0] = "005"; buzon2.getC()[1][1] = "Adriana Santos"; buzon2.getC()[1][2] = "Recibo de la luz.";
        buzon2.getC()[2][0] = "006"; buzon2.getC()[2][1] = "Carlos Guevara"; buzon2.getC()[2][2] = "Recibo del agua.";
        
        Buzon buzon3 = new Buzon(3, 3);
        buzon3.getC()[0][0] = "000"; buzon3.getC()[0][1] = "Juan Perez"; buzon3.getC()[0][2] = "Gracias por su compra.";
        buzon3.getC()[1][0] = "001"; buzon3.getC()[1][1] = "Alfonso Chavez"; buzon3.getC()[1][2] = "Nuevas ofertas disponibles.";
        buzon3.getC()[2][0] = "002"; buzon3.getC()[2][1] = "Lupe Espinoza"; buzon3.getC()[2][2] = "Este es el catalogo de esta semana.";

        int cantidad = buzon1.contarCartasDeDestinatario("Juan Perez");
        System.out.println("Cartas recibidas por Juan Perez: " + cantidad);
        
        String codigoDeCartaAEliminar;
        do{
            System.out.println("Ingrese el codigo de la carta a eliminar (3 digitos): ");
            codigoDeCartaAEliminar = sc.nextLine();
        }while(codigoDeCartaAEliminar.length()<0 || codigoDeCartaAEliminar.length()>3);
        
        if (buzon1.eliminarCartaPorCodigo(codigoDeCartaAEliminar)) {
            System.out.println("La carta fue eliminada correctamente.");
        } else {
            System.out.println("No se encontró ninguna carta con ese código.");
        }
    }
}
