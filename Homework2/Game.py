# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:11:35 2015

@author: home
"""
import random

tries = 10000
npawns = 4
datalist=[]
averageturns = 0
winnersfirst = 0
board = {}
for i in range(1,100):
    board[i]=i
    
board[1]=38
board[4]=14
board[9]=31
board[16]=6
board[21]=42
board[28]=84
board[36]=44
board[48]=26
board[49]=13
board[51]=67
board[56]=53
board[62]=19
board[64]=60
board[71]=91
board[80]=100
board[93]=73
board[95]=75
board[98]=78

class Game:    
    def __init__(self, numpawns):
        self.pawns = []
        self.gameover = False
        self.numpawns = numpawns
        self.numturns = 0
        self.firstplayer = 0
        self.winner = 0
        for i in range(0,self.numpawns):
            self.pawns.append(Pawn())

    def run(self):
        self.firstplayer = random.randint(0,self.numpawns-1)
        while(not self.gameover):
            currentpawn=(self.firstplayer+self.numturns)%self.numpawns
            self.pawns[currentpawn].move()
            if self.pawns[currentpawn].place==100:
                self.winner = currentpawn                
                self.gameover=True
            self.numturns+=1
class Pawn:
    def __init__(self):
        self.place = 1
        self.spins = []

    def move(self):     
        self.place += random.randint(1,6)
        if self.place >= 100:
            self.place = 100
        else:
            self.place = board[self.place]
        
for i in range(0,tries):
    newgame = Game(npawns)
    newgame.run()
    data = {}
    data["Turns"] = newgame.numturns
    data["First"] = newgame.firstplayer
    data["Winner"] = newgame.winner
    datalist.append(data)
    
for data in datalist:
    averageturns+=data["Turns"]
    if data["Winner"]==data["First"]:
        winnersfirst+=1
averageturns/=tries
print (datalist)
print("average turns: " + str(averageturns))
print("minimum turns: "+ str(min(datalist,key=lambda x: x["Turns"])["Turns"]))
print("maximum turns: "+ str(max(datalist,key=lambda x: x["Turns"])["Turns"]))
print("chance of winning when going first " + str(winnersfirst/tries*100) +"%")