<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shape Fusion Game</title>
    <style>
        body {
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        canvas {
            border: 2px solid black;
            background-color: white;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="800" height="600"></canvas>
    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        const WIDTH = canvas.width;
        const HEIGHT = canvas.height;
        const WHITE = 'white';
        const GREEN = 'green';
        const RED = 'red';

        class Shape {
            constructor(x, y, size, color, shapeType) {
                this.x = x;
                this.y = y;
                this.size = size;
                this.color = color;
                this.shapeType = shapeType;
                this.velocity = [(Math.random() * 6) - 3, (Math.random() * 6) - 3];
                this.isMoving = true;
            }

            draw() {
                ctx.fillStyle = this.color;
                ctx.beginPath();
                if (this.shapeType === 'rectangle' || this.shapeType === 'square') {
                    ctx.rect(this.x, this.y, this.size, this.size);
                } else if (this.shapeType === 'triangle') {
                    ctx.moveTo(this.x + this.size / 2, this.y);
                    ctx.lineTo(this.x, this.y + this.size);
                    ctx.lineTo(this.x + this.size, this.y + this.size);
                    ctx.closePath();
                } else if (this.shapeType === 'star') {
                    const points = [
                        { x: this.x + this.size / 2, y: this.y },
                        { x: this.x + this.size / 3, y: this.y + this.size / 3 },
                        { x: this.x, y: this.y + this.size / 2 },
                        { x: this.x + this.size / 3, y: this.y + (2 * this.size / 3) },
                        { x: this.x + this.size / 2, y: this.y + this.size },
                        { x: this.x + (2 * this.size / 3), y: this.y + (2 * this.size / 3) },
                        { x: this.x + this.size, y: this.y + this.size / 2 },
                        { x: this.x + (2 * this.size / 3), y: this.y + this.size / 3 }
                    ];
                    ctx.moveTo(points[0].x, points[0].y);
                    points.forEach(point => ctx.lineTo(point.x, point.y));
                    ctx.closePath();
                }
                ctx.fill();
            }

            move() {
                if (this.isMoving) {
                    this.x += this.velocity[0];
                    this.y += this.velocity[1];
                    if (this.x <= 0 || this.x >= WIDTH) {
                        this.velocity[0] *= -1;
                    }
                    if (this.y <= 0 || this.y >= HEIGHT) {
                        this.velocity[1] *= -1;
                    }
                }
            }
        }

        class Ball {
            constructor(x, y, size) {
                this.x = x;
                this.y = y;
                this.size = size;
                this.color = GREEN;
            }

            draw() {
                ctx.fillStyle = this.color;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        const shapes = [];
        for (let i = 0; i < 10; i++) {
            const x = Math.random() * (WIDTH - 50) + 25;
            const y = Math.random() * (HEIGHT - 50) + 25;
            const size = Math.random() * 30 + 20; // size between 20 and 50
            const color = `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`;
            const shapeType = ['rectangle', 'square', 'triangle'][Math.floor(Math.random() * 3)];
            shapes.push(new Shape(x, y, size, color, shapeType));
        }

        const ball = new Ball(WIDTH / 2, HEIGHT / 2, 20);

        canvas.addEventListener('mousedown', (event) => {
            const mouseX = event.offsetX;
            const mouseY = event.offsetY;

            // Check if a shape is clicked
            shapes.forEach(shape => {
                if (
                    shape.x <= mouseX && mouseX <= shape.x + shape.size &&
                    shape.y <= mouseY && mouseY <= shape.y + shape.size
                ) {
                    shape.isMoving = !shape.isMoving;
                }
            });

            // Check if the ball is clicked
            if (
                ball.x - ball.size <= mouseX && mouseX <= ball.x + ball.size &&
                ball.y - ball.size <= mouseY && mouseY <= ball.y + ball.size
            ) {
                ball.color = ball.color === GREEN ? RED : GREEN;
                shapes.forEach(shape => shape.isMoving = ball.color === GREEN);
            }
        });

        function update() {
            ctx.fillStyle = WHITE;
            ctx.fillRect(0, 0, WIDTH, HEIGHT);

            shapes.forEach(shape => {
                shape.move();
                shape.draw();
            });

            ball.draw();
        }

        function gameLoop() {
            update();
            requestAnimationFrame(gameLoop);
        }

        gameLoop();
    </script>
</body>
</html>
