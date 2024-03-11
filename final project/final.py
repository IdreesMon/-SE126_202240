#Name - Andy Ho, Idrees Abdurrazzak
#Lab - Final Project
#Date - 3/13/24
#Program Prompt - For your Midterm Project in SE126 you will be building a program of your own design! You must work individually to design a program and file of your choosing.

#About Program - A program that will display a menu  of the 2023-2024 Premier League season stats, 2023-2024 NFL Season stats, a 2023-2024 Basketball stats as well as a exit button. The user will be able to choose a sport from the menu and whatever sport they chose they can view the stats of any team they want. 

#Variable Dictionary:
#                      VARIABLES ACCESSED THROUGHOUT PROGRAM
#bin_search - This is the binary search function that will be used to search the list of teams
  #content(parameter) - This is the list of teams that will be used to search the list of teams
  #target(parameter) - This is the team that the user search for
  #min - This is the minimum value of the list
  #max - This is the maximum value of the list
  #mid - This is the middle value of the list
#team_sorted - This is the list of teams that will be sorted
  #listName(parameter) - This is the list of teams that will be sorted
  #position(parameter) - This is the position of the team in the list
  #temp - This is a temporary variable that will be used to swap the values of the list
#answer - This is the answer that the user will input to continue or exit the sport
  #acceptable_answers - This is the list of acceptable answers that the user can input
  #answer_choice - This is the answer that the user will input

#---------------------------------------  END OF VARIABLES ACCESSED THROUGHOUT PROGRAM ----------------------------------------------------
#---------------------------------------------  SOCCER FIELDS/VARIABLES  ----------------------------------------------------

#team - list that holds all the teams from the file(col.0, rec[0]).
#standing - list that holds the each teams standing from the file(col.1 rec[1]).
#points - list that holds each teams points from the file(col.2 rec[2]).
#wins - list that holds each teams wins from the file(col.3, rec[3]).
#draws - list that holds each teams draws from the file(col.4, rec[4]).
#losses - list that holds each teams losses from from the file(col.5, rec[5]).
#goals_scored - list that holds the amount of goals each team has scored(col.6, rec[6]).
#goals_allowed - list that holds the amount of goals each team has allowed(col.7, rec[7]).
#goals_difference - list that holds the goal differences each team has(col.8, rec[8])
#motto - list that holds each teams motto
#nickname - list that holds each teams nickname
#menu - Function that displays all the teams
#display - holds and calls the menu function to the main program to display
#seq_search - function that will search in a sequence through the entire list from the starting index and last index to find the value you are looking for
#pick - parameter of the seq_search function
#choice_index - holds the index(location) to this variable
#soccer_teams - list that holds the amount of soccer teams you searched
#decision - holds and calls the seq_search function to use in the main program

# ------------------------------------------------- END OF SOCCER FIELDS/VARIABLES ------------------------------------------------------------
# --------------------------------------------------   NFL FIELDS/VARIABLES -------------------------------------------------------------------
#team_fb - list that holds all the teams from the file(col.0, rec[0])
#standing_fb - list that holds the each teams standing from the file(col.1 rec[1])
#wins_fb - list that holds each teams wins from the file(col.2, rec[2])
#losses_fb - list that holds each teams losses from from the file(col.3, rec[3])
#pointsScored_fb - list that holds each teams points from the file(col.4 rec[4])
#pointsAllowed_fb - list that holds the amount of goals each team has allowed(col.5, rec[5])
#OffenseFb_ranking - list that holds the amount of goals each team has scored(col.6, rec[6])
#DefenseFb_ranking - list that holds the amount of goals each team has allowed(col.7, rec[7])
#playoffs_fb - list that holds the goal differences each team has(col.8, rec[8])
# -------------------------------------------------- END OF NFL FIELDS/VARIABLES -----------------------------------------------------------
# -------------------------------------------------- BASKETBALL FIELDS/VARIABLES -----------------------------------------------------------
# team_bb - list that holds all the teams from the file(col.0, rec[0])
# standing_bb - list that holds the each teams standing from the file(col.1 rec[1])
# wins_bb - list that holds each teams wins from the file(col.2, rec[2])
# losses_bb - list that holds each teams losses from from the file(col.3, rec[3])
# ------------------------------------------------- END OF BASKETBALL FIELDS/VARIABLES ------------------------------------------------------

#---------------------------------------------------------- PROGRAM BEGINS BELOW ------------------------------------------------------------

import csv

#--------------------------- EMPTY LIST FOR STORED DATA -----------------------------
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

#Football lists
team_fb = []
standing_fb = []
wins_fb = []
losses_fb = []
pointsScored_fb = []
pointsAllowed_fb = []
offenseFb_ranking = []
defenseFb_ranking = []
playoffs_fb = []

#Basketball lists
team_bb = []
standing_bb =[]
wins_bb = []
losses_bb = []

#------------------------------------- CONNECT TO FILES FOR PROGRAM --------------------------------
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
      
#Open the football file
with open("final project/NFLstats_2023.csv") as csvfile1:
    file1 = csv.reader(csvfile1)
    for rec in file1:
        team_fb.append(rec[0].lower())
        standing_fb.append(int(rec[1]))
        wins_fb.append(int(rec[2]))
        losses_fb.append(int(rec[3]))
        pointsScored_fb.append(int(rec[4]))
        pointsAllowed_fb.append(int(rec[5]))
        offenseFb_ranking.append(int(rec[6]))
        defenseFb_ranking.append(int(rec[7]))
        playoffs_fb.append(rec[8])

#Open the basketball file
with open("final project/nba.csv") as csvfile2:
    file2 = csv.reader(csvfile2)
    for rec in file2:
      team_bb.append(rec[0])
      standing_bb.append(int(rec[1]))
      wins_bb.append(int(rec[2]))
      losses_bb.append(int(rec[3]))

#-----------------------------------ADD/APPEND SOCCER TEAM MOTTOS -----------------------------------

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
      
#----------------------------- ADD/APPEND NICKNAMES -----------------------------------------

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
    
#------------------------------ FUNCTIONS BELOW -------------------------------------------------
#Main Menu Function/ Prompt user sports choice

def main_menu():
  print("\n\t\tPlease Select a sport you'd like to view stats for ")
  print("\n\n\t\t\t\t\t\tMenu:\n")
  print("\t\t1.Soccer     | The Premier League")
  print("\t\t2.Football   | National Football League")
  print("\t\t3.Basketball | National Basketball Association")
  print("\t\t4.Exit")
  print("\n\n")
  choice = input("\t\t\t\tEnter your choice [1 - 4]: ")
  if choice not in ["1", "2", "3", "4"]:
    print("\n\t\tInvalid Input")
    print("\n\t\tPlease try again")
    choice = main_menu()
  return choice

#--------------------------- SOCCER MENU FUNCTION ------------------------------------------------
#A menu to list the teams for the 2023-2024 Premier League

def menu():
    print("\t\t\t\t\tLiverpool\n\t\t\t\t\tMancity\n\t\t\t\t\tArsenal\n\t\t\t\t\tAstonvilla\n\t\t\t\t\tTottenham\n\t\t\t\t\tManutd\n\t\t\t\t\tWestham\n\t\t\t\t\tBrighton\n\t\t\t\t\tNewcastle\n\t\t\t\t\tWolverhampton\n\t\t\t\t\tChelsea\n\t\t\t\t\tBournemouth\n\t\t\t\t\tFulham\n\t\t\t\t\tCrystalpalace\n\t\t\t\t\tBrentford\n\t\t\t\t\tNottmforest\n\t\t\t\t\tLutontown\n\t\t\t\t\tEverton\n\t\t\t\t\tBurnley\n\t\t\t\t\tSheffield")

#----------------------- FOOTBALL CONFERENCE FUNCTION --------------------------------------------------
#Menu of AFC teams

def nfl_conferences():
  acceptable_conferences = ["AFC","NFC"]
  print("\n\t\tAFC")
  print("\n\t\tNFC")
  conference = None# sets the variable to nothing
  while conference not in acceptable_conferences:
    conference = input("\n\t\tEnter the conference you want to look at | AFC or NFC: ").upper()
    if conference not in acceptable_conferences:
      print("\t\t\tinvalid choice")

  return conference

#-------------------------- FORMAT FUNCTION ----------------------------------------------------------

def format(inp):
  #start and capitalize at first letter index
  return inp[:1].upper() + inp[1:].lower()
  
#-------------------------- FOOTBALL AFC FUNCTION ------------------------------------------------------
#Menu for AFC Confrence

def afc_teams():
  acceptable_teams = ["bengals", "bills", "broncos", "browns", "chargers", "chiefs", "colts", "dolphins", "jaguars", "jets", "patriots", "raiders", "ravens", "steelers", "texans", "titans",]
  afc_team_choice = None
  while afc_team_choice not in acceptable_teams:
    print("\n\t\t   AFC")
    print("\t\t------------------------")
    print("\n\t\tBengals\n\t\tBills\n\t\tBroncos\n\t\tBrowns\n\t\tChargers\n\t\tChiefs\n\t\tColts\n\t\tDolphins\n\t\tJaguars\n\t\tJets\n\t\tPatriots\n\t\tRaiders\n\t\tRavens\n\t\tSteelers\n\t\tTexans\n\t\tTitans")
    afc_team_choice = input("\n\t\tEnter the team you want to look at: ").lower()
    if afc_team_choice not in acceptable_teams:
      print("\n\t\tTeam does not exist or is not in the AFC")
    
  return afc_team_choice
  
#--------------------------- FOOTBALL NFC FUNCTION -----------------------------------------------------
#Menu for NFC Confrence
def nfc_teams():
  acceptable_teams = ["49ers", "bears", "buccaneers", "cardinals", "commanders", "cowboys", "eagles", "falcons", "giants", "lions", "packers", "panthers", "rams", "saints", "seahawks", "vikings",]
  nfc_team_choice = None
  while nfc_team_choice not in acceptable_teams:
    print("\n\t\t  NFC")
    print("\t\t------------------------")
    print("\n\t\t49ers\n\t\tBears\n\t\tBuccaneers\n\t\tCardinals\n\t\tCommanders\n\t\tCowboys\n\t\tEagles\n\t\tFalcons\n\t\tGiants\n\t\tLions\n\t\tPackers\n\t\tPanthers\n\t\tRams\n\t\tSaints\n\t\tSeahawks\n\t\tVikings")
    nfc_team_choice = input("\n\t\tEnter the team you want to look at: ").lower()
    if nfc_team_choice not in acceptable_teams:
      print("\n\t\tTeam does not exist or is not in the NFC")
      
  return nfc_team_choice
  
#----------------------------- MENU OF NBA CONFRENCES ----------------------------------------------------
def nba_conferences():
  acceptable_conferences = ["EASTERN", "WESTERN"]
  print("\n\t\tEASTERN")
  print("\n\t\tWESTERN")
  conference_choice = None
  while conference_choice not in acceptable_conferences:
    conference_choice = input("\n\t\tEnter the conference you want to look at | EASTERN OR WESTERN: ").upper()
    if conference_choice not in acceptable_conferences:
      print("\t\t\tInvalid choice")
  return conference_choice

#--------------------------- EASTERN CONFERENCE FUNCTION --------------------------------------------------

def eastern_teams():
  acceptable_teams = ["76ers", "bucks","bulls","cavaliers", "celtics", "hawks", "heat", "hornets","knicks","magic", "nets","pacers","pistons","raptors","wizards"]
  eastern_choice = None
  while eastern_choice not in acceptable_teams:
    print("\n\t\t  Eastern")
    print("\t\t------------------------")
    print("\n\t\t76ers\n\t\tBucks\n\t\tBulls\n\t\tCavaliers\n\t\tCeltics\n\t\tHawks\n\t\tHeat\n\t\tHornets\n\t\tKnicks\n\t\tMagic\n\t\tNets\n\t\tPacers\n\t\tPistons\n\t\tRaptors\n\t\tWizards")
    eastern_choice = input("\n\t\tEnter the team you want to look at: ").lower()
    if eastern_choice not in acceptable_teams:
      print("\n\t\tTeam does not exist or is not in the Eastern Conference")
  
  return eastern_choice
      
  


#--------------------------- WESTERN CONFRENCE FUNCTION --------------------------------------------------
def western_teams():
   acceptable_teams = ["clippers","grizzlies","jazz","kings","lakers","mavericks", "nuggets", "pelicans","rockets","spurs", "suns","thunder","timberwolves","trailblazers","warriors"]
   western_choice = None
   while western_choice not in acceptable_teams:
    print("\n\t\t  Western")
    print("\t\t------------------------")
    print("\n\t\tClippers\n\t\tGrizzlies\n\t\tJazz\n\t\tKings\n\t\tLakers\n\t\tMavericks\n\t\tNuggets\n\t\tPelicans\n\t\tRockets\n\t\tSpurs\n\t\tSuns\n\t\tThunder\n\t\tTimberwolves\n\t\tTrailblazers\n\t\tWarriors")
    western_choice = input("\n\t\tEnter the team you want to look at: ").lower()
    if western_choice not in acceptable_teams:
      print("\n\t\tTeam does not exist or is not in the Wastern Conference")
   return western_choice
  
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

#----------------------------------- BINARY SEARCH FUNCTION ------------------------------------------------------------
#create the binary search function which will search through the entire list to find the value/index you are looking for
def bin_search(content, target):
  min = 0
  max = len(content) - 1
  mid = int((min+max) / 2)
  while(min < max and target.lower() != content[mid].lower()):
    if target.lower() < content[mid].lower():
      max = mid - 1
    else:
      min = mid + 1
    mid = int((min+max) /2)
  if target.lower() == content[mid].lower():
    return mid
    
#------------------------------- BUBBLE SORT FUNCTION -----------------------------------------------------------------
#sort the teams that the user chooses alphabetically in each sport they search
def team_sorted(listName, position):
  temp = listName[position]
  listName[position] = listName[position + 1]
  listName[position + 1] = temp
  

#--------------------------------- ANSWER FUNCTION ----------------------------------------------------------
#function that will ask then user after every search if they want to search again in that sport
def answer():
  acceptable_answers = ["y", "n"]
  answer_choice = input("\n\t\tWould you like to continue looking at this sport (y/n): ").lower()
  while answer_choice.lower() not in acceptable_answers:
    print("\n\t\tPlease enter a valid choice[y/n]: ")
  return answer_choice
  
#------------------------------------ MAIN CODE BELOW -------------------------------------------------------

soccer_teams = []
soccer_answer = "y"
football_answer = "y"
basketball_answer = "y"
user_choice = ""
football_teams = []
basketball_teams = []

#create while loop to introduce the user to the program and keep them in as long as they want
while user_choice != "4":
   user_choice = main_menu()
#----------------------------- SOCCER MENU FUNCTION | 1 ------------------------------------------------------
   if user_choice == "1":
    soccer_answer = "y"
    while soccer_answer.lower() == "y":
        #HEADING
        print("\n\n\t\t\t\t2023-2024 Premier League Stats for Each Team")
        print("-"*90)
        display = menu()
        choice = input("\t\t\t\t\t\nEnter the team you want to look at: ")
        decision = seq_search(choice)
    
        if decision != "":#if you have a chosen a team that is in the Premier League
            if decision not in soccer_teams:#this statement will basically store/append the team to total_searches once so that if you search up a team twice, it will only store the team to the list during the first time and not the next few times if you search the same team again.
                soccer_teams.append(choice)
              
            print(f"\n\n\n\t\t\t\t{team[decision].upper()}({nickname[decision]})")
            print(f"\t\t\t\tMOTTO:{motto[decision]}")
            print(f"\t\t\t\t--------------------------------")
            print("\t\t\t\tHow They Are Doing This Season: ")
            print(f"\t\t\t\tStanding: {standing[decision]}\n\t\t\t\tPoints: {points[decision]}\n\t\t\t\tWins: {wins[decision]}\n\t\t\t\tDraws: {draws[decision]}\n\t\t\t\tLosses: {losses[decision]}\n\t\t\t\tGoals Scored: {goals_scored[decision]}\n\t\t\t\tGoals Allowed: {goals_allowed[decision]}\n\t\t\t\tGoal Difference: {goals_difference[decision]}")
            #this ugly tabbing newline method is Andys doing 
            
        else: #if you have chosen a team that is not in the Premier League
            print(f"\n\t\t\t\tThe team {choice} is not in the Premier League this season")
    
        #give user opportunity to stop looking at teams and break out of loop
        soccer_answer = answer()
#--------------------- FOOTBALL CALLING FUNCTIONS | 2 --------------------------------------------------------
  
   if user_choice == "2":#football choices
    football_answer = "y"
    while football_answer == "y":
      football_conference = nfl_conferences()
      if football_conference == "AFC":
        afc_team = afc_teams()
        afc_found = bin_search(team_fb, afc_team) #will find football team through football csv by using binary search
        if afc_found != "":  #if you have chosen a team that is in the AFC
          if afc_found not in football_teams:#this statement will basically store/append the team to total
            football_teams.append(afc_team)
            
        print(f"\n\t\t{team_fb[afc_found].upper()}")
        print("\t\t-----------------------------------------")
        print(f"\t\tSTANDING: {standing_fb[afc_found]}\n\t\tWINS: {wins_fb[afc_found]}\n\t\tLOSSES: {losses_fb[afc_found]}\n\t\tPOINTS SCORED: {pointsScored_fb[afc_found]}\n\t\tPOINTS ALLOWED: {pointsAllowed_fb[afc_found]}\n\t\tOFFENSE RANKING: {offenseFb_ranking[afc_found]}\n\t\tDEFENSE RANKING: {defenseFb_ranking[afc_found]}\n\t\tPLAYOFFS?: {playoffs_fb[afc_found]}")
        
      else:
        nfc_team = nfc_teams()
        nfc_found = bin_search(team_fb, nfc_team)
        if nfc_found != "":
          if nfc_found not in football_teams:
            football_teams.append(nfc_team)
            
        print(f"\n\t\t{team_fb[nfc_found].upper()}")
        print("\t\t-----------------------------------------")
        print(f"\t\tSTANDING: {standing_fb[nfc_found]}\n\t\tWINS: {wins_fb[nfc_found]}\n\t\tLOSSES: {losses_fb[nfc_found]}\n\t\tPOINTS SCORED: {pointsScored_fb[nfc_found]}\n\t\tPOINTS ALLOWED: {pointsAllowed_fb[nfc_found]}\n\t\tOFFENSE RANKING: {offenseFb_ranking[nfc_found]}\n\t\tDEFENSE RANKING: {defenseFb_ranking[nfc_found]}\n\t\tPLAYOFFS?: {playoffs_fb[nfc_found]}")
        
      football_answer = answer()
#--------------------- BASKETBALL CALLING FUNCTIONS | 3 --------------------------------------------------------
  
    if user_choice == "3":#basketball choices
     basketball_answer = "y"
     while basketball_answer == "y":
       basketball_conference = nba_conferences()
       if basketball_conference == "EASTERN":
         eastern_team = eastern_teams()
         eastern_found = bin_search(team_bb, eastern_team)
         if eastern_found != "":
           if eastern_found not in basketball_teams:
             basketball_teams.append(eastern_team)
         print(f"\n\t\t{team_bb[eastern_found].upper()}")
         print("\t\t-----------------------------------------")
         print(f"\t\tSTANDING:{standing_bb[eastern_found]}\n\t\tWINS:{wins_bb[eastern_found]}\n\t\tLOSSES: {losses_bb[eastern_found]}")
       elif basketball_conference == "WESTERN":
          western_team = western_teams()
          western_found = bin_search(team_bb, western_team)
          if western_found != "":
            if western_found not in basketball_teams:
              basketball_teams.append(western_team)
          print(f"\n\t\t{team_bb[western_found].upper()}")
          print("\t\t-----------------------------------------")
          print(f"\t\tSTANDING:{standing_bb[western_found]}\n\t\tWINS:{wins_bb[western_found]}\n\t\tLOSSES:{losses_bb[western_found]}")
       basketball_answer = answer()
       
#---------------------------------------- END OF PROGRAM -----------------------------------------------------------------
   else: #elif user_choice == "4":
     #bubble sort the teams that the user chooses alphabetically in each sport they search
     for i in range (0, len(soccer_teams) - 1):
       for k in range (0, len(soccer_teams) - 1):
         if soccer_teams[k] > soccer_teams[k + 1]:
            team_sorted(soccer_teams, k)
     for i in range (0, len(football_teams) - 1):
       for k in range (0, len(football_teams) - 1):
         if football_teams[k] > football_teams[k + 1]:
            team_sorted(football_teams, k)
     for i in range (0, len(basketball_teams) - 1):
       for k in range (0, len(basketball_teams) - 1):
         if basketball_teams[k] > basketball_teams[k + 1]:
            team_sorted(basketball_teams, k)
       
     
#exit loop
# add everything up at the end
all_searchs = 0
all_searchs = len(soccer_teams) + len(football_teams) + len(basketball_teams)
print(f"\n\t\t\tThank you for using this program, You looked at {all_searchs} teams during your session.")
print("\t\t\tHere are all the teams that you looked at")
print("\t\t\t Soccer")
print("\t\t--------------------------------------------")
for i in range(0, len(soccer_teams)):
  print(f"\t\t\t{soccer_teams[i].upper()}")
print("\n\t\t\t Football")
print("\t\t-------------------------------------------")
for i in range(0, len(football_teams)):
  print(f"\t\t\t{football_teams[i].upper()}")
print("\n\t\t\t Basketball")
print("\t\t-------------------------------------------")
for i in range(0, len(basketball_teams)):
  print(f"\t\t\t{basketball_teams[i].upper()}")
      