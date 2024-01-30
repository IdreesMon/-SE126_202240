#Idrees M Abdurrazzak
##Lab 3B - Voter Registration
#01/29/2024

#Prompt: Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values.

#variiable dictionary:

#total_records:
#not_of_age:
#eligible_unregistered:
#eligible_unvoted:





#----- MAIN CODE BELOW -----
print("")

import csv
print("\n")
#Keep count of records and voter registration 
total_records = 0
not_of_age = 0
eligible_unregistered = 0
eligible_unvoted = 0
individuals_voted = 0  


#initiliaze empty list for CSV data
id = []
age = []
registered = []
voted = []


#access the data from CSV
with open("weekthree/voters_202040.csv") as csvfile:

    #allow for voters csv to be read by program 'r'
    file = csv.reader(csvfile)

    for record in file: 

        print (record)

        #increase by +1 for total records
        total_records += 1


        #store data to the list by using .append method 
        id.append(int(record[0]))
        age.append(int(record[1]))
        registered.append(record[2])
        voted.append(record[3])


#For Loop to pass data through each variable
for i in range(total_records):
    
    #if individual not eligible to vote
    if age[i] <= 18:
        not_of_age += 1
    #if individual is eligible but havent registered
    elif age [i] >= 18 and registered [i]== "N":
        eligible_unregistered += 1
    #if individual are registered but havent voted
    elif registered[i] == "Y" and voted[i] == "N":
        eligible_unvoted += 1
    #if voted
    elif registered[i] == "Y" and voted[i] == "Y":
        individuals_voted += 1
#Exit For Loop

#Print final results
print("\n")
print(f"The Total amount of records processed was {total_records}")
print(f"The amount of individuals NOT eligible due to age is {not_of_age}")
print(f"The amount of individuals OLD enough to vote but have not registered: {eligible_unregistered}")
print(f"The amount of individuals who are eligible but did not vote: {eligible_unvoted}")
print(f"The amount of individuals who voted: {individuals_voted}")