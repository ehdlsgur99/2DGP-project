import OuttroScene
import VillageScene
import DungeonScene
import IntroScene
import time

class Scene_Manager:
    def __init__(self):
        self.index = 0
        self.nowScene = IntroScene.IntroScene()

    def changeScene(this, sceneName):
        this.nowScene.release()
        if sceneName == 'IntroScene':
            this.nowScene = IntroScene.IntroScene()
        elif sceneName == 'VillageScene':
            this.nowScene = VillageScene.VillageScene()
        elif sceneName == 'DungeonScene':
            this.nowScene = DungeonScene.DungeonScene()
        elif sceneName == 'OuttroScene':
            this.nowScene = OuttroScene.OuttroScene()


    def update(this):
        path = this.nowScene.update()
        if path != 'none':
            this.changeScene(path)

    def render(this):
        this.nowScene.render()


