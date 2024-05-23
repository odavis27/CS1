def greet(name):
    print("Hello",name)

##def makeSq(t, color, x, y):
##    t.penup()
##    t.goto(x,y)
##    t.pendown()
##    t.fillcolor(color)
##    t.setheading(0)
##    t.begin_fill()
##    for i in range(0, 4):
##        t.forward(10)
##        t.left(90)
##    t.end_fill()
##    t.penup()
##    t.setheading(0)

def makeCross(t, color, x, y):
    def makeSq(t, color, x, y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.fillcolor(color)
        t.setheading(0)
        t.begin_fill()
        for i in range(0, 4):
            t.forward(10)
            t.left(90)
        t.end_fill()
        t.penup()
        t.setheading(0)
       
    makeSq(t, color, x, y)
    makeSq(t, color, x, y-10)
    makeSq(t, color, x, y+10)
    makeSq(t, color, x-10, y)
    makeSq(t, color, x+10, y)

def makeT(t, color, x, y):
    def makeSq(t, color, x, y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.fillcolor(color)
        t.setheading(0)
        t.begin_fill()
        for i in range(0, 4):
            t.forward(10)
            t.left(90)
        t.end_fill()
        t.penup()
        t.setheading(0)
        
    makeSq(t, color, x, y)
    makeSq(t, color, x, y+10)
    makeSq(t, color, x, y+20)
    makeSq(t, color, x-10, y)
    makeSq(t, color, x+10, y)

def makeClaw(t, color, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.setheading(0)
    t.begin_fill()

    
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(-90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(-90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    
    t.end_fill()
    t.penup()
    t.setheading(0)








        
