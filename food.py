from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh([])

    def refresh(self, occupied_positions):
       
        max_index = 14  
        while True:
            random_x = random.randint(-max_index, max_index) * 20
            random_y = random.randint(-max_index, max_index) * 20
            if (random_x, random_y) not in occupied_positions:
                self.goto(random_x, random_y)
                return
