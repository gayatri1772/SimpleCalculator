print("========================")
print("   SIMPLE CALCULATOR ")
print("========================")

# 1. Display the menu first
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# 2. Get the choice and numbers
choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("-" * 24)

# 3. Perform the selected operation
if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid choice")

# 4. Keeps the window open until you press Enter
input("\nPress Enter to exit...")
