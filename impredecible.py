import turtle

ventana = turtle.Screen()
t = turtle.Turtle()
t.shape ("turtle") 
t.color("purple")
t.width(5)
t.speed(0)
turtle.colormode(255)

import random

while True:
    color1 = random.randint(0,255)
    color2 = random.randint(0,225)
    color3 = random.randint(0,255)
    largo = random.randint(1,100)
    angulo = random.randint(1,100)
    t.color (color1, color2, color3)
    t.forward(angulo)
    t.right(largo)

turtle.done()