
def usernames():

	game_dict = {}
	user = input("Please username:")
	while user != "No":
		game_dict[user] = {'nam': {'ipt': [], 'emtiaz': []},
						 	'shahr': {'ipt': [], 'emtiaz': []},
						 	'ghaza': {'ipt': [], 'emtiaz': []},
						  	'rang': {'ipt': [], 'emtiaz': []}}
		user = input("Please username:")

	return game_dict

def check_validity(char, i):

	if i[0] != char:
		return False
	else:
		return True

def give_emtiaz(game_dict):

	pass

def play_round(char, game_dict):

	for user in game_dict.keys():
		for item in game_dict[user].keys():
			i = input(f" {user} plz enter {item}:")
			if check_validity(char, i):
				game_dict[user][item] = i
			else:
				game_dict[user][item] = "invalid"

	game_dict = give_emtiaz(game_dict)

	return game_dict

def play_game(game_dict):

	char = ""
	round_val = 0
	while char != "No":
		char = input("Please enter char: ")
		game_dict = play_round(char, game_dict)
		round_val += 1

	return game_dict

def main():

	# enter usernames
	game_dict = usernames()
	# play game
	game_dict = play_game(game_dict)
	# print results

if __name__ == "__main__":

	main()
