package operaciones;

public class PruebasAritmetica {
    public static void main(String[] args) {
        int a = 10;//variables locales
        int b = 5;
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

        System.out.println("aritmetica a: "+operacion.a);
        System.out.println("aritmetica b: "+operacion.b);

        //nuevo objeto
        Aritmetica operacion2 = new Aritmetica(8,2);
        System.out.println("aritmetica a: "+operacion2.a);
        System.out.println("aritmetica b: "+operacion2.b);
    }

}
