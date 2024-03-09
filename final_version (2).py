# 100 game
# Purpose: A game played by two players by adding numbers from 1 to 10. The first player who reaches 100 wins.
# Author: Zeyad Elsayed Mahmoud Yousef
# ID: 20230153

# Firstly, create an integer variable for keeping track of the sum.
sum = 0

# Then, show the players how the game works.
print("Welcome to the 100 Game!\nTwo players will add numbers from 1 to 10, and the first player who reaches 100 wins.")

# Loop until the sum reaches 100.
while sum < 100:
    # Player 1's turn
    num1 = int(input("Player 1:\nEnter your number, please: "))

    # Check if the number is between 1 and 10.
    while num1 < 1 or num1 > 10:
        num1 = int(input("Please enter a number from 1 to 10: "))

    # Check if the sum plus the chosen number exceeds 100. If so, prompt the player to choose a smaller number.
    if ( sum + num1 )>100:
        print(f"you lost your trying because the result ={num1+sum } ")


    # Check if player 1 has won.
    sum +=num1
    print(f"the result = {sum}")
    if sum == 100:
        print("Player 1 wins!")
        break
    else:
        # Player 2's turn
        num2 = int(input("Player 2:\nEnter your number: "))

        # Check if the number is between 1 and 10.
        while num2 < 1 or num2 > 10:
            num2 = int(input("Please enter a number from 1 to 10: "))

        # Check if the sum plus the chosen number exceeds 100. If so, prompt the player to choose a smaller number.
    if (num2+sum>100):
      print (f"you lost your trying because the result = {num2+sum}")
      #Update the sum.
    sum += num2
    print(f"The result of the summation = {sum}")

        # Check if player 2 has won.
    if sum == 100:
        print("Player 2 wins!")
        break
