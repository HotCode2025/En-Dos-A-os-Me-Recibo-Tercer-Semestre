class DispositivoEntrada {
    constructor(tipoEntrada, marca) {
        this._tipoEntrada = tipoEntrada;
        this._marca = marca;
    }

    get tipoEntrada() { return this._tipoEntrada; }
    get marca() { return this._marca; }

    set tipoEntrada(tipoEntrada) { this._tipoEntrada = tipoEntrada; }
    set marca(marca) { this._marca = marca; }
}