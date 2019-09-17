def location(x, y):
	if (x == 1 and y == 1) or (x == 2 and y == 1):
		print("You can travel: (N)orth.")
		answer = input("Direction: ")
	if (x == 1 and y == 2):
		print("You can travel: (N)orth or (E)ast or (S)outh.")
	if (x == 2 and y == 2) or (x == 3 and y == 3):
		print("You can travel: (S)outh or (W)est.")
	if (x == 1 and y == 3):
		print("You can travel: (S)outh or (E)ast.")
	if (x== 2 and y === 3):
		print("You can travel: (E)ast or (W)est.")
	if (x == 3 and y == 2):
		print("You can travel: (N)orth or (S)outh.")
	if (x == 3 and y == 1):
		print("Victory")
	return(x, y)
	
	
	
	

def movement(answer, matrix1, matrix2):
	if answer == n or answer == N:
		return matrix1
		return matrix2+1

	elif answer == s or answer == S:
		return matrix1
		return matrix2-1

	elif answer == w or answer == W:
		return matrix1-1
		return matrix2

	elif answer == e or answer == E:
		return matrix1+1
		return matrix2

	

pos1 = 1
pos2 = 1

while pos1 != 3 and pos2 != 1:
	
	
	direction = location(pos1, pos2)
	
	
	pos1, pos2 = movement(direction)


print("Victory!")
		 