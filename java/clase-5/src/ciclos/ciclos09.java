package ciclos;

import java.util.Scanner;

public class ciclos09 {
    public static void main(String[] args){
        //ejercicio 9: pedir dia, mes, anio e indicar si la fecha
        //es correcta, suponiendo que todos los meses son de 30 dias
        Scanner input = new Scanner(System.in);

        //pedir datos
        System.out.print("Ingrese el día: ");
        int dia = Integer.parseInt(input.nextLine());

        System.out.print("Ingrese el mes: ");
        int mes = Integer.parseInt(input.nextLine());

        System.out.print("Ingrese el año: ");
        int anio = Integer.parseInt(input.nextLine());

        //comprobaciones
        if (anio > 0 && mes >= 1 && mes <= 12 && dia >= 1 && dia <= 30) {
            System.out.println("La fecha es correcta.");
        } else {
            System.out.println("La fecha es incorrecta.");
        }
    }
}
