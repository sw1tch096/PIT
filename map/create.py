from pygame import *

import coin
import gameSprite

import settings



"┐ └ │ ┘ ─ ┌ ░"



def create_level(path_level:str)  -> dict["Decor":sprite.Group, "Collision":sprite.Group ]:   
    mapDecor = sprite.Group()
    mapCollision = sprite.Group()

    with open(path_level, "r", encoding='utf-8') as file:
        lines = file.readlines()
        height = round(settings.window_size[1] / len(lines))
        width = round(settings.window_size[0] / len(lines[0].split(" ")))

        y = 0
        for line in lines:
            line = line.split(" ")
            x = 0
            for symbol in line:

                symbol = symbol.replace("\n", "")

                if symbol == ".":
                    block = gameSprite.GameSprite("image/tilles/tile_0014.png",
                                                x, y, width, height, 0)
                    mapDecor.add(block)

                elif symbol == "─":
                    block = gameSprite.GameSprite("image/tilles/tile_0011.png",
                                                x, y, width, height, 0)
                    mapCollision.add(block)
                elif symbol == "│":
                    block = gameSprite.GameSprite("image/tilles/tile_0007.png",
                                                x, y, width, height, 0)
                    mapCollision.add(block)

                elif symbol == "┐":
                    block = gameSprite.GameSprite("image/tilles/tile_0002.png",
                                                x, y, width, height, 0)
                    mapCollision.add(block)
                elif symbol == "└":
                    block = gameSprite.GameSprite("image/tilles/tile_0010.png",
                                                x, y, width, height, 0)
                    mapCollision.add(block)
                
                elif symbol == "┘":
                    block = gameSprite.GameSprite("image/tilles/tile_0012.png",
                                                x, y, width, height, 0)
                    mapCollision.add(block)
                
                elif symbol == "┌":
                    block = gameSprite.GameSprite("image/tilles/tile_0000.png",
                                                x, y, width, height, 0)
                    mapCollision.add(block)
                elif symbol == "░":
                    block = gameSprite.GameSprite("image/tilles/tile_00014.png",
                                                x, y, width, height, 0)
                    mapDecor.add(block)
                
                elif symbol == "1":
                    block = gameSprite.GameSprite("image/tilles/tile_00014.png",
                                                x, y, width, height, 0)
                    mapDecor.add(block)
                    
                    settings.player_pos = [x, y]
                
                elif symbol == "0":
                    block = gameSprite.GameSprite("image/tilles/tile_00014.png",
                                                x, y, width, height, 0)
                    mapDecor.add(block)
                    coin_ = coin.Coin("image/coin/asda.png",
                                                x, y, width, height, 0)
                    settings.coin_list.add(coin_)
                    


                x += width
            y += height 

        settings.player_size = [width, height]
        settings.MapBlock["Decor"] = mapDecor
        settings.MapBlock["Collision"] = mapCollision




































































































