def location(x, y):
	
	for i, r in range(1,4):
		print(i,r)
	

def moveMent(answer, matrix1, matrix2):
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
		 