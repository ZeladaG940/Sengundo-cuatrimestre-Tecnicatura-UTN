package operaciones;

public class Aritmetica {
    //atributos de la clase
    int a;
    int b;
    //metodo
    public void suma(){
        int resultado = a + b;
        System.out.println("la suma es: " + resultado);
    }

    //se una int para indicar que devolvera un dato entero
    public int sumarConRetirno(){
        int resulado = this.a + this.b;
        //retorno
        return resulado;
    }

    //metodos con argumentos (se debe de espesificar el tpo de argumento que resivira)
    public int sumaConArgumento(int arg1, int arg2){
        //variables de argumento
        this.a = arg1;//al argumento a se le asigna el atributo this
        this.b = arg2;
        //return a + b;
        //tambien se puede llamar a un metodo
        return this.sumarConRetirno();
    }


}
