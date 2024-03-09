
import sqlite3
database=sqlite3.connect("app,py")
cr=database.cursor()



def edit():
    while True:
        uid = int(input("Enter student's ID to edit their information:\n"))
        choose_Data = int(input("Write the type of data you want to edit:\nID => 1\nName => 2\nPassword => 3\nLevel => 4\nGPA => 5\n"))
        if choose_Data == 1:
            Data = "ID"
        elif choose_Data == 2:
            Data = "Name"
        elif choose_Data == 3:
            Data = "password"
        elif choose_Data == 4:
            Data = "level"
        elif choose_Data == 5:
            Data = "GPA"
        else:
            print("ERROR")
            break
        new_info = input(f"Write the new {Data} to update it: ")

        try:
            cr.execute(f"UPDATE students_info SET {Data} = '{new_info}' WHERE ID = '{uid}'")
            database.commit()
            print("Update successful!")


        finally:
            # Close cursor and database connection


