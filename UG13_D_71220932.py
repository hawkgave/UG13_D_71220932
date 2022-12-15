import turtle
v = turtle.Turtle()
turtle.Screen().bgcolor("blue")

v.penup()
v.goto(0,200)
v.pendown()

v.pensize(10)
v.pencolor("white")

v.right(180)
v.circle(50,180)

def geser():
    v.penup()
    v.goto(0,-50)
    v.pendown()

geser()

v.penup()
v.goto(0,-180)
v.pendown()

v.pensize(10)
v.pencolor("red")

v.right(65)
v.forward(100)

v.setpos(0,-180)
v.right(50)
v.forward(100)

v.penup()
v.goto(-25,-250)
v.right(65)
v.pendown()
v.backward(50)
v.penup()




#angka
#def Angka3():




sc = turtle.Screen().exitonclick()