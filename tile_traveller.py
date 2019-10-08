import random

def location(x, y, z, v):
	"""
	This function prints out the directions you can take and tells you if it's an invalid direction.
	Then it returns the players decision.
	"""
	
	moveans = ['n','e','s','w']
	levans = ['y','n']
	moves = v
	coins = z
	if (x == 1 and y == 1) or (x == 2 and y == 1):
		print("You can travel: (N)orth.")
		answer = random.choice(moveans)
		print("Direction: {}".format(answer))
		while answer:
			if answer == "n" or answer == "N":
				moves += 1
				return answer, coins, moves
			else:
				moves += 1
				print("Not a valid direction!")
				print("You can travel: (N)orth.")
			answer = random.choice(moveans)
			print("Direction: {}".format(answer))
				
	if (x == 1 and y == 2):
		lever = random.choice(levans)
		print("Pull a lever (y/n): {}".format(lever))
		if lever == 'y':
			coins += 1
			print("You received 1 coin, your total is now {}.".format(coins))
		print("You can travel: (N)orth or (E)ast or (S)outh.")
		answer = random.choice(moveans)
		print("Direction: {}".format(answer))
		while answer:
			if answer == "n" or answer == "N" or answer == "e" or answer == "E" or answer == "s" or answer == "S":
				moves += 1
				return answer, coins, moves
			else:
				moves += 1
				print("Not a valid direction!")
				print("You can travel: (N)orth or (E)ast or (S)outh.")
			answer = random.choice(moveans)
			print("Direction: {}".format(answer))

	if (x == 2 and y == 2) or (x == 3 and y == 3):
		if (x == 2 and y == 2):
			lever = random.choice(levans)
			print("Pull a lever (y/n): {}".format(lever))
			if lever == 'y':
				coins += 1
				print("You received 1 coin, your total is now {}.".format(coins))
		print("You can travel: (S)outh or (W)est.")
		answer = random.choice(moveans)
		print("Direction: {}".format(answer))
		while answer:
			if answer == "w" or answer == "W" or answer == "s" or answer == "S":
				moves += 1
				return answer, coins, moves
			else:
				moves += 1
				print("Not a valid direction!")
				print("You can travel: (S)outh or (W)est.")
			answer = random.choice(moveans)
			print("Direction: {}".format(answer))
		
	if (x == 1 and y == 3):
		print("You can travel: (E)ast or (S)outh.")
		answer = random.choice(moveans)
		print("Direction: {}".format(answer))
		while answer:
			if answer == "s" or answer == "S" or answer == "e" or answer == "E":
				moves += 1
				return answer, coins, moves
			else:
				moves += 1
				print("Not a valid direction!")
				print("You can travel: (E)ast or (S)outh.")
			answer = random.choice(moveans)
			print("Direction: {}".format(answer))

	if (x == 2 and y == 3):
		lever = random.choice(levans)
		print("Pull a lever (y/n): {}".format(lever))
		if lever == 'y':
			coins += 1
			print("You received 1 coin, your total is now {}.".format(coins))
		print("You can travel: (E)ast or (W)est.")
		answer = random.choice(moveans)
		print("Direction: {}".format(answer))
		while answer:
			if answer == "w" or answer == "W" or answer == "e" or answer == "E":
				moves += 1
				return answer, coins, moves
			else:
				moves += 1
				print("Not a valid direction!")
				print("You can travel: (E)ast or (W)est.")
			answer = random.choice(moveans)
			print("Direction: {}".format(answer))

	if (x == 3 and y == 2):
		lever = random.choice(levans)
		print("Pull a lever (y/n): {}".format(lever))
		if lever == 'y':
			coins += 1
			print("You received 1 coin, your total is now {}.".format(coins))
		print("You can travel: (N)orth or (S)outh.")
		answer = random.choice(moveans)
		print("Direction: {}".format(answer))
		while answer:
			if answer == "n" or answer == "N" or answer == "s" or answer == "S":
				moves += 1
				return answer, coins, moves
			else:
				moves += 1
				print("Not a valid direction!")
				print("You can travel: (N)orth or (S)outh.")
			answer = random.choice(moveans)
			print("Direction: {}".format(answer))

	
def movement(answer, matrix1, matrix2):
	"""
	This function takes the input from the function location() and then proceeds to change the players location.
	"""
	if answer == "n" or answer == "N":
		return matrix1, matrix2+1

	elif answer == "s" or answer == "S":
		return matrix1, matrix2-1

	elif answer == "w" or answer == "W":
		return matrix1-1, matrix2

	elif answer == "e" or answer == "E":
		return matrix1+1, matrix2

	
while True:	
	pos1 = 1
	pos2 = 1
	totalcoins = 0
	validmoves = 0
	theseed = int(input("Input seed: "))
	random.seed(theseed)
	while pos1 and pos2:
		"""
		This while loop constantly checks if the player has reached the goal.
		If not it continous to give the player possible directions.
		"""
		direction, totalcoins, validmoves = location(pos1, pos2, totalcoins, validmoves)
		
		pos1, pos2 = movement(direction, pos1, pos2)
	
		if pos1 == 3 and pos2 == 1:
			print("Victory! Total coins {}. Moves {}.".format(totalcoins, validmoves))
			break
	play_again = input("Play again (y/n): ")
			
	if play_again == "n":
		break


		 
