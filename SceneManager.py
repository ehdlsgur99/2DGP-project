from pico2d import *

import VillageScene
import DungeonScene
import IntroScene

class SceneManager():
    def __init__(self):
        self.index = 0
        self.nowScene = IntroScene.IntroScene()

    def changeScene(self, sceneName):
        self.nowScene.release()
        if sceneName == 'IntroScene':
            self.nowScene = IntroScene.IntroScene()
        elif sceneName == 'VillageScene':
            self.nowScene = VillageScene.VillageScene()
        elif sceneName == 'DungeonScene':
            self.nowScene = DungeonScene.DungeonScene()

    def update(self):
        path = self.nowScene.update()
        if path != 'none':
            self.changeScene(path)



    def render(self):
        self.nowScene.render()


