public class DispositivoEntrada {
    private String tipoEntrada;
    private String marca;

    public DispositivoEntrada(String tipoEntrada, String marca) {
        this.tipoEntrada = tipoEntrada;
        this.marca = marca;
    }

    public String getTipoEntrada() {
        return this.tipoEntrada;
    }

    public String getMarca() {
        return this.marca;
    }

    public void setTipoEntrada(String tipoEntrada) {
        this.tipoEntrada = tipoEntrada;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    //  MÉTODO PARA POLIMORFISMO
    public String tipoDispositivo() {
        return "Dispositivo de entrada";
    }

    @Override
    public String toString() {
        return "tipoEntrada=" + tipoEntrada + ", marca=" + marca;
    }
}
