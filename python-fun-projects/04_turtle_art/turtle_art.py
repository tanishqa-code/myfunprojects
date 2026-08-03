import turtle
import random

def draw_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Turtle Art - Colorful Spiral")

    artist = turtle.Turtle()
    artist.speed(0)
    artist.width(2)

    colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

    for i in range(200):
        artist.pencolor(colors[i % len(colors)])
        artist.forward(i * 2)
        artist.left(59)

    screen.exitonclick()

if __name__ == "__main__":
    draw_spiral()
