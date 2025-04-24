from pygame import *

window_size = [700,500]
FPS = 60
game = True
level_run = True


MapBlock = {
            "Decor":sprite.Group(),
            "Collision":sprite.Group()
            }


player_pos = [0,0]
player_size = [0,0]
coin_list = sprite.Group()







window = display.set_mode(window_size)
clock = time.Clock()




























































































