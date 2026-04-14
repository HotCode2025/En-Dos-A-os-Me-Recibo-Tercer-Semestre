class Monitor {
//CONTADOR 
static contadorMonitores = 0

constructor(marca, tamano) {
    Monitor.contadorMonitores++;
    this._idMonitor = Monitor.contadorMonitores;
    this.marca = marca;
    this.tamano = tamano;

 }
// metodo get
get idMonitor() {
    return this._idMonitor;
 }
 // metodo toString
toString() {
    return `Monitor: [idMonitor: ${this._idMonitor}, marca: ${this.marca}, tamano: ${this.tamano}]`;
 }
}