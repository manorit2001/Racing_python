from Game import *
if __name__=="__main__":
    # initialize Qt
    app=QApplication([])

    # add players
    playersdata=[]
    playernames=['hehe','haha','qwer','asdf','xzcvdv']
    random.shuffle(playernames)
    numplayers=len(playernames)
    for i in range(1,numplayers+1):
        playersdata.append(Player(i,playernames[i-1]))

    # display the order given to ppl
    rank=Rank(playernames,'Player Numbers','Number')
    rank.show()
    app.exec_()

    # run the game
    game=Game(playersdata)
    ranklist=game.getRankList()
    pygame.quit()
    print(ranklist)

    #display the ranklist
    rank=Rank(ranklist,'Ranklist','Position')
    rank.show()
    sys.exit(app.exec_())
