# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# print the results
# continue program until user quits

def add(a,b):
    answer=a+b
    print(str(a)+ "+" +str(b) + "=" + str(answer))

def sub(a,b):
    answer=a-b
    print(str(a)+ "-" +str(b) + "=" + str(answer))

def mul(a,b):
    answer=a*b
    print(str(a)+ "*" +str(b) + "=" + str(answer))

def div(a,b):
    answer=a/b
    print(str(a)+ "/" +str(b) + "=" + str(answer))


while True:
    print("A- Addition")
    print("B- Subtraction")
    print("C- Multiplication")
    print("D- Division")
    print("E- Exit")

    choice = input("input your choice: ")

    if choice=="a" or choice=="A":
        print("Addition")
        for i in range (0, 5):
            a= int(input("Enter the number: "))
            b= int(input("Enter the number: "))
        add(a, b)
    elif choice=="b" or choice=="B":
        print("Subtraction")
        a= int(input("Enter first number:  "))
        b= int(input("Enter second number: "))
        sub(a, b)
    elif choice=="c" or choice=="C":
        print("Multiplication")
        a= int(input("Enter first number:  "))
        b= int(input("Enter second number: "))
        mul(a, b)
    elif choice=="d" or choice=="D":
        print("Division")
        a= int(input("Enter first number:  "))
        b= int(input("Enter second number: "))
        div(a, b)
    elif choice=="e" or choice=="E":
        print("Program Ended...")
        quit()