"""
menu_driven_program_function.py

This program isa Menu Driven Structure
It consists four functions:
1. display_menu() - This display the 3 option
2. get_valid_choice() - Prompt the user to input int and validate it
3. greet_user() - This is the greet function
4. check_even_odd() - Check if the user input is even or odd
"""

def display_menu():
    """Displays the main menu."""
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def get_valid_choice() -> int:
    """
    Gets a valid menu choice from the user.

    Returns:
        int: The user's valid menu choice (1, 2, or 3).
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice in [1, 2, 3]:
                return choice  # Valid choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def greet_user():
    """Displays a greeting message."""
    print("Hello! Welcome!")

def check_even_odd():
    """Asks for an integer and checks if it's even or odd."""
    while True:
        try:
            number = int(input("Enter an integer: "))  # Get user input
            if number % 2 == 0:
                print(f"{number} is an Even number.")
            else:
                print(f"{number} is an Odd number.")
            break  # Exit loop after a valid input
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    """Main function to run the menu-driven program."""
    while True:
        display_menu()
        choice = get_valid_choice()
        
        if choice == 1:
            greet_user()
        elif choice == 2:
            check_even_odd()
        elif choice == 3:
            print("Exiting program. Goodbye!")
            break  # Exit the loop when user chooses option 3

if __name__ == "__main__":
    main()
