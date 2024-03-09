#Subtracting Squares Game
#purpose: A game played by two players by choose square number to remove it The player who removes the last coin wins.
# Author : Mohamed Mahmoud Abdelbasset Mohamed
#ID : 20230354

import random
print("Welcome on Subtracting Squares Game")
print("Please Choose Game Mode")

def get_valid_moves(coins):
    return [i ** 2 for i in range(1, int(coins ** 0.5) + 1)] #this function to get Square number

def human_choice(): # this function to take number of coin from human
    coins = int(input("Enter the Number of Coins in the Pile: "))
    play_game_human_choice(coins)

def random_choice(): # this function to take random number of coins from 1 to 100
    play_game_random_choice()


def play_game_human_choice(coins): # this function contain the game for human choice
    player_turn = 1
    while coins > 0:
        print(f"Coins Left: {coins}") # check number of coins left after removing
        if player_turn == 1:
            player_name = "Player 1"
        else:
            player_name = "Player 2"

        print(f"{player_name}'s turn:") # it clarifies a turn in the game

        valid_moves = get_valid_moves(coins)
        print(f"Valid moves: {valid_moves}") # to print the valid number to help the player

        move = int(input(f"Enter a Square Number of Coins to Remove ({player_name}): "))
        if move not in valid_moves:
            print("Invalid move") # to show that there is a mistake in the number
            continue

        coins -= move
        print(f"{player_name} removes {move} coins.") # to clarify the number player want remove
        print()

        if coins == 0:
            print(f"{player_name} wins!") # to print the player who wins the game
            break

        player_turn = 2 if player_turn == 1 else 1


def play_game_random_choice(): # function game for Random number
    coins = random.randint(1, 100)  # Random the number of coins in the pile between 1 and 100
    print(f"the Number of Coins in the Pile: {coins}")

    player_turn = 1
    while coins > 0:
        print(f"Coins Left: {coins}") # check number of coins left after removing
        print(f"Player {player_turn}'s turn:") # to print the player who wins the game
        valid_moves = get_valid_moves(coins)
        print(f"Valid moves: {valid_moves}") # to print the valid number to help the player

        if player_turn == 1:
            player_name = "Player 1"
        else:
            player_name = "Player 2"
        move = int(input(f"Enter a Square Number of Coins to Remove ({player_name})"))
        if move not in valid_moves:
            print("Invalid move")  # to print the valid number to help the player
            continue

        coins -= move
        print(f"Player {player_turn} removes {move} coins.")
        print()

        if coins == 0:
            print(f"Player {player_turn} wins!")
            break

        player_turn = 2 if player_turn == 1 else 1



def mainmenu(): # this function for menu
    print("1. Human Choice")
    print("2. Random Choice")
    while True:
        try:
            selection = int(input("Enter Choice: "))
            if selection == 1:
                human_choice() # to return for human game
                break
            elif selection == 2:
                random_choice() # to return for random game
                break
            else:
                print("Invalid Choice. Enter 1-2") # the choice has error
        except ValueError:
            print("Invalid Choice. Enter 1-2") # the choise not string it's integer
    exit()

if __name__ == "__main__":
    mainmenu()
