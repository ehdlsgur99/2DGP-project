from pico2d import *
import player_object
import stage
import MapInfo

class DungeonScene():
    def __init__(self):
        self.player = player_object.Player()
        self.generateMapInfo()
        self.stage = stage.Stage()


    def generateMapInfo(self):
        MapInfo.generateMapInfo()
        pass

    def update(self):
        self.handle_events()
        self.player.update()

    def render(self):
        self.stage.draw()
        self.player.draw()

    def release(self):
        pass

    def handle_events(self):
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