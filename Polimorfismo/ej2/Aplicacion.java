package Polimorfismo.ej2;

import java.util.Scanner;

public class Aplicacion {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        System.out.println("Ingrese el nombre del videojuego:");
        String nombre1=sc.nextLine();
        Videojuego v1=new Videojuego(nombre1);
        System.out.println(v1.toString());

        System.out.println("Ingrese el nombre del videojuego:");
        String nombre2=sc.nextLine();
        System.out.println("Ingrese la plataforma del videojuego:");
        String plataforma2=sc.nextLine();
        System.out.println("Ingrese la cantidad de jugadores del videojuego:");
        int cantidadDeJugadores2=sc.nextInt();
        Videojuego v2=new Videojuego(nombre2, plataforma2, cantidadDeJugadores2);
        System.out.println(v2.toString());

        v1.agregarJugadores();
        System.out.println("Ingrese la cantidad de jugadores a agregar al videojuego 2:");
        int cantidad = sc.nextInt();
        v2.agregarJugadores(cantidad);
        System.out.println(v2.toString());
    }
}
