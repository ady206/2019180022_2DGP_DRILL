from pico2d import *
import game_world
import game_framework

TIMER_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIMER_PER_ACTION
FRAMES_PER_ACTION = 8

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KPH = 10.0
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

class Bird:
    def __init__(self):
        self.x, self.y = 100, 300
        self.frame = 0
        self.dir = 1
        self.face_dir = ' '
        self.radian = 0
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1600)

        if self.x == 1600:
            self.dir = -1
            self.face_dir = 'h'
        elif self.x == 0:
            self.dir = 1
            self.face_dir = ' '

    def draw(self):
        if int(self.frame) < 4:
            self.image.clip_composite_draw(int(self.frame) * 180, 0, 180, 140,
                                       self.radian, self.face_dir, self.x, self.y, 54, 42)
        elif 4 <= int(self.frame) < 9:
            self.image.clip_composite_draw((int(self.frame) - 4) * 180, 176, 180, 140,
                                       self.radian, self.face_dir, self.x, self.y, 54, 42)
        elif 9 <= int(self.frame) < 14:
            self.image.clip_composite_draw((int(self.frame) - 9) * 180, 346, 180, 140,
                                       self.radian, self.face_dir, self.x, self.y, 54, 42)