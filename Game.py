# 1 - Import library
from pygame.locals import *
import random
from Screen import * 
from Player import Player
from Rank import *

class Game(Screen):

    def __init__(self,allPlayers):
        super().__init__()
        self.offsetRightX=50
        self.offsetLeftX=50
        self.endRaceXcoord=self.width-self.carSize[0]-self.endlineSize[0]-self.offsetRightX
        self.endlineX=self.width-self.endlineSize[0]-self.offsetRightX
        self.clock = pygame.time.Clock()
        self.playersReachedEndline=0
        self.rankList=[]
        self.incrementInCarPosition=15
        self.decrementInCarPosition=0
        self.semiRankList=[]
        self.recursive=1
        self.run(allPlayers,0)
    def dispCars(self,players):
        for i in players:
            self.screen.blit(self.car, i.coord)
            self.showPlayerNo(i)
    def dispEndline(self,players):
        for i in players:
            self.screen.blit(self.endline, [self.endlineX,i.coord[1]])
    def dispRaceline(self,players):
        colorGreen=(0,255,0)
        for i in range(len(players)+1):
            playerY=(i+1)*self.trackwidth
            # draw the raceline(Green coloured)
            startPoint=[self.offsetLeftX,playerY]
            endPoint=[self.endlineX,playerY]
            pygame.draw.line(self.screen,colorGreen,startPoint,endPoint)
    def displayall(self,players):
        # 5 - clear the screen before drawing it again
        colorBackground=(0,0,100)
        self.screen.fill(colorBackground)
        # call other display functions
        self.dispRaceline(players)
        self.dispEndline(players)
        self.dispCars(players)

    def updateplayer(self,player):
        currentPlayer=player
        currentPlayer.coord[0]+=random.randint(self.decrementInCarPosition,self.incrementInCarPosition) # change the location of currentplayer
        playerX,playerY=currentPlayer.coord
        playerNo=currentPlayer.playerNo

        # Decrease Car Increment Speed after 4/5th of the track 
        if(playerX>=4*self.width/5): 
            self.incrementInCarPosition=5 
            self.decrementInCarPosition=0

        # check if player has reached the endline
        if(playerX>=self.endRaceXcoord):
            if currentPlayer not in self.rankList:
                self.rankList.append(currentPlayer)
                self.semiRankList.append(currentPlayer)
                print(playerNo)
                #print(self.semiRankList)
                #self.wait()
    def resolveTie(self,players):
        for i in self.semiRankList:
            self.rankList.remove(i) # remove the players with same end time in ranklist
        self.recursive+=1
        print(self.semiRankList)
        coords=[(players.index(i),i.coord[1]) for i in self.semiRankList] # save the Y coord of the current users to set it back after recurse
        for i in range(3,1,-1): # countdown for tie match
            self.displayall(players)
            self.showInfo("Resolving tie between {} in {}".format(str(self.semiRankList),i))
            pygame.display.update()
            time.sleep(1)
        self.run(self.semiRankList,len(self.rankList)) # recurse for tie match
        for index,coordY in coords:
            players[index].coord[1]=coordY # set the Y coordinates again of the players in the tie
        self.recursive-=1 # for debugging purpose

        
    def run(self,players,initial):
        # assign starting offset and position to all the players
        self.incrementInCarPosition=15
        self.decrementInCarPosition=0
        self.semiRankList=[]
        for j in range(len(players)):
            i=players[j]
            i.coord[0]=self.offsetLeftX
            i.coord[1]=(j+1)*self.trackwidth
        while 1:
            times=self.clock.tick(30)
            # 6 - draw the screen elements
            self.displayall(players)

            for i in range(len(players)):
                self.updateplayer(players[i])

            # resolve tie between people
            if(len(self.semiRankList)>1):
                print(self.semiRankList)
                self.resolveTie(players)

            # print the ith winner
            if(len(self.semiRankList)==1):
                ithPosition=len(self.rankList)
                temp=['st','nd','rd','th']
                self.showInfo(str(ithPosition)+temp[ithPosition-1 if ithPosition<=4 else 3]+" is:"+str(self.rankList[-1]))
                pygame.display.update()
                time.sleep(1)

            self.semiRankList=[]
            
            # check if all the players have crossed the end line
            if(initial+len(players)==len(self.rankList)):
                break

            pygame.display.update()
            instruction=self.eventHandler()
            if(instruction=="exit"):
                self.rankList=[]
                exit(0)



    def getRankList(self):
        return self.rankList

if __name__=="__main__":
    # add players
    playersdata=[]
    playernames=['hehe','haha','qwer','asdf','xzcvdv']
    random.shuffle(playernames)
    numplayers=len(playernames)
    for i in range(1,numplayers+1):
        playersdata.append(Player(i,playernames[i-1]))

    # display the order given to ppl
    rank=Rank(playernames,'Player Numbers','Number')

    # run the game
    game=Game(playersdata)
    ranklist=game.getRankList()
    pygame.quit()
    print(ranklist)

    #display the ranklist
    rank=Rank(ranklist,'Ranklist','Position')
