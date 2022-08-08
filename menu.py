while True:
    print("1 for adding two numbers \n 2 for subtracting two numbers \n 3 for multiplying two numbers \n 4 for dividing two numbers \n 5 for Exit")
    choice=int(input("Enter your choice : "))
    if (choice==1):
        num1=int(input("Enter your first number : "))
        num2=int(input("Enter your second number : "))
        result=num1+num2
        print(result)
    elif (choice==2):
        num1=int(input("Enter your first number : "))
        num2=int(input("Enter your second number : "))
        result=num1-num2
        print(result)
    elif (choice==3):
        num1=int(input("Enter your first number : "))
        num2=int(input("Enter your second number : "))
        result=num1*num2
        print(result)
    elif (choice==4):
        num1=int(input("Enter your first number : "))
        num2=int(input("Enter your second number : "))
        result=num1/num2
        print(result)
    elif (choice==5):
        break
    