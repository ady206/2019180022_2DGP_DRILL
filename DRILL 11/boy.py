from pico2d import *
import game_framework

RD, LD, RU, LU, auto = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): auto,
}


class IDLE:
    @staticmethod
    def enter(self, event):
        print('enter idle')
        self.dir = 0

    @staticmethod
    def exit(self):
        print('exit idle')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass



class RUN:
    def enter(self, event):
        print('enter run')
        if event == RD: self.dir += 1
        elif event == LD: self.dir -= 1
        elif event == RU: self.dir -= 1
        elif event == LD: self.dir += 1

    def exit(self):
        print('exit run')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class AUTO:
    def enter(self, event):
        print('enter auto')

    def exit(self):
        print('exit auto')

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.face_dir
        self.x = clamp(0, self.x, 800)
        if(self.x == 0): self.face_dir = 1
        elif(self.x == 800): self.face_dir = -1
        pass

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.face_dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass


next_state = {
    AUTO: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, auto: IDLE},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, auto: AUTO},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE}
}




class Boy:

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event): #소년 스스로 이벤트 처리할 수 있도록
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_ESCAPE:
        #             game_framework.quit()
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)