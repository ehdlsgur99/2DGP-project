import random

import ObjectManager
from pico2d import *
import player_object
import stage
import MapInfo
import object
import time
import monster_object
import KeyManager


class DungeonScene():
    def __init__(self):
        self.player = ObjectManager.Player
        self.generateMapInfo()
        self.stage = stage.Stage()
        self.changeScene = 'none'
        self.objects = []
        self.begin = time.time()
        self.monsters = []
        self.generateMonster()

    def generateMonster(self):
        self.monsters = []
        if self.stage.mapInfo[self.stage.nowMapIndex] == '1':
            for i in range(random.randint(0, 5)):
                if random.randint(0, 1):
                    self.monsters.append(monster_object.GoblinMonster())
                else:
                    self.monsters.append(monster_object.zombieMonster())
        if self.stage.mapInfo[self.stage.nowMapIndex] == '2':
            self.monsters.append(monster_object.bossMonster())



    def generateMapInfo(self):
        MapInfo.generateMapInfo()
        pass

    def update(self):
        KeyManager.handle_events()
        self.changeScene = self.stage.update(self.player, self.monsters)
        self.player.update(self.objects)
        self.player.checkMonster(self.monsters)
        if self.stage.isStageChange == True:
            self.generateMonster()
            self.stage.isStageChange = False

        for i in self.monsters:
            i.update()
            i.checkPlayer(self.player)

        if self.changeScene != 'none':
            return self.changeScene
        return 'none'

    def render(self):

        self.stage.draw()
        self.player.draw()
        for i in self.monsters:
            i.render()

    def release(self):
        pass
