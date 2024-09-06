from turtle import *

fillcolor("yellow")
begin_fill()
for i in range(2):
    forward(200)
    right(90)
    forward(80)
    right(90)
end_fill()
fillcolor("red")
begin_fill()
for a in range(2):
    forward(200)
    left(90)
    forward(80)
    left(90)
end_fill()
    
mainloop()
