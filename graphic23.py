from turtle import* 
import colorsys 
tracer(100)
bgcolor('black')
pensize(4)
h=0.3
for i in range(400): 
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.1 
    color('black')
    fillcolor(c)
    begin_fill()
    rt(250)
    fd(i)
    circle(20,180)
    circle(20,180)
    circle(65,11)
    end_fill()
    fd(100)
done()
