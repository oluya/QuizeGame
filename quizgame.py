#We are writing a quiz game on python

print("Welcome to my quiz game!!!")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()
else:
    score =0 #Initializing the score
    answer = input("1. What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct")
        score +=1 #Incrementing the score
    else:
        print("Incorrect")
    
    answer = input("2. Write USB in full: ")
    if answer.lower() == "universal serial bus":
        print("Correct")
        score +=1
    else:
        print("Incorrect")

    answer = input("3. What does the acronym RAM stand for? ")
    if answer.lower() == "random access unit":
        print("Correct")
        score +=1
    else:
        print("Incorrect")
    
    print("Thank you for playing. You got "+ str(score)+ " question(s) correct.")