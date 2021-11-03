from pico2d import *
import player_object
import Collision_Manager
import object
import time

class VillageScene():
    def __init__(self):
        self.bg = load_image('Resource/Stage/map.png')
        self.player = player_object.Player()
        print(self.player.state)
        self.changeScene = 'none'
        self.begin = time.time()

        self.portal = load_image('Resource/Stage/portal.png')

        self.objects = []
        self.objects.append(object.obj('Resource/Stage/aaa.png', 100, 350, 1000, 700))
        self.objects.append(object.obj('Resource/Stage/aaa.png', 300, 350, 1000, 700))
    def update(self):
        self.handle_events()
        self.player.update(self.objects)

        # 포탈에 들어갔다면?

        if Collision_Manager.CollisionManager.checkCircleCollision(self.player.x, self.player.y, 500, 100, 100):
            self.changeScene = 'DungeonScene'
        return self.changeScene

    def render(self):

        self.bg.clip_composite_draw(0, 0, 1000, 700, 0.0, 'none', 500, 350)

        for i in self.objects:
            i.render()
        # 포탈 출력
        self.portal.clip_composite_draw(0, 0, 100, 100, 0.0, 'none', 500, 100, 200, 200)

        self.player.draw()

        pass

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