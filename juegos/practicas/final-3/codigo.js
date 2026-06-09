const loginBtn = document.getElementById("loginBtn");

// Agrandar botón Login al pasar el mouse
loginBtn.addEventListener("mouseenter", () => {
    loginBtn.style.transform = "scale(1.2)";
});

// Volver al tamaño normal
loginBtn.addEventListener("mouseleave", () => {
    loginBtn.style.transform = "scale(1)";
});