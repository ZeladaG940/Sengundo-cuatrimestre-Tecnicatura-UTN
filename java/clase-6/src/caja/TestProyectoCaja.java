package caja;

public class TestProyectoCaja {
    public static void main(String[] args) {

        //objeto 1
        ProyectoCaja caja = new ProyectoCaja(10, 10, 15);
        System.out.println(caja.volumen());

        //objeto 2
        ProyectoCaja caja2 = new ProyectoCaja(5,5,5);
        System.out.println(caja2.volumen());
    }

}
