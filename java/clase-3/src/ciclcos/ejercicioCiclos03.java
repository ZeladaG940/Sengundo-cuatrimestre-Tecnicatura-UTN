package ciclcos;

import javax.swing.*;

public class ejercicioCiclos03 {
    public static void main(String[] args) {
        //ejercicio 3: leer numeros asta que se introdusca un 0
        //para cada uno indicar si es par o inpar con scanner y OPTion

        /*boolean cero = false;
        System.out.println("programam apra saber si un numero es par o impar");
        System.out.println("Para terminar el programa digite el 0");
        while (cero == false){
            Scanner input = new Scanner(System.in);
            //pedir datos
            System.out.println("Ingrese el numero: ");
            int numero = Integer.parseInt(input.nextLine());

            //comprobaciones
            if (numero % 2 == 0){
                System.out.println("el numero es par: " + numero);
            }else{
                System.out.println("el numero es impar: " + numero);
            }

            //si nuero es 0 pasar cero = true para terminar el ciclo
            if(numero == 0){
                System.out.println("el programam termino. Nos vemos...");
                cero = true;
            }
        }*/

        //Con Option
        boolean CERO = false;
        System.out.println("programam apra saber si un numero es par o impar");
        System.out.println("Para terminar el programa digite el 0");
        while (CERO == false) {
            //pedir datos
            int numero = Integer.parseInt(JOptionPane.showInputDialog("ingrese el numero: "));
            if (numero % 2 == 0) {
                System.out.println("el numero es par: " + numero);
            } else {
                System.out.println("el numero es impar: " + numero);
            }
            if (numero == 0){
                System.out.println("el programam a finalizado: Nos vemos...");
                CERO = true;
            }
        }
    }
}
