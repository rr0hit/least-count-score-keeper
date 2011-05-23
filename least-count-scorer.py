'''
/* This program is free software. It comes without any warranty, to
 * the extent permitted by applicable law. You can redistribute it
 * and/or modify it under the terms of the Do What The Fuck You Want
 * To Public License, Version 2, as published by Sam Hocevar. See
 * http://sam.zoy.org/wtfpl/COPYING for more details. */
'''

import os
global limit
global num_players
global players_alive
players_alive=[]
class player:
    def __init__(self,n):
        self.points=0
        self.name=n
    def update_score(self,p):
        self.points=self.points+p
    def display(self):
        print "\t\t"+self.name+" "+str(self.points)

def get_players():
    num_players=int(raw_input("Number of players :"))
    os.system("clear")
    for i in range(num_players):
        print "Name of player number "+str(i+1)
        p=player(raw_input())
        os.system("clear")
        players_alive.append(p)

def get_scores():	
    for p in players_alive:
	oops=1
	while oops==1:
	    oops=0
	    try:
                p.update_score(int(raw_input(p.name+" :")))
	    except ValueError:
	        print "Oops not a number"
	        oops=1

def check_alive():
    for p in players_alive:
        if p.points>=limit:
            print "*******************************************************"
            print "\t\t"+p.name+" is OUT !!"
            print "*******************************************************"
            players_alive.remove(p)
            check_alive()
        
def show_scores():
    print "*******************************************************"
    print "======================SCORE============================"
    for p in players_alive:
        p.display()
    print "*******************************************************"
    
os.system("clear")
print "*******************************************************"
print "         rr0hit's least count score keeper"
print "*******************************************************\n\n"
limit=int(raw_input("Enter Limit :"))
os.system("clear")
get_players()

round_num=1
while len(players_alive)>1:
    print "\t\tRound number "+str(round_num)+"\n"
    print "Enter the scores:\n" 
    get_scores()
    os.system("clear")
    show_scores()
    check_alive()
    round_num=round_num+1
        
for p in players_alive:
    print "\n\n*******************************************************"
    print "======================WINNER==========================="
    print "\t\t"+p.name+" !!" 
    print "*******************************************************\n\n"
