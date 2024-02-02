#Idrees M Abdurrazzak
#SE126.10 Intermediate Prog Using Python
#Lab 4A
#02/01/2024


#prompt:


#Variable Dictionary
import csv
#------------------------ MAIN CODE STARTS BELOW ----------------------------

#create 1D lists [will be parallel to each other]
fname = []
lname = []
age = []
nick_name = []
house_allegiance = []
#create counter
total_records = 0
print(f"\n{'FIRST':10} {'LAST':10} {'AGE':5}  {'NICKNAME':18}  {'ALLEGIANCE'} ")
print("----------------------------------------------------------------")      

with open("week4/files/lab4A_GOT_NEW.txt") as csvfile:
    
    file = csv.reader(csvfile)

    for record in file:
        total_records += 1
        fname.append(record[0])
        lname.append(record[1])
        age.append(record[2])
        nick_name.append(record[3])
        house_allegiance.append(record[4])

for i in range (0, len(fname)):
    print(f"{fname[i]:10} {lname[i]:10} {age[i]:6} {nick_name[i]:18} {house_allegiance[i]}")

print("\n\n")

#-----------REPROCESS LIST-------------
print(f"\n{'FIRST':12} \t {'LAST':12} \t {'AGE'} \t {'NICKNAME':18} \t {'ALLEGIANCE':16} HOUSE MOTTO")
print("-------------------------------------------------------------------------------------------")     

#store allegiances to variables
house_stark = 0
nights_watch = 0
house_lannister = 0
house_baratheon = 0
house_targaryen = 0
#store motto as list
motto=[]

 
for i in range(0, len(fname)):

    motto.append(house_allegiance)
    if house_stark[i]:
      motto.append("Winter is Coming")
    elif nights_watch[i]:
      motto.append('And now my watch begins')
    elif house_lannister[i]:
      motto.append('Hear me roar!')
    elif house_baratheon[i]:
      motto.append('Ours is the fury')
    else:
        print('Fire & Blood')



