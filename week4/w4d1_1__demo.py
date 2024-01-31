import csv 

#create 1D lists [will be parallel to each other]
#base lists on fields in file 

fname = []
lname = []
test1 = []  
test2 = []
test3 = []

#connect to file & read data into 1D lists
with open("Week4/files/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    #come back and show print(file) later
    for record in file:
        #store data from file fields to their respective list 
        #we call this parallel because we are storing initial file record data as same position as index in each list. Use the same index across each list to find "matching"
        fname.append(record[0])
        lname.append(record[1])
        test1.append(int(record[2])) #cast as interger for math
        test2.append(int(record[3]))
        test3.append(int(record[4]))
#disconnected from file --------------------------------
        
#PROCESS the lists --> for loop (looping through things with multiple values)
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'} ")
print("---------------------------------------------------------------------")      
for i in range(0, len(fname)):
    #len() --> returns LENGTH of (item) -> for lists, it is the # of items in the list 
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")
print ("---------------------------------------------------------------------")

#calculate and store each students average TEST SCORE
#make an avg
#make a count
#make a list
avg = 0
total_count = 0
average = []

for i in range(0,len(test1)):
        #i is a local variable. Can be re used because it is working the current value till it reaches its final value and loop ends.
       
       #calculate avg for student
        avg = (test1[i] + test2[i] + test3[i]) /3
       
       #append this avg to the average[]
        average.append(avg)
    #test1-test3 are all being processed through their respective index. Their variables were stored as empty list meaning they begin at 0 and end at final value of index. 
        
#display students fname and test average
print(f"{'FIRST'}\t{'AVERAGE':20}")
for i in range(0, len(fname)):
     print(f"{fname[i]:12} \t {average[i]:8.1f}")

#SEQUENTIAL SEARCH - "in sequence" --> from beginning THROUGH the end
     #looks through every value in the list and compares the data to eachother
low_name = ""
low_avg = 100 #start with highest value to drop to find lowest

for i in range(0, len(average)):
     
     #determine if current average is lower than current low_avg

     #if statments are for one time questions to data
     # [i] CURRENT POSITION
     if average[i]< low_avg:
          
          low_avg = average[i] #current average is lower, so becomes new low value
          low_name = fname[i]

#DISPLAY: total students in file, highest test average and score

#MY WAY
print(f"\nTHE LOWEST AVERAGE: {low_avg}. \nTHIS AVERAGE BELONGS TO: {low_name}")
#KT's WAY
print(f"\nSTUDENTS IN FILE: {len(fname)}")
print(f"LOWEST AVERAGE: {low_name} - {low_avg:.1f}")


#-------------------------2D LISTS------------------------------------
#use your 1D parallel lists to populate a new, 2D list
#HINT: the 2D list is a list ... populated with lists 8D
all_students = []

for i in range(0, len(fname)):
     
     #add each student's data to their (index(i)) place in the all_students[]
     all_students.append([fname[i], lname[i], test1[i], test2[i], test3[i], average[i]])


#display the 2D list to the console - for now just get the list to display ie ['Floyd', 'Eastham', '100', '85', '93']
for i in range(0, len(all_students)):
    print(f"{all_students[i]}")

print(f"\n---------------------2D LIST - INDIV VALUES!--------------------------------")
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'},{'AVERAGE'} ")


#display the 2D list to the console where each value for each list appears as a value (and not a list item)
for i in range(0, len(all_students)):
    #we have lists within a list - outtter for handles main list (all_students)

#x which value in the list are we looking at 
    for x in range(0, len(all_students[i])):
        #Inner for handles each value found at current list (all_students[i])
        print(f"{all_students[i][x]} ", end="")


#include an extra empty print() to cancel the interior print's end=""
print()

     
