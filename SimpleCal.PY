#TASK 2
#A SIMPLE CALCULATOR
def addition(num1, num2):
    return num1+num2
def subtraction(num1, num2):
    return num1-num2
def multiplication(num1, num2):
    return num1*num2
def division(num1, num2):
    return num1/num2
def remainder(num1, num2):
    return num1%num2
n1 = float(input("Enter the First Number: "))
45
n2 = float(input("Enter the Second Number: "))
def calculator():
    while True:
        print("Select operations:\n"
              "1.ADD\n"
              "2.SUB\n"
              "3.MUL\n"
              "4.DIV\n"
              "5.REM\n"
              "6.EXIT\n")
        choice = int(input("Enter choice of operation 1/2/3/4/5: "))
        if choice == 1:
           print (n1, "+", n2, "=", addition(n1, n2))
        elif choice == 2:
           print (n1, "-", n2, "=", subtraction(n1, n2)) 
        elif choice == 3:
           print (n1, "*", n2, "=", multiplication(n1, n2))
        elif choice == 4:
           print (n1, "/", n2, "=", division(n1, n2)) 
        elif choice == 5:
           print (n1, "/", n2, "=", remainder(n1, n2))
        elif choice == 6:
           print("Exiting Calculator")
           break
        else:
           print("Invalid Input")
calculator()
