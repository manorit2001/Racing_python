import pygame
from screeninfo import get_monitors
from pygame.locals import *
class Screen:
    def __init__(self):
        pygame.init()
        temp=get_monitors()[0]
        self.trackwidth=40
        self.width, self.height = temp.width,temp.height
        self.fontSize=16
        # for debug purpose
        #self.width=800
        #self.height=600

        self.screen=pygame.display.set_mode((self.width, self.height))
        self.initcar()
        self.initendline()
    def initcar(self):
        self.fontConfig = pygame.font.Font('freesansbold.ttf', self.fontSize)
        self.car= pygame.image.load("res/images/car.png")
        self.carSize=self.car.get_rect().size
    def initendline(self):
        self.endline = pygame.image.load("res/images/end.jpg")
        self.endline.convert_alpha()
        self.endline=pygame.transform.scale(self.endline,(10,self.trackwidth))
        self.endlineSize=self.endline.get_rect().size
    def wait(self):
        clock = pygame.time.Clock()
        while True:
            time=clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_p:
                    return
                if event.key==pygame.K_q:
                    pygame.quit()
                    exit(0)

    def showPlayerNo(self,currentPlayer):
        text=self.fontConfig.render(str(currentPlayer.playerNo),True,(255,0,0))
        self.screen.blit(text, (currentPlayer.coord[0]-len(str(currentPlayer.playerNo))*16,currentPlayer.coord[1]+(32-16)/2))
    def showInfo(self,stri):
        text=self.fontConfig.render(stri,True,(255,0,0))
        self.screen.blit(text, (self.trackwidth,0))
    def eventHandler(self):
            # 8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button 
                if event.type==pygame.QUIT:
                    # if it is quit the game
                    return "exit"
                    pygame.quit() 
                    #check if it's a key press
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        # wait till p is pressed again
                        return "pause"
                        self.wait()
                    if event.key==pygame.K_q:
                        return "exit"
                        pygame.quit()
                    if event.key==pygame.K_RETURN:
                        return "continue"
