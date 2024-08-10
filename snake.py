from turtle import Turtle
#Turtle library for graphics.


#Setting starting position of snake.
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    #Create snake body.   
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)  #: (x,y) are the co-ordinates.
            self.segments.append(new_segment)
            
    #Move snake body.        
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        
    #Control snake body using keys.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        
        
            