#Idrees M Abdurrazzak
#SE126.10 Intermediate Prog Using Python
#03/01/2024

#Prompt: Write a program that can be used by a small theater to sell tickets for performances. The theater’s auditorium has 15 rows of seats with 30 seats in each row. The program should display a screen that shows which seats are available and which are taken. Seats thar are available are represented by # and seats that are taken are represent by a *. There are aisles after seats H and V.

#variable dictionary:
#columns - a string of the alphabet and numbers
#rows - a list of lists that contains the rows and columns of the theater
#cart - a list that contains the seats that have been taken
#calculate_price - a function that calculates the price of the seat based on the row
#display_seats - a function that displays the seats in the theater
#prompt_menu - a function that prompts the user to select an option from the menu
#get_column_index - a function that returns the index of the column
#get_column_name - a function that returns the column name
#is_seat_available - a function that returns the row and column index of the seat
#add_to_cart - a function that adds the seat to the cart
#view_total_seat_sales - a function that displays the total seat sales
#view_seat_information - a function that displays the seat information
#checkout - a function that checks out the user
#handle_answer - a function that handles the answer from the user



#-------------------------------------- PROGRAM BEGINS BELOW ---------------------------------



#create lists for rows and columns
columns = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234"
rows = []
cart = []


#append "#" to rows 
for row in range(1, 16):
    rows.append(["#"] * len(columns)) #multiply the rows by the length of the columns and popluate with # for seats available

#assign prices to the rows
def calculate_price(row):
    if row in range(0, 6): #if the row is in the range of 0-6
        return 200
    
    elif row in range(6, 11): #if the row is in the range of 6-11
        return 175
    
    else:
        return 150 #if the row is not in the range of 0-6 or 6-11, then the price is 150
    
    
def display_seats():
    print("Rows\tSeats")
    
    print("\t", end="") #this statment is used to print the rows and seats with appropriate spacing
    
    #enumarate returns the element of the list and the index
    for i, column in enumerate(columns):
        print(column, end=" ") #print the columns

        if column in ['H', 'V']:
            print("  ", end="") 
            
    print()
    
    for i, row in enumerate(rows):
        print(f"{i+1}\t", end="")
        
        for j, seat in enumerate(row):
            print(seat, end=" ")
            
            if j in [7, 21]:
                print("  ", end="")
                
        print()

#prompt the user to select an option from menu function
def prompt_menu():
    print("\n\nMenu")
    print("0. Display Seats")
    print("1. Add to cart")
    print("2. View Total Seat Sales")
    print("3. View Seat Information")
    print("4. Checkout")
    print("5. Exit")

    answer = False #set answer to False so that the while loop can run
    while answer is False:
        try:
            answer = int(input("Please select an option: "))
            if answer not in [0, 1, 2, 3, 4, 5]:
                print("Please select a valid option")
                answer = None
                
        except Exception:
            print("Please enter a number")
    return answer


def get_column_index(column):
    return columns.index(column) #return the index of the column


def get_column_name(index):
    return columns[index] #return the column name


def is_seat_available(row, column):
    return rows[row][get_column_index(column)] == "#"
#return the row and column index of the seat

def add_to_cart(): #add to cart function
    row = None
    while row is None:
        try:
            row = int(input("Please enter the row number (1-15): ")) - 1
            if row not in range(0, 15):
                print("Please enter a valid row number")
                row = None
        except Exception:
            print("Please enter a number")
            continue
        
    column = None
    while column is None:
        try:
            #prompt the user to enter the seat letter
            column = input("Please enter the seat letter (A-4): ").upper()
            if column not in columns:
                print("Please enter a valid seat letter")
                column = None
        except Exception:
            print("Please enter a valid seat letter")
            continue
    #if seat is already in cart, print "Seat is already in cart"    
    if (row, column) in cart:
        print("Seat is already in cart")
    else:
        if not is_seat_available(row, column):
             #if seat is not available, print "Seat is not available"
            print("Seat is not available") #seat has already been taken prompt user to select available seat 
            return
        else:
            cart.append((row, column)) #append the row and column to the cart to store the seat as unavailable
    
    if input("Would you like to add another seat? (y/n): ").lower() == "y":
        add_to_cart()


def view_total_seat_sales():
    for i, row in enumerate(rows):
        for j, seat in enumerate(row):
            if seat == "*": #if the seat is taken, calculate the price and print the seat and price
                price = calculate_price(i)
                print(f"Seat {get_column_name(j)} in row {i+1} - ${price}")
    
    
def view_seat_information():
    #prompt the user to view seat information by row
    view_row_info = input("Would you like to view seat information by row? (y/n): ").lower() == "y"
    
    if view_row_info:
        row = None
        while row is None:
            try:
                row = int(input("Please enter the row number (1-15): ")) - 1
                if row not in range(0, 15):
                    print("Please enter a valid row number")
                    row = None
            except Exception:
                print("Please enter a number")
                continue
        
        seats_taken = rows[row].count("*") # "*" signifies the number of seats taken in the row
        seats_available = rows[row].count("#") # "#" signifies the number of seats available in the row
        
        print(f"Seats taken in row {row+1}: {seats_taken}") #+1 is used to add seat since we start at 0
        print(f"Seats available in row {row+1}: {seats_available}")
    
    else:
        seats_taken = 0  #if seats have not been purchased, set the seats available to 0
        seats_available = 0 #if seats HAVE been purchased, set the seats available to 0
        
        for row in rows:
            seats_taken += row.count("*")
            seats_available += row.count("#")
        
        print(f"Total seats taken: {seats_taken}") #print the total seats taken
        print(f"Total seats available: {seats_available}")
        
    
def checkout():
    if len(cart) == 0:
        print("Cart is empty")
        return
    
    total = 0
    for seat in cart:
        row, column = seat
        price = calculate_price(row)
        total += price
        print(f"Seat {column} in row {row+1} - ${price}")
        rows[row][get_column_index(column)] = "*" # * displays in final map output during checkout to show that the seat has been taken
        
    print(f"Total: ${total}")
    
 
def handle_answer(answer):
    if answer == 1:
        add_to_cart() #if the user selects 1, add to cart
        
        
    elif answer == 2:
        view_total_seat_sales() #if the user selects 2, view total seat sales
        
    elif answer == 3:
        view_seat_information() #if the user selects 3, view seat information
        
    elif answer == 4:
        checkout() #if the user selects 4, checkout and view total of tickets purchased
        
    else:
        print("Thank you for using the program")
        exit() #exit program


if __name__ == "__main__":
    answer = None
    while answer != 5:
        answer = prompt_menu()
        
        if answer == 0:
            display_seats()
            
        elif answer == 1:
            add_to_cart()

        elif answer == 2:
            view_total_seat_sales()

        elif answer == 3:
            view_seat_information()

        elif answer == 4:
            checkout()
