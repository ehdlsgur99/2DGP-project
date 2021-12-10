from pico2d import *
import player_object
import Collision_Manager
import object
import time
import KeyManager
import ObjectManager
import Store
import Inventory

class VillageScene():
    def __init__(self):
        self.bgm = load_music('Resource/Sound/peace.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

        self.bg = load_image('Resource/Stage/map.png')
        if ObjectManager.Player == None:
            ObjectManager.Player = self.player = player_object.Player()
        else:
            self.player = ObjectManager.Player

        print(self.player.state)
        self.changeScene = 'none'
        self.begin = time.time()

        self.portal = load_image('Resource/Stage/portal.png')

        self.store = Store.store()

        self.objects = []
        self.objects.append(object.obj('Resource/Stage/aaa.png', 100, 350, 1000, 700))
        self.objects.append(object.obj('Resource/Stage/aaa.png', 300, 350, 1000, 700))

        self.npc = object.obj('Resource/NPC/npc.png', 700, 400, 80, 80, 7)
        self.npcPopUp = load_image('Resource/NPC/popup.png')
        self.isPopUp = False
    def update(self):
        KeyManager.handle_events()
        self.player.update(self.objects)
        self.npc.update()
        self.store.update()
        # 포탈에 들어갔다면?

        if KeyManager.now_key_state['SPACE'] == True and self.isPopUp == False:
            self.isPopUp = True
        if KeyManager.now_key_state['SPACE'] == False:
            self.isPopUp = False

        if Collision_Manager.CollisionManager.checkCircleCollision(self.player.x, self.player.y, 500, 100, 100):
            self.changeScene = 'DungeonScene'
        return self.changeScene

    def render(self):
        self.bg.clip_composite_draw(0, 0, 1000, 700, 0.0, 'none', 500, 350)

        for i in self.objects:
            i.draw()
        # 포탈 출력
        self.portal.clip_composite_draw(0, 0, 100, 100, 0.0, 'none', 500, 100, 200, 200)


        self.npc.drawSize(150, 150)

        if self.isPopUp == True:
            self.npcPopUp.draw(300, 350, 600, 500)
            self.store.draw()
            Inventory.inventory.instance().render()
            self.player.draw()
        else:
            self.player.draw()

    def release(self):
        pass
