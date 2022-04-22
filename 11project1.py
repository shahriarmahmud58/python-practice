# calculator
#function creat
def Addition(num1,num2):
    result=num1+num2
    print("{0}+{1}={2}".format(num1,num2,result))
    
def Substraction(num1,num2):
    result=num1-num2
    print("{0}-{1}={2}".format(num1,num2,result))
    
def Multiplication(num1,num2):
    result=num1*num2
    print("{0}*{1}={2}".format(num1,num2,result))
    
def Division(num1,num2):
    if num2==0.0:
        print("please enter valid number without 0")
    else:
        result=num1/num2
        print("{0}/{1}={2}".format(num1,num2,result))


while True :
    
    # Display
    print("What do you want to do ?")
    print("press 1 for Addition")
    print("press 2 for Substraction")
    print("press 3 for Multiplication")
    print("press 4 for Division")
    print("Enter Q or q for quit")


    # user input 2 disit number
    choice = input("Enter Your Choice : ")
    if choice=='Q' or choice=='q':
        break
    
    # taking 2 number from User

    num1 = float(input("enter number 1 "))
    num2 = float(input("enter number 2 "))

    # condition
    if choice == '1':
     Addition(num1, num2)
    elif choice == '2':
     Substaction(num1, num2)
    elif choice == '3':
     Multiplication(num1, num2)
    elif choice == '4':
     Division(num1, num2)
    else:
     print("invalid Choice")
