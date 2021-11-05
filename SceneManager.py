from pico2d import *

import VillageScene
import DungeonScene
import IntroScene

class Scene_Manager:

    index = 0
    nowScene = IntroScene.IntroScene()
    _sing = None

    def __new__(self, *args, **kwargs):
        if not self._sing:
            self._sing = super(Scene_Manager, self).__new__(self, *args, **kwargs)
            return self._sing

    def changeScene(this, sceneName):
        Scene_Manager.nowScene.release()
        if sceneName == 'IntroScene':
            this.nowScene = IntroScene.IntroScene()
        elif sceneName == 'VillageScene':
            this.nowScene = VillageScene.VillageScene()
        elif sceneName == 'DungeonScene':
            this.nowScene = DungeonScene.DungeonScene()

    def update(this):
        path = this.nowScene.update()
        if path != 'none':
            this.changeScene(path)

    def render(this):
        this.nowScene.render()


