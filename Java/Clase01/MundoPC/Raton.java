

public class Raton extends DispositivoEntrada {
    //Atributos
    private final int idRaton;
    private static int contadorRatones;

    //Constructor
    public Raton(String tipoEntrada, String marca) {
        super(tipoEntrada, marca);
        this.idRaton = ++contadorRatones; // Incrementamos el contador de ratones y asignamos el ID
    }

    //toString
    @Override
    public String toString() {
        return "Raton{" + "idRaton=" + this.idRaton + ',' + super.toString() + '}';
    }
}
