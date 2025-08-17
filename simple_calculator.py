# Simple Calculator Program

# Ask the user for the first number
num1_input = input("Enter the first number: ")

# Check if the first number is valid
if not num1_input.replace('.', '', 1).isdigit() and not (num1_input.startswith('-') and num1_input[1:].replace('.', '', 1).isdigit()):
    print("Invalid input! The first value is not a number.")
else:
    num1 = float(num1_input)

    # Ask the user for the second number
    num2_input = input("Enter the second number: ")

    # Check if the second number is valid
    if not num2_input.replace('.', '', 1).isdigit() and not (num2_input.startswith('-') and num2_input[1:].replace('.', '', 1).isdigit()):
        print("Invalid input! The second value is not a number.")
    else:
        num2 = float(num2_input)

        # Ask the user for the operator
        operator = input("Enter an operator (+, -, *, /): ")

        # Check for a valid operator
        if operator not in ('+', '-', '*', '/'):
            print("Invalid operator! Only +, -, *, / are allowed.")
        else:
            # Check for division by zero
            if operator == '/' and num2 == 0:
                print("Division by zero is not allowed!")
            else:
                # Perform the calculation
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    result = num1 / num2

                # Print the result
                print(f"You entered the two numbers {num1} and {num2} and the operator entered was {operator}.")
                print(f"The result of {num1} {operator} {num2} is {result}.")

