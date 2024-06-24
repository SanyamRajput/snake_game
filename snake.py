from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.createSnake()
        self.head = self.segment[0]

    def createSnake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)


    def add_segment(self,pos):
        s = Turtle("square")
        s.penup()
        s.color('white')
        s.goto(pos)
        self.segment.append(s)

    def reset(self):
        for s in self.segment:
            seg.goto(1000,1000)
            
        self.segments.clear()
        self.creatSnake()
        self.head = self.segments[0]
        
    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for segnum in range(len(self.segment) - 1, 0, -1):
            newx = self.segment[segnum - 1].xcor()
            newy = self.segment[segnum - 1].ycor()
            self.segment[segnum].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
