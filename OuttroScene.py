from pico2d import *
import time
import KeyManager

class OuttroScene():
    def __init__(self):
        self.died = load_image('Resource/died.png')
        self.changeScene = 'none'

        self.rad = 0

        self.bgm = load_music('Resource/Sound/die.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def update(self):
        KeyManager.handle_events()
        if KeyManager.now_key_state['SPACE'] == True:
            self.changeScene = 'IntroScene'
            return self.changeScene

    def render(self):
        self.died.clip_composite_draw(0, 0, 800, 600, self.rad, 'none', 500, 350, 1000, 700)

    def release(self):
        pass
