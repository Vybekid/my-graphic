from turtle import* 
from colorsys import* 
bgcolor('black')
speed(0)
tracer(200)
h=0
goto(200,50)
for i in range(300): 
    color(hsv_to_rgb(h,1,1))
    for j in range(75): 
        h+=0.005 
        fd(100)
        bk(100)
        rt(2)
    fd(400)
done()

