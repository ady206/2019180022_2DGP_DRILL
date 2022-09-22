from os import *
from pico2d import *

open_canvas()
sonic = load_image('sonic.png')
grass = load_image('grass.png')

frame = 0
Delay = 0.03

hide_lattice()
while(True):
    # 0 line
    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        sonic.clip_draw(frame*65, -10,  62, 52, x, 80)
        update_canvas()
        frame = (frame + 1) % 4
        get_events()
        delay(Delay)

    # 1 line
    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        sonic.clip_draw(frame*65, 40,  45, 51, x, 70)
        update_canvas()
        frame = (frame + 1) % 4
        get_events()
        delay(Delay)

    # 2 line
    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        sonic.clip_draw(frame*65, 90,  45, 51, x, 70)
        update_canvas()
        frame = (frame + 1) % 8
        get_events()
        delay(Delay)

    # 3 line
    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        sonic.clip_draw(frame*65, 140,  45, 50, x, 70)
        update_canvas()
        frame = (frame + 1) % 8
        get_events()
        delay(Delay)

    # 4 line
    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        sonic.clip_draw(frame*47, 190,  48,  47, x, 70)
        update_canvas()
        frame = (frame + 1) % 3
        get_events()
        delay(Delay)

    # 5 line
    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        sonic.clip_draw(frame*47, 235,  48, 47, x, 70)
        update_canvas()
        frame = (frame + 1) % 3
        get_events()
        delay(Delay)

    # 6 line
    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        sonic.clip_draw(frame*48, 285,  48, 48, x, 70)
        update_canvas()
        frame = (frame + 1) % 6
        get_events()
        delay(Delay)

    # 7 line
    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        sonic.clip_draw(frame*48, 335,  48, 48, x, 70)
        update_canvas()
        frame = (frame + 1) % 9
        get_events()
        delay(Delay)

    # 8 line
    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        sonic.clip_draw(frame*48, 380,  48, 50, x, 70)
        update_canvas()
        frame = (frame + 1) % 7
        get_events()
        delay(Delay)

close_canvas()

