def check_list() :
    list_1=[]
    list_2=[]
    while True:
        num1=input( "Enter a number to add to the first list or click on anything except numbers to go to the second list\n")
        try:
            num1=int(num1)
            list_1.append(num1)

        except:
            print("now move to the second list ")
            break
        finally:
            for i in range(len(list_1)):
               for n in range(0,len(list_1)-i-1):
                  if list_1[n]>=list_1[n+1]:
                     list_1[n],list_1[n+1]=list_1[n+1],list_1[n]
            print("______________________")
    while True:
        num2=input("enter a number for the second list and click on anything except numbers to go to checking if the two list are equal or not\n")
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
    else:
       print(f"the element for the first list ==>{list_1}")
       print(f"the element for the second list==> {list_2}")
       print(f"Lists are equal = {(list_1)==(list_2)}")

print(check_list())
