import time,sys
from Screen import *

class Rank(Screen):
    def __init__(self,rankList,heading,word):
        super().__init__()
        self.textColor=(255,0,0)
        self.offset=20
        # clear screen
        self.screen.fill((0,0,100))
        # write heading
        self.fontConfig.set_underline(True)
        self.fontConfig.set_bold(True)
        string="\t\t\t"+heading+"\t\t\t"
        string=string.replace('\t',' '*8)
        group=(string,self.centreX([string])[0],self.offset)
        self.writeText(group)
        self.fontConfig.set_underline(False)
        self.fontConfig.set_bold(False)
        self.textColor=(255,255,255)
        self.writeWords(word+" {} is:\t{}".replace('\t',' '*8),rankList)
        pygame.display.flip()
        while 1:
            instruction=self.eventHandler()
            if(instruction=="exit"):
                exit(0)
            elif(instruction=="continue"):
                break

    def writeText(self,group):
        string,coordx,coordy=group
        text=self.fontConfig.render(string,True,self.textColor)
        self.screen.blit(text, [coordx,coordy])
    def writeWords(self,stringf,words):
        strings=[]
        for i in range(len(words)):
            strings+=[stringf.format(i+1,words[i])]
        centrex=self.centreX(strings)
        print(centrex)
        centrey=self.centreY(strings)
        print(centrey)
        for i in range(len(strings)):
            self.writeText((strings[i],centrex[i],centrey[i]))

        text="PRESS ENTER TO CONTINUE!"
        self.textColor=(0,255,0)
        y=centrey[-1]+self.fontSize+self.offset*2
        x=self.centreX([text])[0]
        self.writeText((text,x,y))
    def centreX(self,strings):
        coordX=[]
        for i in strings:
            coordX+=[self.width//2-self.fontConfig.size(i)[0]//2]
        return [min(coordX)]*len(coordX)
    def centreY(self,strings):
        coordY=[]
        startingY=self.height//2-(len(strings)//2*(self.fontSize+self.offset))
        for i in strings:
            coordY+=[startingY]
            startingY+=self.fontSize+self.offset
        return coordY 

if __name__=="__main__":
    rank=Rank([1,2,3],'RankList','No')
    pygame.quit()
    sys.exit(0)


