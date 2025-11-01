package ciclos;

import javax.swing.*;
import java.util.Scanner;

public class ciclos06 {
    public static void main(String[] args) {
        //ejercicio 6: pedir numeros hasta que se teclee un 0, mostrar la suma
        //de todos los numeros introducions

        //variables
        /*int contador = 0;
        boolean cero = false;
        Scanner input = new Scanner(System.in);

        while (cero == false){
            //pedir numero
            System.out.println("ingrese el numero: ");
            int numero = Integer.parseInt(input.nextLine());

            //comprobaciones
            if (numero > 0){
                contador += numero;
            }else{
                System.out.println("la suma de los numero introducidos es: " + contador);
                cero = true;
            }

        }*/

        //con JOPtion
        int cont = 0;
        boolean cero = false;
        while (cero == false) {
            //pedir datos
            int numero = Integer.parseInt(JOptionPane.showInputDialog("ingrese el numero: "));
            System.out.println(numero);

            //comprobaciones
            if (numero > 0){
                cont += numero;
            }else{
                System.out.println("la suma de los numeros es: " + cont);
                cero = true;
            }
        }

    }
}
