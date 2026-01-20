import random

print("""WELCOME TO  R   PPPP  X   
	   RRR  PPPP   O>>>						                              X """)
player_scores = 0
computer_scores = 0
winning_score = 3 #... Use this if you want to play a best of three or whatever number you want..

#while player_scores < 2 and computer_scores <2:
	while player_scores < winning_score and computer_scores < 2:
		print(f"Player score: {player_scores}, Computer score: {computer_scores}")

		player_1 = input("Player, make your move: ").lower()
		if player_1 = input("quit"):
			break
		rand_num = random.randint(0,2)
		if rand_num == 0:
			computer_move = "rock"
		elif rand_num == 1:
			computer_move = "paper"
		else:
			computer_move = "scissors"
		print(computer_move)

		if player_1 == "rock" and computer_move == "scissors":
			print(" SHOOT !!! \n player 1 scores")
			player_scores += 1
		elif player_1 == "paper" and computer_move == "scissors":
			print("DANG IT !!! \n computer_move scores")
			computer_scores += 1
		elif player_1 == "scissors" and computer_move == "scissors":
			print("SORRY !!! \n no one scores")
		elif player_1 == "rock" and computer_move == "rock":
			print("SHOOT !!! \n no one scores")
		elif player_1 == "rock" and computer_move == "paper":
			print("DANG IT !!! \n computer_move scores")
			computer_scores += 1
		elif player_1 == "paper" and computer_move == "rock":
			print("SORRY !!! \n player 1 scores")
			player_scores += 1
		elif player_1 == "paper" and computer_move == "paper":
			print("SORRY !!! \n no one scores")
		elif player_1 == "scissors" and computer_move == "rock":
			print("SORRY !!! \n computer_move scores")
			computer_scores += 1
		elif player_1 == "scissors" and computer_move == "paper":
			print("SORRY !!! \n player 1 scores")
			player_scores += 1
		else:
			print("Wrong choice !!!")

if player_scores > computer_scores:
	print("CONGRATS, YOU WON!")
elif player_scores == computer_scores:
	print("NO ONE WON :(")
else:
	print("SORRY, COMPUTER WON")
print(f"FINAL SCORES... Player: {player_scores}, Computer: {computer_scores}")

