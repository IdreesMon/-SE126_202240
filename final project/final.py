#Name - Idrees M. Abdurrazzak, Andy Ho
#Lab - Final Project
#Date - 03/6/2024
#Program Prompt - For your Midterm Project in SE126 you will be building a program of your own design! You must work individually to design a program and file of your choosing.

#About Program - A 2023-2024 Premier League(England Soccer League) stat sheet program that allows users to see how teams are doing from their current standing, how many goals they have scored, how many points they have, and etc. 

#Variable Dictionary:
#field 0 - teams, col.0, rec[0]
#team - list that holds all the teams from the file(col.0, rec[0])

#field 1 - current standing in the league, col.1, rec[1]
#standing - list that holds the each teams standing from the file(col.1 rec[1]) 

#field 2 - how many points the team has, col.2, rec[2]
#points - list that holds each teams points from the file(col.2 rec[2])

#field 3 - amount of wins each team has, col.3, rec[3]
#wins - list that holds each teams wins from the file(col.3, rec[3])

#field 4 - amount of draws each team has, col.4, rec[4]
#draws - list that holds each teams draws from the file(col.4, rec[4])

#field 5 - amount of losses each team has, col.5, rec[5]
#losses - list that holds each teams losses from from the file(col.5, rec[5])

#field 6 - amount of goals each team has scored, col.6, rec[6]
#goals_scored - list that holds the amount of goals each team has scored(col.6, rec[6])

#field 7 - amount of goals each team has allowed, col.7, rec[7]
#goals_allowed - list that holds the amount of goals each team has allowed(col.7, rec[7])

#field 8 - the goals differences(goals_scored - goals_allowed) each team has, (col.8, rec[8])
#goals_difference - list that holds the goal differences each team has(col.8, rec[8])

#motto - list that holds each teams motto
#nickname - list that holds each teams nickname

#menu - Function that displays all the teams
#display - holds and calls the menu function to the main program to display
#seq_search - function that will search in a sequence through the entire list from the starting index and last index to find the value you are looking for
#pick - parameter of the seq_search function
#choice_index - holds the index(location) to this variable
#total_searchs - list that holds the amount of teams you searched
#decision - holds and calls the seq_search function to use in the main program



#-----------------------PROGRAM BEGINS BELOW-----------------------------------

import csv

#----------------Empty LISTS for data from file to be stored-----------------
#Soccer lists
team = []
standing = []
points = []
wins = []
draws = []
losses = []
goals_scored = []
goals_allowed = []
goals_difference = []
motto = []
nickname = []

#football lists
team_fb = []
standing_fb = []
wins_fb = []
losses_fb = []
pointsScored_fb = []
pointsAllowed_fb = []
OffenseFb_ranking = []
DefenseFb_ranking = []
playoffs_fb = []

#basketball lists


#connect to file for program to read and append(store) the data to lists
#Open the soccer file
with open("final project/Premier_League_Stats.csv") as csvfile:
   
    file = csv.reader(csvfile)

    for rec in file:
        team.append(rec[0])
        standing.append(int(rec[1]))
        points.append(int(rec[2]))
        wins.append(int(rec[3]))
        draws.append(int(rec[4]))
        losses.append(int(rec[5]))
        goals_scored.append(int(rec[6]))
        goals_allowed.append(int(rec[7]))
        goals_difference.append(int(rec[8]))
#open the football file
with open("final project/NFLstats_2023.csv") as csvfile1:
    file1 = csv.reader(csvfile1)
    for rec in file1:
        team_fb.append(rec[0])
        standing_fb.append(int(rec[1]))
        wins_fb.append(int(rec[2]))
        losses_fb.append(int(rec[3]))
        pointsScored_fb.append(int(rec[4]))
        pointsAllowed_fb.append(int(rec[5]))
        OffenseFb_ranking.append(int(rec[6]))
        DefenseFb_ranking.append(int(rec[7]))
        playoffs_fb.append(rec[8])
#open the basketball file

#add/append team mottos
for i in range(0, len(team)):
    if team[i] == "Liverpool":
        motto.append("You'll Never Walk Alone")
    elif team[i] == "Mancity":
        motto.append('Pride In Battle')
    elif team[i] == "Arsenal":
        motto.append('Victory Through Harmony')
    elif team[i] == "Astonvilla":
        motto.append('Prepared')
    elif team[i] == "Tottenham":
        motto.append('To Dare Is To Do')
    elif team[i] == "Manutd":
        motto.append("Wisdom and Effort")
    elif team [i] == "Westham":
        motto.append("I'm Forever Blowing Bubbles")
    elif team [i] == "Brighton":
        motto.append('We Never Give Up')
    elif team [i] == "Newcastle":
        motto.append('Triumphing by Brave Defense')
    elif team [i] == "Wolverhampton":
        motto.append('Out of Darkness Cometh Light')
    elif team[i] == "Chelsea":
        motto.append('Unless God Is With Us, All Will Be In Vain')
    elif team [i] == "Bournemouth":
        motto.append('Together, Anything Is Possible')
    elif team [i] == "Fulham":
        motto.append('Building Better Lives Through Sport')
    elif team [i] == "Crystalpalace":
        motto.append("Passion and Determination")
    elif team [i] == "Brentford":
        motto.append('Nothing Is Impossible')
    elif team[i] == "Nottmforest":
        motto.append('Virtue Outlives Death')
    elif team [i] == "Lutontown":
        motto.append('May It Be Given to Skill and Industry')
    elif team[i] == "Everton":
        motto.append('Nothing But The Best Is Good Enough')
    elif team [i] == "Burnley":
        motto.append('The Prize and The Cause of Our Labour')
    elif team [i] == "Sheffield":
        motto.append('Out Run Out Fight Out Play')

#add/append nicknames
for i in range(0, len(team)):
    if team[i] == "Liverpool":
        nickname.append('The Reds')
    elif team[i] == "Mancity":
        nickname.append('The Sky Blues')
    elif team[i] == "Arsenal":
        nickname.append('The Gunners')
    elif team[i] == "Astonvilla":
        nickname.append('Lions')
    elif team[i] == "Tottenham":
        nickname.append('Spurs')
    elif team[i] == "Manutd":
        nickname.append("The Red Devils")
    elif team [i] == "Westham":
        nickname.append("The Hammers")
    elif team [i] == "Brighton":
        nickname.append('Seagulls/Albions')
    elif team [i] == "Newcastle":
        nickname.append('The Magpies')
    elif team [i] == "Wolverhampton":
        nickname.append('Wolves')
    elif team[i] == "Chelsea":
        nickname.append('The Blues')
    elif team [i] == "Bournemouth":
        nickname.append('The Cherries')
    elif team [i] == "Fulham":
        nickname.append('The Cottagers')
    elif team [i] == "Crystalpalace":
        nickname.append("Eagles")
    elif team [i] == "Brentford":
        nickname.append('The Bees')
    elif team[i] == "Nottmforest":
        nickname.append('Tricky Trees')
    elif team [i] == "Lutontown":
        nickname.append('The Hatters')
    elif team[i] == "Everton":
        nickname.append('The Toffees')
    elif team [i] == "Burnley":
        nickname.append('The Clarets')
    elif team [i] == "Sheffield":
        nickname.append('The Blades')
#-------------------------FUNCTIONS------------------------------
#a menu to list the teams for the 2023-2024 Premier League
def menu():
    print("\t\t\t\t\tLiverpool\n\t\t\t\t\tMancity\n\t\t\t\t\tArsenal\n\t\t\t\t\tAstonvilla\n\t\t\t\t\tTottenham\n\t\t\t\t\tManutd\n\t\t\t\t\tWestham\n\t\t\t\t\tBrighton\n\t\t\t\t\tNewcastle\n\t\t\t\t\tWolverhampton\n\t\t\t\t\tChelsea\n\t\t\t\t\tBournemouth\n\t\t\t\t\tFulham\n\t\t\t\t\tCrystalpalace\n\t\t\t\t\tBrentford\n\t\t\t\t\tNottmforest\n\t\t\t\t\tLutontown\n\t\t\t\t\tEverton\n\t\t\t\t\tBurnley\n\t\t\t\t\tSheffield")

#create the sequential search function which will search through the entire list to find the value you are looking for
def seq_search(pick):

    #initilaize the index variable
    choice_index = "" #this is empty or you could co chouce_index = -1

    #create a for loop so that the program looks through the list from start to end to find the value you are looking for
    for i in range(0, len(team)):

        #look at each value in the list to see if it matches what you are looking for from your input
        if team[i].lower() == pick.lower():
            choice_index = i #stores the index(location) to this variable
        
    return choice_index #returns your choice

#----------------------MAIN CODE BELOW--------------------------------

total_searchs = []
answer = "y"


#create while loop to introduce the user to the program and keep them in as long as they want
while answer.lower() == "y":
    #HEADING
    print("\n\n\t\t\t2023-2024 Premier League Stats for Each Team")
    print("---------------------------------------------------------------------------------------------------")
    display = menu()
    

    choice = input("\t\t\t\tEnter the team you want to look at:")

    decision = seq_search(choice)

    if decision != "":#if you have a chosen a team that is in the Premier League
        if decision not in total_searchs:#this statement will basically store/append the team to total_searches once so that if you search up a team twice, it will only store the team to the list during the first time and not the next few times if you search the same team again.
            total_searchs.append(decision)
        print(f"\n\n\n\t\t\t\t{team[decision]}({nickname[decision]})")
        print(f"\t\t\t\tMOTTO:{motto[decision]}")
        print(f"\t\t\t\t-------------------------------")
        print("\t\t\t\tHow They Are Doing This Season:")
        print(f"\t\t\t\tStanding:{standing[decision]}\n\t\t\t\tPoints:{points[decision]}\n\t\t\t\tWins:{wins[decision]}\n\t\t\t\tDraws:{draws[decision]}\n\t\t\t\tLosses:{losses[decision]}\n\t\t\t\tGoals Scored:{goals_scored[decision]}\n\t\t\t\tGoals Allowed:{goals_allowed[decision]}\n\t\t\t\tGoal Difference:{goals_difference[decision]}")
    else: #if you have chosen a team that is not in the Premier League
        print(f"\t\t\t\tThe team {choice} is not in the Premier League this season")

    #give user opportunity to stop looking at teams and break out of loop
    answer = input("\t\t\t\tDo you want to continue looking at teams [y/n]:")
#exit loop
print(f"\t\t\t\tThank you for using this program, You looked at {len(total_searchs)} teams during your session.")

##how to add everything up at the end
#all_searchs = 0
#all_searchs = len(total_searchs) + len(football_searchs) + len(basketball_searchs)
#print(f"\t\t\t\tYou looked at {all_searchs} teams during your session.")