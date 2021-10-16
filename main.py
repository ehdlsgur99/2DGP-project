from pico2d import *
import player_object


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

player = player_object.Player()

running = True
while running:
    clear_canvas()
    handle_events()

    # Game Logic
    player.update()
    print(player.x)
    # Game Rendering
    player.draw()

    update_canvas()
    delay(0.05)