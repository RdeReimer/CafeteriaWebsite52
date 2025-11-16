document.addEventListener("DOMContentLoaded", () => {
    const popupReseña = document.getElementById("popup-reseña");
    const btnCerrarReseña = document.getElementById("cerrar-reseña");
    const btnIrReseñas = document.getElementById("ir-reseñas");

    if (popupReseña) {

        setTimeout(() => {
            popupReseña.classList.add("mostrar");
        }, 2500);

        btnCerrarReseña.addEventListener("click", () => {
            popupReseña.classList.remove("mostrar");
        });

        btnIrReseñas.addEventListener("click", () => {
            window.location.href = btnIrReseñas.dataset.url;
        });
    }
});
