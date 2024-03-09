# Function to Subtract a Square Game
def subtract_a_square():
    print("Welcome to ** Subtract a Square Game **")
# Function to check if the input is integer or no
    def take_only_an_integer():
        while True:
            try:
                num_of_coins = input("Enter the number of coins that the players will be using:\n")

                int_value = int(num_of_coins)

                break
            except ValueError:
                print(""""Invalid" Please enter an integer""")

        return int_value

    num_of_coins = take_only_an_integer()
    a = num_of_coins
    while num_of_coins > 0:

        while True:
#when player 2 is win print
            if num_of_coins == 0:
                print("Player 2 is win")
                break
# Function to check if the input is integer or no

            def take_only_an_integer():
                while True:
                    try:
                        # The first player’s turn
                        num2 = input("Player 1:Enter the number you want to remove:\n")

                        int_value = int(num2)

                        break
                    except ValueError:
                        print(""""Invalid" Please enter an integer""")

                return int_value

            num2 = take_only_an_integer()
# Function to check if the number has a root or no

            def check_number_root():

                if num2 < 0:
                    return False
                root = int(num2 ** 0.5)
                return root * root == num2
            if check_number_root():
                num_of_coins = num_of_coins - num2
                while True:
                    if num_of_coins > 0:
                        print("The remaining coins is:", num_of_coins)

                    elif num_of_coins < 0:
                        print(""""Invalid" The number you entered cannot be subtracted from the remainder""")
                        num2 = int(input("Player1:Enter a valid number:\n"))
                        if check_number_root():
                            num_of_coins = a - num2
                        else:
                            print("Please always removing a square number of coins")
                        continue
                    break
            else:
                print("Please always removing square number of coins")
                continue
            break
# When player 1 is win print
        if num_of_coins == 0:
            print("Player 1 is win")
            break
        b = num_of_coins
        while True:
            # Function to check if the input is integer or no

            def take_only_an_integer():
                while True:
                    try:
                        # The second player’s turn
                        num3 = input("Player 2:Enter the number of coins you want to remove:\n")

                        int_value = int(num3)

                        break
                    except ValueError:
                        print(""""Invalid" Please enter an integer""")

                return int_value

            num3 = take_only_an_integer()
# Function to check if the number has a root or no

            def check_number_root():

                if num3 < 0:
                    return False

                root = int(num3 ** 0.5)
                return root * root == num3
            if check_number_root():
                num_of_coins = num_of_coins - num3
                while True:
                    if num_of_coins > 0:

                        print("The remaining coins is:", num_of_coins)

                    elif num_of_coins < 0:
                        print(""""Invalid" The number you entered cannot be subtracted from the remainder""")
                        num3 = int(input("Player2:Enter a valid number:\n"))
                        if check_number_root():
                            num_of_coins = b - num3
                        else:
                            print("Please always removing a square number of coins")

                        continue
                    break

            else:
                print("Please always removing square number of coins")
                continue
            break

# The  main menu that will appear to the user
while True:
    print("A)Insert a Game\nB)Exit Game")
    choice1 = str(input("Please enter your choice(A/B):\n")).upper()
    if choice1 == "A":
        subtract_a_square()
        print("Do you want to play again")
    elif choice1 == "B":
        print("** Exit Program **")
        break
    else:
        print("*Please enter a valid choice*")
