from turtle import Screen, Turtle
from hero import Hero


screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.screensize(600, 600)

square = Turtle()
square.shape("square")
square.color("blue")
square.shapesize(33)

hero = Hero()

screen.listen()
screen.onkey(hero.up, "w")
screen.onkey(hero.down, "s")
screen.onkey(hero.left, "a")
screen.onkey(hero.right, "d")

screen.exitonclick()
