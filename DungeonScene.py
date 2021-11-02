import random

from pico2d import *
import player_object
import stage
import MapInfo
import object
import time
import monster_object


class DungeonScene():
    def __init__(self):

        self.player = player_object.Player()
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



    def generateMapInfo(self):
        MapInfo.generateMapInfo()
        pass

    def update(self):

        self.handle_events()
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
            print('render')
            i.render()

    def release(self):
        pass

    def handle_events(self):
        if time.time() - self.begin <= 1.0:
            events = get_events()
            return
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.player.update_state('right')
                elif event.key == SDLK_LEFT:
                    self.player.update_state('left')
                elif event.key == SDLK_UP:
                    self.player.update_state('up')
                elif event.key == SDLK_DOWN:
                    self.player.update_state('down')
                elif event.key == SDLK_a:
                    self.player.update_state('attack')
                elif event.key == SDLK_ESCAPE:
                    running = False
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.player.update_state('right')
                elif event.key == SDLK_LEFT:
                    self.player.update_state('left')
                elif event.key == SDLK_UP:
                    self.player.update_state('up')
                elif event.key == SDLK_DOWN:
                    self.player.update_state('down')