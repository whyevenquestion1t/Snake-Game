from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            x_axis = 0

            new_t = Turtle(shape="square")
            new_t.shapesize(stretch_wid=0.7, stretch_len=0.7)
            new_t.color("white")
            new_t.penup()
            new_t.setx(x_axis)
            x_axis -= 20
            self.segments.append(new_t)

    def new_segment(self):
        new_t = Turtle(shape="square")
        new_t.shapesize(stretch_wid=0.7, stretch_len=0.7)
        new_t.color("white")
        new_t.penup()
        new_t.goto(self.segments[-1].position())
        self.segments.append(new_t)

    def move(self, pace):
        for seg_n in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_n - 1].xcor()
            new_y = self.segments[seg_n - 1].ycor()
            self.segments[seg_n].goto(new_x, new_y)

        self.segments[0].forward(pace)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 100)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
