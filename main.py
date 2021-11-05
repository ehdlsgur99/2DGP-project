from pico2d import *
import SceneManager

open_canvas(1000, 700)

running = True
while running:
    clear_canvas()

    SceneManager.Scene_Manager.update()
    SceneManager.Scene_Manager.render()

    update_canvas()
    delay(0.05)