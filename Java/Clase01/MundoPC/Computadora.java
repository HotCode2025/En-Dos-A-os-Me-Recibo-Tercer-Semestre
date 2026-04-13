

public class Computadora {
    //Contador
    private static int contadorComputadoras = 0;

    //Atributos
    private final int idComputadora;
    private String nombre;
    private Monitor monitor;
    private Teclado teclado;
    private Raton raton;

    //Constructor vacio para el contador
    public Computadora() {
        this.idComputadora = ++contadorComputadoras;
    }

    //Constructor con parametros
    public Computadora(String nombre, Monitor monitor, Teclado teclado, Raton raton) {
        this(); // Llamamos al constructor vacío para asignar el ID
        this.nombre = nombre;
        this.monitor = monitor;
        this.teclado = teclado;
        this.raton = raton;
    }

    //Getters
    public int getIdComputadora() {
        return this.idComputadora;
    }
    public String getNombre() {
        return this.nombre;
    }
    public Monitor getMonitor() {
        return this.monitor;
    }
    public Teclado getTeclado() {
        return this.teclado;
    }
    public Raton getRaton() {
        return this.raton;
    }

    //Setters
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public void setMonitor(Monitor monitor) {
        this.monitor = monitor;
    }
    public void setTeclado(Teclado teclado) {
        this.teclado = teclado;
    }
    public void setRaton(Raton raton) {
        this.raton = raton;
    }

    //toString
    @Override
    public String toString() {
        return "Computadora{" + "idComputadora=" + this.idComputadora + ", nombre=" + this.nombre + ", monitor=" + this.monitor + ", teclado=" + this.teclado + ", raton=" + this.raton + '}';
    }
}
