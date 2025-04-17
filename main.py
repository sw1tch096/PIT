from pygame import *


import settings
import gameSprite
import player
import coin




while settings.game:
    for ev in event.get():
        if ev.type == QUIT:
               settings.game = False
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
             settings.game = False

    if settings.level_run:
        pass


    display.update()
    settings.clock.tick(settings.FPS)
