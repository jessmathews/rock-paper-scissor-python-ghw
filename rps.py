import random
print("----------------------------------")
print(" Welcome to Rock, Paper, Scissors ")
print("----------------------------------")

choices = ['r','p','s']
print("Choose:")
print("r: Rock")
print("p: Paper")
print("s: Scissors")
print("q: Quit")
dict = {
	"r":"Rock",
	"p": "Paper",
	"s":"Scissors"
	}
player =0
comp=0
def print_score():
	print("-------Scoreboard-------")
	print("       You  |  Computer  ")
	print(f"\t{str(player)}  |  {str(comp)} ")
	print("------------------------")
	if player > comp:
		print("You win!!!")
	elif player < comp:
		print("Computer wins!!!")
	else:
		print("It's a tie!")

while True:
	player_choice = input("Your choice:").lower()

	if player_choice in choices or player_choice == 'q':
		bot_choice = random.choice(choices)
		if player_choice != 'q':
					print("Computer:"+dict[bot_choice])
		if player_choice == bot_choice:
			print("Tie!")
		elif player_choice == 'r' and bot_choice == 's':
			print("You win!")
			player+=1
		elif player_choice == 'p' and bot_choice == 'r':
			print("You win!")
			player+=1
		elif player_choice == 's' and bot_choice == 'p':
			print("You win!")
			player+=1
		elif player_choice == 'q':
			print_score()
			exit()
		else:
			print("Computer wins!")
			comp+=1
	else:
		print("Invalid option!")
