import javax.swing.*;
import java.util.Scanner;

public class ejerciciosConLosDos {
    public static void main(String[] args){
        //Leer un numero y indicar si es positivo y negativo, el proceso se repetira esta que se introdusca un 0

        //num confirmara si el ciclo continua
        /*Boolean num = false;

        //do while
        do{
            //class scaneer importado
            Scanner input = new Scanner(System.in);

            //pedir info y almacenar en numero
            System.out.println("Digite um numero: ");
            int numero = Integer.parseInt(input.nextLine());

            //comprobaciones con numero
            if(numero >= 0){
                System.out.println("el numero "+numero+" es positivo: Felicidades....");
            }else{
                //si num es menor a 0
                System.out.println("el numero "+numero+" es negativo: Nos vemos...");
                //el determinante pasa a verdadero y termina el ciclo
                num = true;
            }
        }while (num == false);*/

        //con JOPtion

        //buleano
        boolean nega = false;

        //ciclo while
        while(nega == false){
            //pedimos datos con JOPtion
            int num = Integer.parseInt(JOptionPane.showInputDialog("ingese el numero: "));

            //comprovaciones
            if (num >= 0){
                System.out.println("el numero "+num+" es positivo: Felicidades...");
            }else{
                //si las comprobaciones fallan pasa a else y termina
                System.out.println("el numero "+num+" es negativo: Adios...");
                nega = true;
            }
        }
    }
}
