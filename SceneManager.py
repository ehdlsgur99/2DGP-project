from pico2d import *

import VillageScene
import DungeonScene
import IntroScene

class SceneManager():
    def __init__(self):
        self.index = 0
        self.nowScene = DungeonScene.DungeonScene()

    def changeScene(self, sceneName):
        self.nowScene.release()
        if sceneName == 'IntroScene':
            self.nowScene = IntroScene.IntroScene()
        elif sceneName == 'VillageScene':
            self.nowScene = VillageScene.VillageScene()
        elif sceneName == 'DungeonScene':
            self.nowScene = DungeonScene.DungeonScene()

    def update(self):
        self.nowScene.update()

    def render(self):
        self.nowScene.render()


