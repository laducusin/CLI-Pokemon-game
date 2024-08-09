
import random

def map_zone(height, width, map_safari):
	for x in range(width+2):
		print("-", end="")
	print()
	for x in range(height):
		print("|", end="")
		for y in range(width):
			print (map_safari[x][y], end="")
		print("|")
	for x in range(width+2):
		print("-", end="")
	print()

def map_item(height, width, grass):
	grass_item = ["*" for x in range(grass)]
	area = height*width-1
	spaces = area - grass
	space_item = [" " for x in range(spaces)]
	items = grass_item + space_item
	map_safari = [[] for x in range(height)]
	for x in range(height):
		for y in range(width):
			if x == height -1 and y == 0:
				map_safari[x].append("A")
			else:
				item_len = len(items) - 1
				item_random = random.randint(0, item_len)
				item = items.pop(item_random)
				map_safari[x].append(item)
	return map_safari

def is_success(chance):
	x = random.randint(1, 10) / 10
	if x <= chance:
		return True
	return False

def pokemon_encounter():
	pokemon_names = ['Venonat', 'Politoad', 'Rhyhorn', 'Dratini', 'Chansey']
	pokemon_capture_rate = [0.5, 0.5, 0.4, 0.2, 0.1]
	pokemon_index = random.randint(0,4)
	print("Wild " + pokemon_names[pokemon_index] + " appeared!")
	action = ""
	current_rate = pokemon_capture_rate[pokemon_index]
	while action != "r":
		action = input("Action? [s/p/r]: ")
		if action == "s":
			print("You threw a stone at wild " + pokemon_names[pokemon_index])
			current_rate *= 2
		if action == "p":
			print(pokemon_names[pokemon_index], end="")
			if is_success(current_rate):
				print(" was captured.")
				nickname = False
				while nickname != True:
					nickname = str(input("Give a nickname to your captured Pokemon? [y/n]: "))
					if nickname == "y":
						name = str(input("please input a nickname to your pokemon: "))
						captured_pokemon.append(name)
						nickname = True
						action = "r"
					elif nickname == "n":
						captured_pokemon.append(pokemon_names[pokemon_index])
						nickname = True
						action = "r"
			else:
				print(" was not captured")
				break

def map_move(map_safari, map_new, direction, width, height):
	for x in range(0,height):
		for y in range(0,width):
			if map_new[x][y]=="A":
				map_copy = map_safari[x][y]
				if map_copy == "A":
					map_safari[x][y] = " "
					map_copy = " "		
				if y == width - 1 and direction == "d":
						print("Can't Move! Right border")
						return 0	
				elif x == 0 and direction == "w":
						print("Can't Move! Top border")
						return 0
				elif x == height - 1 and direction == "s":
						print("Can't Move! Bottom border")
						return 0
				elif y == 0 and direction == "a":
						print("Can't Move! Left border")
						return 0	
				if direction == "d":
					v = y + 1
					map_new[x][y] = map_copy
					map_new[x][v] = "A"
					if map_safari[x][v] == "*":
						if is_success(0.5):
							a = pokemon_encounter()		
				elif direction == "w":
					u = x - 1
					map_new[x][y] = map_copy
					map_new[u][y] = "A"
					if map_safari[u][y] == "*":
						if is_success(0.5):
							a = pokemon_encounter()		
				elif direction == "s":
					u = x + 1
					map_new[x][y] = map_copy
					map_new[u][y] = "A"
					if map_safari[u][y] =="*":
						if is_success(0.5):
							a = pokemon_encounter()	
				elif direction == "a":
					v = y - 1
					map_new[x][y] = map_copy
					map_new[x][v] = "A"
					if map_safari[x][v] =="*":
						if is_success(0.5):
							a = pokemon_encounter()	
				return map_new

import copy

print("Welcome to the Safari Zone where you can play to catch Pokemon!")
height = int(input("Please input height of the safari: "))
width = int(input("Please input width of the safari: "))
grass  = int(input("Please input number of grass tiles in the safari: "))

area = height*width

while area -1 < grass:
	grass  = int(input("Invalid input of number of grass tiles! Please input again: "))

captured_pokemon=[]

steps = 50
map_safari = map_item(height, width, grass )
map_new = copy.deepcopy (map_safari)

while steps > 0:
	direction=""
	map_zone(height, width, map_new)
	print("Steps:", steps)
	while direction != "w" and direction != "a" and direction != "s" and direction != "d":
		direction =input("Move where? [w/a/s/d]: ")
	map_copy_ = copy.deepcopy(map_new)
	map_new = map_move(map_safari, map_new, direction, width, height)
	if map_new == 0:
		map_new = map_copy_
	else:
		steps = steps - 1

map_zone(height, width, map_new)
print("Steps remaining:", steps)

if steps == 0:
	print("Time's up! Thank you for playing the Safari game. We hope to see you again in the future.")
	print("Pokemon you've caught:")
	for i, item in enumerate(captured_pokemon,1):
		print(i,".",item)
	

			
			
		