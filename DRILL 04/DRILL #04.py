import turtle

turtle.goto(0, -250)
turtle.forward(500)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.forward(500)
turtle.left(90)

i = 2
while(i>0):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.left(90)
    i -= 1

turtle.forward(100)
turtle.left(90)

j=2
while(j>0):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.left(90)
    j -= 1

turtle.forward(100)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.forward(500)

turtle.exitonclick()
