#W7DD2 - Bubble sort & Binary Search
import csv


#create empty 1D lists
type_ = []
name = []
meaning = []
origin = []

with open("algorithms/party.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
     type_.append(rec[0])
     name.append(rec[2])
     meaning.append(rec[3])
     origin.append(rec[3])
print("----ORIGINAL FILE----------------------------------------------")
print(f"{'TYPE':8} {'NAME':30} {'MEANING':18} \t{'ORIGIN'}")
for i in range(0, len(type_)):#outter loop
        print(f"{type_[i]:8} {name[i]:30} {meaning[i]:30} {origin[i]}")
print("---------------------------------------------------------------")

for index in range(0, - 1):#inner loop
        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing

        if(name[index] > name[index + 1]):

          
            #if above is true, swap places!

            temp = name[index]

            name[index] = name[index + 1]

            name[index + 1] = temp

    #TEST DATA TO SEE THAT IT HAS ORDERED
print("----SORTED FILE-------------------------------------------------")
print(f"{'TYPE':8} {'NAME':12} {'MEANING':30} {'ORIGIN'}")





search = input("Get search from user!")

min = 0
max = len(name) - 1       #can also use len(listName) for 'records' value
mid = int((min + max) / 2)

#this is for INCREASING order

while (min < max and search != name[mid].lower()):

   if search <name[mid]:

       max = mid - 1

   else:

       min = mid + 1

   mid = int((min + max) / 2)

if search.lower() == name[mid].lower():
    #found them! use 'guess' for index of found search item
     print(f"\n\tWe found {search}! Here is their info:")
     print(f"\t{'TYPE':8} {'NAME':12} {'MEANING':20} {'ORIGIN'}")
     print(f"{type_[mid]:8} {name[mid]:12} {meaning[mid]:30} {origin[mid]}")

else:
    #boooo not found
     print(f"\n\tWe DID NOT find {search}! Try again:]\n")

answer = input("Would you like to search again? [y/n]: ")
 


