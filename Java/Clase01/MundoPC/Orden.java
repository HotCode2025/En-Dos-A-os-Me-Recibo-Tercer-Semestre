
public class Orden {
    //Contador
    private static int contadorOrdenes = 0;

    //Atributos
    private final int idOrden;
    private Computadora computadoras[];
    private static final int MAX_COMPUTADORAS = 10; // Constante para el tamaño máximo del arreglo de computadoras
    private int contadorComputadoras; // Contador para el número de computadoras agregadas a la orden

    //Constructor vacio para el contador
    public Orden() {
        this.idOrden = ++contadorOrdenes; // Incrementamos el contador de ordenes y asignamos el ID
        this.computadoras = new Computadora[Orden.MAX_COMPUTADORAS]; // Inicializamos el arreglo de computadoras con el tamaño máximo
    }

   //Métodos
    public void agregarComputadora(Computadora computadora) {
        if (contadorComputadoras < Orden.MAX_COMPUTADORAS) {
            this.computadoras[contadorComputadoras++] = computadora;
        } else {
            System.out.println("Has superado el límite de computadoras permitidas en esta orden: " + Orden.MAX_COMPUTADORAS);
        }
    }

    //Mostrar orden
    public void mostrarOrden() {
        System.out.println("Orden #" + this.idOrden);
        System.out.println("Computadoras de la orden #" + this.idOrden);
        for (int i = 0; i < contadorComputadoras; i++) {
            System.out.println(this.computadoras[i]);
        }
    }
}
