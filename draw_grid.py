import turtle

turtle.reset()

# draw horizontal lines - 수평선
y = 0
while y <= 500:
    turtle.penup()
    turtle.goto(0,y)
    turtle.pendown()
    turtle.goto(500,y)
    y += 100
    

# draw vertical lines - 수직선
