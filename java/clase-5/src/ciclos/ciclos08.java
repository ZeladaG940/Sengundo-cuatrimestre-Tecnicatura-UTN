package ciclos;

import javax.swing.*;
import java.util.Scanner;

public class ciclos08 {
    public static void main(String[] args) {
        //ejercicio N numeros, y mostrar todos los numero
        /*Scanner input = new Scanner(System.in);

        System.out.println("ingrese la cantidad de numeros ue desea ver: ");
        int numero = Integer.parseInt(input.nextLine());

        for(int i=0; i<=numero; i++){
            System.out.println(i);
        }*/
        int numero = Integer.parseInt(JOptionPane.showInputDialog("ingrese la cantida de numeros a mostrar: "));

        for(int i=0; i<=numero; i++) {
            System.out.println(i);
        }
    }
}
