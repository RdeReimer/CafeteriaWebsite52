document.addEventListener("DOMContentLoaded", () => {
    const popup = document.getElementById("popup-navidad");
    const cerrar = document.getElementById("cerrar-popup");

    setTimeout(() => {
        popup.classList.add("mostrar");
    }, 2500);

    cerrar.addEventListener("click", () => {
        popup.classList.remove("mostrar");
    });
});
