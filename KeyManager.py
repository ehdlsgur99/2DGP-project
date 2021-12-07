from pico2d import *

now_key_state = {'LEFT': False, 'RIGHT': False, 'UP': False, 'DOWN': False, 'ATTACK': False, 'DASH' : False,
                 'SMASH' : False, 'SPACE' : False}

mouseXPos, mouseYPos = 0, 0
mouseDown = False

def handle_events():
    events = get_events()
    global mouseXPos
    global mouseYPos
    global mouseDown

    for event in events:
        if event.type == SDL_MOUSEMOTION:
            mouseXPos, mouseYPos = event.x, event.y
        if event.type == SDL_MOUSEBUTTONDOWN:
            mouseDown = True
        elif event.type == SDL_MOUSEBUTTONUP:
            mouseDown = False

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                now_key_state['RIGHT'] = True
            elif event.key == SDLK_LEFT:
                now_key_state['LEFT'] = True
            elif event.key == SDLK_UP:
                now_key_state['UP'] = True
            elif event.key == SDLK_DOWN:
                now_key_state['DOWN'] = True
            elif event.key == SDLK_a:
                now_key_state['ATTACK'] = True
            elif event.key == SDLK_d:
                now_key_state['DASH'] = True
            elif event.key == SDLK_s:
                now_key_state['SMASH'] = True
            elif event.key == SDLK_SPACE:
                now_key_state['SPACE'] = True
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                now_key_state['RIGHT'] = False
            elif event.key == SDLK_LEFT:
                now_key_state['LEFT'] = False
            elif event.key == SDLK_UP:
                now_key_state['UP'] = False
            elif event.key == SDLK_DOWN:
                now_key_state['DOWN'] = False
            elif event.key == SDLK_a:
                now_key_state['ATTACK'] = False
            elif event.key == SDLK_d:
                now_key_state['DASH'] = False
            elif event.key == SDLK_s:
                now_key_state['SMASH'] = False
            elif event.key == SDLK_SPACE:
                now_key_state['SPACE'] = False