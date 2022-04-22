import random
guess = random.randint(5,10)

while True:
    print( "I have a number in my mind can you guess it?")
    usernum=int(input("enter the Number : "))
 
    if usernum == guess:
        print ("number is matched ")
    elif usernum > guess:
        print("number is greater than my number")
    else :
        print("number is less than my number")