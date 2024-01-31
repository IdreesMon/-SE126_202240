#Idrees M Abdurrazzak
#SE_126


import csv 
#----------------------------------- PART 1 ------------------------------------------>
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
#disconnected from file --------------------------------------------------------------
        
#PROCESS the lists --> for loop (looping through things with multiple values)
print(f"\n{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'} ")
print("----------------------------------------------------------------")      
for i in range(0, len(fname)):
    #len() --> returns LENGTH of (item) -> for lists, it is the # of items in the list 
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")
print ("----------------------------------------------------------------")

#------------------------------------------- PART 2 ---------------------------------------->

#initiate a counter storing data in list -- avg, letter grade
letter_grade = []
num_average = []



for i in range(0,len(fname)):
        
        #i is a local variable. Can be re used because it is working the current value till it reaches its final value and loop ends.
       
       #calculate avg for student
        avg = (test1[i] + test2[i] + test3[i]) /3
       
       #append this avg to the average[]
        num_average.append(avg)
    #test1-test3 are all being processed through their respective index. Their variables were stored as empty list meaning they begin at 0 and end at final value of index. 
        
#display students fname and test average
print(f"{'FIRST'}\t\t{'AVERAGE'}\n")
for i in range(0, len(fname)):
     print(f"{fname[i]:12} \t {num_average[i]:.1f}")

#SEQUENTIAL SEARCH - "in sequence" --> from beginning THROUGH the end
     #looks through every value in the list and compares the data to eachother
low_name = ""
low_avg = 100 #start with highest value to drop to find lowest

for i in range(0, len(num_average)):
     
     #determine if current average is lower than current low_avg

     #if statments are for one time questions to data
     # [i] CURRENT POSITION
     if num_average[i]< low_avg:
          
          low_avg = num_average[i] #current average is lower, so becomes new low value
          low_name = fname[i]
     
print(f"\n\t\tTHE LOWEST AVERAGE: {low_avg}. \n\t\tTHIS AVERAGE BELONGS TO: {low_name}")

#DISPLAY: total students in file, highest test average and score

print(f"\n{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'} \t\t {'AVERAGE':12}")
print("--------------------------------------------------------------------------")      

for i in range(0, len(fname)):
    #len() --> returns LENGTH of (item) -> for lists, it is the # of items in the list 
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]} \t {round(num_average[i]):12}")


 

  
    












