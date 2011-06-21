'''
/* This program is free software. It comes without any warranty, to
 * the extent permitted by applicable law. You can redistribute it
 * and/or modify it under the terms of the Do What The Fuck You Want
 * To Public License, Version 2, as published by Sam Hocevar. See
 * http://sam.zoy.org/wtfpl/COPYING for more details. */
'''
import sys
import os
global round_num,scoring_start
round_num=1
scoring_start=0
global limit
global num_players
num_players=0
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

def get_players(start,numplayersset):
    global num_players
    if numplayersset==0:
    	oops=1
    	while oops==1:
		try:
			oops=0
			num_players=int(raw_input("Number of players :"))
		except ValueError:
			oops=1
			print "Ooops not a number !!"
    	os.system("clear")
    for i in range(start,num_players):
        print "Name of player number "+str(i+1)
        p=player(raw_input())
        os.system("clear")
        players_alive.append(p)

def get_scores(start):
    global scoring_start
    for p in players_alive[start:]:
	scoring_start=players_alive.index(p)
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

def save_game(filename):
	f=open(filename,'w')
	f.write(str(limit)+'\n')
	f.write(str(round_num)+'\n')
	f.write(str(num_players)+'\n')
	f.write(str(scoring_start)+'\n')
	for p in players_alive:
		f.write(p.name+'\n')
		f.write(str(p.points)+'\n')
	f.close()

def load_game(filename):
	global limit,players_alive,round_num,num_players,scoring_start
	f=open(filename,'r')
	limit=int(f.readline())
	round_num=int(f.readline())
	num_players=int(f.readline())
	scoring_start=int(f.readline())
	while True:
		try:
			data=f.readline()
			p=player(data[:-1])
			p.update_score(int(f.readline()))
			players_alive.append(p)
		except:
			break
	if num_players==0:
		get_players(0,0)
	elif len(players_alive)<num_players:
		get_players(len(players_alive),1)
	if scoring_start==0:
		pass
	else:
		get_scores(scoring_start)
def lc():
	global limit,players_alive,round_num
	if len(sys.argv)==1:
		ooops=1
		while ooops==1:
			try:
				ooops=0
				limit=int(raw_input("Enter Limit :"))
			except ValueError:
				ooops=1
				print "Ooops not a number"
		os.system("clear")
		get_players(0,0)
	else:
		load_game(sys.argv[1])

	while len(players_alive)>1:
    		print "\t\tRound number "+str(round_num)+"\n"
    		print "Enter the scores:\n" 
    		get_scores(0)
    		os.system("clear")
   		show_scores()
    		check_alive()
    		round_num=round_num+1
        
	for p in players_alive:
    		print "\n\n*******************************************************"
    		print "======================WINNER==========================="
    		print "\t\t"+p.name+" !!" 
    		print "*******************************************************\n\n"

if __name__=='__main__':
	try:
		lc()
	except KeyboardInterrupt:
		print "Save game?(y/n) :"
		if(raw_input()=='y'):
			try:
				save_game(raw_input("Save as :"))
			except:
				print "Nothing to save. Aborting..."
		else:
			print "Bye..."

