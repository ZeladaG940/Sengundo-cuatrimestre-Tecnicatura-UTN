package ciclos;

import javax.swing.*;
import java.util.Scanner;

public class ciclos10 {
    public static void main(String[] args) {
        //ejercicio 10: Pedir 10 numeros y escribir la sumna total

        //acumulador
        /*int total = 0;
        Scanner input = new Scanner(System.in);
        for (int i=1; i<=10; i++){

            //pedir datos
            System.out.println("digite un numero: ");
            int numero = Integer.parseInt(input.nextLine());
            //suma a total cada dato
            total +=  numero;
        }
        //imprime cada dato
        System.out.println("la suma de los numeros es: " + total);*/

        //con JOtion
        int total = 0;
        for (int i=1; i<=10; i++){

            //pedir datos
            System.out.println("digite un numero: ");
            int numero = Integer.parseInt(JOptionPane.showInputDialog("digite el numnero: "));
            System.out.println(numero);
            //suma a total cada dato
            total +=  numero;
        }
        //imprime cada dato
        System.out.println("la suma de los numeros es: " + total);
    }
}
