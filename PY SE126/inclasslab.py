#Idrees M Abdurrazzak
#Lab 2 - In Class Lab
#01/16/24

#-------------------- MAIN STARTS CODE BELOW -------------------------------
#Import the csv
import csv 

print("Welcome to our Room Capacitor program! Lets see how many each room can fit\n")

#store the total amount of records
total_records = 0

#initialize empty lists for variables
rooms = []
maxs = []
mins = []

#connect to CSV file
with open("lab2a.csv") as csvfile:
    
    #Allow the file to be read by the program 
    #Reader allows for CSV file to be read
    file = csv.reader(csvfile)

    #read/process the file data one at a time
    for rec in file:
        
        #store data to a list and add it to a list
        rooms.append(rec[0]) #rooms
        maxs.append(int(rec[1])) #max capacity for rooms
        mins.append(int(rec[2])) # minimum capacity for rooms

        #keep literal count of numbers of records
        total_records += 1

#set count for rooms over limit
#print the header #assign distances
print(f"{'ROOM':20} {'MAX':5} {'MIN':6} OVER")

total_room = 0
for index in range(total_records):
    if mins[index] > maxs[index]:
        total_room += 1
        #Calculate the sum of rooms that have reached over capacity
        over = mins[index] - maxs[index]
        #print rooms that have over capacities
        print(f"{rooms[index]:20} {maxs[index]:3} {mins[index]:5} {over:5}")

print(f"There were {total_records} records processed")
print(f"there were {total_room} rooms over the limit")
print("Thank You for using this program!")



        
    




