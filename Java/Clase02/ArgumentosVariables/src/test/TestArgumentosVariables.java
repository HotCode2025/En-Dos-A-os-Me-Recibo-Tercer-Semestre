package test;

public class TestArgumentosVariables {

    public static void main(String[] args) {

        System.out.println("test.TestArgumentosVariables.main()");
        //imprimimos los numeros
        imprimirNumeros(3, 4, 5);
        imprimirNumeros(1, 2);
        
        //método con varios parámetros
        variosParametros("En dos años me recibo", 9, 10, 20, 45, 23, 18, 33);
    }

    private static void imprimirNumeros(int... numeros) {
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Elementos: " + numeros[i]);
        }
    }

    private static void variosParametros(String nombre, int... numeros) {
        System.out.println("Nombre: "+nombre);
        imprimirNumeros(numeros);
    }

}
