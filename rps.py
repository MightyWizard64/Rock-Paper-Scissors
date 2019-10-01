# Eric Nunez
# Rock Paper Scissors
# rps.py
import random
#Variables
pScore = 0
cScore = 0
ties = 0
cMoves = ["rock", "paper", "scissors"]
# Welcome Message (done)
# Print a welcome message
print("Welcome to rock, paper, scissors")
# prompt for name
pName = input("What is your name?: ")


# Score Tracker
# Make a function
def printScore():
	# Prints score
	print("Score: ")
# Shows player score
	print(pName + ": " + str(pScore))
# Shows computer score
	print("Computer Score: " + str(cScore))
# Shows how many ties
	print("Ties: " + str(ties))

# Game loop
# loop until q is entered
while True:
	# prompt for player move (r, p, s, q)
	pMove = input("Enter 'r' for rock, 'p' for paper, 's' for scissors, or 'q' for quit: ")
	# print score
	printScore()
	# check if q is entered if so end the game
	if pMove == "q":
		break
	# get a computer move (random)
	cMove = random.choice(cMoves)
	# compare player move with the computer move
		# player picks rock
	if pMove == "r":
		print(pName + " picked Rock")
		if cMove == "rock":
				print("Computer picks Rock")
				print("Tie")
				ties += 1
		elif cMove == "paper":
				print("Computer picks Paper")
				print("Paper covers Rock")
				cScore += 1
		else:
				print("Computer picks Scissors")
				print("Rock breaks Scissors")
				pScore += 1
		# player picks paper
	elif pMove == "p":
			print(pName + " picked Paper")
			if cMove == "rock":
				print("Computer picks Rock")
				print("Paper covers Rock")
				pScore += 1
			elif cMove == "paper":
				print("Computer picks Paper")
				print("Tie")
				ties += 1
			else:
				print("Computer picks Scissors")
				print("Scissors cut Paper")
				cScore += 1
		# player picks scissors
	elif pMove == "s":
			print(pName + " picked Scissors")
			if cMove == "rock":
				print("Computer picks Rock")
				print("Rock breaks Scissors")
				cScore += 1
			elif cMove == "paper":
				print("Computer picks Paper")
				print("Scissors cut Paper")
				pScore += 1
			else:
				print("Computer picks Scissors")
				print("Tie")
				ties += 1
	# check if pMove is valid
	else:
			print("That is not an option")