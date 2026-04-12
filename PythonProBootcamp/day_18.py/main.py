from turtle import  Turtle,Screen
import math
monika = Turtle()
monika.shape("turtle")
monika.color("red")
monika.pencolor("white")
monika.left(45)
monika.fd(math.sqrt(20000)/2)
monika.right(45+90)
monika.pencolor("purple")
for i in range(4):
    monika.forward(100)
    monika.right(90)



screan = Screen()
screan.exitonclick()
