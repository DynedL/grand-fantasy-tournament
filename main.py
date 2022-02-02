import random

roundNumber = 1
playerLives = 5
running = True

enemywizard = 0
enemyarcher = 0
enemywarrior = 0

names = ['James', 'Jeff', 'Charles', 'Jack', 'Danielle', 'Grace', 'Farnsworth', 'Tom', 'Tim']
enemyName = random.choice(names)

print('----------------------------------------')
print('Welcome to the Great Fantasy Tournament!')
print()
print('Opponent:', enemyName)
print()
print(' >>>----> Archer beats Wizard')
print(' ---O(0)O Wizard beats Warrior')
print(' --|----- Warrior beats Archer')
print()
print('----------------------------------------')
print()

while running: 
	print()
	print("Round", roundNumber, "of 5")
	print("Lives:", playerLives)
	print("Choose your move: archer(1), wizard(2) warrior(3)")

	playermove = input('> ')

	if playermove not in ['1','2','3']:
		print("Invalid Response")
		continue
	else:
		if playermove == '1':
			playermove = 'archer'
		elif playermove == '2':
			playermove = 'wizard'
		else:
			playermove = 'warrior'
  
		enemymove = random.randint(1,3)
		if enemymove == 1:
			enemymove = 'archer'
		elif enemymove == 2:
			enemymove = 'wizard'
		else:
			enemymove = 'warrior'
		
		print()
		print('You Picked: ', playermove.upper())
		print(enemyName, 'Picked: ', enemymove.upper())

		if enemymove == 'wizard':
			enemywizard += 1
		if enemymove == 'archer':
			enemyarcher += 1
		if enemymove == 'warrior':
			enemywarrior += 1

		if playermove == enemymove:
			print("It's a draw! Play again!")
			continue
		elif playermove == 'archer':
			if enemymove == 'wizard':
				print("You won!")
				roundNumber += 1
			elif enemymove == 'warrior':
				print("You lost!")
				roundNumber += 1
				playerLives -= 1
		elif playermove == 'wizard':
			if enemymove == 'archer':
				print("You lost!")
				roundNumber += 1
				playerLives -= 1
			elif enemymove == 'warrior':
				print("You won!")
				roundNumber += 1
		else:
			if enemymove == 'wizard':
				print("You lost!")
				roundNumber += 1
				playerLives -= 1
			elif enemymove == 'archer':
				print("You won!")
				roundNumber += 1


	if playerLives == 0:
		print()
		print("You Lost! Good luck next time!")
		print("You got to round", roundNumber,"!")
		running = False
	elif roundNumber > 5:
		print()
		print("You won the game!")
		print("You had", playerLives, "lives left!")
		running = False
