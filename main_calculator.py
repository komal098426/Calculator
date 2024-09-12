import add
import sub
import multiply
import divide


def main():
    while True:
        # Get user input
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input.Please enter numeric values.")
            continue

        operator = input("Enter an operator (+, -, *, /): ").strip()

        # Perform the calculation based on the operator
        if operator == '+':
            result = add.add(num1, num2)
        elif operator == '-':
            result = sub.sub(num1, num2)
        elif operator == '*':
            result = multiply.multiply(num1, num2)
        elif operator == '/':
            result = divide.divide(num1, num2)
        else:
            result = "Error: Invalid operator"

        # Print the result
        print(f"The result is: {result}")

        # Ask the user if they want to quit or continue
        continue_calculating = input("Do you want to quit the calculator? (Y/N): ").strip().upper()
        if continue_calculating == 'Y':
            print("Exiting the calculator. Goodbye!")
            break
        elif continue_calculating != 'N':
            print("Invalid input.Please enter Y to quit or N to continue.")


if __name__ == "__main__":
    main()