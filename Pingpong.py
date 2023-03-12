from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))

clock = time.Clock()
FPS = 60

game = True 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((147, 112, 219))

    display.update()
    clock.tick(FPS)