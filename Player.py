class Player:
    def __init__(self,number):
        self.coord=[0,number*1]
        self.playerNo=number
    def __str__(self):
        return str(self.playerNo)
