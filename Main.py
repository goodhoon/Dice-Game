"""
Author: KHP
"""


import random

#----------------------------------------------------------
# 6 functions which print information to the 
# standard output window.  
#----------------------------------------------------------
def display_welcome():
	print()
	print("Welcome to DICEY, written by Kyung Hoon Park")
	print()
	
def display_turn_info(player_name):
	print("  " + player_name + "'s turn")
	
def display_dice(list_of_dice):
	print("    " + "Dice:  ", end=" ")
	for num in list_of_dice:
		print(num, end=" ")
	print()
	
def display_exactly_two_matches_message(dice_number):
	print("    " + "Two ", dice_number, "'s." + "  " + "Roll the remaining 3 dice.")
	
def display_round_results(round_number, player1_name, player1_score, player2_name, player2_score):
	print("Round", round_number, "results: ", player1_name, "has", player1_score, "points, and", player2_name, "has", player2_score, "points")
	print()

def display_final_results(player1_name, player1_score, player2_name, player2_score):
	star = "*"
	tie_message = "The result is a tie"
	win_message = "Congratulations to"
	string_player1 = str(player1_name)
	string_player2 = str(player2_name)
	if player1_score > player2_score:
		line_star = star * (len(win_message) + len(string_player1) + 1)
		print()
		print(line_star)
		print(win_message, player1_name)
		print(line_star)
		print()
	elif player1_score < player2_score:
		line_star = star * (len(win_message) + len(string_player2) + 1)
		print()
		print(line_star)
		print(win_message, player2_name)
		print(line_star)
		print()
	else:
		line_star = star * len(tie_message)
		print()
		print(line_star)
		print(tie_message)
		print(line_star)
		print()
		
#----------------------------------------------------------
# 3 functions which obtain the maximum number of matches and
# the dice number if there are exactly two matches
#----------------------------------------------------------
def get_how_many_match(value_to_match, list_of_dice):
	count = 0
	for num in list_of_dice:
		if num == value_to_match:
			count += 1
	return count
	
def get_dice_number_with_two_matches(list_of_dice):
	for num in range(1, 7):
		if get_how_many_match(num, list_of_dice) == 2:
			return num

def get_max_number_of_matches(list_of_dice):
	list = []
	for num in range(1,7):
		list = list + [get_how_many_match(num, list_of_dice)]
	max_count = max(list)
	return max_count
	
#----------------------------------------------------------
# 3 functions which process a player's turn.
#----------------------------------------------------------
def get_list_of_dice_rolls(number_of_rolls):
	dice_list = []
	for i in range(number_of_rolls):
		dice_list += [random.randrange(1, 7)]
	return dice_list

def get_score(list_of_dice):
	if get_max_number_of_matches(list_of_dice) == 0 or get_max_number_of_matches(list_of_dice) == 1 or get_max_number_of_matches(list_of_dice) == 2:
		return 0
	elif get_max_number_of_matches(list_of_dice) == 3:
		return 3
	elif get_max_number_of_matches(list_of_dice) == 4:
		return 4
	elif get_max_number_of_matches(list_of_dice) == 5:
		return 5

def process_player_turn(player_name):
	display_turn_info(player_name)
	list_five_rolls = get_list_of_dice_rolls(5)
	display_dice(list_five_rolls)
	if get_max_number_of_matches(list_five_rolls) == 2:
		num = get_dice_number_with_two_matches(list_five_rolls)
		new_list = [num] + [num]
		display_exactly_two_matches_message(get_dice_number_with_two_matches(list_five_rolls))
		another_list = get_list_of_dice_rolls(3)
		new_list = new_list + another_list
		display_dice(new_list)
		return get_score(new_list)
	else:
		return get_score(list_five_rolls)

#----------------------------------------------------------
# main function
#----------------------------------------------------------
def main():

	display_welcome()
	
	round_number = 1
	player1_total_score = 0
	player2_total_score = 0
	player1_name = "Popeye"
	player2_name = "Bluto"
	
	for i in range(3):
		player1_score = process_player_turn(player1_name)
		player2_score = process_player_turn(player2_name)
		display_round_results(round_number, player1_name, player1_score, player2_name, player2_score)
		round_number += 1
		player1_total_score += player1_score
		player2_total_score += player2_score

	display_final_results(player1_name, player1_total_score, player2_name, player2_total_score)
	
main()