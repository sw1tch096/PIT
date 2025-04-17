from pygame import *
import settings
import gameSprite

class Player(gameSprite.GameSprite):
    def __init__(self, image_right, image_up , x, y, width, height, speed, *groups):
        super().__init__(image_right, x, y, width, height, speed, *groups)
        self.image_right = transform.scale(image.load(image_right),(width),(height))
        self.image_up = transform.scale(image.load(image_up),(width),(height))
        

        self.xMove = 0
        self.yMove = 0

        self.isMove = True

    def move(self):
        key_list = key.get_pressed()

        if key_list[K_a] and self.isMove:
            self.isMove = False
            self.xMove = -self.speed
            self.image = transform.flip(self.image_right, True, False)

        elif key_list[K_d] and self.isMove:
            self.isMove = False
            self.xMove = self.speed
            self.image = self.image_right
            
        elif key_list[K_w] and self.isMove:
            self.isMove = False
            self.yMove = -self.speed
            self.image = self.image_up
        elif key_list[K_s] and self.isMove:
            self.isMove = False
            self.yMove = self.speed
            self.image = transform.flip(self.image_up, False, True)

        self.rect.x += self.xMove
        self.rect.y += self.yMove

    def collide(self):
        for block in settings.MaBlock["Collision"]:
            if sprite.collide_rect(self, block):
                if self.xMove > 0:
                    self.rect.right = block.rect.left
                    self.xMove = 0
                    self.isMove = True 

                if self.xMove > 0:
                    self.rect.left = block.rect.right
                    self.xMove = 0
                    self.isMove = True 

                if self.yMove > 0:
                    self.rect.bottom = block.rect.top
                    self.yMove = 0
                    self.isMove = True 

                if self.yMove > 0:
                    self.rect.top = block.rect.bottom
                    self.yMove = 0
                    self.isMove = True 

    def update(self, *args, **kwargs):
        self.move()
        self.collide()
        
        
        
        return super().update(*args, **kwargs)
