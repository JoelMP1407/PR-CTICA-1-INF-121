package ej13;

public class Aplicacion {
    public static void main(String[] args) {
        Fruta fruta1 = new Fruta("Naranja", "Citrica", new String[]{"C", "A", "B1", "B2"});
        Fruta fruta2 = new Fruta("Manzana", "templada", new String[]{"B1", "B2", "E"});
        Fruta fruta3 = new Fruta("Platano", "tropical", new String[]{"C", "B6", "E", "K", "B2"});

        Fruta mayor = Fruta.masVitaminas(fruta1, fruta2, fruta3);
        System.out.println("La fruta con mas vitaminas es: " + mayor.getNombre());

        System.out.println("Vitaminas de cada fruta:");
        System.out.println(fruta1.mostrarVitaminas());
        System.out.println(fruta2.mostrarVitaminas());
        System.out.println(fruta3.mostrarVitaminas());

        int vitaminasCitricas = fruta1.contarVitaminasCitricas() + fruta2.contarVitaminasCitricas() + fruta3.contarVitaminasCitricas();
        System.out.println("Cantidad total de vitaminas citricas (C y A): " + vitaminasCitricas);

        fruta1.ordenarVitaminas();
        fruta2.ordenarVitaminas();
        fruta3.ordenarVitaminas();

        System.out.println("Vitaminas ordenadas:");
        System.out.println(fruta1.mostrarVitaminas());
        System.out.println(fruta2.mostrarVitaminas());
        System.out.println(fruta3.mostrarVitaminas());
    }
}
