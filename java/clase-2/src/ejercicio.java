import java.util.Scanner;

public class ejercicio {
    public static void main(String[] args) {
        //ejercicio: ller un numero y mostrar su cuadrado, repetir el proceso asta que se introdusca un numero negativo
        //introduccion ala clase scaner

        System.out.println("programa para sacarel cuadrado");
        var negatico = false;
        while (negatico == false) {

            //ingresa el numero
            Scanner input = new Scanner(System.in);
            System.out.println("introduzca el numero: ");
            int numero = input.nextInt();

            //comprobacion
            if(numero >= 0){
                int cuadrado = numero * numero;
                System.out.println("su cuadrado es: " + cuadrado);
            }else {
                negatico = true;
            }
        }
    }
}