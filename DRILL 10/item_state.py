import pico2d
from pico2d import *
import game_framework
import title_state
import play_state

image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('add_delete_boy.png')

# 게임 종료 - 객체를 소멸
def exit():
    global image
    del image

# 게임 월드 객체를 업데이트 - 게임 로직
def update():
    global logo_time
    if logo_time > 1.0:
        logo_time = 0
    delay(0.01)
    logo_time += 0.01

    # 게임 월드 렌더링
def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_KP_PLUS:
                    play_state.draw_world()
                    game_framework.pop_state()
                case pico2d.SDLK_KP_MINUS:
                    play_state.draw_world()
                    game_framework.pop_state()

def test_self():
    import sys
    this_module = sys.modules['__main__']
    open_canvas()
    game_framework.run(this_module)
    close_canvas()

if __name__ == '__main__': # 만약 단독 실행 상태이면
    test_self()