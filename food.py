from turtle import Turtle
#Turtle library for graphics.
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.food_shape()
        
    
    def food_shape(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.random_color()
        self.speed("fastest")
        self.refresh()
        
    def random_color(self):
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        self.color(self.r/255,self.g/255,self.b/255)
                     
        
    def refresh(self):
        self.random_color()
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)      
        
        self.goto(random_x,random_y)
        
    def get_color(self):
        return (self.r/255,self.g/255,self.b/255)
        
   