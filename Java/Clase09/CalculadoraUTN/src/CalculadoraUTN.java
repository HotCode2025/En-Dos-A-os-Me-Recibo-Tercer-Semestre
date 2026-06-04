import java.util.Scanner;

public class CalculadoraUTN {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        while (true) {

            System.out.println("******** APLICACIÓN CALCULADORA **********");
            mostrarMenu(); //MOSTRAMOS EL MENU A TRAVEZ DE UNA FUNCION

            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {


                    ejecutarOperacion(operacion, entrada);



                } else if (operacion == 5) {

                    System.out.println("Saliendo....");
                    break; // Rompe y sale del programa

                } else {

                    System.out.println("Opción errónea " + operacion);
                }

                System.out.println();

            } catch (Exception e) { //fin del try, comienzo del catch
                System.out.println("Ocurrió un error: " + e.getMessage());
            }
        }

        entrada.close();
    }
    private static void mostrarMenu(){
        // Mostramos el menú
        System.out.println("""
                    1. Sumar
                    2. Restar
                    3. Multiplicar
                    4. División
                    5. SALIR
                    """);

        System.out.print("Operaciones a realizar? ");
    }
    private static void ejecutarOperacion(int operacion, Scanner entrada){
        System.out.print("Ingrese el valor para el operando1: ");
        var operando1 = Double.parseDouble(entrada.nextLine());

        System.out.print("Ingrese el valor para el operando2: ");
        var operando2 = Double.parseDouble(entrada.nextLine());
        double resultado;

        switch (operacion) {
            case 1 -> {
                resultado = operando1 + operando2;
                System.out.println("Resultado de la suma: " + resultado);
            }

            case 2 -> {
                resultado = operando1 - operando2;
                System.out.println("Resultado de la resta: " + resultado);
            }

            case 3 -> {
                resultado = operando1 * operando2;
                System.out.println("Resultado de la multiplicación: " + resultado);
            }

            case 4 -> {
                resultado = operando1 / operando2;
                System.out.println("Resultado de la división: " + resultado);
            }

            default -> System.out.println("OPCIÓN ERRÓNEA " + operacion);
        }//fin metodo ejecutarOperacion
    }
}