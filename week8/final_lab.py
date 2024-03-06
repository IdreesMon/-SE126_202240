#Idrees M Abdurrazzak
#SE126.10 Intermediate Prog Using Python
#03/01/2024

#Prompt: Write a program that can be used by a small theater to sell tickets for performances. The theater’s auditorium has 15 rows of seats with 30 seats in each row. The program should display a screen that shows which seats are available and which are taken. Seats thar are available are represented by # and seats that are taken are represent by a *. There are aisles after seats H and V.

columns = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234"
rows = []
cart = []

for row in range(1, 16):
    rows.append(["#"] * len(columns))


def calculate_price(row):
    if row in range(0, 6):
        return 200
    
    elif row in range(6, 11):
        return 175
    
    else:
        return 150
    
    
def display_seats():
    print("Rows\tSeats")
    
    print("\t", end="")
    
    for i, column in enumerate(columns):
        print(column, end=" ")

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


def prompt_menu():
    print("\n\nMenu")
    print("0. Display Seats")
    print("1. Add to cart")
    print("2. View Total Seat Sales")
    print("3. View Seat Information")
    print("4. Checkout")
    print("5. Exit")

    answer = False
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
    return columns.index(column)


def get_column_name(index):
    return columns[index]


def is_seat_available(row, column):
    return rows[row][get_column_index(column)] == "#"


def add_to_cart():
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
            column = input("Please enter the seat letter (A-4): ").upper()
            if column not in columns:
                print("Please enter a valid seat letter")
                column = None
        except Exception:
            print("Please enter a valid seat letter")
            continue
        
    if (row, column) in cart:
        print("Seat is already in cart")
    else:
        if not is_seat_available(row, column):
            print("Seat is not available")
            return
        else:
            cart.append((row, column))
    
    if input("Would you like to add another seat? (y/n): ").lower() == "y":
        add_to_cart()


def view_total_seat_sales():
    for i, row in enumerate(rows):
        for j, seat in enumerate(row):
            if seat == "*":
                price = calculate_price(i)
                print(f"Seat {get_column_name(j)} in row {i+1} - ${price}")
    
    
def view_seat_information():
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
        
        seats_taken = rows[row].count("*")
        seats_available = rows[row].count("#")
        
        print(f"Seats taken in row {row+1}: {seats_taken}")
        print(f"Seats available in row {row+1}: {seats_available}")
    
    else:
        seats_taken = 0
        seats_available = 0
        
        for row in rows:
            seats_taken += row.count("*")
            seats_available += row.count("#")
        
        print(f"Total seats taken: {seats_taken}")
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
        rows[row][get_column_index(column)] = "*"
        
    print(f"Total: ${total}")
    
 
def handle_answer(answer):
    if answer == 1:
        add_to_cart()
        
    elif answer == 2:
        view_total_seat_sales()
        
    elif answer == 3:
        view_seat_information()
        
    elif answer == 4:
        checkout()
        
    else:
        print("Thank you for using the program")
        exit()


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
