from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move(x, y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)

x=400
y=90
turn = 0
dex=0
dey=90
dez=180
der=270


while(True):
    if((turn % 2) == 0):
        while(x<800):
            move(x, y)
            x = x+2
            delay(0.0001)
        while(y<600):
            move(x, y)
            y = y+2
            delay(0.0001)
        while(x>0):
            move(x, y)
            x = x-2
            delay(0.0001)
        while(y>90):
            move(x, y)
            y = y-2
            delay(0.001)
        while(x<400):
            move(x, y)
            x = x+2
            delay(0.0001)
        turn = turn +1
    elif((turn % 2) == 1):
        while(dex<90):
            move(400-cos(dex/180*pi)*250,300+sin(dex/180*pi)*250)
            delay(0.01)
            dex = dex+2
        while(dey<180 ):
            move (400-cos(dey/180*pi)*250,300+sin(dey/180*pi)*250)
            delay(0.01)
            dey = dey+2
        while(dez<270):
            move(400-cos(dez/180*pi)*250,300+sin(dez/180*pi)*250)
            delay(0.01)
            dez = dez+2
        while(der<360):
            move(400-cos(der/180*pi)*250,300+sin(der/180*pi)*250)
            delay(0.01)
            der = der+2   
        turn = turn + 1


close_canvas()
