let ataqueJugador;
let ataqueEnemigo;
let vidasJugador = 3;
let vidasEnemigo = 3;

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

    let spanvidasJugador = document.getElementById('vidas-jugador')
    let spanvidasEnemigo = document.getElementById('vidas-enemigo')

    //COMBATE 
    if (ataqueEnemigo == ataqueJugador) {
        crearMensaje("EMPATE");
    } 
    else if (ataqueJugador == 'punio' && ataqueEnemigo == 'barrida') {
        vidasEnemigo--;
        crearMensaje("GANASTE");
    } 
    else if (ataqueJugador == 'patada' && ataqueEnemigo == 'punio') {
        vidasEnemigo--;
        crearMensaje("GANASTE");
    } 
    else if (ataqueJugador == 'barrida' && ataqueEnemigo == 'patada') {
        vidasEnemigo--;
        crearMensaje("GANASTE");
    } 
    else {
        vidasJugador--;
        crearMensaje("PERDISTE");
        
        spanvidasJugador.innerHTML = vidasJugador
    }

    actualizarVidas();
    revisarFinDeJuego();
}

function crearMensaje (resultado){
    let sectionMensajes = document.getElementById('mensajes')
    let parrafo = document.createElement('p')

    parrafo.innerHTML = 'Tu personaje atacó con ' + ataqueJugador + 
    ', el personaje del enemigo atacó con ' + ataqueEnemigo + 
    '. ' + resultado

    sectionMensajes.appendChild(parrafo)
}

function actualizarVidas() {
    document.getElementById('vidas-jugador').innerHTML = vidasJugador;
    document.getElementById('vidas-enemigo').innerHTML = vidasEnemigo;
}

function revisarFinDeJuego() {
    if (vidasJugador === 0 || vidasEnemigo === 0) {
        let mensajeFinal = vidasJugador === 0 ? '¡Perdiste el juego!' : '¡Ganaste el juego!';
        crearMensaje(mensajeFinal);
        finalizarJuego();
    }
}

function finalizarJuego() {
    document.getElementById('boton-punio').disabled = true;
    document.getElementById('boton-patada').disabled = true;
    document.getElementById('boton-barrida').disabled = true;
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
