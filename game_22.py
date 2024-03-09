all=[( 1, 5, 9),(1, 6, 8),(2, 4, 9),(2, 5, 8),(2, 6, 7),(3, 4, 8),(3, 5, 7),(4, 5, 6)]
# creat tree lists one to show avilable numbers and two list  for players
list_player1=[]
list_player2=[]
nums=[1,2,3,4,5,6,7,8,9]
print("welcome in Number scrabble!!\n")
print("played with the list of numbers between 1 and 9.\n Each player takes turns picking a number  from the list. \nyou con select each number just one time \nif you select a number between 1 and 9 and it already selected before you will lose trying  ")
while True :
    num1=int(input(f"player 1!\nenter your number from {nums}:\n"))
    if num1 in nums:
        list_player1.append(num1)
        nums.remove(num1)
        print(nums)
    else:
        print("you lost your trying!!")
    if list_player1 in all:
        print ("player 1 wins!!")
        break
    if len(all)==0:
        print (" Draw !")
        break
    num2=int(input(f"player 2!\nenter your number from {nums}:\n"))
    if num2 in nums:
        list_player2.append(num2)
        nums.remove(num2)
        print(nums)
    else:
        print("you lost your trying!!")

    if list_player2 in all:
        print("player two wins")
        break
    if len(all)==0:
        print (" Draw !")
        break



