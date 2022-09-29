from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dirside
    global dirup
    global right

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                dirup += 1
            elif event.key == SDLK_LEFT:
                right = 0
                dirside -= 1
            elif event.key == SDLK_DOWN:
                dirup -= 1
            elif event.key == SDLK_RIGHT:
                right = 1
                dirside += 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                dirup -= 1
            elif event.key == SDLK_LEFT:
                dirside += 1
            elif event.key == SDLK_DOWN:
                dirup += 1
            elif event.key == SDLK_RIGHT:
                dirside -= 1

    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
dirside, dirup = 0, 0
right = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if(dirside > 0 and dirup > 0 or right == 1):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    if (dirside < 0 and dirup < 0 or right == 0):
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    x += dirside * 5
    y += dirup * 5

    if (x > KPU_WIDTH):
        x = KPU_WIDTH
        x -= dirside * 5
    if (y > KPU_HEIGHT):
        y = KPU_HEIGHT
        y -= dirside * 5
    if (x < 0):
        x = 0
        x -= dirside * 5
    if (y < 0):
        y = 0
        y -= dirside * 5
    handle_events()

close_canvas()