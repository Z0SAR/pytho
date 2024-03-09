# A game played by two players by adding numbers from 1 to 10. The first player who reaches 100 wins.

# Initialize the sum variable for adding
sum = 0

# Show players how the game works
print("Welcome to the 100 Game!")
print("Two players will add numbers from 1 to 10. The first player who reaches 100 wins.")

# Game loop
while sum < 100:
    # Player 1's turn
    num1 = int(input("Player 1, enter your number from 1 to 10: "))
    while num1 < 1 or num1 > 10:
        num1 = int(input("Please enter a number from 1 to 10: "))
    sum += num1
    print (sum)
    if sum >= 100:
        print("Player 1 wins!")
        break

    # Player 2's turn
    num2 = int(input("Player 2, enter your number from 1 to 10: "))
    while num2 < 1 or num2 > 10:
        num2 = int(input("Please enter a number from 1 to 10: "))
    sum += num2
    print(sum)
    if sum >= 100:
        print("Player 2 wins!")
        break

