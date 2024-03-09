sum=0
# then shew to players how the game works
print (" welcome on 100 Game!!\ntwo players will add number from 1 to 10 and the first player who reaches 100 wins\nif you insert number make the result bigger 100 you lost your trying\nif you enter anything another number the will end  \nGood luck!!")
while True:
  try:
    while sum<100:

        # player1's turn
        num1=int (input("player 1:\nenter your number please \n "))
        # check if the number is between 1 and 10
        while num1 < 1 or num1 > 10:
           num1=int(input("please enter you number from 1 to 10\n"))
# check if the sumtion is bigger than 100 i will make the player choose aouther smaller number
        if (num1+sum)>100:
            print (f"you lost you trying because the result ={num1+sum}")
#check if playr 1 won
        elif num1+sum==100:
            print("player 1 won!!")
            sum=100
            continue
        else:
            sum+=num1
            print (f"the result ={sum}")
        #player2's turn
        num2=int(input("player2:\nenter your number\n"))
         # check if the number is between 1 and 10
        while num2<1 or num2>10:
          num2=int (input("please enter you number from 1 to 10\n"))
          # check if the sumtion is bigger than 100 is will make the player choose aouther smaller number
        if (num2+sum)>100:
          print (f"you lost you trying because the result ={num2+sum}")
        #check if payer 2 won
        elif num2+sum==100:
          print ("player2 wins!!")
          sum=100
          continue

        else:
            sum+=num2
            print(f"the result = {sum}")
  except:
   print("the game is ended because you did not enter number" )
  finally:
   #ask the player to play again or exit
    ask=(input("are you want to play again \n"
                 "press (A) to play again \n"
                 "press (B) to exist ")).lower()

    if ask=="a":
            sum=0
    elif ask=="b":
            print ("thanks for playing")
            break
    else:
        sum=100

