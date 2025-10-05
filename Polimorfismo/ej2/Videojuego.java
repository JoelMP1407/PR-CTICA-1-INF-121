package Polimorfismo.ej2;

class Videojuego{
    public String nombre;
    public String plataforma;
    public int cantidadDeJugadores;

    public Videojuego(String nombre, String plataforma, int cantidadDeJugadores){
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadDeJugadores = cantidadDeJugadores;
    }

    public Videojuego(String nombre, String plataforma){
        this(nombre, plataforma, 1);
    }

    public Videojuego(String nombre){
        this(nombre, "Desconocida", 1);
    }

    public void agregarJugadores(){
        cantidadDeJugadores = cantidadDeJugadores + 1;  
    }

    public void agregarJugadores(int cantidad){
        cantidadDeJugadores = cantidadDeJugadores + cantidad;  
    }

    @Override
    public String toString() {
        return "Videojuego [nombre: " + nombre + ", plataforma: " + plataforma + ", cantidad de jugadores: " + cantidadDeJugadores + "]";
    }
}