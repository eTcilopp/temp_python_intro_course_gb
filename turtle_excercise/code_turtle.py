# pip install PythonTurtle

import turtle
t = turtle.Turtle()

angle = 89
for i in range(100):
	t.forward(150)
	t.right(angle)
	angle -= 1 if angle > 0 else 90
	
turtle.done()
