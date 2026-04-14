class Raton extends DispositivoEntrada {
    static contadorRatones = 0; 

    constructor(tipoEntrada, marca){
        super(tipoEntrada, marca)

        this._idRaton = ++Raton.contadorRatones;
    }

    get idRaton() { return this._idRaton; }

    toString() {
        return `Raton: [idRaton: ${this._idRaton}, tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}]`;
    }
}


class Teclado extends DispositivoEntrada {
    static contadorTeclados = 0;

    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this._idTeclado = ++Teclado.contadorTeclados;
    }

    get idTeclado() { return this._idTeclado; }

    toString() {
        return `Teclado: [idTeclado: ${this._idTeclado}, tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}]`;
    }
}