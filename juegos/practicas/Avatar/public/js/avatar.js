let ataqueJugador;
let ataqueEnemigo;

function iniciarJuego(){

    let botonPunio = document.getElementById('boton-punio')
    botonPunio.addEventListener('click', ataquePunio)

    let botonPatada = document.getElementById('boton-patada')
    botonPatada.addEventListener('click', ataquePatada)

    let botonBarrida = document.getElementById('boton-barrida')
    botonBarrida.addEventListener('click', ataqueBarrida)

}

// selección de personaje
function seleccionarPersonajeJugador() {
    let inputZuko = document.getElementById('zuko');
    let inputKatara = document.getElementById('katara');
    let inputAang = document.getElementById('aang');
    let inputToph = document.getElementById('toph');

    let spanPersonajeJugador = document.getElementById('personaje-jugador')

    if (inputZuko.checked) {
        spanPersonajeJugador.innerHTML = 'Zuko'
    } else if (inputKatara.checked) {
        spanPersonajeJugador.innerHTML = 'Katara'
    } else if (inputAang.checked) {
        spanPersonajeJugador.innerHTML = 'Aang'
    } else if (inputToph.checked) {
        spanPersonajeJugador.innerHTML = 'Toph'
    } else {
        alert('Por favor seleccioná un personaje');
        return;
    }

    seleccionarPersonajeEnemigo();
}

// ataques
function ataquePunio(){
    ataqueJugador = 'punio'
    ataqueAleatorioEnemigo()
}
function ataquePatada(){
    ataqueJugador = 'patada'
    ataqueAleatorioEnemigo()
}
function ataqueBarrida(){
    ataqueJugador = 'barrida'
    ataqueAleatorioEnemigo()
}

function ataqueAleatorioEnemigo(){
    let ataqueAleatorio = aleatorio (1, 3)

    if(ataqueAleatorio == 1){
        ataqueEnemigo = 'punio'
    }
    else if (ataqueAleatorio == 2){
        ataqueEnemigo = 'patada'
    }
    else {
        ataqueEnemigo = 'barrida'
    }

    combate()
}

function combate(){
    if (ataqueEnemigo == ataqueJugador) {
        crearMensaje("EMPATE");
    } 
    else if (ataqueJugador == 'punio' && ataqueEnemigo == 'barrida') {
        crearMensaje("GANASTE");
    } 
    else if (ataqueJugador == 'patada' && ataqueEnemigo == 'punio') {
        crearMensaje("GANASTE");
    } 
    else if (ataqueJugador == 'barrida' && ataqueEnemigo == 'patada') {
        crearMensaje("GANASTE");
    } 
    else {
        crearMensaje("PERDISTE");
    }
}

function crearMensaje (resultado){
    let sectionMensajes = document.getElementById('mensajes')
    let parrafo = document.createElement('p')

    parrafo.innerHTML = 'Tu personaje atacó con ' + ataqueJugador + 
    ', el personaje del enemigo atacó con ' + ataqueEnemigo + 
    ' ' + resultado

    sectionMensajes.appendChild(parrafo)
}

// enemigo
function seleccionarPersonajeEnemigo() {
    let personajes = ['Zuko', 'Katara', 'Aang', 'Toph'];
    let random = Math.floor(Math.random() * personajes.length);

    document.getElementById('personaje-enemigo').innerHTML = personajes[random];
}

// función aleatoria
function aleatorio(min, max){
    return Math.floor(Math.random() * (max - min + 1) + min)
}

// botón personaje
let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

// ✅ BOTON REINICIAR (AGREGADO)
function reiniciarJuego() {
    location.reload();
}

let botonReiniciar = document.getElementById('boton-reiniciar');
botonReiniciar.addEventListener('click', reiniciarJuego);

// iniciar juego
iniciarJuego();
