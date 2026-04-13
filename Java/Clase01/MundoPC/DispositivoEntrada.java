

public class DispositivoEntrada {
    //Atributos
    private String tipoEntrada;
    private String marca;


    //Constructor
    public DispositivoEntrada(String tipoEntrada, String marca) {
        this.tipoEntrada = tipoEntrada;
        this.marca = marca;
    }

    //Getters
    public String getTipoEntrada() {
        return this.tipoEntrada;
    }

    public String getMarca() {
        return this.marca;

    }

    //Setters
    public void setTipoEntrada(String tipoEntrada) {
        this.tipoEntrada = tipoEntrada;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    //toString
    @Override
    public String toString() {
        return "DispositivoEntrada{" + "tipoEntrada=" + tipoEntrada + ", marca=" + marca + '}';
    }

}
