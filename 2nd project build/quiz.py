#Idrees M Abdurrazzak
#06/05/2024
#Quiz project

print("\nWelcome to my computer quiz!")

playing = input("\nDo you want to play? ")

#text = "Tim IS GReat"
#print(text.lower())

if playing.lower() != "yes": 
    #yes is the condition. if NOT equal to yes quit program. 
    quit()
    
print("Okay! Let's play :)")
score = 0 #keep track of how many correct anwser

anwser = input("What does CPU stand for? ")
if anwser.lower() == "central processing unit":
    print("Correct!")
    score += 1 #when correct add 1 to score
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")
    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")
    
print("You got " + str(score) + " question correct!")
print("You got " + str((score / 4)* 100) + "%." )






    

 