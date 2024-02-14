# Idrees M Abdurrazzak
# SE126.10 Intermediate Prog Using Python
# Mid term
# 02/12/2024

# prompt:
# This program will prompt user with a menu function from which they can select between a music genre(1), a curated mood playlist(2) &  (3) dislay list of entire playlist and total records,  or to exit the program(4). The program will then display the user's selection and then display the playlist of the user's selection. The program will then prompt the user to select another option from the menu. The program will continue to loop until the user selects the exit option.

# variable dictionary:


# --------------------------- MAIN CODE STARTS BELOW ---------------------------
import csv

# create some lists first
genre = []
year = []
song = []
artist = []
mood = []
records = 0
rock = 0
reggae = 0
hiphop = 0
rnb = 0

with open("midterm/music_midterm.csv") as libra:
    for rec in csv.reader(libra):
        records += 1
        genre.append(rec[0])
        year.append(int(rec[1]))
        artist.append(rec[2])
        song.append(rec[3])
        mood.append(rec[4])
        


def menu():
    print("\n")
    print("\t1. Show Music Genre")
    print("\t2. Show Mood Playlist")
    print("\t3. Display full playlist")
    print("\t4. Exit")

    choice = int(input("\n\tPlease enter your selection: "))

    while choice < 0 or choice > 4:

        choice = int(input("\n\tPlease enter your selection: "))
        print("**ERROR**ERROR**")

    return choice



menu_choice = None
while menu_choice != "4":
    menu_choice = menu()


# --------------------- CHOICE 1 --------------------------------------------------
   
    if menu_choice == 1:
        print("\n")
        print("1. Rock")
        print("2. Hip Hop")
        print("3. Reggae")
        print("4. RnB")
        print("5. Exit")
        print("\n")
        genre_choice = (input("Please select your preffered genre: "))

        print(f"\n{'GENRE':10}  {'YEAR':12} {'ARTIST':18} \t{'SONG':15}")
        print("----------------------------------------------------------------------------------------")
        #nested flow -- > option 1 song genre
        if genre_choice[0] == "1":
            for i in range(0, len(genre)):
                if genre[i] == "Rock":
                    rock +=1
                    print(
                        f"{genre[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")
                        
                    
        elif genre_choice[0] == "2":
            for i in range(0, len(genre)):
                if genre[i] == "Hip Hop":
                    hiphop +=1
                    print(
                        f"{genre[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")
                   
        elif genre_choice == "3":
            for i in range(0, len(genre)):
                if genre[i] == "Reggae":
                    reggae +=1
                    print(
                        f"{genre[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")
                    
        elif genre_choice == "4":
            for i in range(0, len(genre)):
                if genre[i] == "RnB":
                    rnb +=1
                    print(
                        f"{genre[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")
               

# --------------------- CHOICE 2 -----------------------------------------------------
    #user input option 2 for Mood selection playlist
    elif menu_choice == 2:
        print("\n")
        print("1. Upbeat")
        print("2. Melancholy")
        print("3. Motivated")
        print("4. Relaxed")
        mood_choice = input("\n\tSelect your mood: ")
        print(f"\n{'MOOD':10}  {'YEAR':12} {'ARTIST':18} \t{'SONG':15}")
        print("------------------------------------------------------------------------------------------")

        if mood_choice == "1":
            #print(f"\nUPBEAT")
            for i in range(0, len(mood)):
                if mood[i] == "Upbeat":
                    print(f"{mood[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")

        elif mood_choice == "2":
            #print(f"\nMELANCHOLY")

            for i in range(0, len(mood)):
                if mood[i] == "Melancholy":
                    print(f"{mood[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")

        elif mood_choice == "3":
            #print(f"\nMOTIVATED")

            for i in range(0, len(mood)):
                if mood[i] == "Motivated":
                    print(f"{mood[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")
                    
        elif mood_choice == "4":
            #print(f"\nRELAXED")
            
            for i in range(0, len(mood)):
                if mood[i] == "Relaxed":
                    print(f"{mood[i]:7} {year[i]:8} \t {artist[i]:15} \t{song[i]:8}")

# --------------------- CHOICE 3 ----------------------------------------------------------
    #3 option to display entire playlist
    elif menu_choice == 3:  
        print(f"\n{'GENRE':12} \t {'YEAR':12} \t {'ARTIST'} \t\t\t {'SONG':15}")
        print("----------------------------------------------------------------------------------------------")
        for i in range(0, len(genre)):
        
            print(
                f"{genre[i]:8} \t {year[i]} \t\t {artist[i]:15} \t\t {song[i]:8}")
            
        
   
# --------------------- CHOICE 4 -----------------------------------------------------------
    elif menu_choice == 4:
        print(f"\n\tTotal records in playlist: {records}")
        #I WILL UPDATE WITH INDIVIDUAL GENRE COUNTS
        print("\nThank You for scrolling through my curated playlist! Come back for better tunes!\n")
        exit()
