class Player:
    def __init__(self,number,name):
        self.coord=[0,number*1]
        self.playerNo=number
        self.playerName=name
    def __str__(self):
        return str(self.playerName)
    def __repr__(self):
        return str(self.playerName)
