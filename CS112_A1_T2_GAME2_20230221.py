"""
game_scrabble
purpose : the player who gets the number 15 first is the winner
Author: Abdelrahman yasser awes
ID: 20230221
"""
# message welcome
print("welcome")
print("==============")
# instruction
print("instruction")
print("1)played by only two people")
print("2)whoever can get number 15 first is the winner")
print("3)you can take numbers that fall between (1,9)")
print("4)the number cannot be taken more than once")
print("==============")
print("Good luck\n==============\nstart ")
# make lists for 2 player and numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_one_choice = []
player_two_choice = []
while True:
    try:
     print("The  available choices :", numbers)
# take a number form user one
     choice = int(input("player1: enter the choice number "))
# make sure the number is on the list
     if choice in numbers:
        player_one_choice.append(choice)
# delete choice number form the list
        numbers.remove(choice)
        print("list of player one is :", player_one_choice)
        print("list of player two is :", player_two_choice)
# checking the winning statue of the first player
        if len(player_one_choice) == 3:
           if sum(player_one_choice) == 15:
               print(" =====player1 is win===== ")
               break
        elif len(player_one_choice)==4:
           if (sum(player_one_choice[-3:]) == 15 or sum(player_one_choice[0:3]) == 15):
               print(" =====player1 is win===== ")
               break
           elif (player_one_choice[0] + player_one_choice[2] + player_one_choice[3] == 15):
               print("=====player1 is win====")
               break
           elif (player_one_choice[0] + player_one_choice[1] + player_one_choice[3] == 15):
               print(" ====player1 is win==== ")
               break
        elif len(player_one_choice) == 5:
           if (sum(player_one_choice[-3:]) == 15 or sum(player_one_choice[0:3]) == 15):
               print(" ====player1 is win==== ")
               break
           elif (player_one_choice[0] + player_one_choice[1] + player_one_choice[3] == 15 or player_one_choice[0] + player_one_choice[1] + player_one_choice[4] == 15 ):
               print(" ====player1 is win==== ")
               break
           elif (player_one_choice[0] + player_one_choice[2] + player_one_choice[3] == 15 or player_one_choice[0] + player_one_choice[3] + player_one_choice[4] == 15 ):
               print(" ====player1 is win==== ")
               break
           elif (player_one_choice[1] + player_one_choice[2] + player_one_choice[3] == 15 or player_one_choice[1] + player_one_choice[2] + player_one_choice[4] == 15 ):
               print(" ====player1 is win==== ")
               break
           elif (player_one_choice[0] + player_one_choice[2] + player_one_choice[4] == 15 or player_one_choice[1] + player_one_choice[3] + player_one_choice[4] == 15 ):
               print(" ====player1 is win==== ")
               break
# if the first player enters a number that is not on the list
     else:
        print("invalid number")
        continue
# check the tie condition
     if len(player_one_choice) == 5:
        print(" ====the first and second player are tied==== ")
        break
     print("The  available choices :", numbers)
# take a number form user two
     choice = int(input("player2: enter the choice number "))
# make sure the number is on the list
     if choice in numbers:
       player_two_choice.append(choice)
# delete choice number form the list
       numbers.remove(choice)
       print ( "list of player two is :" ,player_two_choice)
       print ( "list of player one is :" ,player_one_choice)
# checking the winning statue of the second player
       if len(player_two_choice) == 3:
          if sum(player_two_choice) == 15:
              print(" ====player2 is win==== ")
              break
       elif len(player_two_choice)==4:
          if (sum(player_two_choice[-3:]) == 15 or sum(player_two_choice[0:3]) == 15):
              print(" ====player2 is win==== ")
              break
          elif (player_two_choice[0] + player_two_choice[2] + player_two_choice[3] == 15):
              print(" ====player2 is win==== ")
              break
          elif (player_two_choice[0] + player_two_choice[1] + player_two_choice[3] == 15):
              print(" ====player2 is win==== ")
              break
# if the second player enters a number that is not on the list
     else:
        print("invalid number")
        print("The choices :", numbers)
        choice = int(input("player2: enter the choice number "))
        if choice in numbers:
           player_two_choice.append(choice)
           numbers.remove(choice)
           print("list of player two is :", player_two_choice)
           print("list of player one is :", player_one_choice)
           if len(player_two_choice) == 3:
               if sum(player_two_choice) == 15:
                   print(" ====player 2 is win==== ")
                   break
           elif len(player_two_choice) == 4:
               if (sum(player_two_choice[-3:]) == 15 or sum(player_two_choice[0:3]) == 15):
                   print(" ====player2 is win==== ")
                   break
               elif (player_two_choice[0] + player_two_choice[2] + player_two_choice[3] == 15):

                   print(" ====player2 is win==== ")
                   break
               elif (player_two_choice[0] + player_two_choice[1] + player_two_choice[3] == 15):
                   print(" ====player2 is win==== ")
                   break
        else:
            print("invalid number")
            print("The  available choices :", numbers)
            choice = int(input("player2: enter the choice number "))
            if choice in numbers:
                player_two_choice.append(choice)
                numbers.remove(choice)
                print("list of player two is :", player_two_choice)
                print("list of player one is :", player_one_choice)
                if len(player_two_choice) == 3:
                    if sum(player_two_choice) == 15:
                        print(" ====player2 is win==== ")
                        break
                elif len(player_two_choice) == 4:
                    if (sum(player_two_choice[-3:]) == 15 or sum(player_two_choice[0:3]) == 15):
                        print(" ====player2 is win==== ")
                        break
                    elif (player_two_choice[0] + player_two_choice[2] + player_two_choice[3] == 15):
                        print(" ====player2 is win==== ")
                        break
                    elif (player_two_choice[0] + player_two_choice[1] + player_two_choice[3] == 15):
                        print(" ====player2 is win==== ")
                        break
# if you do not enter a number
    except ValueError:
         print ("the game is over because you did not enter a number ")
         break
print("Game end ")






















