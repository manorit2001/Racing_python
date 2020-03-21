# 1 - Import library
from pygame.locals import *
import random
from Screen import * 
from Player import Player



class Game(Screen):
    def __init__(self,allPlayers):
        super().__init__()
        self.offsetRightX=50
        self.offsetLeftX=50
        self.endRaceXcoord=self.width-self.carSize[0]-self.endlineSize[0]-self.offsetRightX
        self.clock = pygame.time.Clock()
        #pygame.Rect(0,0,width,trackwidth)
        self.playersReachedEndline=0
        self.rankList=[]
        self.incrementInCarPosition=15
        self.decrementInCarPosition=0
        self.run(allPlayers)
    def updateplayer(self,player):
            currentPlayer=player
            self.text(currentPlayer)
            currentPlayer.coord[0]+=random.randint(self.decrementInCarPosition,self.incrementInCarPosition) #change the location of currentplayer
            playerX,playerY=currentPlayer.coord
            playerNo=currentPlayer.playerNo

            colorGreen=(0,255,0)
            startPoint=[self.offsetLeftX,playerY]
            endlineX=self.width-self.endlineSize[0]-self.offsetRightX
            endPoint=[endlineX,playerY]
            pygame.draw.line(self.screen,colorGreen,startPoint,endPoint) #draw the raceline(Green coloured)

            if(playerX>=4*self.width/5): #
                self.incrementInCarPosition=5 #Decrease Car Increment Speed
                self.decrementInCarPosition=-2 #Decrease Car Increment Speed

            if(playerX>=self.endRaceXcoord):
                if playerNo not in self.rankList:
                    self.rankList.append(playerNo)
                    print(playerNo)
                    self.wait()

            if(len(self.rankList)>0):
                ithPosition=len(self.rankList)+1
                self.drawtext(str(ithPosition)+" is:"+str(self.rankList[-1]))
            self.screen.blit(self.endline, [endlineX,playerY]) #endline
            self.screen.blit(self.car, [playerX,playerY]) #player
    def run(self,players):
        for i in players:
            i.coord[0]+=self.offsetLeftX
            i.coord[1]*=self.trackwidth
        while 1:
            # 5 - clear the screen before drawing it again
            time=self.clock.tick(30)
            self.screen.fill(0)
            # 6 - draw the screen elements
            for i in range(len(players)):
                self.updateplayer(players[i])

            if(len(players)==len(self.rankList)):
                print(self.rankList)
                pygame.quit()
                exit(0)
            # 7 - update the screen
            pygame.display.update()
            # 8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button 
                if event.type==pygame.QUIT:
                    # if it is quit the game
                    pygame.quit() 
                    exit(0) 
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        self.wait()
                    if event.key==pygame.K_q:
                        pygame.quit()
                        exit(0)
if __name__=="__main__":
    numplayers=10
    playersdata=[]
    for i in range(1,numplayers+1):
        playersdata.append(Player(i))
    Game(playersdata)
