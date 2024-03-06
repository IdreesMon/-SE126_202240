#WEEK 9: FINAL REVIEW

#This review demo will cover all major topics from SE126.  It utilizes: 'finalReview_text.txt'
#Documentation has been added post demo to enhance understandig of the code

#in this review program, you will:
#   1 - connect to a file and import its data into lists
#               1a - the lists are UNEVEN so a filter system must be used
#               1b - count the total number of people in the file
#   2 - process the lists to print the original data to the console
#   3 - process the lists to find:
#               3a - the youngest person in the list
#               3b - the oldest person in the list
#               3c - the average age of the people in the list
#   4 - a search option to search for id codes within the list
#           ** utilize menu '1. Sequential 2. Binary 3. Exit' that is printed from a function that returns the user's selection choice
#               4A - allow user to search multiple time
#               4a - sequential search will be performed w/ output to visualize search
#               4b - binary search will be performed w/ output to visualize search

#FUNCITONS-----------------------------------------------------------------------
def hello():

    print("Welcome to the SE126 FINAL REVIEW!")

def goodbye():

    print("Thank you for viewing the review. Now GO STUDY and kick some Finals butt!")


#a function that swaps values for bubble sorting
def swap(listName, posi):

    #posi --> current position (index) of where swap needs to occur
    temp = listName[k]
    listName[posi] = listName[k + 1]
    listName[posi + 1] = temp

    #this function could not return OR return TWO values ...
    
        #this function could not return OR return TWO values...
        #return nothing: because lisrs are stored to memory for program; when we swap value places, list is automatically updated
    
    #python supports multi return values
    #return listName[posi], listName[posi + 1]

#a function that allows a user to search by sequential search or binary search
def search_menu():

    menu_options = [1, 2, 3]
    print("1. Sequential Search")
    print("2. Binary Search")
    print("3. Exit")
    try:
        response = int(input("Please enter your choice [1 - 3]: "))
    except:
     print("*INVALID CHOICE*")
     return search_menu()

    while response not in menu_options:

        print("*ERROR*ERROR*")
        response = int(input("Please enter your choice [1 - 3]: "))


    #this function should return the user's selection AFTER checking that it is a valid input()


#---------------------------------------------------------------------------------
import csv

hello()


num_rec = 0

#create empty lists in order to store file data
idCode = []
lastname = []
firstName = []
age = []
allegiance = []
num = [] #if == 1, no color2 value ... only when == 2 is there a color2 value
color1 = []
color2 = [] #only when num (rec[5] from file) is == 2 is there a color2 present

#1 - connect to a file and import its data into lists
with open("week9/finalReview_text.csv") as csvfile:

    file = csv.reader(csvfile)
        #when reading files, each record is treated as a list
        #each field of data (rec[#]) represents a new value
    for rec in file:

        #this for loop will run for as many records (rows) of data in the file

        #store data into lists --> .append()
        idCode.append(rec[0])
        lastname.append(rec[1])
        firstName.append(rec[2])
        age.append(int(rec[3]))
        allegiance.append(rec[4])
        num.append(rec[5])
        color1.append(rec[6])
        

        #1a - the lists are UNEVEN so a filter system must be used
        #(not all records in the file have a color2, so we must filter)
        if rec[5] == "2": 
            color2.append(rec[7])
        elif rec[5] == "1":
            color2.append("N/A")
        else:
            color2.append("ERROR")




        #1b - count the total number of people in the file
        #add one to total number of records, necessary for for loop processing
        num_rec += 1 

print("Finished storing data from file. Disconnecting from file now.\n\n")


#   2 - process the lists to print the original data to the console
print("-"*150)
print(f"{'idCode':10}\t{'LASTNAME':15}\t {'FIRSTNAME':15}\t {'AGE':3}\t {'ALLEGIANCE':35}\t {'NUM':3}\t {'COLOR1':7}\t {'COLOR2':7}")
print("-"*150)
for i in range(0, num_rec):

#the for loop will start with 'i = 0'
#for loop will +1 to value of 'i' through each pass through the loop
#for loop will run for 'num_rec' times (for each record in the list)
#wherever 'i' is present, replace with current loop integer value

#8 potential list
    print(f"ID: {idCode[i]:10}\t{lastname[i]:15}\t {firstName[i]:15}\t {age[i]:3}\t {allegiance[i]:35}\t {num[i]:3}\t {color1[i]:7}\t {color2[i]:7}")

print("-"*150)
print(f"{'idCode':10}\t{'LASTNAME':15}\t {'FIRSTNAME':15}\t {'AGE':3}\t {'ALLEGIANCE':35}\t {'NUM':3}\t {'COLOR1':7}\t {'COLOR2':7}")
print("-"*150)




#   3 - process the lists to find:
#PROCESS = FOR LOOP! for loops were BUILT for list/array processing!

#Ask yourself: 
#If the AGE list were ordered in *increasing numeric* order, 
#where would you find:
#  [0]         - the youngest person in the list
#   [len(age)-1]        - the oldest person in the list

#sort the lists by age in increasing order
#BUBBLE SORT    
for i in range(0, len(age) - 1):
    for k in range(0, len(age) - 1):
        if age[k] > age[k +1]:

            #swap values
            ageSwap = age[k]
            age[k] = age[k +1]
            age[k +1] = ageSwap

            swap(firstName, k)
            swap(lastname, k)
            swap(idCode, k)
            swap(allegiance, k)
            swap(num, k)
            swap(color1, k)
            swap(color2, k)

total_age = 0
for i in range(0, num_rec):
    total_age += age[i]




#Ask yourself:
#What do you need to find an average? 
#               3c - the average age of the people in the list
    
ave_age = total_age / len(age)

old_age = age[len(age) - 1]
old_fName = firstName[len(firstName) - 1]

young_age = age[0]
young_fName = firstName[0]


print(f"\n\n ---- HERE IS SOME AGE DATA:")
print(f"\t\t               Oldest Person: {old_fName} is {old_age} years old, ")
print(f"\t\t               Youngest Person: {young_fName} is {young_age} years old, ")
print(f"\t\t               Average Age in file: {ave_age:.1f} years old. \n\n")








#   4 - a search option to search for id codes within the list
#           ** utilize menu '1. Sequential 2. Binary 3. Exit' that is printed from a function that returns the user's selection choice
#4A - allow user to search multiple time
#if the function has a RETURN we must store its return to use in our base program

answer = "y" #allows us to get in loop

while answer == "y":
    

    #call menu function so we have options from menu -- this function will be returning the user's selection and storing it into the var userChoice
    userChoice = search_menu()

    if userChoice == 1:
        print("You selected Sequential Search")
        #4a - sequential search will be performed w/ output to visualize search

        #ask for search query
        search = input("\n\tWhich Last Name are you looking for: ")
        #we could  also search for: allegiance, nums, color1, color2 (all non-unique)

        #create an empty list to store found items
        found = []
        #run sequential search
        for i in range(0,len(lastname)):
            if search.lower() == lastname[i].lower():
                #found someone!
                found.append(i) #REMEMBER: i is the index of the found item

        
        #print results
        if not found: #checks to see if list is empty
            print(f"\n\tHere is what we found: ")
            for i in range(0, len(found)):
                print(f"{idCode[found[i]]:10}\t{lastname[found[i]]:15}\t {firstName[found[i]]:15}\t {age[found[i]]:3}\t {allegiance[found[i]]:35}\t {num[found[i]]:3}\t {color1[found[i]]:7}\t {color2[found[i]]:7}")

    if userChoice == 2:
        print("You selected Binary Search")

        #4b - binary search will be performed w/ output to visualize search
        #BINARY SEARCH CAN ONLY BE USED ON ORDERED LISTS

        #ask for search query
        search = input("\n\tWhich Last Name are you looking for: ")


        #sort list & linked data
        for i in range(0, len(firstName) - 1):
            for k in range(0, len(firstName) - 1):
                if firstName[k] > firstName[k +1]:

                    #swap values!
                    swap(firstName, k)
                    swap(lastname, k)
                    swap(idCode, k)
                    swap(allegiance, k)
                    swap(num, k)
                    swap(color1, k)
                    swap(color2, k)


        #binary search list
        min = 0
        max = len(firstName) - 1
        mid = int(( min + max) / 2)

        while min < max and search != firstName[mid]:
            if search > firstName[mid]:
                min = mid + 1
            else:
                min = mid - 1
            mid = int((min + max) / 2)


        #print results
        if search == firstName[mid]:
            print(f"\n\tHere is what we found: ")
            print(f"{idCode[mid[i]]:10}\t{lastname[mid[i]]:15}\t {firstName[mid[i]]:15}\t {age[mid[i]]:3}\t {allegiance[mid[i]]:35}\t {num[mid[i]]:3}\t {color1[mid[i]]:7}\t {color2[mid[i]]:7}")
        else:
            print(f"\n\tWOMPWOMP No results found for {search}")
            


    if userChoice == 3: 
         print("You selected to EXIT the program")

        #EXIT PROGRAM
         answer = "x"

    #which menu choices do NOT want to be asked if they want to run again?
    if userChoice not in [1,2]:

       answer = input("Would you like to search again? [y/n]: ").lower()

goodbye()