from random import randint

WIDTH = 500
HEIGHT = 300

axie = Actor('idle_000')
axie.state = 'idle'
axie.frame = 0
axie.x_speed = 0
axie.y_speed = 0
axie.worms_caught = 0

IDLE_FPS = 8

worm = Actor('worm')
worm.x = randint(WIDTH/2, WIDTH-50)
worm.y = randint(0, HEIGHT-50)

def set_state(actor, state):
    actor.state = state
    actor.image = f'{state}_000'
    actor.frame = 0

def next_sprite(sprite):
    prefix, num = sprite.split('_')
    next_num = (int(num)+1) % 3
    return f"{prefix}_{next_num:03d}"

def update_sprite():
    axie.image = next_sprite(axie.image)

def update():
    axie.frame += 1
    
    axie.x = (axie.x + axie.x_speed) % WIDTH
    axie.y = (axie.y + axie.y_speed) % HEIGHT

    if axie.frame % IDLE_FPS == 0:
        update_sprite()

    if axie.colliderect(worm):
        axie.worms_caught += 1
        worm.x = randint(WIDTH/2, WIDTH-50)
        worm.y = randint(0, HEIGHT-50) 

        # get scared go to hide
        # if randint(0,5) == 5:
        #     axie.pos = (370, 180)



def on_key_down(key):
    if key == keys.RIGHT:
        if axie.state != 'swim':
            set_state(axie, 'swim')
        axie.x_speed = 4
    elif key == keys.LEFT:
        if axie.state != 'swim':
            set_state(axie, 'swim')
        axie.x_speed = -2
    elif key == keys.UP:
        if axie.state != 'climb' and axie.state != 'swim':
            set_state(axie, 'climb')
        axie.y_speed = -1
    elif key == keys.DOWN:
        axie.y_speed = 2


def on_key_up(key):
    set_state(axie, 'idle')
    axie.x_speed = 0
    axie.y_speed = 0

def draw():
    screen.clear()
    screen.blit('hide', (350, 180))
    axie.draw()
    worm.draw()