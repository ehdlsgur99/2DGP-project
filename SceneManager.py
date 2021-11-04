from pico2d import *

import VillageScene
import DungeonScene
import IntroScene

class SceneManager():

    index = 0
    nowScene = IntroScene.IntroScene()
    _sing = None

    def __new__(self, *args, **kwargs):
        if not self._sing:
            self._sing = super(SceneManager, self).__new__(self, *args, **kwargs)
            return self._sing

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


