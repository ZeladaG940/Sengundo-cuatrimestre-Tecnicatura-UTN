//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //ciclos en java
        //while  //el ciclo se repetira mientras que contador sea menor o igual a 10
        var contador = 1;
        while (contador <= 10) {
            System.out.println("Contador: " + contador);
            contador++;
        }

        //do while  //el siclo se repetira mientras contador sea menor o igual a 10
        var contador2 = 1;
        do {
            System.out.println("Contador2: " + contador2);
            contador2++;
        } while (contador2 <= 10);

        //ciclo for  //el ciclo se repetira mientras i sea menor o igual a 10
        for (var i=0; i<=10; i++){
            System.out.println("Contador3: " + i);
        }

        //etiquetas brack y continue
        for (var i=0; i<=10; i++){
            if (i == 3){
                System.out.println("llegaste al limite: " + i);
                break; //break rompe el ciclo y ase que salga
            }
            System.out.println("Contador4: " + i);
        }

        for (var i=0; i<=10; i++){
            if(i == 5){
                System.out.println("este es el limimte marcado: " + i);
                continue; //no rompe pero marca que llegaste al limite
            }
            System.out.println("Contador5: " + i);
        }

        //labels llamada a funciones u otras cosas  a travez de una palabra clave y dos puntos
        inicio:
        for (var i=0; i<=10; i++){
            if  (i == 3){
                System.out.println("llegaste al limitem llamaremos a labels");
                break inicio;
            }
        }
    }
}