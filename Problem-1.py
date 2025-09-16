def addition():
    Sum=a+b
    print(Sum)

def subtraction():
    Diff=a-b
    print(Diff)

def multiplication():
    Product=a*b
    print(Product)

def division():
    Quotient=a/b
    print(Quotient)

def cont():
    choice=input("Do you want to continue? (y/n)")
    if choice.lower()=='n':
        exit()
    elif choice.lower()=='y':
        return
    else:
        print("Invalid Input")
        exit()



while True:
    
    print("Select the operation you want to perform:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    option=input("Enter the option(1/2/3/4:)")
    a=float(input("Enter the First input:"))
    b=float(input("Enter the Second input:"))

    if option=='1':
        addition()
        cont()
        
    elif option=='2':
        subtraction
        cont()

    elif option=='3':
        multiplication()
        cont()

    elif option=='4':
        division()
        cont()

    else:
        print("Invalid Input")
        break
