from pygame import *

import settings
import gameSprite




class Coin(gameSprite.GameSprite):
    def __init__(self, img, x, y, width, height, speed, *groups):
        super().__init__(img, x, y, width, height, speed, *groups)