'''
/* This program is free software. It comes without any warranty, to
 * the extent permitted by applicable law. You can redistribute it
 * and/or modify it under the terms of the Do What The Fuck You Want
 * To Public License, Version 2, as published by Sam Hocevar. See
 * http://sam.zoy.org/wtfpl/COPYING for more details. */
'''

import os
import gtk
global limit
global players_alive
players_alive=[]
class player:
	def __init__(self,n):
		self.points=0
		self.name=n
		self.name_label=gtk.Label(self.name)
		self.points_label=gtk.Label(str(self.points))
		self.score_entry=gtk.Entry(2)
		self.score_entry.connect("activate",self.update_score)
	def update_score(self, widget):
		global limit
		global status_label
		global players_alive
		try:
			self.points=self.points+int(widget.get_text())
			widget.set_text("")
		except ValueError:
			pass
		if self.points < limit:
			self.points_label.set_text(str(self.points))
			status_label.set_text("")
		else:
			self.name_label.hide()
			self.points_label.hide()
			self.score_entry.hide()
			status_label.set_text(self.name+" is out !!")
			players_alive.remove(self)
			if len(players_alive)==1:
				status_label.set_text(players_alive[0].name+" wins !!")

def set_limit(self):
	try:
		global limit
		limit=int(self.get_text())
		current_limit.set_text("Limit set at "+str(limit))
	except ValueError:
		pass
	self.set_text("")

def add_new_player(self):
	new_player=player(self.get_text())
	self.set_text("")
	players_alive.append(new_player)
	v4.pack_start(new_player.name_label,1,1,1)
	v5.pack_start(new_player.points_label,1,1,1)
	v6.pack_start(new_player.score_entry,1,1,1)
	new_player.name_label.show()
	new_player.points_label.show()
	new_player.score_entry.show()
	
	
main_window=gtk.Window()
main_window.set_title("Least Count Score Keeper")
main_window.set_default_size(500,500)
v=gtk.VBox()
main_window.add(v)


v1=gtk.VBox()
h1=gtk.HBox()
v2=gtk.VBox()
h2=gtk.HBox()
v3=gtk.VBox()
h3=gtk.HBox()
v4=gtk.VBox()
v5=gtk.VBox()
v6=gtk.VBox()

limit_label=gtk.Label("Enter Limit :")
limit_entry=gtk.Entry(3)
limit_entry.connect("activate",set_limit)
current_limit=gtk.Label("Limit not set !!")

add_players_label=gtk.Label("Add Players")
add_players_name_label=gtk.Label("Enter Name :")
add_players_entry=gtk.Entry()
add_players_entry.connect("activate",add_new_player)

global status_label
status_label=gtk.Label("")

v.pack_start(v1,0,1,1)
v.pack_start(v2,0,1,1)
v.pack_start(v3,0,1,1)
v.pack_start(status_label,0,1,1)
v1.pack_start(h1,0,1,1)
h1.pack_start(limit_label,0,1,1)
h1.pack_start(limit_entry,0,1,1)
v1.pack_start(current_limit,0,1,1)
v2.pack_start(add_players_label)
v2.pack_start(h2,0,1,1)
h2.pack_start(add_players_name_label,0,1,1)
h2.pack_start(add_players_entry,0,1,1)
v3.pack_start(h3,0,1,1)
h3.pack_start(v4,1,1,1)
h3.pack_start(v5,1,1,1)
h3.pack_start(v6,1,1,1)

add_players_entry.show()
add_players_name_label.show()
add_players_label.show()
current_limit.show()
limit_label.show()
limit_entry.show()
h1.show()
h2.show()
h3.show()
v1.show()
v2.show()
v3.show()
v4.show()
v5.show()
v6.show()
v.show()
main_window.show_all()
gtk.main()
