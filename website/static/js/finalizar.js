document.addEventListener("DOMContentLoaded", () => {

    const botonFinalizar = document.getElementById("finalizar-pedido");

    if (!botonFinalizar) return;

    botonFinalizar.addEventListener("click", function () {

        const personas = [
            "Carlos Ramírez",
            "Ana Torres",
            "Luis Mendoza",
            "María López",
            "Mateo González"
        ];

        const vehiculos = [
            "Auto Café Express",
            "Camioneta Latte",
            "Motocicleta Espresso"
        ];

        const personaRandom = personas[Math.floor(Math.random() * personas.length)];
        const vehiculoRandom = vehiculos[Math.floor(Math.random() * vehiculos.length)];

        window.location.href = `/gracias/?persona=${encodeURIComponent(personaRandom)}&vehiculo=${encodeURIComponent(vehiculoRandom)}`;
    });

});
