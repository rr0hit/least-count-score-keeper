'''
/* This program is free software. It comes without any warranty, to
 * the extent permitted by applicable law. You can redistribute it
 * and/or modify it under the terms of the Do What The Fuck You Want
 * To Public License, Version 2, as published by Sam Hocevar. See
 * http://sam.zoy.org/wtfpl/COPYING for more details. */
'''

# TODO currently 18 lines are skipped to clear space. This is machine specific. Env variable has to be read.

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
    clear_lines(18)
    for i in range(num_players):
        print "Name of player number "+str(i+1)
        p=player(raw_input())
        clear_lines(18)
        players_alive.append(p)

def clear_lines(num):
    for i in range(num):
        print ""
        
def get_scores():
    for p in players_alive:
        p.update_score(int(raw_input(p.name+" :")))

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
    
clear_lines(18)
limit=int(raw_input("Enter Limit :"))
clear_lines(18)
get_players()

while len(players_alive)>1:
    get_scores()
    clear_lines(18)
    show_scores()
    check_alive()
        
for p in players_alive:
    print "\n\n*******************************************************"
    print "======================WINNER==========================="
    print "\t\t"+p.name+" !!" 
    print "*******************************************************\n\n"
