function actualizarReloj(){

    const ahora = new Date();

    const h = String(ahora.getHours()).padStart(2,"0");
    const m = String(ahora.getMinutes()).padStart(2,"0");
    const s = String(ahora.getSeconds()).padStart(2,"0");

    document.getElementById("hora").textContent =
        `${h}:${m}:${s}`;

    document.getElementById("fecha").textContent =
        ahora.toLocaleDateString("es-ES", {
            weekday:"long",
            day:"numeric",
            month:"long",
            year:"numeric"
        });
}

setInterval(actualizarReloj,1000);

actualizarReloj();