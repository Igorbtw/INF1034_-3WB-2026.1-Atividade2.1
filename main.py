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

#figura geometrica 1

color = textinput("Obter cor","Digite a cor desejada:")

t.pu()
t.goto(200,300)
t.pd()
t.color("blue")
t.begin_fill()
t.fillcolor(color)
for _ in range(3):
      t.fd(100)
      t.lt(120)    
t.end_fill()

#figura geometrica 2

color = textinput("Obter cor","Digite a cor desejada:")

t.pu()
t.goto(-150,150)
t.pd()
t.stamp()
t.color("red")
t.begin_fill()
t.fillcolor(color)
for _ in range(6):
      t.right(60)
      t.fd(90)
t.end_fill()


#figura geometrica 3

color = textinput("Obter cor","Digite a cor desejada:")

t.pu()
t.goto(-150,-150)
t.pd()
t.stamp()
t.color("gray")
t.begin_fill()
t.fillcolor(color)
for _ in range(5):
       t.fd(108)
       t.right(72)
t.end_fill()

mainloop()
