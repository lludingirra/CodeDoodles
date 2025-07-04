import math

# Constants for mathematical operations
MATH_CONSTANTS = {"pi": math.pi, "e": math.e}

# Trigonometric functions mapping
TRIGONOMETRIC_FUNCTIONS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "cot": lambda x: 1 / math.tan(x),
    "sec": lambda x: 1 / math.cos(x),
    "csc": lambda x: 1 / math.sin(x),
}

def is_integer(value_str):
    """
    Checks if a string represents an integer.
    Args:
        value_str (str): The string to check.
    Returns:
        bool: True if the string is an integer, False otherwise.
    """
    return value_str.lstrip('-+').isdigit()

def get_integer_input(prompt):
    """
    Prompts the user for an integer input and validates it.
    Args:
        prompt (str): The message to display to the user.
    Returns:
        int: The validated integer input.
    """
    while True:
        user_input = input(prompt)
        if is_integer(user_input):
            return int(user_input)
        print("Invalid input. Please enter an integer.")

def solve_equation():
    """
    Solves linear and quadratic equations.
    """
    print("\n------------Equation Solver------------\n")
    print("1. Linear Equation (ax + b = 0)")
    print("2. Quadratic Equation (ax^2 + bx + c = 0)\n")

    equation_degree = get_integer_input("Select the degree of the equation: ")

    while not (1 <= equation_degree <= 2):
        print("Invalid choice. Please select 1 or 2.")
        equation_degree = get_integer_input("Select the degree of the equation: ")

    if equation_degree == 1:
        print("\nEnter coefficients for ax + b = 0:")
        a = get_integer_input("a: ")
        b = get_integer_input("b: ")

        if a == 0:
            if b == 0:
                print("Infinite solutions (0 = 0).")
            else:
                print("No solution (e.g., 0 = 5).")
        else:
            x = -b / a
            print(f"For a = {a}, b = {b}:")
            print(f"x = {x}")

    elif equation_degree == 2:
        print("\nEnter coefficients for ax^2 + bx + c = 0:")
        a = get_integer_input("a: ")
        b = get_integer_input("b: ")
        c = get_integer_input("c: ")

        # Calculate discriminant for quadratic equation
        discriminant = (b * b) - (4 * a * c)

        if discriminant >= 0:
            # Real roots
            root1 = (-b - math.sqrt(discriminant)) / (2 * a)
            root2 = (-b + math.sqrt(discriminant)) / (2 * a)
            print(f"For a = {a}, b = {b}, c = {c}:")
            print(f"x1 = {root1}")
            print(f"x2 = {root2}")
        else:
            # Complex roots (no real roots)
            print(f"For a = {a}, b = {b}, c = {c}:")
            print("No real roots.")

def calculate_expression():
    """
    Evaluates a mathematical expression using Python's eval.
    Handles constants and trigonometric functions.
    """
    print("\n------------Calculator------------\n")
    expression = input("Please enter the expression to calculate: ")

    # Replace constants like 'pi' and 'e' with their math module values
    for const_name, const_value in MATH_CONSTANTS.items():
        expression = expression.replace(const_name, str(const_value))

    # Replace trigonometric functions (e.g., 'sin(90)')
    for func_name in TRIGONOMETRIC_FUNCTIONS:
        # This is a basic replacement, for robust parsing, consider a proper math expression parser
        # For example, sin(90) becomes math.sin(90)
        expression = expression.replace(f"{func_name}(", f"math.{func_name}(")

    # Handle power operator '^' with '**'
    expression = expression.replace("^", "**")

    try:
        # Use eval for expression evaluation. Be cautious with eval in production code.
        result = eval(expression)
        print(f"Result: {result}")
    except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
        print(f"Error in expression: {e}")
        print("Please ensure your expression is valid.")

def main():
    """
    Main function to run the calculator and equation solver application.
    """
    while True:
        print("\nChoose an operation:")
        print("1. Equation Solver")
        print("2. Calculator")
        print()

        choice = get_integer_input("Enter your choice: ")

        if choice == 1:
            solve_equation()
        elif choice == 2:
            calculate_expression()
        else:
            print("Invalid choice. Please select 1 or 2.")
            continue # Continue the loop to ask for input again

        while True:
            print()
            continue_choice = input("Do you want to perform another operation? (Yes: y | No: n): ").lower()
            if continue_choice == "y":
                break  # Break inner loop to restart main loop
            elif continue_choice == "n":
                print("Exiting application. Goodbye!")
                return # Exit the main function, terminating the program
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()