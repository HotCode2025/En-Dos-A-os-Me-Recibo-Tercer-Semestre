class Computadora {
  static contadorComputadoras = 0;

  constructor(nombre, monitor, teclado, raton) {
    this.idComputadora = ++Computadora.contadorComputadoras;
    this.nombre = nombre;
    this.monitor = monitor;
    this.teclado = teclado;
    this.raton = raton;
  }

  toString() {
    return `
Computadora [ID: ${this.idComputadora}, Nombre: ${this.nombre}]
${this.monitor.toString()}
${this.teclado.toString()}
${this.raton.toString()}
    `;
  }
}






















