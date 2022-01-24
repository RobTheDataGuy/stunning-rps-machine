'''
Begin code for rock, paper, scissors game
Author: Rob Pirdy
Date: 02/20/2020
'''

import random as rd
import time

#Begin defining the function
def r_p_s():
	player = True
	while player == True:
		p1_val = input("Rock, Paper, or Scissors? ")
		#def possible opponent outcomes as a list
		outcomes = ["Rock", "Paper", "Scissors"]
		shoot = outcomes[rd.randint(0,2)]
		
		#print what happens in the game
		display = ["Ready?", "Rock...", "Paper...", "Scissors...", "Shoot!"]
		for words in display:
			print(words)
			time.sleep(1)

		#print the outcome of player v computer
		time.sleep(.5)
		print(f"\n{p1_val} vs. {shoot}")

		#print the game results
		time.sleep(.5)
		if p1_val == shoot:
			print("\nIt's a draw! Play again.")
		elif p1_val == "Rock":
			if shoot == "Paper":
				print("\nCongrats, you win!")
			break
		elif p1_val == "Paper" and shoot != "Scissors":
			print("\nCongrats, you win!")
			break
		elif p1_val == "Scissors" and shoot != "Rock":
			print("\nCongrats, you win!")
			break
		else:
			print("\nYou lose!")
            
r_p_s()


