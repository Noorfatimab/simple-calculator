# simple_calculator.py
# Interactive Python calculator with error handling

print("Welcome to the Interactive Python Calculator!")
print("You can perform Addition, Subtraction, Multiplication, Division, Modulus, and Power.\n")

try:
    # Step 1: Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Step 2: Perform calculations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Division and modulus can fail if num2 is zero
    try:
        division = num1 / num2
        modulus = num1 % num2
    except ZeroDivisionError:
        division = "Error: Cannot divide by zero"
        modulus = "Error: Cannot divide by zero"

    power = num1 ** num2

    # Step 3: Print results
    print("\nResults:")
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)
    print("Remainder (modulus):", modulus)
    print("Power:", power)

except ValueError:
    print("Error: Please enter valid numbers only.")

print("\nThank you for using the calculator!")
