import turtle

#Initializing Class Instance
#Turtle Screen Object
wn = turtle.Screen()
wn.bgcolor("Light Green")    #Setting Background Color Attribute

#Turtle Object
alex = turtle.Turtle()
alex.color("Blue")              #Setting turtle color
alex.pensize(3)                 #Setting turtle width

tess = turtle.Turtle()
tess.pensize(3)

#Calling Method for Alex
alex.forward(70)
alex.left(120)
alex.forward(95)
alex.left(135)
alex.forward(90)

#Calling Method for Tess
tess.forward(100)
tess.left(90)
tess.forward(75)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(75)

turtle.done()