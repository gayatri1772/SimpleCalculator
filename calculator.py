print("========================")
print("   SIMPLE CALCULATOR ")
print("========================")

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))



print("First number:",num1)
print("Second number:",num2)
print("Addition",num1 +num2)
print("Subtraction",num1 -num2)
print("Multiplication",num1 *num2)
print("Division",num1/num2)

choice=int(input("Enter your choice: "))
if choice == 1:
    print("Result:",num1 + num2)
elif choice == 2:
    print("Result:",num1 - num2)
elif choice == 3:
    print("Result:",num1 * num2)
elif choice == 4:
    if num2 != 0:
        
        print("Result:",num1 / num2)
    else:
        print("Error cannot divide by zero")
else:
    print("Invalid choice")