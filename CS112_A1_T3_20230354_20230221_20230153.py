#/ Program: Description of the program
#/ Authors: Author one and what problems s/he solved
#/ Author 2 and what problems s/he solved
#/ Author 3 and what problems s/he solved
#/ Version: Number of program version
#/ Date: Date of creating it

def calculate_grade():
    print("Welcome in Calculate grade mode!")
    print()
    while True:
        try:
            grade = int(input("Enter your grade: "))
            # check the grade
            if (grade >= 0) and (grade <= 100):
                if grade >= 90:
                    print("the grade is A+.")
                elif (grade < 90) and (grade >= 85):
                    print("the grade is A.")
                elif (grade < 85) and (grade >= 80):
                    print("the grade is B+.")
                elif (grade < 80) and (grade >= 75):
                    print("the grade is B.")
                elif (grade < 75) and (grade >= 70):
                    print("the grade is C+.")
                elif (grade < 70) and (grade >= 65):
                    print("the grade is C.")
                elif (grade < 65) and (grade >= 60):
                    print("the grade is D+.")
                elif (grade < 60) and (grade >= 50):
                    print("the grade is D.")
                else:
                    print("the grade is F,")
                    print()
            else:
                print("Please enter the grade from 0 to 100.")
                print()
                continue
            # check if you want to calculate the another grade
            again = input("0. Do you this program again? : " )
            print()
            if again.lower() != '0':

                break

        except ValueError:
            print("please enter the grade from 0 to 100.")
            continue


            calculate_grade()


def check_Armstrong():
    print("Welcome in Armstrong number mode!")
    print()
    try:
        while True:
            Armstrong = 0
            num = int(input("Enter a positive number to check if it is an Armstrong number or not: "))
            while num <= 0:
                num = int(input("Enter a positive number: "))
            num = str(num)
            len_num = len(str(num))
            for i in range(len_num):
                Armstrong += int(num[i])**len_num
            if Armstrong == int(num):
                print(f"Number {num} is an Armstrong number.")
                print()
            else:
                print(f"Number {num} is not an Armstrong number.")
                print()
            again = input("0. Do you this program again? : ")
            print()
            if again.lower() != '0':
                break

    except ValueError:
        print("Invalid input. Please enter a positive integer.")

        check_Armstrong()




def calculate_pi():
     print("Welcome in Calculate PI value mode!")
     print()
     while True:
         try:
             terms = int(input("Enter term to calculate approximately PI value: "))
             while terms <= 0 :
                 terms = int(input("Please enter positive Term: "))

             term_sum = 0
             for i in range (terms):
                 term = (-1) ** i / (2 * i + 1)
                 term_sum = term_sum + term
                 pi = term_sum * 4
             print(f"The value for pi on {terms} term approximately = {pi}")
             print()
         except ValueError:
             print("Invalid input. Please enter a positive integer.")
         again = input("0. Do you this program again? : ")
         print()
         if again.lower() != '0':
             break

             calculate_pi()




def Encryption_texts():
    print("Welcome in Encryption Text mode!")
    print()
    # list containing all letters,whether small or capital,except for Z
    character_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u"]
    character_1_1 = ["v", "w", "x", "y", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
    character_1_2 = ["Q", "R", "S", "T", "U", "V", "W", "X", "Y"]
    while True:
        before_encryption = input("Enter anything you want to encrypt: ")
        after_encryption = ""
        for i in before_encryption:
            # check the digit if it is a space
            if i == " ":
                after_encryption = after_encryption + " "
            # check the digit if the letter Z is converted to the letter A
            elif i == "Z":
                after_encryption = after_encryption + "A"
            # check the digit if the letter z is converted to the letter a
            elif i == "z":
                after_encryption = after_encryption + "a"
            # check the digit if it is present in the lists that will be encrypted
            elif i in character_1 or i in character_1_1 or i in character_1_2:
                ASCII_Value_number = ord(i)
                New_ASCII_Value_number = ASCII_Value_number+1
                ASCII_Value_char = chr(New_ASCII_Value_number)
                after_encryption = after_encryption + ASCII_Value_char
            # otherwise it remains as it is
            else:
                anther = i
                after_encryption = after_encryption + anther
        print("after_encryption::", after_encryption)
        print()
        # check if you want to use the program again or not

        again = input("0. Do you this program again? :")
        print()
        if again.lower() != '0':
            break

            Encryption_texts()




def check_list() :
    print("Welcome in Compare between Two lists mode!")
    print()
    while True:
            list_1=[]
            list_2=[]
            while True:
                num1=input( "Enter a number to add to the first list or click on anything except numbers to go to the second list: ")
                try:
                    num1=int(num1)
                    list_1.append(num1)

                except:
                    print("Now move to the second list.")
                    break
                finally:
                    for i in range(len(list_1)):
                       for n in range(0,len(list_1)-i-1):
                          if list_1[n]>=list_1[n+1]:
                             list_1[n],list_1[n+1]=list_1[n+1],list_1[n]
                    print("______________________")
            while True:
                num2=input("Enter a number for the second list and click on anything except numbers to go to checking if the two list are equal or not: ")
                print()
                try:
                    num2=int(num2)
                    list_2.append(num2)
                #print(list_2)
                    print("_______________________")
                except:
                     break
                finally:
                    for i in range(len(list_2)):
                       for n in range(0,len(list_2)-i-1):
                          if list_2[n]>=list_2[n+1]:
                             list_2[n],list_2[n+1]=list_2[n+1],list_2[n]
            if len(list_1)==len(list_2):
               if list_1==list_2:
                  print(f"the element for the first list ==> {list_1}")
                  print(f"the element for the second list==> {list_2}")
                  print(f"Lists are equal = {(list_1)==(list_2)}")
               else:
                  print(f"the element for the first list ==> {list_1}")
                  print(f"the element for the second list==> {list_2}")
                  print(f"Lists are equal = {(list_1)==(list_2)}")
                  print()
            else:
               print(f"the element for the first list ==>{list_1}")
               print(f"the element for the second list==> {list_2}")
               print(f"Lists are equal = {(list_1)==(list_2)}")
               print()
            again = input("0. Do you this program again? : ")
            print()
            if again.lower() != '0':
                break

                check_list()


def get_factors(number):

        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        return factors


def factors_program():
    print("Welcome in Number Factors mode!")
    print()
    while True:
        try:
            number = int(input("Please Enter Positive Number: "))
            if number <= 0:
                print("Invalid Number . Please Enter Positive Number")
                return factors_program()
            else:
                factors = get_factors(number)
                print(f"Factors for {number} are: {factors}")
                print()
        except ValueError:
            print("Invalid Number . Please Enter Positive Number")
            print()
        again = input("0. Do you want Factors for other Number? : ")
        print()
        if again.lower() != '0':

            break

            factors_program()



def mainmenu():
    # Function to display the main menu and start the game
    print("Welcome in our Program")
    print()
    print("This Program helps the user to select Mode from 6")
    print("1. Mode(1): CalCulate Grade:- This mode print grade for user")
    print("2. Mode(2): Armstrong Number:-")
    print("3. Mode(3): Pi Calculate:- This mode calculate approximately for pi")
    print("4. Mode(4): Encryption:- This mode print fact value for letters ")
    print("5. Mode(5): Check Equal Lists:- This mode compare between two lists")
    print("6. Mode(6): Nubmer Factors:- This mode print the factors for the input number from user")
    print()
    while True:
        print("1. Mode(1): CalCulate Grade.")
        print("2. Mode(2): Armstrong Number")
        print("3. Mode(3): Pi Calculate")
        print("4. Mode(4): Encryption")
        print("5. Mode(5): Check Equal Lists")
        print("6. Mode(6): Nubmer Factors")
        print("7. Exit")
        try:
            selection = int(input("Enter Number to Select Mode: "))
            print()
            if selection == 1:
                calculate_grade()
            elif selection == 2:
                check_Armstrong()
            elif selection == 3:
                calculate_pi()
            elif selection == 4:
                Encryption_texts()
            elif selection == 5:
                check_list()
            elif selection == 6:
                factors_program()
            elif selection == 7:
                print("Exiting Program. Goodbye!")
                break
            else:
                print("Invalid Choice. Enter 1-7")
                print()
        except ValueError:
            print("Invalid Choice. Enter 1-7")
            print()
        program_again = input("1. Do you want back to menu? : ")
        print()
        if program_again.lower() != '1':
            print("Exiting Program. Goodbye!")
            break
if __name__ == "__main__":
    mainmenu()
