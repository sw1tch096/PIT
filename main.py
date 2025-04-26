from pygame import *


import settings
import gameSprite
import player
import coin
import map.create as mapCreate


level = 0


mapCreate.create_level(f"map/level/{settings.level_list[level]}.txt")





mapCreate.create_level("map/level/1.txt")

player_ = player.Player("image/player/фчффыв.png", "image/player/фчффыв.png",
                        settings.player_pos[0],settings.player_pos[1],
                        settings.player_size[0],settings.player_size[1],
                        5)

num_coin = 0












while settings.game:
    for ev in event.get():
        if ev.type == QUIT:
               settings.game = False
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
             settings.game = False

    if settings.level_run:
        settings.MapBlock["Decor"].draw(settings.window)
        settings.MapBlock["Decor"].update()
        settings.MapBlock["Collision"].draw(settings.window)
        settings.MapBlock["Collision"].update()
        settings.coin_list.draw(settings.window)
        settings.coin_list.update()
        player_.show()
        player_.update()

        list_coin = sprite.spritecollide(player_,settings.coin_list,True)
        for collide in list_coin:
            num_coin += 1
            print (num_coin)

        if num_coin >= 6:
            settings.level_run = False 
    else:
        level += 1
        if level > len(settings.level_list)-1:
            level = 0

        settings.MapBlock["Collision"].empty
        settings.MapBlock["Decor"].empty
        settings.coin_list.empty()

        mapCreate.create_level(f"map/level/{settings.level_list[level]}.txt")

        player_ = player.Player("image/player/фчффыв.png", "image/player/фчффыв.png",
                        settings.player_pos[0],settings.player_pos[1],
                        settings.player_size[0],settings.player_size[1],
                        5)


        num_coin = 0
        settings.level_run = True



    display.update()
    settings.clock.tick(settings.FPS)

