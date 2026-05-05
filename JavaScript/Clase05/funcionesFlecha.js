// Función tradicional
function miFuncion() {
  console.log("Saludos desde mi función");
}
miFuncion();

// Función anónima
let myFuncion = function () {
  console.log("Saludos desde mi función anónima");
};
myFuncion();

// Función flecha
let miFuncionFlecha = () => {
  console.log("Saludos desde mi función flecha");
};
// Hay mas variantes para las funciones flecha, esta es la forma más básica
miFuncionFlecha();

// En una sola línea
const saludar = () =>
  console.log("Hola desde una función flecha en una sola línea");
console.log(saludar); // Esto no ejecuta la función, solo muestra la referencia a la función, undefined

const saludar2 = () => {
  return "Saludos desde una función flecha con return";
};
console.log(saludar2());

// Simplificamos la funcion anterior
const saludar3 = () => "Saludos desde una función flecha simplificada 3";
console.log(saludar3());

// Si queremos regresar un objeto, debemos envolverlo entre paréntesis para evitar confusiones con el bloque de código
const regresaObj = () => ({ nombre: "Juan", edad: 30 });
console.log(regresaObj());

// Función flecha con parámetros
const funcionParametros = (mensaje) => {
  console.log(mensaje);
};
funcionParametros("Hola desde una función flecha con parámetros");

//Funcion clasica
const funcionParametrosClasica = function (mensaje) {
  console.log(mensaje);
};
funcionParametrosClasica("Hola desde una función clásica con parámetros");

// se pueden omitir los paréntesis en la función flecha
const funcionConParametros = (mensaje) => {
  console.log(mensaje);
};
funcionConParametros(
  "Hola desde una función flecha sin paréntesis en los parámetros",
);

// Funcion flecha con varios parámetros
const funcionVariosParametros = (a, b) => {
  let resultado = a + b;
  return resultado;
};
console.log(funcionVariosParametros(5, 10));

// se pueden omitir los paréntesis en la función flecha
const funcionVariosParametros2 = (a, b) => a + b;
console.log(funcionVariosParametros2(2, 10));
