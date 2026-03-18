from turtle import *

t = Turtle()


#começo do plano cartesiano



t.color("blue")
t.pu()
t.goto(0, 0)
t.pd()


t.fd(300)
t.stamp()
t.goto(0, 0)
t.pd()
t.lt(90)
t.fd(300)
t.goto(0, 0)
t.pd()
t.lt(90)
t.fd(300)
t.goto(0, 0)
t.pd()
t.lt(90)
t.fd(300)

#figura geometrica
t.pu()
t.goto(200,300)
t.pd()
t.stamp()
t.color("red")
t.begin_fill()
t.fillcolor("purple")
for _ in range(3):
      t.fd(100)
      t.lt(120)    
t.end_fill()

mainloop()
