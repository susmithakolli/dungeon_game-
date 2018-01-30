import os
import random 


CELLS = [(0,0),(1,0),(2,0),(3,0),(4,0),
         (0,1),(1,1),(2,1),(3,1),(4,1),
		 (0,2),(1,2),(2,2),(3,2),(4,2),
		 (0,3),(1,3),(2,3),(3,3),(4,3),
		 (0,4),(1,4),(2,4),(3,4),(4,4)]

def clear_screen():
	os.system('cls')
def get_locations():
	return random.sample(CELLS,3)
	
def move_player(player,moves):
	x,y = player
	if moves == "left":
		x = x-1
	if moves == "right":
		x = x+1
	if moves == "up":
		y = y-1
	if moves == "down":
		y = y+1
	return x,y
	
def get_moves(player):
	moves = ["left","right","up","down"]
	x,y = player
	if x==0: 
		moves.remove("left")
	if x==4: 
		moves.remove("right")
	if y==0: 
		moves.remove("up")
	if y==4: 
		moves.remove("down")
	return moves
	
def draw_map(player):
	print(" _"*5)
	tile ="|{}"
	for cell in CELLS:
		x,y = cell
		if x<4:
			line_end = ""
			if cell == player:
				output = tile.format("X")
			else:
				output = tile.format("_")
		else:
			line_end = "\n"
			if cell == player:
				output = tile.format("X|")
			else:
				output = tile.format("_|")
		print(output, end=line_end)
			
			
def game_loop():
	player,door,monster = get_locations()	
	while True:
		draw_map(player)
		valid_moves = get_moves(player)
		print("You are currently in the room{}". format(player))
		print("you can move {}".format(", ".join(valid_moves)))
		print("enter q to quit")
		
		moves = input("> ").lower()
		if moves == 'q':
			break
		if moves in valid_moves:
			player = move_player(player,moves)
			
			if player == monster:
				print("oh my god!. monster caught you.you loose")
				break
			if player == door:
				print("wow!! you are saved. you win!")
				break
		else:
			input("Wall are hard.Dont run into them")
		clear_screen()
			

clear_screen()
print("Welcome to Dungeon Game")
input("press return to start")
clear_screen()
game_loop()
			
			
			