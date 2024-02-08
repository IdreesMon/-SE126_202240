#Idrees M Abdurrazzak
#SE126.10 Intermediate Prog Using Python
#Lab 4
#02/07/2024


#prompt: Process the lists to print the them as they appear in the file
#-Re-process the lists to add the House Motto 
#-Re-Process the lists to print each record fully with the House Mottos
#-Re-process the lists to find the average age within the list, then
#-Print the total number of people in the list
#-Print the average age - rounded to a whole number {:.0f}
#-Print tallies/final counts for each allegiance (Field4)


#Variable Dictionary

#fname: First names of Games of Thrones characters
#lname: Last names of Games of Thrones characters
#age: Ages of individuals
#nick_name: Alias' of individuals
#house_allegiance: To which house/family the individual belongs to
#total_records: Total records of characterrs
#house_stark: Great House of Westeros and the royal house of the Kingdom of the North
#nights_watch: The Night's Watch is an organization of soldiers on Westeros that protect the Wall on the north end of the continent
#house_lannister: One of the Great Houses of Westeros, one of its richest and most powerful families and one of its oldest dynasties.
#house_baratheon: The youngest of the Great Houses of Westeros
#house_targaryen:  A noble family of Valyrian descent who once ruled the Seven Kingdoms of Westeros.
#motto: Motto associated with each house
#avg: average age counter
#average:
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

#store allegiances to variables
house_stark = 0
nights_watch = 0
house_lannister = 0
house_baratheon = 0
house_targaryen = 0
#store motto as list
motto=[]

 
for i in range(0, len(fname)):

    # motto.append(house_allegiance)
    if house_allegiance[i] == "House Stark":
      motto.append("Winter is Coming")
      house_stark += 1
    elif house_allegiance[i] == "Night's Watch":
      motto.append('And now my watch begins')
      nights_watch += 1
    elif house_allegiance[i] == "House Lannister":
      motto.append('Hear me roar!')
      house_lannister +=1
    elif house_allegiance[i] == "House Baratheon":
      motto.append('Ours is the fury')
      house_baratheon += 1
    elif house_allegiance[i] == "House Targaryen":
        motto.append ('Fire & Blood')
        house_targaryen += 1
print(f"{'ALLEGIANCE':25} \t {'MOTTO'}")
print("-----------------------------------------------------------------")      
for i in range (0, len(motto)):
    print(f"{house_allegiance[i]:15} \t\t {motto[i]}")

print(f"\n")
   

#counters
avg = 0
total_count = 0
average = []

for i in range(0,len(age)):
    avg = avg + int(age[i])
    total_count += 1
    
#reprocess variables as an empty list to store records of each house
house_stark = []
nights_watch = []
house_lannister = []
house_baratheon = []
house_targaryen = []

#reprocess the list to find the count of each house
for i in range(0, len(house_allegiance)):
    if house_allegiance[i] == "House Stark":
        house_stark.append(house_allegiance[i])
    elif house_allegiance[i] == "Night's Watch":
        nights_watch.append(house_allegiance[i])
    elif house_allegiance[i] == "House Lannister":
        house_lannister.append(house_allegiance[i])
    elif house_allegiance[i] == "House Baratheon":
        house_baratheon.append(house_allegiance[i])
    elif house_allegiance[i] == "House Targaryen":
        house_targaryen.append(house_allegiance[i])
    
print(f"\t\tHOUSE STARK:   {len(house_stark)}")
print(f"\t\tNIGHT'S WATCH: {len(nights_watch)}")
print(f"\t\tHOUSE LANNISTER: {len(house_lannister)}")
print(f"\t\tHOUSE BARATHEON: {len(house_baratheon)}")
print(f"\t\tHOUSE TARGARYEN: {len(house_targaryen)}")

print(f"\t\tTOTAL AGE AVERAGE: {avg/total_records:.0f}")
print(f"\t\tTOTAL RECORD:  {total_records}")
print("\n Thank you for entering the Game of Thrones. Farwell!")



