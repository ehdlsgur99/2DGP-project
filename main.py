from pico2d import *
import SceneManager

open_canvas(1000, 700)

SM =  SceneManager.Scene_Manager()

running = True
while running:
    clear_canvas()

    SM.update()
    SM.render()

    update_canvas()
    delay(0.05)