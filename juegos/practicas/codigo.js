
// 1 = Piedra, 2 = Papel, 3 = Tijera

// Variables principales
let jugador = 0;
let pc = 0;
let triunfos = 0;
let perdidas = 0;

// El juego se repite hasta que alguien llegue a 
while (triunfos < 3 && perdidas < 3) {

    pc = numAleatorio(1, 3);
    jugador = parseInt(prompt("Elige : 1 piedra, 2 papel, 3 tijera"));

    alert("PC elige: " + eleccion(pc));
    alert("Tú eliges: " + eleccion(jugador));

    // Lógica del juego (combate)
    if (pc == jugador) {
        alert("Empate");
    } else if (jugador == 1 && pc == 3) {
        alert("Ganaste");
        triunfos++;
    } else if (jugador == 2 && pc == 1) {
        alert("Ganaste");
        triunfos++;
    } else if (jugador == 3 && pc == 2) {
        alert("Ganaste");
        triunfos++;
    } else {
        alert("Perdiste");
        perdidas++;
    }
}

// Resultado final
alert("GANASTE " + triunfos + " veces. Perdiste: " + perdidas + " veces.");

//Función que genera número aleatorio entre min y max (incluidos)
// Math.random genera número entre 0 y 0.999...
// Se ajusta al rango deseado

function numAleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}
//Función que convierte número en texto (para mostrar)
function eleccion(jugada) {
    if (jugada == 1) return "Piedra 🥌";
    if (jugada == 2) return "Papel 🧻";
    if (jugada == 3) return "Tijera ✂️";
    return "Mal elegido";
}