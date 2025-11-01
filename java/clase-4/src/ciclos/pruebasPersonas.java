package ciclos;

public class pruebasPersonas {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona();//llamamos al constructor
        persona1.nombre = "Fernando";
        persona1.apellido = "Mendoza";
        persona1.obtenerInformacion();//imprime

        //creacion de mas objetos
        Persona persona2 = new Persona();
        persona2.nombre = "Orlando";
        persona2.apellido = "Zelada";
        persona2.obtenerInformacion();
    }
}
