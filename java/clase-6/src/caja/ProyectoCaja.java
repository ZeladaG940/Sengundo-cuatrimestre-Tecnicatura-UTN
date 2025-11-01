package caja;

public class ProyectoCaja {
    //ejercicio 1: Crear im proyecto segun las especificaciones mostradas a continuacion
    //la formula es: volumen = ancho* alto * profundidad

    //atributos o carateristicaas(muy importante)
    int ancho;
    int alto;
    int profundidad;

    //constructor: siempre lleva el nombre de la clase
    public ProyectoCaja(int  ancho, int alto, int profundidad) {
        this.alto = alto;
        this.ancho = ancho;
        this.profundidad = profundidad;
    }

    //metodo: con un tipo de retorno y nombre
    public int volumen(){
        int volumen = this.ancho*this.alto*this.profundidad;
        return volumen;
    }
}
