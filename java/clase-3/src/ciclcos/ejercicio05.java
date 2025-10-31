package ciclcos;

import javax.swing.*;
import java.util.Scanner;

public class ejercicio05 {
    public static void main(String[] srgs){
        //ejercicio 5: realizar un juego para adivinar un numero, para ello generar un numero
        //aleatorio entre 0 y 100 y luego ir pidiendo numneros indicando si "es mayor" o "es menor"
        //con respecto a N el procesos termina cuando el usuario acierta y mostramos el numero de intentos

        //esto genera un numero aleatorio
        /*int aleatorio = (int)(Math.random()*100);
        //System.out.println(aleatorio);

        boolean encontrado = false;
        Scanner input = new Scanner(System.in);
        int contador = 0;
        while (encontrado == false) {

            //datos y contador
            System.out.println("Digite um numero: ");
            int numero = Integer.parseInt(input.nextLine());
            contador++;

            //comprobaciones
            if (numero == aleatorio) {
                System.out.println("Felicidades el número era " + aleatorio);
                System.out.println("Intentos: " + contador);
                encontrado = true;
            } else {
                // metodo ternario
                System.out.println((numero < aleatorio) ? "Es mayor..." : "Es menor...");
            }

        }*/

        //con JOTion
        int aleatorio = (int)(Math.random()*100);
        //System.out.println(aleatorio);

        boolean encontrado = false;
        int contador = 0;
        while (encontrado == false) {

            //datos y contador
            int numero = Integer.parseInt(JOptionPane.showInputDialog("digite el numero: "));
            System.out.println(numero);
            contador++;

            //comprobaciones
            if (numero == aleatorio) {
                System.out.println("Felicidades el número era " + aleatorio);
                System.out.println("Intentos: " + contador);
                encontrado = true;
            } else {
                // metodo ternario
                System.out.println((numero < aleatorio) ? "Es mayor..." : "Es menor...");
            }

        }
    }
}
