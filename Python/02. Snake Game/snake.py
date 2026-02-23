import turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]

move_distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.segments = [] # If we want to use this in methods, use self.segments
        self.create_snake()
        self.head = self.segments[0] # In order to reuse the head of the snake


    def create_snake(self):
        # Create a 3 square snake
        for position in starting_position:
            self.add_segment(position)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
            
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        snake_segment = turtle.Turtle(shape="square")
        snake_segment.shapesize(1,1)
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        # Move the snake
        for segment in range(len(self.segments) - 1, 0, -1): # start, stop, step
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        # Turn the snake up
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        # Turn the snake down
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        # Turn the snake left
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        # Turn the snake right
        if self.head.heading() != left:
            self.head.setheading(right)
        


    