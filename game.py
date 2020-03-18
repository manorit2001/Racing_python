# 1 - Import library
import pygame
from pygame.locals import *
import random
class Player:
    def __init__(self,number):
        self.loc=[40,number*40]
        self.playerno=number

#def color_surface(surface, red, green, blue):
#    arr = pygame.surfarray.pixels3d(surface)
#    arr[:,:,0] = red
#    arr[:,:,1] = green
#    arr[:,:,2] = blue
#    return arr
#def colorize(image, newColor):
#    """
#    Create a "colorized" copy of a surface (replaces RGB values with the given color, preserving the per-pixel alphas of
#    original).
#    :param image: Surface to create a colorized copy of
#    :param newColor: RGB color to use (original alpha values are preserved)
#    :return: New colorized Surface instance
#    """
#    image = image.copy()
#
#    # zero out RGB values
#    #image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
#    # add in new RGB values
#    image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
#
#    return image

def game(players):
    # 2 - Initialize the game
    pygame.init()
    width, height = 640, 480
    screen=pygame.display.set_mode((width, height))

    # 3 - Load images
    font = pygame.font.Font('freesansbold.ttf', 16)
    player = pygame.image.load("res/images/car.png")
    player.convert_alpha()
    clock = pygame.time.Clock()
    # 4 - keep looping through
    while 1:
        # 5 - clear the screen before drawing it again
        time=clock.tick(60)
        screen.fill(0)
        # 6 - draw the screen elements
        #loc[0]+=1;
        #play=colorize(player,(255,0,0))
        for i in range(len(players)):
            players[i].loc[0]+=random.randint(0,1)
            text=font.render(str(i),True,(255,0,0))
            screen.blit(player, players[i].loc)
            screen.blit(text, (players[i].loc[0]-10,players[i].loc[1]))
        # 7 - update the screen
        pygame.display.update()
        # 8 - loop through the events
        for event in pygame.event.get():
            # check if the event is the X button 
            if event.type==pygame.QUIT:
                # if it is quit the game
                pygame.quit() 
                exit(0) 

if __name__=="__main__":
    numplayers=5
    players=[]
    for i in range(numplayers):
        players.append(Player(i))
    game(players)
