import turtle
import random

def initialize_skydivers(num_skydivers):
    skydivers = []
    for _ in range(num_skydivers):
        skydiver = turtle.Turtle()
        skydiver.shape("circle")
        skydiver.color(random.choice(["orange", "purple", "blue", "green"]))
        skydiver.penup()
        skydiver.speed(0)
        skydiver.setx(random.randint(-200, 200))
        skydiver.sety(300)
        skydivers.append(skydiver)
    return skydivers

def animate_skydivers(skydivers):
    while True:
        for skydiver in skydivers:
            skydiver.sety(skydiver.ycor() - random.randint(3, 8))
            if skydiver.ycor() < -300:
                skydiver.hideturtle()
                skydiver.sety(300)
                skydiver.showturtle()

def main():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("Skydivers Animation")

    skydivers = initialize_skydivers(8)
    animate_skydivers(skydivers)

    screen.mainloop()

if __name__ == "__main__":
    main()
