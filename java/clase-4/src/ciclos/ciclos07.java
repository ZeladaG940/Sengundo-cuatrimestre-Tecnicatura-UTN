package ciclos;

import javax.swing.*;
import java.util.Scanner;

public class ciclos07 {
    public static void main(String[] args) {
        //ejercicio /: Pedir numeros hasta que se introduzca uno negativo
        //y calcular la media

        //variables
        /*boolean negativo = false;
        int suma = 0;
        int contador = 0;
        Scanner input = new Scanner(System.in);

        while (negativo == false){
            //pedir datos
            System.out.println("ingrese un numero: ");
            int numero = Integer.parseInt(input.nextLine());

            //por cada datos se sumara a suma y se agregara a contador +1 como un nuevo dato
            if (numero > 0){
                suma += numero;
                contador++;
            }else{
                //imprime media y pasa a negativo como verdadero
                double media =  suma / contador;
                System.out.println("la media es: " + media);
                negativo = true;
            }
        }*/

        //con JOPtion
        boolean negativo = false;
        int suma = 0;
        int contador = 0;
        Scanner input = new Scanner(System.in);

        while (negativo == false){
            //pedir datos
            int numero = Integer.parseInt(JOptionPane.showInputDialog("ingre un numero: "));
            System.out.println(numero);

            //por cada datos se sumara a suma y se agregara a contador +1 como un nuevo dato
            if (numero > 0){
                suma += numero;
                contador++;
            }else{
                //imprime media y pasa a negativo como verdadero
                double media =  suma / contador;
                System.out.println("la media es: " + media);
                negativo = true;
            }
        }
    }
}
