from turtle import  Turtle,Screen
t = Turtle()
def draw(sides):
    angle = 360/sides
    for i in range(sides):
        t.forward(100)
        t.right(angle)
for i in range(3,11):
    draw(i)
screan = Screen()
screan.exitonclick()