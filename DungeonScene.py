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
        self.generateMapInfo()

        self.changeScene = 'none'
        self.begin = time.time()

        self.stage = stage.Stage()
        ObjectManager.add_object(self.stage, 0)
        self.player = player_object.Player()
        ObjectManager.add_object(self.player, 1)
        self.generateMonster()

    def generateMonster(self):
        if self.stage.mapInfo[self.stage.nowMapIndex] == '1':
            for i in range(random.randint(0, 5)):
                if random.randint(0, 1):
                    ObjectManager.add_object(monster_object.GoblinMonster(), 2)
                else:
                    ObjectManager.add_object(monster_object.zombieMonster(), 2)



    def generateMapInfo(self):
        MapInfo.generateMapInfo()
        pass

    def update(self):

        self.handle_events()

        if self.stage.isStageChange == True:
            self.generateMonster()
            self.stage.isStageChange = False

        self.changeScene = self.stage.update()
        if self.changeScene != 'none':
            ObjectManager.clear()
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