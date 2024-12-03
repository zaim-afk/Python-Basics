def event_1():
    """
    It's the first Monday of the term. You just got back from Fajr.
    There is still an hour before you need to get to school and the trip takes half an hour at most.
    The bed and the comforts beckons you to join them.
    What do you do?
    a) 'Rest' you eyes for 30 minutes and get to school just on time
    b) Leave now and get to school early and greet all the other early people
    """
   
    choice = input("What will you do? (1/2): ")

    if choice == "1":
        print("You chose to teach your class diligently.")
        stats["energy"] -= 10
        stats["motivation"] += 5
        stats["students_helped"] += 1
        print("Your energy decreases, but your students appreciate your effort!")
    elif choice == "2":
        print("You chose to take a quick break.")
        stats["energy"] += 5
        stats["motivation"] -= 5
        print("You feel a bit more energized, but your motivation drops slightly.")
    else:
        print("Invalid choice. Try again.")
        event_1()  # Recurse if the choice is invalid
    
    print("\nCurrent Stats:")
    print(f"Energy: {stats['energy']}")
    print(f"Motivation: {stats['motivation']}")
    print(f"Students Helped: {stats['students_helped']}")
    print("\n")

def event_2():
    """
    The second event of the game, where the player faces a new challenge.
    """
    print("Event 2: A student approaches you after class, seeking help with an assignment.")
    print("You have a choice:")
    print("1. Help the student with the assignment.")
    print("2. Tell the student to figure it out on their own.")

    choice = input("What will you do? (1/2): ")

    if choice == "1":
        print("You chose to help the student.")
        stats["energy"] -= 15
        stats["motivation"] += 10
        stats["students_helped"] += 1
        inventory.append("Student's Gratitude")  # Add an item to the inventory
        print("The student is grateful and you feel good about making a difference!")
    elif choice == "2":
        print("You chose to tell the student to figure it out.")
        stats["energy"] += 5
        stats["motivation"] -= 10
        print("The student seems disappointed, and your motivation takes a hit.")
    else:
        print("Invalid choice. Try again.")
        event_2()  # Recurse if the choice is invalid
    
    print("\nCurrent Stats:")
    print(f"Energy: {stats['energy']}")
    print(f"Motivation: {stats['motivation']}")
    print(f"Students Helped: {stats['students_helped']}")
    print("Inventory:", inventory)
    print("\n")
