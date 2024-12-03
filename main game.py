# Teacher Adventure Game Template
from events import event_1, event_2
# Stats dictionary to keep track of player's stats
stats = {
    "energy": 100,  # The energy level of the teacher
    "motivation": 100,  # The motivation level of the teacher
    "students_helped": 0  # How many students the teacher has helped
}

# Inventory list to keep track of items
inventory = []

def intro():
    """
    Introduces the game and provides background.
    """
    print("Welcome to the Teacher Adventure Game!")
    print("You are a dedicated teacher navigating through a typical school day.")
    print("Your goal is to manage your energy and motivation while helping students.")
    print("Let's begin!")
    print("\n")

    

def main():
    """
    The main function to start the game.
    """
    intro()  # Call the intro function
    event_1()  # Trigger the first event
    event_2()  # Trigger the second event

    print("Game Over. Here's how you did:")
    print(f"Final Energy: {stats['energy']}")
    print(f"Final Motivation: {stats['motivation']}")
    print(f"Total Students Helped: {stats['students_helped']}")
    print("Final Inventory:", inventory)

# Start the game by calling the main function
if __name__ == "__main__":
    main()
