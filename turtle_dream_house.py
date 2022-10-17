import turtle


t = turtle.Turtle()

turtle.bgcolor("olivedrab1")

t.right(90) 

t.fillcolor("green")
t.begin_fill()
#ve hcn dau tien
t.forward(150)
t.right(50)
t.forward(100)
t.right(130)
t.forward(150)
t.right(50)
t.forward(100)
t.right(130)
t.end_fill()

t.penup()

t.goto(-30,-80) 

t.pendown()

#cua so
t.fillcolor("yellow")
t.begin_fill()

t.forward(20)
t.right(50)
t.forward(30)
t.right(130)
t.forward(50)
t.right(50)
t.forward(30)
t.right(130)
t.end_fill()

t.penup()

t.goto(0,0) 

t.pendown()

#mai nha

t.fillcolor("pink")
t.begin_fill()
t.left(230)
t.forward(100)
t.left(80)
t.forward(100)
t.left(100)
t.forward(100)
t.left(80)
t.forward(100)

t.end_fill()

#mat trc ngoi nha
t.backward(100)

t.fillcolor("yellow")
t.begin_fill()
t.left(140)
t.forward(142)
t.left(90)
t.forward(150)
t.left(90)
t.forward(142)
t.left(90)
t.forward(150)
t.end_fill()

#noi mat trc voi mai nha
t.fillcolor("darkred")
t.begin_fill()
t.left(90)
t.forward(142)
t.right(135)
t.forward(100)
t.end_fill()

#cua ra vao
t.penup()

t.goto(-180,-215) 

t.pendown()

t.left(45)

t.fillcolor("darkcyan")
t.begin_fill()
t.forward(80)
t.right(90)
t.forward(50)
t.right(90)
t.forward(80)
t.end_fill()

#mat troi
t.penup()

t.goto(100,150) 

t.pendown()

t.fillcolor("rosybrown")
t.begin_fill()
t.circle(60)
t.end_fill()

#tia nang to so 1
t.penup()

t.goto(95,150) 

t.pendown()

t.pencolor("coral")
t.pensize(10)

t.right(90)
t.forward(50)

#tia nang to so 2
t.penup()

t.backward(120) 
t.right(90)
t.forward(63)

t.pendown()

t.pencolor("coral")
t.pensize(10)

t.forward(50)

#tia nang to so 3
t.penup()

t.backward(120) 
t.right(90)
t.forward(62)

t.pendown()

t.pencolor("coral")
t.pensize(10)

t.forward(50)

#tia nang to so 4
t.penup()

t.backward(120) 
t.right(90)
t.forward(60)

t.pendown()

t.pencolor("coral")
t.pensize(10)

t.forward(50)

#tia nang nho so 1
t.penup()

t.backward(120) 
t.right(45)
t.forward(60)

t.pendown()

t.pencolor("darkred")
t.pensize(5)

t.forward(30)

#tia nang nho so 2
t.penup()

t.backward(90) 
t.right(90)
t.forward(60)

t.pendown()

t.pencolor("darkred")
t.pensize(5)

t.forward(30)

#tia nang nho so 3
t.penup()

t.backward(90) 
t.right(90)
t.forward(60)

t.pendown()

t.pencolor("darkred")
t.pensize(5)

t.forward(30)

#tia nang nho so 4
t.penup()

t.backward(90) 
t.right(90)
t.forward(63)

t.pendown()

t.pencolor("darkred")
t.pensize(5)

t.forward(30)

#than cay
t.penup()
t.goto(220,-230)
t.pendown()

t.pencolor("black")
t.pensize(1)

t.fillcolor("firebrick")
t.begin_fill()
t.left(45)
t.forward(30)
t.left(90)
t.forward(60)
t.left(90)
t.forward(30)
t.left(90)
t.forward(60)
t.end_fill()

#la cay tang 1
t.penup()
t.backward(60)
t.right(90)
t.forward(40)
t.pendown()

t.fillcolor("darkcyan")
t.begin_fill()
t.right(120)
t.forward(110)
t.right(120)
t.forward(110)
t.right(120)
t.forward(110)
t.end_fill()

#la cay tang 2
t.penup()
t.right(90)
t.forward(95)
t.pendown()

t.fillcolor("darkcyan")
t.begin_fill()
t.right(30)
t.forward(110)
t.right(120)
t.forward(110)
t.right(120)
t.forward(110)
t.end_fill()


turtle.done()