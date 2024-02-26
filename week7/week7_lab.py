# Idrees M Abdurrazzak
# SE126.10 Intermediate Prog Using Python
# 02/21/2024

#prompt: 

#variable dictionary:



#------------ MAIN CODE -------------------
import csv

#create lists
stud_id = [] #binary
lname = []
fname = []
class1 = [] #sequential for classes
class2 = []
class3 = []
found = [] #sequential list
records = 0




with open ("week7/w7_demoFile.txt") as csvfile:
    for rec in csv.reader(csvfile):
        records += 1
        stud_id.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

#--------- DISPLAY FUNCTION -------------------        
def menu():
    print("\n")
    print("\t1. See All Student Report")
    print("\t2. Search for a Student [ID]")
    print("\t3. Search for a Student] [Last]")
    print("\t4. View Class Roster")
    print("\t5. Exit/Quit Program\n")
    choice = int(input("\n\tPlease enter your selection: "))

    while choice < 0 or choice > 5:

        choice = int(input("\n\tPlease enter your selection: "))
        print("**ERROR**ERROR**")

    return choice

menu_choice = None
while menu_choice != "5":
    menu_choice = menu()

    if menu_choice == 1:
        print(f"\n{'STUDENT ID':15} {'LAST':30} {'FIRST':30} {'CLASS1':8}{'CLASS2':8} {'CLASS3':8}")

        print("----------------------------------------------------------------------------------------------------------")
        for i in range(0, len(stud_id)):#outter loop
            print(f"{stud_id[i]:8}\t{lname[i]:30} {fname[i]:30} {class1[i]:8} {class2[i]:8} {class3[i]:8}")
        print("----------------------------------------------------------------------------------------------------------")


