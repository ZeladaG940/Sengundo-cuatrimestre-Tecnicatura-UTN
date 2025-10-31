import javax.swing.*;

public class ojPtionPane {
    public static void main(String[] args){
        //leer un numero y mostrar su cuadrado, repetir el proceso asta que se introdusca un numero negativo

        boolean numNegativo = false;
        while (numNegativo == false){

            //pide un dato numerico
            int numero = Integer.parseInt(JOptionPane.showInputDialog("ingrese el numero"));
            if (numero >= 0){

                //mortiplica el numero por si mismo = cuadrado
                int cuadrado = (int)Math.pow(numero,2);
                System.out.println("Su cuadrado es: " + cuadrado);
            }else{
                System.out.println("Ingreso un numero negativo, nos vemos....");
                numNegativo = true;
            }
        }


    }
}
