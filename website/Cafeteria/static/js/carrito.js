let carrito = [];
let total = 0;

document.querySelectorAll('.agregar-carrito').forEach(boton => {
    boton.addEventListener('click', () => {
        const nombre = boton.dataset.nombre;
        const precio = parseFloat(boton.dataset.precio);
        carrito.push({ nombre, precio });
        total += precio;
        actualizarCarrito();
    });
});

function actualizarCarrito() {
    const lista = document.getElementById('lista-carrito');
    lista.innerHTML = '';
    carrito.forEach(p => {
        const li = document.createElement('li');
        li.textContent = `${p.nombre} - $${p.precio}`;
        lista.appendChild(li);
    });
    document.getElementById('total').textContent = total.toFixed(2);
}

document.getElementById('finalizar-pedido').addEventListener('click', () => {
    alert('Tu pedido ha sido enviado. 🚗 Está siendo preparado y será entregado pronto.');
    carrito = [];
    total = 0;
    actualizarCarrito();
});
