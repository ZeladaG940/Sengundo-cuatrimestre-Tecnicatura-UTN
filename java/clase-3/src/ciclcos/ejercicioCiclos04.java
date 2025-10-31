package ciclcos;

import javax.swing.*;
import java.util.Scanner;

public class ejercicioCiclos04 {
    public static void main(String[] args) {
        //ejercicio 4: Pedir numeros asta que se teclee uno negativo y mostrar cuantos numero se
        //an introducido con scaner  JOtion

        //SCANNER
        /*boolean negativo = false;
        int contador = 0;
        Scanner input  = new Scanner(System.in);

        //mientras negativo sea falso
        while (negativo  == false){
            //pedir datos
            System.out.println("digite el numero: ");
            int numero = Integer.parseInt(input.nextLine());
            //por cada vuelta el contador sumara 1
            contador++;

            //si el numero es menor a 0 se mostrara el total de numero introducido y negativo pasa a true
            if (numero < 0){
                System.out.println("el total de numero introducciones es: " + contador);
                negativo = true;
            }
        }*/


        //JOPtion
        boolean nega = false;
        int contador = 0;
        while (nega == false){

            //pedir datos
            int numero = Integer.parseInt(JOptionPane.showInputDialog("ingrese un numero: "));
            System.out.println("numero: " + numero);

            //contador
            contador++;

            //test
            if (numero < 0){
                System.out.println("el total de numero introdusidos es: " + contador);
                nega = true;
            }
        }

    }
}
