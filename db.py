"""# Author : zeyad elsayed mamhoud yousef
# ID : 20230153

def check_Armstrong():
    try:
        Armstrong=0
        num=int(input("enter a positive number to check if is an Armstrong number or not :\n"))
        while num<=0:
            num=int(input("enter a positive number :\n"))
        num=str(num)
        len_num=len(str(num))
        for i in range(len_num):
            Armstrong+=int(num[i])**len_num
        if Armstrong==int(num):
            print(f"number {num} is Armstrong number .")
        else :
            print(f"number {num} is not Armstrong number .")
    except:
        print("invalid!!")
print(check_Armstrong())
"""
