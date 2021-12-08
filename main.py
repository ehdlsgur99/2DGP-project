from pico2d import *
import SceneManager
import ObjectManager

open_canvas(1000, 700)

SM = SceneManager.Scene_Manager()

running = True
while running:
    clear_canvas()

    SM.update()
    SM.render()

    delay(0.05)

    update_canvas()