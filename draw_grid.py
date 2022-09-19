import turtle

turtle.reset()

# draw horizontal lines - 수평선
y = -100
while y <= 400:
    turtle.penup()
    turtle.goto(-100,y)
    turtle.pendown()
    turtle.goto(400,y)
    y += 100
    

# draw vertical lines - 수직선
x = -100
while x <= 400:
    turtle.penup()
    turtle.goto(x,-100)
    turtle.pendown()
    turtle.goto(x,400)
    x += 100
