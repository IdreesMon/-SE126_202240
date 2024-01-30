#Idrees M Abdurrazzak
#Lab 3
#Prompt 
#Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier


import csv 

total_records = 0

#initiliaze list 
comp_type_list = []
manu_list = []
processor_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []


text_file_list = []

with open("Week3_ClassLab/lab3a.csv") as csvfile:

   print(f"\n{'TYPE':8} {'MANU':8} {'PROC':6} {'RAM':6} {'HDD1':6} {'#HDD':6} {'HDD2':6} {'OS':6} {'YEAR':6}")
print("------------------------------------------------------------------")
with open("Week3/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)
      

    for rec in file:

        #print(rec) #shows a LIST -> []

        #keep track of the rec count in the file
        total_records += 1 #adding each rec for a total (29)
        

        #FILTER for DISPLAY---------------
        #--comp type-- rec[0]
        if rec[0] =="D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else: 
            comp_type = "*ERROR - -" + str(rec[0])

        #--manufacturer-- rec[1]
        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "Gateway"
        elif rec[1] == "HP":
            manu = rec[1]
        else:
            manu = "*ERROR -- " + str(rec[1])
        

        #--processor / ram / hdd_1 / num_hdd - exact from file
        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]

        if rec[5] == "1":
            hdd_2 = " " #"---" #"none"
            os = rec[6]
            year = rec [7]



        elif rec[5] == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec [8]


        else:
            hdd_2 = "*ERROR -- " + str(rec[5])
            os =  "ERROR"
            year = "ERROR"


        #append respective values to the appropriote field list (after empty values)
        comp_type_list.append(comp_type)
        manu_list.append(manu)
        processor_list.append(processor)
        ram_list.append(ram)
        hdd_1_list.append(hdd_1)
        num_hdd_list.append(num_hdd)
        hdd_2_list.append(hdd_2)
        os_list.append(os)
        year_list.append(year)

        #final print for each record 
        #assign field width 
        
#------DISCONNECTED FROM FILE--------------
print(f"TOTAL RECORDS: {total_records}")

#process the list to: print the machine data
for index in range(0, total_records):
    #for index in range(0, len(comp_type)): --> len (comp_type_list) returns the INTEGER count of values
    #each time we go through the For loop it increments by +1
    print(f"{comp_type_list[index]:8} {manu_list[index]:8} {processor_list[index]:6} {ram_list[index]:6} {hdd_1_list[index]:6} {num_hdd_list[index]:6} {hdd_2_list[index]:6} {os_list[index]:6} {year_list[index]:6}")

#process the lisy to: count the number of desktops
desktop_count_two = 0
desktop_count = 0
laptop_count = 0
desktop_cost = 0
laptop_cost = 0

#first position in a list is 0 if you wish to go through a list from the beginning 
for index in range (0, len(comp_type_list)):

    #look through the comp_type_list to find "Desktop"
    if comp_type_list[index] == "Desktop" and int(year_list[index]) <= 16:
        desktop_count += 1 #add 1 for every time "Desktop" is found
        desktop_cost +=2000
    if comp_type_list[index] == "Laptop" and int(year_list[index]) <= 16:
        laptop_count += 1
        laptop_cost += 1500


#Display exit message for user
print(f"\n\t\tTOTAL DESKTOPS IN FILE: {total_records}")
print(f"\nTo replace {desktop_count} it will cost ${desktop_cost}")
print(f"To replace {laptop_count} it will cost ${laptop_cost}")


#len() --> LENGTH FUNCTION; when passed a (list) it returns an integer: # of values in list
#for index in comp_type_list (no need for length, "for index" will go through the whole list)


#process the list to: find average hdd_1 size

total_size = 0
count_size = 0

for index in range (0, len(hdd_1_list)):
    if hdd_1_list[index] == '001TB':
        total_size += 1
    else:
        total_size += 0.5
    count_size += 1

average = total_size / count_size 
#could also use: 'len(hdd_1_list)' or 'total_records' in place of 'count size'

#empty list for cost
laptop_cost = [0]
desktop_cost = [0]




