# creat tree lists one to show avilable numbers and two list  for players
list_player1=[]
list_player2=[]
nums=[1,2,3,4,5,6,7,8,9]
print("welcome in Number scrabble!!\n")
print("played with the list of numbers between 1 and 9.\n Each player takes turns picking a number  from the list. \nyou con select each number just one time \nif you select a number between 1 and 9 and it already selected before you will lose trying  ")
while True :

    player1_choic=int(input(f"player 1:\nselect from {nums})\n"))
    if player1_choic in nums:

        list_player1.append(player1_choic)
        nums.remove(player1_choic)
        print(f"numbers of player 1 {list_player1}")
    else:
        print("you lost your trying!!")

    if sum(list_player1)==15 and len(list_player1>=3):
        print("player1 wins !!")
        break
    player2_choic=int(input(f"player 2:\nselect from {nums})\n"))
    if player2_choic in nums:
        list_player2.append(player2_choic)
        nums.remove(player2_choic)
        print(f"numbers of player 2 {list_player2}")
    else:
        print("you lost your trying!!")

    if sum(list_player2)==15 and len(list_player2>=3):
        print("player2 wins !!")
        break

