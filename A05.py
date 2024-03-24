import turtle
wn = turtle.Screen()
turtle = turtle.Turtle()
turtle.pensize(6)
r = 100
turtle.up()
turtle.goto(-r/2**0.5,0)
turtle.right(45)
turtle.down()
turtle.circle(r,120)
turtle.left(90)

turtle.circle(r,120)
turtle.right(165)
turtle.forward(100)
wn.exitonclick()