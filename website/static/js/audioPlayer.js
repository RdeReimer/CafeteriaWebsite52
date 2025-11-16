const audio = document.getElementById("musicaNavidad");
const btn = document.getElementById("btnPlayPause");
const volumen = document.getElementById("volumen");

btn.addEventListener("click", () => {
    if (audio.paused) {
        audio.play();
        btn.textContent = "⏸ Pausa";
    } else {
        audio.pause();
        btn.textContent = "▶ Reproducir";
    }
});

volumen.addEventListener("input", () => {
    audio.volume = volumen.value;
});
