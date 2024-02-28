# Idrees M Abdurrazzak
# SE126.10 Intermediate Prog Using Python
# 02/21/2024

import csv

#create lists
stud_id = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []
found = []
records = 0

#---------- PART 1 // DISPLAY MENU FUNCTION -------------------    
def menu():
    print("\n")
    print("\t1. See All Student Report")
    print("\t2. Search for a Student [ID]")
    print("\t3. Search for a Student [Last]")
    print("\t4. View Class Roster")
    print("\t5. Exit/Quit Program\n")
    choice = int(input("\n\tPlease enter your selection: "))

    while choice < 0 or choice > 5:
        choice = int(input("\n\tPlease enter your selection: "))
        print("**ERROR**ERROR**")
        
    return choice


#---------- PART 2 // READ FILE INTO LISTS ----------------------
with open ("week7/w7_demoFile.txt") as csvfile:
    for rec in csv.reader(csvfile):
        records += 1
        stud_id.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])
      

#---------- SEARCH FUNCTION -------------------
def binary_search(question, input_list):
    search = input(f"\n\t{question}: ")
    
    min = 0
    max = len(input_list) - 1
    mid =  int((min + max) / 2)

    while (min < max and search.lower() != input_list[mid].lower()):
        if search.lower() < input_list[mid].lower():
            max = mid - 1
        else:
            min = mid + 1
        mid = int((min + max) / 2)
    if search.lower() == input_list[mid].lower():
        print(f"\n{'STUDENT ID':15} {'LAST':30} {'FIRST':30} {'CLASS1':8}{'CLASS2':8} {'CLASS3':8}")
        print("----------------------------------------------------------------------------------------------------------") 
        print(f"{stud_id[mid]:8}\t{lname[mid]:30} {fname[mid]:30} {class1[mid]:8} {class2[mid]:8} {class3[mid]:8}")
    else:
        print("\tThe student ID was not found.")


def class_search():
    search = input(f"\n\tWhat class do you want to search for?: ")

    print(f"\n{'STUDENT ID':15} {'LAST':30} {'FIRST':30} {'CLASS1':8}{'CLASS2':8} {'CLASS3':8}")
    print("----------------------------------------------------------------------------------------------------------")

    for i in range(0, len(lname)):
        if search.lower() == class1[i].lower() or search.lower() == class2[i].lower() or search.lower() == class3[i].lower():
            print(f"{stud_id[i]:8}\t{lname[i]:30} {fname[i]:30} {class1[i]:8} {class2[i]:8} {class3[i]:8}")


#----------------- MAIN PROGRAM --------------------------------------
answer = "y"
while answer.lower() == "y":
    user_choice = menu()

    if user_choice == 1:
        print(f"\n{'STUDENT ID':15} {'LAST':30} {'FIRST':30} {'CLASS1':8}{'CLASS2':8} {'CLASS3':8}")
        print("----------------------------------------------------------------------------------------------------------")

        for i in range(0, len(stud_id)):
            print(f"{stud_id[i]:8}\t{lname[i]:30} {fname[i]:30} {class1[i]:8} {class2[i]:8} {class3[i]:8}")
        
        print("----------------------------------------------------------------------------------------------------------")

    elif user_choice == 2:
        binary_search("Enter the student ID you are looking for", stud_id)

    elif user_choice == 3:
        binary_search("Enter the LAST NAME you are looking for", lname)

    elif user_choice == 4:
        class_search()
    elif user_choice == 5:
        print("\n\tGoodbye!")
    
    answer = input("\n\tDo you want to continue? (y/n): ")
    while answer.lower() != "y" and answer.lower() != "n":
        answer = input("\n\tDo you want to continue? (y/n): ")
        print("**ERROR**ERROR**")
        
