// Esta función se ejecuta cuando el usuario hace click en el botón para elegir su personaje
function seleccionarPersonajeJugador() {
    // Se obtienen los elementos de cada opción de personaje
    let inputZuko = document.getElementById('zuko');
    let inputKatara = document.getElementById('katara');
    let inputAang = document.getElementById('aang');
    let inputToph = document.getElementById('toph');

    // Se obtiene el lugar donde se va a mostrar el personaje elegido por el jugador
    let spanPersonajeJugador = document.getElementById('personaje-jugador')

    // Se verifica cuál personaje está seleccionado y se muestra su nombre
    if (inputZuko.checked) {
        spanPersonajeJugador.innerHTML = 'Zuco'
    } else if (inputKatara.checked) {
        spanPersonajeJugador.innerHTML = 'Katara'
    } else if (inputAang.checked) {
        spanPersonajeJugador.innerHTML = 'Aang'
    } else if (inputToph.checked) {
        spanPersonajeJugador.innerHTML = 'Toph'
    } else {
        // Si no se eligió ningún personaje, se muestra un mensaje y se detiene la función
        alert('Por favor seleccioná un personaje');
        return;
    }

    // Luego de elegir el personaje del jugador, se llama a la función del enemigo
    seleccionarPersonajeEnemigo();
}


// Esta función elige un personaje al azar para el enemigo
function seleccionarPersonajeEnemigo() {
    // Se crea una lista con los nombres de los personajes posibles
    let personajes = ['Zuko', 'Katara', 'Aang', 'Toph'];

    // Se genera un número al azar dentro del rango de la lista
    let random = Math.floor(Math.random() * personajes.length);

    // Se muestra el personaje elegido en la parte del enemigo
    document.getElementById('personaje-enemigo').innerHTML = personajes[random];
}




// Se obtiene el botón que sirve para confirmar la selección del personaje
let botonPersonajeJugador = document.getElementById('boton-personaje');

// Se indica que al hacer click en el botón se ejecute la función de selección del jugador
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);