from turtle import Turtle


class Hero(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed = 10

    def up(self):
        y = self.pos()[1]
        if y <= 300:
            new_pos = y + self.speed
            self.sety(new_pos)

    def down(self):
        y = self.pos()[1]
        if y >= -300:
            new_pos = y - self.speed
            self.sety(new_pos)

    def left(self):
        x = self.pos()[0]
        if x >= -300:
            new_pos = x - self.speed
            self.setx(new_pos)

    def right(self):
        x = self.pos()[0]
        if x <= 300:
            new_pos = x + self.speed
            self.setx(new_pos)
