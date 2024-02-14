#Idrees M Abdurrazzak
#SE126.10 Intermediate Prog Using Python
#Mid term
#02/12/2024

#prompt:
#This program will prompt user with a menu function from which they can select between a music genre(1), a curated mood playlist(2) &  (3) dislay list of entire playlist and total records,  or to exit the program(4). The program will then display the user's selection and then display the playlist of the user's selection. The program will then prompt the user to select another option from the menu. The program will continue to loop until the user selects the exit option.

#variable dictionary:









#--------------------------- MAIN CODE STARTS BELOW ---------------------------
import csv

#create some lists first
genre = []
year = []
song =[]
artist = []
mood = []


with open("midterm/music.csv") as libra:

    file = csv.reader(libra)

    for rec in file:
        genre.append(rec[0]) 
        year.append(int(rec[1]))
        artist.append(rec[2])
        song.append(rec[3])
        mood.append(rec[4])



rock = []
reggae = []
hiphop = []
rnb = []




def menu():
    print("\n")
    print("\t1. Show Music Genre")
    print("\t2. Show Mood Playlist")
    print("\t3. Display full playlist")
    print("\t4. Exit")

#def genre_menu():
    #print("\n")
    #print("\t1. Rock")
    #print("\t2. Hip Hop")
    #print("\t3. Reggae")
    #print("\t4. Exit")


   
    choice = int(input("\n\tPlease enter your selection: "))

    while choice < 0 or choice > 4:

        
        choice = int(input("\n\tPlease enter your selection: "))
        print("**ERROR**ERROR**")
   

    return choice


#--------------------- CHOICE 1 ---------------------
menu_choice = menu()


if menu_choice== 1:
    print("\n")
    print("1. Rock")
    print("2. Hip Hop")
    print("3. Reggae")
    print("4. RnB")
    print("5. Exit")
    print("\n")
    genre_choice = (input("Please select your preffered genre: "))

    print(f"\n{'GENRE':10}  {'YEAR':12} {'ARTIST':18} \t{'SONG':15}")
    print("------------------------------------------------------------------------------------------")
   
    if genre_choice[0] == "1" :
       for i in range(0, len(genre)):
            if genre[i] == "Rock":
                print(f"{genre[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")
    
                
    elif genre_choice[0] == "2":
        for i in range(0, len(genre)):
            if genre[i] == "Hip Hop":
              print(f"{genre[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")
         
          
    elif genre_choice == "3":
        for i in range(0, len(genre)):
            if genre[i] == "Reggae":
                print(f"{genre[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")

    elif genre_choice == "4":
        for i in range(0, len(genre)):
            if genre[i] == "RnB":
                print(f"{genre[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")

       


#--------------------- CHOICE 2 ---------------------
mood =[]
upbeat = []
melancholy = []
motivated = []
relaxed = []     

if menu_choice == 2:
    print("\n")
    print("1. Upbeat")
    print("2. Melancholy")
    print("3. Angry")
    print("4. Relaxed")
    mood_choice = (input("\nSelect your mood: "))
    
    #print(f"\n{'UPBEAT':8} {'MELANCHOLY':8} {'MOTIVATED':6} {'RELAXED':6}")
    #print("-------------------------------------------------")

    if mood_choice == "1":
        for i in range(0, len(mood)):
            if mood[i] == "Upbeat":
                print(f"\n{'UPBEAT':8}")
                print(f"{mood[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")
    elif mood_choice == "2":
        for i in range(0, len(mood)):
            if mood[i] == "Melancholy":
                print(f"{mood[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")
    elif mood_choice == "3":
        for i in range(0, len(mood)):
            if mood[i] == "Motivated":
                print(f"{mood[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")
    elif mood_choice == "4":
        for i in range(0, len(mood)):
            if mood[i] == "Relaxed":
                print(f"{mood[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")
                
                
    
   
   
elif menu_choice == 3: #while menu_choice is not the exit option 

    print(f"\n{'GENRE':12} \t {'YEAR':12} \t {'ARTIST'} \t\t\t {'SONG':15}")
    print("-------------------------------------------------------------------------------")      
    for i in range(0, len(genre)):
        #len() --> returns LENGTH of (item) -> for lists, it is the # of items in the list 
        print(f"{genre[i]:12} \t {year[i]:8} \t {artist[i]:15} \t\t {song[i]:8}")
#else:
    #print("Goodbye")






        

            
                
        






