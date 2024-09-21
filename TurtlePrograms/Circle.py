import turtle
wn = turtle.Screen()
wn.bgcolor("black")

my_turtle = turtle.Turtle()
my_turtle.shape("blank")
my_turtle.color("turquoise")

for _ in range(46):
     my_turtle.speed(10)
     my_turtle.down()
     my_turtle.forward(50)
     my_turtle.stamp()
     my_turtle.backward(50)
     my_turtle.right(8)

wn.exitonclick()
