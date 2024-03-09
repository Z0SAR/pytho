# # 100 game
# # purpose: A game played by twe players by adding number from 1 to 10 the first player who reaches 100 is winner
# # Author : zeyad elsayed mamhoud yousef
# ID : 20230153
result = 0
# then shew to players how the game works
print(
    " welcome on 100 Game!!\ntwo players will add number from 1 to 10 and the first player who reaches 100 wins\nif you insert number make the result bigger 100 you lost your trying\nif you enter anything another number the will end  \nGood luck!!")
while True:
    try:
        while result < 100:
            # player1's turn
            num1 = int(input("player 1:\nenter your number please \n "))
            # check if the number is between 1 and 10
            while num1 < 1 or num1 > 10:
                num1 = int(input("please enter you number from 1 to 10\n"))
            # check if the sum is bigger than 100 I will make the player choose auther smaller number
            if (num1 + result) > 100:
                print(f"you lost you trying because the result ={num1 + result}")
            # check if player 1 won
            elif num1 + result == 100:
                print("player 1 won!!")
                result = 100
                continue
            else:
                result += num1
                print(f"the result ={result}")
            # player2's turn
            num2 = int(input("player2:\nenter your number\n"))
            # check if the number is between 1 and 10
            while num2 < 1 or num2 > 10:
                num2 = int(input("please enter you number from 1 to 10\n"))
                # check if the sum is bigger than 100 is will make the player choose other smaller number
            if (num2 + result) > 100:
                print(f"you lost you trying because the result ={num2 + result}")
            # check if payer 2 won
            elif num2 + result == 100:
                print("player2 won!!")
                result = 100
                continue
            else:
                result += num2
                print(f"the result = {result}")
    except:
        print("the game is ended because you did not enter number")
    finally:
        # ask the player to play again or exit
        ask = (input("are you want to play again \n"
                     "press (A) to play again \n"
                     "press (B) to exist ")).lower()

        if ask == "a":
            result = 0
        elif ask == "b":
            print("thanks for playing")
            break
        else:
            print("invalid"
                  "\nenter A or B")
            result = 100
# import ascii
