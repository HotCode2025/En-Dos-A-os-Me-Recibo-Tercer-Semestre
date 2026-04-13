

public class Teclado extends DispositivoEntrada {
    //Atributos
    private final int idTeclado;
    private static int contadorTeclados;

    //Constructor
    public Teclado(String tipoEntrada, String marca) {
        super(tipoEntrada, marca);
        this.idTeclado = ++contadorTeclados; // Incrementamos el contador de teclados y asignamos el ID
    }

    //toString
    @Override
    public String toString() {
        return "Teclado{" + "idTeclado=" + this.idTeclado + ',' + super.toString() + '}';
    }

}
