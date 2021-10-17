from pico2d import *
import player_object
import stage


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                player.update_state('right')
            elif event.key == SDLK_LEFT:
                player.update_state('left')
            elif event.key == SDLK_UP:
                player.update_state('up')
            elif event.key == SDLK_DOWN:
                player.update_state('down')
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.update_state('idle')
            elif event.key == SDLK_LEFT:
                player.update_state('idle')
            elif event.key == SDLK_UP:
                player.update_state('idle')
            elif event.key == SDLK_DOWN:
                player.update_state('idle')



open_canvas(960, 640)

player = player_object.Player()
stage = stage.Stage()

running = True
while running:
    clear_canvas()
    handle_events()

    # Game Logic
    player.update()
    print(player.x)
    # Game Renderin
    stage.draw()
    player.draw()

    update_canvas()
    delay(0.05)