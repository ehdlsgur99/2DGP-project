from pico2d import *
import SceneManager

open_canvas(1000, 700)

sceneManager = SceneManager.SceneManager()

running = True
while running:
    clear_canvas()

    sceneManager.update()
    sceneManager.render()

    update_canvas()
    delay(0.05)