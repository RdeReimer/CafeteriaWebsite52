const canvas = document.getElementById("snowCanvas");
const ctx = canvas.getContext("2d");

function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
resize();
window.onresize = resize;

let flakes = [];

for (let i = 0; i < 100; i++) {
    flakes.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 4 + 1,
        d: Math.random() + 1
    });
}

function drawFlakes() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "white";
    ctx.beginPath();
    for (let f of flakes) {
        ctx.moveTo(f.x, f.y);
        ctx.arc(f.x, f.y, f.r, 0, Math.PI * 2);
    }
    ctx.fill();
    moveFlakes();
}

let angle = 0;

function moveFlakes() {
    angle += 0.01;
    for (let f of flakes) {
        f.y += Math.pow(f.d, 2) + 1;
        f.x += Math.sin(angle) * 2;

        if (f.y > canvas.height) {
            f.y = -10;
            f.x = Math.random() * canvas.width;
        }
    }
}

setInterval(drawFlakes, 25);
