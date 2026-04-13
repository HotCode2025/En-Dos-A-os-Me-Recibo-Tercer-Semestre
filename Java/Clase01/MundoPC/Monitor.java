

public class Monitor {
    //Contador
    private static int contadorMonitores = 0;

    //Atributos
    private final int idMonitor;
    private String marca;
    private double tamano;

    //Constructor
    public Monitor(String marca, double tamano) {
        this.idMonitor = ++contadorMonitores; // Incrementamos el contador de monitores y asignamos el ID
        this.marca = marca;
        this.tamano = tamano;
    }

    //Getters
    public int getIdMonitor() {
        return this.idMonitor;
    }

    public String getMarca() {
        return this.marca;
    }

    public double getTamano() {
        return this.tamano;
    }

    //Setters
    public void setMarca(String marca) {
        this.marca = marca;
    }    

    public void setTamano(double tamano) {
        this.tamano = tamano;
    }

    //toString
    @Override
    public String toString() {
        return "Monitor{" + "idMonitor=" + this.idMonitor + ", marca=" + this.marca + ", tamano=" + this.tamano + '}';
    }

}
