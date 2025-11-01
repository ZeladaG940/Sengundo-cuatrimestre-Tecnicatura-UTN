package operaciones;

public class PruebasAritmetica {
    public static void main(String[] args) {
        Aritmetica operacion = new Aritmetica();
        //agregando valores
        operacion.a = 3;
        operacion.b = 5;
        operacion.suma();

        //asi se mustra el metodo con retorno
        int resultado = operacion.sumarConRetirno();
        System.out.println(resultado);

        //asi se muestra un metodo con argumentos
        resultado = operacion.sumaConArgumento(7, 8);
        System.out.println("resultado usando argumentos: " + resultado);
    }

}
