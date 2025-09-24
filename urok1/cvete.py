# цвете с 10 венчелистчета
from turtle import *
colormode(255)
screen = Screen ()
screen.bgcolor(250, 250, 210)
my_turtle = Turtle()
my_turtle.clear()
my_turtle.pensize(5)
my_turtle.pencolor(0, 250, 0)
my_turtle.goto(0, 100)
my_turtle.pencolor(250, 0, 0)
my_turtle.goto(-35, 100)
for i in range(10):
    my_turtle.forward(70)
    my_turtle.left(108)  
      