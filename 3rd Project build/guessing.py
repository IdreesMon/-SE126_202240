import random #module that imports all functionlaity


#r = random.randrange(-5,11) #(start, stop) the stop does not stop at the value entered but instead is the value before. i.e. 10 is 9. if you wish to stop at 10 you enter 11 


#r2 = random.randint(-5,11) #this way includes the actually value entered as the stop
#print(r)


top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('please type a number larger than 0 next (time')
        quit()
else: 
    print("Please type a number next time. ")
    quit()
    
random_number= random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ") 
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("Please type a number next time. ")
        continue 
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")
#print("You got it in" + str(guesses) + " guesses")
 




   
      






#print(random_number)




#random_number = random.randint(11)
   