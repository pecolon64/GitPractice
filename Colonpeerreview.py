# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for playing")
		
#line 4 update name
#line 5 update date
#line 19 indention error (cave = '')
#line 24 "return caves" instead of "return cave"
#line 32 time.sleep(3) instead of time.sleep(2)
#line 42 print 'Gobbles you down in one bite!' instead of print('Gobbles you down in one bite!')
#line 45 while playAgain = 'yes' or playAgain = 'y': instead of while playAgain == 'yes' or playAgain == 'y':
#line 45 while playAgain = 'yes' or playAgain = 'y': instead of while playAgain == 'yes' or playAgain == 'y':
#line 47 choosecave is lowercase instead of camel case (chooseCave)
#line 53 print("Thanks for planing") instead of print("Thanks for playing")
