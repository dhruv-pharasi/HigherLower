from game_data import data
from random import randint
from os import system

HIGHER_LOWER = """
  _    _ _       _               
 | |  | (_)     | |              
 | |__| |_  __ _| |__   ___ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__|
 | |  | | | (_| | | | |  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|   
 | |        __/ |                
 | |     __|___/    _____ _ __   
 | |    / _ \ \ /\ / / _ \ '__|  
 | |___| (_) \ V  V /  __/ |     
 |______\___/ \_/\_/ \___|_|                                                                    
"""

VS = """
 __      _______ 
 \ \    / / ____|
  \ \  / / (___  
   \ \/ / \___ \ 
    \  /  ____) |
     \/  |_____/             
"""


def generate_index(prev_index, current_index):
    '''Returns a unique index.'''
    idx = randint(0, len(data) - 1)

    # Ensures idx is different
    while idx == current_index or idx == prev_index:
        idx = randint(0, len(data) - 1)

    return idx


def give_sentence(index):
    '''Returns a sentence from data at index.'''
    dic = data[index]

    return f"{dic['name']}, a {dic['description']}, from {dic['country']}"


def correct_answer(user_ans, idx1, idx2):
    '''Returns True if correct answer, False otherwise.'''
    dic1 = data[idx1]
    dic2 = data[idx2]

    if user_ans == "A" and (dic1['follower_count'] > dic2['follower_count']):
        return True
    if user_ans == "B" and (dic2['follower_count'] > dic1['follower_count']):
        return True

    return False


def print_comparisons(idx1, idx2):
    '''Prints the comparison statements and VS ASCII art.'''

    # Print first comparison personality
    compare_a = f"\nCompare A: {give_sentence(idx1)}.\n"
    print(compare_a)

    # Print VS ASCII art
    print(VS)

    # Print second comparison personality
    against_b = f"\nAgainst B: {give_sentence(idx2)}.\n"
    print(against_b)


def game_loop():
    '''Runs the game.'''

    # Generate initial indices
    idx1 = randint(0, len(data) - 1)
    idx2 = generate_index(-1, idx1)
    current_score = 0

    # Clear terminal
    system("clear")

    # Print ASCII art and current score
    print(HIGHER_LOWER)
    print(f"Current score: {current_score}")

    # Print VS and comparison statements
    print_comparisons(idx1, idx2)

    # Take answer from user
    ans = input(f"\nWho has more Instagram followers? Type 'A' or 'B': ").upper()

    # Runs the game until answer is incorrect
    while correct_answer(ans, idx1, idx2):

        # Clear the console after every iteration
        system("clear")

        # Increment player score
        current_score += 1

        # Generate a new index that does not equal idx1 and idx2
        prev_index = idx1
        idx1 = idx2
        idx2 = generate_index(prev_index, idx1)

        # Print ASCII art and new current score
        print(HIGHER_LOWER)
        print(f"Correct! Current score: {current_score}")

        # Print VS and comparison statements
        print_comparisons(idx1, idx2)

        # Take answer from user
        ans = input(
            f"\nWho has more Instagram followers? Type 'A' or 'B': ").upper()

    # Clear the console
    system("clear")

    # Print ASCII art
    print(HIGHER_LOWER)

    # Print the final score
    print(f"\nWrong answer. Final score: {current_score}\n")

    # Play again?
    play_again = input(
        "Play again? Enter 'y' to play again, or any other character to exit.\n")

    if play_again == 'y':
        game_loop()


game_loop()
