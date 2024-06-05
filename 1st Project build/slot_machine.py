#Idrees M Abdurrazzak
#06/02/2024
#My first python project

#This program involves me following a tutorial that works as practice on
#For loops, constants, arrays, indexes, while loops

#------------ FUNCTIONS BELOW -----------------
import random #generate slot machine values randomnly
 
#GLOBAL const. This variable can be accessed throughout entire program. All caps means its a constant and cant be changed. If changed, the variable refrenced anywhere else in the program will also update

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8   
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2   
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #looping through every row user bet on
        symbol = columns[0][line] #check whatever symbol is in first column of current row
        for column in columns: #loop through every column and check for symbol . The symbol to check is = at the current row we are looking at
            symbol_to_check = column[line]
            if symbol != symbol_to_check: #if symbol are not the same we break out #return to beggining of for loop and check the next line cause symbols were not the same 
                break #if symbols are the same they DONT break out 
            else: 
                winnings += values[symbol] * bet #^ means user won on that line
                winning_lines.append(line + 1)
                 
    return winnings, winning_lines
                
    

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #.items gives you the key and value associated with value.
        for _ in range(symbol_count): # _ is an anonymous variable in python so whenever looping thorugh something without caring for its count or ititeration value
            all_symbols.append(symbol)
            
    columns = [] #define column list
    for _ in range(cols): #generate col for every col we have. so if there is 3 col we need to do everything below three times
        column = []
        current_symbols = all_symbols[:] # : slice operator -- to copy a list you put a colon  #otherwise if you simply made it equal to all_symbols it would refrence all_symbols and will change eachother inherently 
        for _ in range (rows):
            value = random.choice(current_symbols) #picks random value from list 
            current_symbols.remove(value) #removes value chosen to not repeat 
            column.append(value) #add value to column []
            
        columns.append(column) 
        # code above picking random values for each row in column. 
    return columns 

def print_slot_machine(columns): #Transposing
    for row in range(len(columns[0])):
        for i, column in enumerate (columns): #enumarate -- gives index & item as you loop through (i.e. 0 , 'Apple' | 2 , 'Orange')
            if i != len(columns) - 1: 
                print(column[row],  end=" | ") #end tells the print stat what to end the line on. the \n character 
            else: 
                print(column[row], end="")
        print()
                
    
        
            

#function that  collect user input 
#function: something you can call that executes a block of code
def deposit():
    while True:  #ask user to enter deposit amount until a valid amount is entered #will continue to do this until breakout
     
        amount = input ("What would you like to deposit?: $ ") #pass prompt - text happens before user typing
      
        if amount.isdigit(): #isdigit() will tell us if something is a valid bool number i.e. 1000, 10, 45. if -9, -1000, etc this will be not true #if this is a digit will convert to integer on next line
          
            amount = int(amount) #if is integer, it is valid and wil break out
            if amount > 0:
                break #ends while loop and jumps to return amount
            else:
                print("Amount must be greater than 0.") #if not greater than 0 wil continiue loop
        else:
            print("Please enter a number.") #if not number will continue loop till breakout
            
    return amount 

# ----------- MAIN PROGRAM BEGINS BELOW --------------

def get_number_of_lines():
    while True: 
        lines = input("Enter the number of lines to bet on: (1-" + str(MAX_LINES) + ")? ") 
      
        if lines.isdigit():   
            lines = int(lines) 
            if 1 <= lines <= MAX_LINES:
                break 
            else:
                print("Amount must be greater than 0.") 
        else:
            print("Please enter a number.") 
            
    return lines 


def get_bet():
     while True:  #ask user to enter deposit amount until a valid amount is entered #will continue to do this until breakout
     
        amount = input ("What would you like to bet on each line?: $ ") #pass prompt - text happens before user typing
      
        if amount.isdigit(): #isdigit() will tell us if something is a valid bool number i.e. 1000, 10, 45. if -9, -1000, etc this will be not true #if this is a digit will convert to integer on next line
          
            amount = int(amount) #if is integer, it is valid and wil break out
            if MIN_BET <= amount <= MAX_BET:
                break #ends while loop and jumps to return amount
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") #if not greater than 0 wil continiue loop
        else:
            print("Please enter a number.") #if not number will continue loop till breakout
            
     return amount 
 
 

def spin(balance): #can call this function to rerun program
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount hoe nigga, your current balance is: ${balance}")
        else: 
            break  
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet
    
def main():
     balance = deposit() #balance is the function that contains the user input 
     while True:
        print(f"Current balance is ${balance}")
        anwser = input("Press enter to play (q to quit).")
        if anwser == "q":
            break
        balance += spin(balance)
        
     print("You left with ${balance}")
    
       
main()
        
        