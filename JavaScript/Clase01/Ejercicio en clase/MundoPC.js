class DispositivoEntrada {
  // Constructor
  constructor(tipoEntrada, marca) {
    this._tipoEntrada = tipoEntrada;
    this._marca = marca;
  }

  // Getters
  get tipoEntrada() {
    return this._tipoEntrada;
  }

  get marca() {
    return this._marca;
  }

  //Setters
  set tipoEntrada(tipoEntrada) {
    this._tipoEntrada = tipoEntrada;
  }

  set marca(marca) {
    this._marca = marca;
  }
}

class Raton extends DispositivoEntrada {
  // Herencia de la clase DispositivoEntrada
  static contadorRatones = 0; // Variable estática para contar el número de ratones creados

  // Constructor
  constructor(tipoEntrada, marca) {
    super(tipoEntrada, marca); // Llamada al constructor de la clase padre
    this._idRaton = ++Raton.contadorRatones; // Asignamos un ID único al ratón
  }

  toString() {
    return `Raton [ID: ${this._idRaton}, Tipo Entrada: ${this.tipoEntrada}, Marca: ${this.marca}]`;
  }
}

let raton1 = new Raton("USB", "Logitech");
console.log(raton1.toString());

let raton2 = new Raton("Bluetooth", "Microsoft");
console.log(raton2.toString());

class Teclado extends DispositivoEntrada {
  // Herencia de la clase DispositivoEntrada
  static contadorTeclados = 0; // Variable estática para contar el número de teclados creados

  //Constructor
  constructor(tipoEntrada, marca) {
    super(tipoEntrada, marca); // Llamada al constructor de la clase padre
    this._idTeclado = ++Teclado.contadorTeclados; // Asignamos un ID único al teclado
  }

  toString() {
    return `Teclado [ID: ${this._idTeclado}, Tipo Entrada: ${this.tipoEntrada}, Marca: ${this.marca}]`;
  }
}

let teclado1 = new Teclado("Cable", "Redragon");
console.log(teclado1.toString());

let teclado2 = new Teclado("Bluetooth", "HyperX");
console.log(teclado2.toString());

class Monitor {
  static contadorMonitores = 0; // Variable estática para contar el número de monitores creados

  // Constructor
  constructor(marca, tamaño) {
    this._marca = marca;
    this._tamaño = tamaño;
    this._idMonitor = ++Monitor.contadorMonitores; // Asignamos un ID único al monitor
  }

  // Getters
  get idMonitor() {
    return this._idMonitor;
  }

  // Métodos
  toString() {
    return `Monitor [ID: ${this._idMonitor}, Marca: ${this._marca}, Tamaño: ${this._tamaño}]`;
  }
}

let monitor1 = new Monitor("Samsung", 27);
console.log(monitor1.toString());

let monitor2 = new Monitor("LG", 32);
console.log(monitor2.toString());

class Computadora {
  static contadorComputadoras = 0; // Variable estática para contar el número de computadoras creadas

  // Constructor
  constructor(nombre, monitor, teclado, raton) {
    this._nombre = nombre;
    this._monitor = monitor;
    this._teclado = teclado;
    this._raton = raton;
    this._idComputadora = ++Computadora.contadorComputadoras; // Asignamos un ID único a la computadora
  }

  // Métodos
  toString() {
    return `Computadora [ID: ${this._idComputadora}, Nombre: ${this._nombre}]\n${this._monitor.toString()}\n${this._teclado.toString()}\n${this._raton.toString()}`;
  }
}

let computadora1 = new Computadora("Gaming PC", monitor1, teclado1, raton1);
console.log(computadora1.toString());

let computadora2 = new Computadora("Office PC", monitor2, teclado2, raton2);
console.log(computadora2.toString());

class Orden {
  static contadorOrdenes = 0; // Variable estática para contar el número de órdenes creadas

  // Constructor
  constructor() {
    this._idOrden = ++Orden.contadorOrdenes; // Asignamos un ID único a la orden
    this._computadoras = []; // Array para almacenar las computadoras en la orden
  }

  //Métodos
  get idOrden() {
    return this._idOrden;
  }

  agregarComputadora(computadora) {
    this._computadoras.push(computadora); // Agrega una computadora a la orden
  }

  mostrarOrden() {
    let computadorasOrden = "Computadoras en la orden:\n";
    for (let computadora of this._computadoras) {
      computadorasOrden += `${computadora.toString()}\n`;
    }
    return `Orden [ID: ${this._idOrden}]\n${computadorasOrden}`;
  }
}

let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);
console.log(orden1.mostrarOrden());
